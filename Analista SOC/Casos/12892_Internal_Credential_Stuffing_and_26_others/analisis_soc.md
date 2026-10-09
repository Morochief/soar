### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Administrative Noise`, `Exchange HealthMailbox`, `Kerberos 4768`, `Credential Stuffing Anomaly`

### Análisis Lote de Eventos (15 Eventos Recibidos)
Se han identificado y analizado 15 eventos individuales de auditoría de seguridad de Windows registrados por los Domain Controllers (`VMBASE8` / `172.16.201.8`) provenientes de peticiones del servidor de correo (`172.16.201.4`).

---

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Internal Credential Stuffing & Internal Account/User Login Failure Anomaly (12892).
* **Activos Involucrados:** Servidor de origen `172.16.201.4` realizando solicitudes Kerberos hacia el Controlador de Dominio `VMBASE8` (`172.16.201.8`) en la red `CAJAANDE.LOCAL`.
* **Cuentas Afectadas:** Cuentas del sistema de monitoreo automático de Microsoft Exchange: `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py` y `HealthMailbox73cb57c1bc0641e48692c639da6248bf@cajaande.local`.
* **Comportamiento Anómalo:** Múltiples fallos consecutivos de autenticación Kerberos (Evento Windows 4768 con código de estado `0x6` - `KDC_ERR_C_CLIENT_NOT_FOUND`). El motor de Machine Learning de Stellar Cyber (`new_ml`) interpretó la ráfaga de consultas fallidas como un ataque de *Credential Stuffing* o *Brute Force*.
* **Causalidad Probable:** Ruido administrativo interno producido por el servicio de monitoreo integrado de Microsoft Exchange Server (*Managed Availability*). Las sondas automáticas del servidor de correo intentan autenticar las cuentas de salud (*HealthMailbox*); si una cuenta fue recreada o posee discrepancias entre el sufijo UPN (`@cajaande.gov.py`) y el reino Kerberos Kerbtgt (`CAJAANDE.LOCAL`), el KDC responde con código `0x6` (Cliente no encontrado).

---

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Cuenta Afectada | Observación Forense |
|---|---|---|---|---|
| 2026-08-01T08:41:37 | 2026-08-01 05:41:37 | Kerberos 4768 Fail | `HealthMailbox0ab06aa4d66...` | Estado Kerberos `0x6` (Client Not Found). |
| 2026-08-01T08:45:00 | 2026-08-01 05:45:00 | Credential Stuffing ML | `HealthMailbox0ab06aa4d66...` | Ráfaga de 146 fallos acumulados en 25 min. |
| 2026-08-01T08:50:12 | 2026-08-01 05:50:12 | Kerberos 4768 Fail | `HealthMailbox73cb57c1bc0...` | Reintentos continuos de la sonda Exchange. |

---

### 🔬 Desglose Técnico y Disección Forense
* **Origen:** `172.16.201.4` (Servidor Microsoft Exchange).
* **Destino:** `VMBASE8` (`172.16.201.8` - Domain Controller / KDC).
* **ID de Evento de Windows:** 4768 (*A Kerberos authentication ticket (TGT) was requested*).
* **Código de Error Kerberos (`Status`):** `0x6` (`KDC_ERR_C_CLIENT_NOT_FOUND`).
* **ServiceName:** `krbtgt/CAJAANDE.LOCAL`.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "WinEventLog:Security (4768)",
  "payload_value": "Kerberos TGT Request Failure",
  "payload_hash": "N/A (Auditoría de Eventos)",
  "payload_firma": "Microsoft-Windows-Security-Auditing",
  "payload_accion": "Failure Audit",
  "payload_destino": "VMBASE8 (172.16.201.8)"
}
```

**Contexto Didáctico del SIEM (Stellar Cyber):**
Los algoritmos de detecciones de identidad de Stellar Cyber monitorean la tasa de fallos de inicio de sesión por cuenta. Cuando un proceso automático genera más de 100 fallos en un intervalo corto, las reglas `internal_cloud_account_login_failure` y `credential_stuffing` se activan automáticamente mapeando la táctica de MITRE T1110 (*Brute Force*). Sin embargo, al inspeccionar el nombre del usuario (`HealthMailbox...`), queda descartada cualquier intencionalidad maliciosa.

### 🧠 ¿Por qué es (o no es) una Threat / Amenaza?
**Es un Falso Positivo (Ruido Administrativo).** Las cuentas `HealthMailbox` son cuentas de servicio internas creadas automáticamente por el motor de autodiagnóstico de Microsoft Exchange. No hay un atacante probando contraseñas; se trata de una sonda de software del propio servidor Exchange solicitando tickets TGT para validar la salud de los buzones.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto.",
  "Integrity": "Sin impacto.",
  "Availability": "Sin impacto en servicios corporativos."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive (Administrative Noise)",
  "Confianza": "100%",
  "Motivo": "Tráfico generado exclusivamente por cuentas de sonda HealthMailbox de Microsoft Exchange Managed Availability con código Kerberos 0x6."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Alta",
  "Razón": "Las sondas de Exchange generan ráfagas constantes de eventos Kerberos si las cuentas HealthMailbox tienen incoherencias UPN."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Inspección de logs WinEvent 4768. Validación de UPN y origen Exchange. |
| Erradicación y Recuperación | N/A (Tráfico de servicio). Opción de tunear la regla ML o reparar las HealthMailbox en Exchange via PowerShell (`Update-HealthMailbox`). |
| Actividad Post-Incidente | Ninguna. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Descarte de alertas de seguridad generadas por servicios legítimos de infraestructura (Exchange probes). |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior / System Service Traffic.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`01/08/2026 08:15 | Analista | technoma | 12892 | Stellar Cyber | - | Baja | Internal Credential Stuffing / Login Failure | Fallos de autenticación Kerberos 4768 en cuentas HealthMailbox de Exchange | 172.16.201.8 | Falso Positivo (Ruido Administrativo). Las alertas de Credential Stuffing fueron gatilladas por la sonda de monitoreo interno de Microsoft Exchange Managed Availability (cuentas HealthMailbox0ab06... y HealthMailbox73cb...) solicitando tickets TGT con error 0x6 (Client Not Found). Es tráfico de diagnóstico automatizado sin impacto de seguridad. | Windows EventLog | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo validado. Las alertas asociadas al lote 12892 ("Internal Credential Stuffing" e "Internal Account Login Failure") se originaron por el tráfico de autodiagnóstico del servidor Microsoft Exchange (`172.16.201.4`). Las cuentas involucradas corresponden a buzones de salud (*HealthMailbox*) de Exchange Managed Availability fallando la autenticación Kerberos (Event ID 4768, Status `0x6`). No constituye un ataque de fuerza bruta ni compromiso de credenciales. Se procede al cierre administrativo del ticket.

> [!TIP]
> **Sugerencia de Mantenimiento:** Para eliminar la fatiga por estas alertas, se recomienda ejecutar en el servidor de Exchange el script de mantenimiento `Update-HealthMailbox.ps1` o agregar una excepción en Stellar Cyber para nombres de cuenta que comiencen con `HealthMailbox*`.

---

### 🔬 Desglose Ultra Quirúrgico

* **Capa 1: Origen y Enrutamiento (`srcip` / `computer_name`)**
  - `srcip`: `172.16.201.4` (Servidor Exchange).
  - `computer_name`: `VMBASE8` (`172.16.201.8` - Controlador de Dominio principal).
* **Capa 2: Aplicación y Evento (`msg_class` / `event_id`)**
  - `msg_class`: `Microsoft-Windows-Security-Auditing`.
  - `event_id`: `4768` (Solicitud de Ticket TGT Kerberos).
* **Capa 3: Identidad y Fallo (`TargetUserName` / `Status`)**
  - `TargetUserName`: `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py`.
  - `Status`: `0x6` (`KDC_ERR_C_CLIENT_NOT_FOUND`). Significa que el KDC no encuentra la cuenta exacta en Active Directory debido a descalce de UPN o reconstrucción de buzones de monitoreo.
* **Capa 4: Motor de ML (`event_source` / `weighted_anomaly_score`)**
  - `event_source`: `new_ml`.
  - `weighted_anomaly_score`: `1301`. El modelo matemático acumula los 146 intentos fallidos en ventanas de 5 minutos y dispara la firma de anomalía por volumen.

**Resumen Quirúrgico Final:** El servidor de correo de la infraestructura (`172.16.201.4`) realiza peticiones Kerberos recurrentes al Domain Controller `VMBASE8` para validar la disponibilidad de los servicios de transporte mediante cuentas automáticas `HealthMailbox`. Debido a discrepancias en el nombre del cliente Kerberos, el DC devuelve el error auditor `0x6`. El motor de ML de Stellar interpreta la frecuencia como fuerza bruta (*Credential Stuffing*), cuando en realidad es un proceso automático recurrente de mantenimiento de Microsoft Exchange.
