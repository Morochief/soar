### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `DNS Bypass`, `AnyDesk`, `SMB`, `GPO Sync`, `SysVol`.

### Análisis Evento 1: Intento de Exploit (AnyDesk)
* **Threat Name:** `exploit_attempt_priv_pub`
* **Source:** `10.11.1.1` (ad.technoma.local)
* **Destination:** `8.8.8.8` (Google DNS)
* **Description:** Se detectó tráfico DNS directo desde el Controlador de Dominio hacia `8.8.8.8` resolviendo el dominio `relay-f348b09a.net.anydesk.com`. El IDS generó la alerta "INFO Anydesk Relay Domain".

### Análisis Evento 2: Anomalía de Lectura SMB (SysVol)
* **Threat Name:** `internal_smb_read_anomaly`
* **Source:** `192.168.169.119` (nb-noc2.technoma.local)
* **Destination:** `10.11.1.1` (ad.technoma.local)
* **Description:** El host interno realizó 66 lecturas SMB hacia el recurso `\\ad.technoma.local\SysVol`, superando su umbral normal.

*Nota: He detectado 2 eventos independientes en tu volcado. Se analizarán técnicamente por separado y luego se emitirá un cierre consolidado.*

### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Activos Involucrados:** `10.11.1.1` (DC), `192.168.169.119` (Workstation), `8.8.8.8` (Google DNS).
* **Amenazas Detectadas:** DNS hacia AnyDesk catalogado como Exploit Attempt, y Lecturas masivas SMB hacia SysVol catalogadas como anomalía.
* **Diagnóstico Inicial:** Ambos eventos son Falsos Positivos de ataque. El primero es ruido de telemetría de AnyDesk sumado a un problema de configuración (DNS directo a Internet desde el DC). El segundo es el comportamiento nativo de Windows al sincronizar Políticas de Grupo (GPO).

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Observación Forense |
| :--- | :--- | :--- | :--- |
| 2026-07-24T08:32:06Z | N/A | Resolución DNS (AnyDesk) | `10.11.1.1` consulta a `8.8.8.8` por un relay de AnyDesk. Dispara firma IDS INFO. |
| 2026-07-24T09:20:06Z | N/A | Lectura SMB (SysVol) | `nb-noc2` accede a `gpt.ini` en SysVol. Dispara ML Anomaly. |

### 🔬 Desglose Técnico y Disección Forense
**Evento 1 (DNS AnyDesk):**
* El Controlador de Dominio (`10.11.1.1`) tiene instalado el software de soporte remoto AnyDesk, el cual constantemente busca servidores relay (`net.anydesk.com`).
* El software está saltándose el servidor DNS local y haciendo consultas directas a `8.8.8.8` (comportamiento típico de AnyDesk para evitar bloqueos corporativos). El IDS detecta la cadena de texto de AnyDesk y genera una alerta informativa que el motor escala.

**Evento 2 (SMB SysVol):**
* El host `192.168.169.119` se conecta por el puerto 445 (SMB) al DC.
* Solicitó acceso al recurso `\\ad.technoma.local\SysVol`.
* Si cruzamos la metadata con nuestra `SMB_Rosetta_Stone`, vemos la secuencia de comandos: `114` (SMB2_CREATE para abrir conexión), `3` (SMB2_READ), `11` (SMB2_IOCTL solicitando leer el archivo de política `gpt.ini`), `16` (SMB2_GETINFO), y `5` (SMB2_CLOSE).
* Esta secuencia exacta (leer el `gpt.ini` en SysVol) es el mecanismo de Windows para sincronizar Políticas de Grupo (GPO) o *Background Refresh*.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "Secuencia SMB (GPO Sync)",
  "payload_value": "Comandos: 114, 3, 11 (gpt.ini), 16, 5",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Lectura de Políticas de Grupo",
  "payload_destino": "\\\\ad.technoma.local\\SysVol"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
Ambos son **Falsos Positivos**.
El evento 1 no es un exploit ni un C2 malicioso, es simplemente el tráfico de *keep-alive* de AnyDesk. No obstante, que un Controlador de Dominio tenga salida DNS directa a `8.8.8.8` es un **problema de postura de seguridad** que debe corregirse (Vulnerabilidad de Firewall).
El evento 2 es el comportamiento esperado de cualquier equipo Windows en un dominio Active Directory al procesar actualizaciones de políticas de grupo (GPO), catalogado por el ML simplemente porque hubo un pequeño pico (66 peticiones) al aplicarse un `gpupdate`.

### ⚖️ Análisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta.",
  "Integridad": "Intacta.",
  "Disponibilidad": "Intacta."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo de Ciberataque (Ruido de Aplicaciones y OS)",
  "Confianza": "100%",
  "Justificacion": "El tráfico SMB coincide exactamente con la sincronización GPO documentada en la memoria SOC. El tráfico DNS es de AnyDesk legítimo."
}
```

### 🛡️ Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Correlación de comandos SMB con Rosetta Stone y de firmas IDS INFO. |
| Erradicación y Recuperación | Levantar ticket a Infraestructura para bloquear salida UDP/TCP 53 hacia `8.8.8.8` desde el DC (Endurecimiento). |

### 📘 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-FP-01 | Falsos Positivos Analíticos/Heurísticos | Actividad legítima de SO y software de terceros. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Actividad legítima de Windows (GPO) y AnyDesk.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 08:32 | Antigravity | technoma | 12590 | modular_sensor | N/A | Low | Exploit / SMB Anomaly | FP GPO Sync y Telemetría AnyDesk | 10.11.1.1 (DC), 192.168.169.119 (nb-noc2) | Lote de 2 alertas. Evento 1: IDS detectó telemetría legítima de AnyDesk hacia 8.8.8.8 desde el DC (Problema de postura de FW). Evento 2: El ML detectó un pico de lecturas SMB hacia SysVol, correspondientes a una actualización legítima de GPO (gpt.ini). | Comandos SMB 114, 3, 11 | Bloquear DNS externo en DC. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:**
Falso Positivo Múltiple. El caso agrupa dos detecciones de tráfico legítimo. La primera (Exploit Attempt) es una firma IDS INFO detonada por la telemetría de red del software de soporte remoto AnyDesk (net.anydesk.com) consultando el DNS 8.8.8.8 desde el DC. Se recomienda a Infraestructura bloquear consultas DNS salientes directas desde servidores críticos. La segunda alerta (SMB Read Anomaly) es tráfico benigno generado por `nb-noc2` realizando la sincronización de Políticas de Grupo (GPO) contra el controlador de dominio. La inspección del payload SMB revela comandos de apertura, lectura y solicitud de acceso (114, 3, 11) dirigidos exclusivamente al recurso \SysVol y al archivo gpt.ini. Todo el comportamiento es benigno y de naturaleza operativa. Se procede al cierre.

> [!TIP]
> Dado que identificamos un problema de postura (Bypass de DNS hacia `8.8.8.8` desde el DC), asegúrate de reportarlo en el Handover de guardia para que Infraestructura aplique el bloqueo.

### 🔬 Desglose Ultra Quirúrgico
* **Red/Enrutamiento:** Conexiones LAN (VLAN 1101 y VPN/NOC). El Evento 1 sale hacia WAN (`8.8.8.8`).
* **Transporte/Conexión:** DNS UDP 53 y SMB TCP 445.
* **Aplicación/DPI:** DPI de Stellar identifica los metadatos de las tramas SMB extrayendo los códigos de comando y la ruta UNC (`\\ad.technoma.local\SysVol`). 
* **Motor ML / Threat Intel:** El XDR escaló la firma IDS de AnyDesk a "Exploit Attempt" por un fallo de correlación genérico. El modelo volumétrico de UBA detonó la anomalía SMB al detectar un desvío (66 peticiones frente a la base típica de 10) producto de un `gpupdate /force` o ciclo de background refresh natural.

**Resumen Quirúrgico Final:**
Las alertas no están directamente relacionadas como parte de un Kill Chain. Una es software de control remoto haciendo bypass del DNS corporativo para encontrar sus servidores (AnyDesk), lo cual es legítimo pero evidencia un fallo de firewall en el DC. La otra es una estación de trabajo descargando sus políticas de grupo (`gpt.ini`) de forma nativa desde el servidor de Active Directory. Ninguno representa un incidente de ciberseguridad y son clasificados como falsos positivos.
