# Reporte SOC - Caso: Internal Account Login Failure Anomaly (HealthMailbox - VMBASE8)

**Tenant:** Caja de Jubilaciones y Pensiones del Personal de la ANDE (`cajaande`) | **Sensor:** Agente Stellar Cyber en `VMBASE8` (`172.16.201.8`) | **Dispositivo:** `VMBASE8` (DC principal)  
**XDR Event:** Internal Account Login Failure Anomaly (`internal_cloud_account_login_failure`) / Internal User Login Failure Anomaly (`internal_user_login_fail`) | **Técnica:** T1110 (Brute Force) | **Táctica:** TA0006 (Credential Access) | **Kill Chain:** Exploitation

---

## Declaración de Conteo Inicial
Se han detectado **10 eventos independientes** en el lote de alertas nativas de Interflow/Stellar Cyber:
- **Evento 1 (ID Anomaly: `0DSoj6ABI3UnQyDOC01i` | Doc 1):** Alerta `internal_cloud_account_login_failure_kerberos` registrada a las 09:00:06 UTC sobre `VMBASE8` por 1274 fallos acumulados en la cuenta `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py` desde `172.16.201.4`.
- **Evento 2 (ID Anomaly: `0DSoj6ABI3UnQyDOC01i` | Doc 2):** Alerta emparejada `internal_user_login_fail_kerberos` registrada a las 09:00:06 UTC para el mismo evento Kerberos 4768 con código de error `Status 0x6`.
- **Evento 3 (ID Anomaly: `-DSpj6ABI3UnQyDObVj1` | Doc 3):** Alerta `internal_cloud_account_login_failure_kerberos` a las 09:05:06 UTC (ventana recurrente de 5 minutos).
- **Evento 4 (ID Anomaly: `-DSpj6ABI3UnQyDObVj1` | Doc 4):** Alerta emparejada `internal_user_login_fail_kerberos` a las 09:05:06 UTC.
- **Evento 5 (ID Anomaly: `SDSuj6ABI3UnQyDOdH3f` | Doc 5):** Alerta `internal_cloud_account_login_failure_kerberos` a las 09:30:06 UTC (ventana agregada de 25 minutos).
- **Evento 6 (ID Anomaly: `SDSuj6ABI3UnQyDOdH3f` | Doc 6):** Alerta emparejada `internal_user_login_fail_kerberos` a las 09:30:06 UTC.
- **Evento 7 (ID Anomaly: `SDSuj6ABI3UnQyDOdH3f` | Doc 7):** Duplicado de telemetría de agente en `VMBASE8` para la ventana de las 09:30:06 UTC.
- **Evento 8 (ID Anomaly: `VDSyj6ABI3UnQyDOlZ_D` | Doc 8):** Alerta `internal_cloud_account_login_failure_kerberos` a las 09:50:06 UTC (ventana de 20 minutos).
- **Evento 9 (ID Anomaly: `VDSyj6ABI3UnQyDOlZ_D` | Doc 9):** Alerta emparejada `internal_user_login_fail_kerberos` a las 09:50:06 UTC.
- **Evento 10 (ID Anomaly: `sDXAj6ABI3UnQyDOUBLX` | Doc 10):** Alerta `internal_cloud_account_login_failure_kerberos` a las 10:50:06 UTC (persistencia de la cadencia automática horaria).

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#RuidoOperativo` `#InternalAccountLoginFailure` `#Exchange` `#HealthMailbox` `#ManagedAvailability` `#Kerberos` `#Event4768` `#VMBASE8`

---

## Análisis Evento 1 y 2 (Anomaly ID: 0DSoj6ABI3UnQyDOC01i)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** La dirección IP interna `172.16.201.4` (servidor de correo Microsoft Exchange `VM-MARANDU`) generó solicitudes continuas de tickets TGT Kerberos hacia el Controlador de Dominio `VMBASE8` (`172.16.201.8`) para la cuenta sintética `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py`.
* **Acción de Seguridad:** El servicio KDC en `VMBASE8` rechazó las peticiones con código de estado `0x6` (`KDC_ERR_C_PRINCIPAL_UNKNOWN`), registrando el evento de auditoría de seguridad Windows `4768`.
* **Causa Raíz:** Desincronización de sufijo UPN provocada por la configuración de Microsoft Exchange Managed Availability (`MSExchangeHM`). Las sondas sintéticas de monitorización utilizan el dominio default de la directiva de correo (`@cajaande.gov.py`), mientras que la cuenta de salud en Active Directory tiene configurado el UPN con sufijo del bosque (`@cajaande.local`).
* **Mapeo en SIEM (Stellar Cyber):** El motor analítico disparó dos reglas en paralelo (`internal_cloud_account_login_failure` e `internal_user_login_fail`) al acumular 1274 intentos fallidos, clasificándolo erróneamente bajo la técnica MITRE `T1110 (Brute Force)`.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 09:00:06 | 2026-09-11 06:00:06 | Event ID 4768 (KDC TGT) | 1274 fallos | Basal ML | Alto | Solicitud rechazada con Status `0x6` (`KDC_ERR_C_PRINCIPAL_UNKNOWN`). |
| 2026-09-11 09:02:15 | 2026-09-11 06:02:15 | Ingesta de Agente Stellar | Interflow Log | - | - | Agente en `VMBASE8` procesa evento de log de seguridad. |
| 2026-09-11 09:10:02 | 2026-09-11 06:10:02 | Disparo de Alerta ML | Severidad 70 | - | - | Creación de anomalías paralelas de Login Failure en Stellar Cyber. |

### Desglose Técnico y Disección Forense
* **Flujo de Autenticación:** `172.16.201.4` (`VM-MARANDU`) -> `172.16.201.8:88` (`VMBASE8`, Kerberos KDC).
* **Servicio Solicitado:** `krbtgt/CAJAANDE.LOCAL` (Ticket Granting Ticket).
* **Parámetros Criptográficos:** Tipo de cifrado `0x12` (`AES256-CTS-HMAC-SHA1-96`), opciones de ticket `0x40810010`, tipo de preautenticación `0`.
* **Identidad:** `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py`. Es un buzón sintético de Exchange utilizado exclusivamente para pruebas de disponibilidad interna.

```json
/* Payload / Evidencia Principal: */
{
  "payload_type": "Windows Security Audit 4768",
  "payload_value": "TargetUserName=HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py ServiceName=krbtgt/CAJAANDE.LOCAL Status=0x6 IpAddress=::ffff:172.16.201.4",
  "payload_hash": "N/A",
  "payload_firma": "Microsoft-Windows-Security-Auditing:4768",
  "payload_accion": "deny_kdc",
  "payload_destino": "VMBASE8 (172.16.201.8:88)"
}
```

#### Hipótesis Formuladas
| ID | Hipótesis | Evaluación | Justificación Forense |
| :--- | :--- | :--- | :--- |
| H1 | Ataque de fuerza bruta o password spraying | Descartada | La IP origen es el servidor de Exchange legítimo; el usuario es una cuenta interna de monitoreo; no se prueban múltiples contraseñas ni múltiples usuarios. |
| H2 | Intento de explotación o movimiento lateral Kerberoasting | Descartada | No se solicita Service Ticket TGS a cuentas con SPN vulnerable; se solicita TGT básico y el error es principal inexistente (Status 0x6). |
| H3 | Ruido operativo por desalineación de UPN en Exchange Managed Availability | Confirmada | Corresponde al comportamiento documentado en `Casos/CajaAnde_HealthMailbox/diagnostico_soc.md`. El servicio `MSExchangeHM` envía el probe con `@cajaande.gov.py` en vez de `@cajaande.local`. |

---

## Análisis Eventos 3 al 10 (Persistencia Temporal Recurrente)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** Ráfagas automáticas idénticas de solicitudes TGT Kerberos para `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py` desde `172.16.201.4` hacia `VMBASE8` registradas en ventanas sucesivas (09:05, 09:30, 09:50 y 10:50 UTC).
* **Acción de Seguridad:** El KDC mantiene la denegación consistente con `Status 0x6`.
* **Correlación con Eventos Previos:** Se confirma un ciclo determinista y permanente generado por temporizadores de Windows Services (`MSExchangeHM`), descartando cualquier componente interactivo o malicioso.

### Línea de Tiempo Temporal Consolidada (Eventos 3 al 10)
| Hora (UTC) | Hora (Local GMT-3) | Evento Detectado | Anomaly ID | Status Kerberos | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 09:05:06 | 2026-09-11 06:05:06 | Eventos 3 y 4 | `-DSpj6ABI3UnQyDObVj1` | `0x6` | Reintento a los 5 minutos exactos del probe. |
| 2026-09-11 09:30:06 | 2026-09-11 06:30:06 | Eventos 5, 6 y 7 | `SDSuj6ABI3UnQyDOdH3f` | `0x6` | Ejecución de sondeo tras ventana de 25 minutos. |
| 2026-09-11 09:50:06 | 2026-09-11 06:50:06 | Eventos 8 y 9 | `VDSyj6ABI3UnQyDOlZ_D` | `0x6` | Ciclo recurrente a los 20 minutos. |
| 2026-09-11 10:50:06 | 2026-09-11 07:50:06 | Evento 10 | `sDXAj6ABI3UnQyDOUBLX` | `0x6` | Mantenimiento continuo del patrón determinista de sondeo. |

---

## ¿Por qué es (o no es) una Amenaza?
No representa una amenaza para la seguridad de la organización. La actividad corresponde a un comportamiento estándar de auto-monitorización de Microsoft Exchange Server (función Managed Availability implementada por el servicio `MSExchangeHM`). Dichas sondas evalúan periódicamente la salud de los servicios de transporte y buzones simulando inicios de sesión. Al existir una discrepancia entre el dominio primario configurado en la Email Address Policy (`cajaande.gov.py`) y el sufijo UPN real de la cuenta en el Directorio Activo (`cajaande.local`), el KDC rechaza la solicitud de autenticación Kerberos. No existe riesgo de compromiso, filtración ni alteración de datos.

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "No existio acceso no autorizado a informacion, alteracion de credenciales ni indisponibilidad de los servicios criticos de correo o directorio activo."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Operativo / Error de Configuracion de Exchange HealthMailbox",
  "justificacion": "Peticiones TGT Kerberos automatizadas originadas por el servicio legitimo MSExchangeHM desde el servidor Exchange 172.16.201.4 hacia el DC 172.16.201.8, rechazadas por disparidad de dominio UPN (Status 0x6)."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Muy Alta",
  "frecuencia": "10 eventos generados en una ventana de menos de 2 horas sobre el mismo host y usuario",
  "razon": "Stellar Cyber correlaciona la cantidad acumulada de fallos de sondas internas como anomalías de fuerza bruta T1110.",
  "accion_recomendada": "Implementar regla de supresion en Stellar Cyber para solicitudes Kerberos 4768 de HealthMailbox* provenientes de 172.16.201.4 hacia 172.16.201.8."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Análisis de logs de seguridad 4768, validación de host origen Exchange (`computers_and_servers.md`) y diagnóstico de UPN mismatch. |
| Contención, Erradicación y Recuperación | No aplica contención ni aislamiento sobre activos críticos de producción (DC / Exchange). |
| Post-Incidente | Notificación al equipo de Infraestructura/Exchange para ajustar la directiva de Accepted Domains / Email Address Policy o UPN de HealthMailboxes. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB 5.2 | Problemas de Configuración, Postura y Servicios Vulnerables Abiertos | Gestión y documentación de discrepancias de configuración en servicios internos de autenticación y correo. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta cerrada como falso positivo operativo originado por pruebas sintéticas de Microsoft Exchange Managed Availability con UPN no resuelto en KDC.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11/09/2026 10:50 | Analista SOC | cajaande | 0DSoj6ABI3UnQyDOC01i | VMBASE8 (Stellar Agent) | - | Baja | Internal Account Login Failure Anomaly | Fallos Kerberos de sonda Exchange HealthMailbox contra VMBASE8 | VMBASE8 (172.16.201.8), VM-MARANDU (172.16.201.4), HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py | 10 alertas correlacionadas. FP operativo: sondas de monitoreo de Exchange Managed Availability generan solicitudes Kerberos (Event 4768) rechazadas por Status 0x6 debido a desalineación de sufijo UPN. Sin riesgo. | Windows Security 4768 (Status: 0x6 KDC_ERR_C_PRINCIPAL_UNKNOWN, TargetUserName: HealthMailbox...@cajaande.gov.py, IpAddress: 172.16.201.4) | Notificar a Sysadmin/Exchange para alinear UPN de cuentas HealthMailbox y aplicar regla de supresión en XDR. | Cerrado | - | No | - | PB 5.2 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro:**
> Se analizaron 10 eventos correlacionados bajo las alertas Internal Account Login Failure Anomaly e Internal User Login Failure Anomaly sobre el Controlador de Dominio VMBASE8 (172.16.201.8).
> 
> Los registros de auditoría de Windows (Event ID 4768) confirman que las peticiones provienen del servidor Microsoft Exchange VM-MARANDU (172.16.201.4) y corresponden a la cuenta sintética HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py. Los fallos son causados por Status 0x6 (KDC_ERR_C_PRINCIPAL_UNKNOWN) debido a que el servicio MSExchangeHM ejecuta sondas de salud utilizando el sufijo default SMTP (@cajaande.gov.py), mientras que la cuenta en Active Directory posee su UPN bajo @cajaande.local.
> 
> Evento descartado como Falso Positivo Operativo / Ruido de Configuración. No existe actividad de fuerza bruta ni compromiso de credenciales. Caso cerrado.

---

### Desglose Ultra Quirúrgico
* **Capa de Red y Enrutamiento:**
  * `hostip`: `172.16.201.8` (`VMBASE8`, Domain Controller de `CAJAANDE.LOCAL`).
  * `srcip`: `172.16.201.4` (`VM-MARANDU`, Servidor Exchange en Windows Server 2012 R2 Standard).
  * Enrutamiento interno directo dentro de la VLAN de servidores de infraestructura (`172.16.201.0/24`).
* **Capa de Transporte y Conexión:**
  * Protocolo: TCP/UDP puerto `88` (Kerberos Authentication Service).
  * `service_id`: `CAJAANDE.LOCAL` / `ServiceName: krbtgt/CAJAANDE.LOCAL`.
* **Capa de Aplicación y Protocolo (Kerberos):**
  * `event_id`: `4768` (A Kerberos authentication ticket (TGT) was requested).
  * `TargetUserName`: `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py`.
  * `Status`: `0x6` (`KDC_ERR_C_PRINCIPAL_UNKNOWN` - El cliente no fue hallado en la base de datos Kerberos bajo el reino/sufijo especificado).
  * `TicketOptions`: `0x40810010`.
  * `TicketEncryptionType`: `0x12` (`AES256-CTS-HMAC-SHA1-96`).
  * `PreAuthType`: `0` (Sin preautenticación).
* **Capa de Detección XDR y Motor ML:**
  * `xdr_event.name`: `internal_cloud_account_login_failure` e `internal_user_login_fail`.
  * `accumulated_anomalous_failures`: `1274`.
  * `fidelity`: `98.41`, `event_score`: `70`, `severity`: `medium`.
  * Asignación errónea a MITRE ATT&CK T1110 (Brute Force) basada únicamente en volumen estadístico de fallos acumulados en ventanas de tiempo de 5 y 25 minutos.

**Resumen Quirúrgico Final:**  
El servicio legítimo de monitorización `MSExchangeHM` alojado en el servidor Exchange `172.16.201.4` ejecuta periódicamente sondas de disponibilidad sintéticas solicitando tickets TGT al KDC de `VMBASE8` (`172.16.201.8`) para la cuenta `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py`. Al existir una inconsistencia entre el dominio configurado en la política de correo (`cajaande.gov.py`) y el UPN registrado en Active Directory (`cajaande.local`), el KDC rechaza las solicitudes con error Kerberos `0x6`. El motor de Machine Learning de Stellar Cyber agrupa los 1274 fallos acumulados y emite alertas de fuerza bruta. La actividad es 100% legítima, inocua y catalogada como Falso Positivo Operativo por error de configuración interna.
