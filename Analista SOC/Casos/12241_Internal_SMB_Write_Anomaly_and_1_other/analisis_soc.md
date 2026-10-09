# Reporte del SOC: Análisis de Alertas - Caso 12241

Se han detectado **2 eventos independientes** en el lote de logs analizado. A continuación se realiza el procesamiento técnico individual e independiente de cada uno de ellos, seguido de una correlación y cierre maestro unificado del caso.

---

# [Parte I] Análisis Individual de Eventos

## Análisis Evento 1: Internal SMB Read Anomaly

### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `SMB` | `SAMR` | `IPC$` | `GPO Sync` | `False Positive`

### 📝 Resumen Ejecutivo del Evento 1 (Formato Nativo Stellar)
- **Origen:** El host `nb-calvarez.technoma.local` (IP: `192.168.169.16`, usuario `carlosalvarez` verificado en AD) en la subred `VLAN1101`.
- **Comportamiento:** Picos de solicitudes de lectura SMB (59 consultas vs 8 típicas en 5 minutos) accediendo a los recursos compartidos administrativos de dominio.
- **Destino / Activo Afectado:** Controlador de Dominio `ad.technoma.local` (IP: `10.11.1.1`).
- **Severidad / Acción:** Severidad baja (20).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-16 07:39:07 | 2026-07-16 04:39:07 | smb_read_anomaly | 59 | 8 | 7.38x | El host lee la tubería IPC$\samr para validar grupos/políticas de usuario en AD. |

### 🔍 Desglose Técnico y Disección Forense
- **Mecanismo:** El host cliente inició una conexión de red hacia el recurso compartilhado `\\ad.technoma.local\IPC$` abriendo la tubería interna `samr` (Security Account Manager Remote Protocol) para consultar información de la cuenta local del dominio.
- **Traducción de Comandos SMBv2 (Rosetta Stone):**
  - **Comando 3 (`SMB2_OP_TREE_CONNECT`):** Conexión al recurso compartido `IPC$`.
  - **Comando 5 (`SMB2_OP_CREATE`):** Abre un manejador (handle) apuntando a la tubería con nombre (`samr`).
  - **Comando 16 (`SMB2_OP_GETINFO`):** Pide descriptores de seguridad y permisos de ACL.
  - **Comando 8 (`SMB2_OP_READ`):** Realiza la lectura del flujo de respuesta del pipe.
  - **Comando 6 (`SMB2_OP_CLOSE`):** Cierra el manejador de la sesión.
- **Causalidad:** Las operaciones de lectura ocurren de forma legítima durante el inicio de sesión o actualización rutinaria de GPOs (Group Policy Object) para importar grupos y RIDs del usuario local.

**Payload / Evidencia Principal (Evento 1):**
```json
{
  "payload_type": "SMB Named Pipe Access",
  "payload_value": "\\\\ad.technoma.local\\IPC$ - Pipe samr",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Allowed Pipe Read",
  "payload_destino": "10.11.1.1:445"
}
```

---

## Análisis Evento 2: Internal SMB Write Anomaly

### 📘 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `SMB` | `SAMR` | `IPC$` | `RPC Write` | `False Positive`

### 📝 Resumen Ejecutivo del Evento 2 (Formato Nativo Stellar)
- **Origen:** El host `nb-calvarez.technoma.local` (IP: `192.168.169.16`, usuario `carlosalvarez` en AD) en la subred `VLAN1101`.
- **Comportamiento:** Picos de solicitudes de escritura SMB (28 consultas vs 2 típicas en 5 minutos) en el pipe IPC$\samr.
- **Destino / Activo Afectado:** Controlador de Dominio `ad.technoma.local` (IP: `10.11.1.1`).
- **Severidad / Acción:** Severidad media (40).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-16 07:39:07 | 2026-07-16 04:39:07 | smb_anomaly | 28 | 2 | 14.0x | Escritura de solicitudes RPC en la tubería samr para consultar identidades al DC. |

### 🔍 Desglose Técnico y Disección Forense
- **Mecanismo:** En las llamadas de RPC sobre named pipes (en este caso SAMR), la comunicación es bidireccional:
  - El cliente realiza una **escritura** (Comando 9 `SMB2_OP_WRITE`) para inyectar su consulta RPC en la tubería.
  - El cliente realiza una **lectura** (Comando 8 `SMB2_OP_READ`) para recuperar la respuesta del servidor.
- **Explicación de la Anomalía:** El volumen de consultas escritas (28) fue marcado como anomalía de escritura por el ML, debido a que el baseline estadístico asume un flujo menor. Sin embargo, corresponde a la misma y única sesión interactiva que generó el pico de lecturas del **Evento 1**.

**Payload / Evidencia Principal (Evento 2):**
```json
{
  "payload_type": "SMB Named Pipe Write",
  "payload_value": "\\\\ad.technoma.local\\IPC$ - Pipe samr",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Allowed Pipe Write (Command 9)",
  "payload_destino": "10.11.1.1:445"
}
```

#### Comandos de Diagnóstico Recomendados
* Para auditar conexiones del host al DC: `Get-SmbConnection -ServerName "ad.technoma.local"`

#### Hipótesis Formuladas
| Hipótesis | Detalles y Validación | Veredicto |
| :--- | :--- | :--- |
| **Escaneo WMI / Fuerza Bruta** | Un atacante ejecuta herramientas de descubrimiento de AD (como BloodHound) consultando SAMR. Refutada porque el volumen y duración (9s) corresponden a un flujo acotado de login del usuario. | Refutada |
| **Logon de usuario / GP Update** | El sistema operativo realiza consultas de grupo y sincronización ordinaria de políticas mediante SAMR. | **Confirmada** |

### 🔬 Desglose Ultra Quirúrgico (Caso Completo)
- **Capa de Red/Enrutamiento:** Conexión interna dentro del segmento de administración local `VLAN1101`.
- **Capa de Transporte:** Protocolo TCP (proto 6), puerto origen `64429` y puerto destino `445` (SMB).
- **Capa de Aplicación:** Protocolo SMBv2 con comandos de sistema (`TREE_CONNECT` a `IPC$`, `CREATE` sobre `samr`, `GETINFO`, `READ` y `WRITE` bidireccionales).
- **Motor ML:** El motor `new_ml` detecta la desviación estadística en lecturas y escrituras por separado, detonando dos alertas estadísticas redundantes sobre una sola conexión.

---

# [Parte II] Correlación y Cierre Maestro de Caso

### ❓ ¿Por qué es (o no es) una Amenaza?
**No representa una amenaza.** 
Los dos eventos corresponden a una única conexión legítima de Carlos Alvarez para validar sus credenciales y directivas en Active Directory utilizando el protocolo estándar SAMR. Las llamadas RPC escriben en el named pipe y leen la respuesta, lo cual es interpretado erróneamente por el motor de Machine Learning de Stellar Cyber como dos picos de anomalías de red por separado (Lectura y Escritura).

### 🔐 Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "None",
  "Integrity": "None",
  "Availability": "None",
  "Justification": "Tráfico operativo benigno de autenticación y lectura de directivas GPO. Sin impacto de seguridad."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Verdict": "False_Positive",
  "Confidence_Score": 100,
  "Justification": "Patrón de comandos SMBv2 de lectura y escritura coincidente al 100% con llamadas RPC sobre la tubería samr para procesos nativos de Active Directory."
}
```

### ⚠️ Indicador de Fatiga de Alertas
```json
{
  "Fatigue_Level": "High",
  "Reason": "El SIEM separa una sola conexión benigna en múltiples alertas de anomalía basadas en lecturas y escrituras, aumentando la carga del analista."
}
```

### 🔄 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| **Detección y Análisis** | Cruce de la telemetría de red con el inventario de AD para validar host y usuario. |
| **Contención, Erradicación y Recuperación** | Sin acciones requeridas. |

### 🧪 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| **PB 2.5** | Anomalía de Lectura SMB por Sincronización GPO / SAMR | Proceso de autenticación y refresco de políticas corporativas legítimas. |

### 🏷️ Resolution Tag para Stellar Cyber
* **Tag:** `False Positive`
* **Descripción:** Tráfico benigno SAMR de inicio de sesión y sincronización GPO a través del named pipe en IPC$.

### 📋 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-16 07:39:07 | Antigravity | technoma | 12241 | new_ml (Network NBA) | 12241-M | Baja | False Positive | Falsos positivos por anomalía SMB (lectura/escritura) en named pipe samr | nb-calvarez (192.168.169.16), ad.technoma.local (10.11.1.1) | Peticiones y escrituras de red a través del pipe samr en IPC$ para inicio de sesión y validación GPO | path: \IPC$\samr; comandos SMB: 3, 5, 8, 9, 16 | Ninguna. Actividad benigna y esperada del sistema operativo. | Cerrado | N/A | No | N/A | PB 2.5 |

### ✅ Instrucción para Cierre Maestro en Stellar Cyber
* **Estado:** Cerrado / Falso Positivo
* **Resolution Tag:** `False Positive`
* **Comentario:**
> "Alerta descartada como Falso Positivo. El análisis de metadatos SMB y las trazas de red confirman que los picos de lectura y escritura hacia el named pipe `samr` en el recurso compartido `IPC$` del Controlador de Dominio corresponden a la comunicación RPC estándar del host `nb-calvarez` (`192.168.169.16`) para sincronizar políticas de grupo (GPO) y validar la cuenta del usuario. Comportamiento legítimo y esperado en infraestructura Active Directory."

> [!TIP]
> Dado que las consultas a la tubería `samr` son parte de las operaciones ordinarias de Active Directory, se recomienda ajustar los perfiles de Machine Learning para no alarmar sobre picos de escritura en puertos administrativos internos.
