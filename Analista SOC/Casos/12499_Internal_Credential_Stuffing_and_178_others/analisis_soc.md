### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `Credential Stuffing`, `Login Failure Anomaly`, `False Positive`, `HealthMailbox`, `Exchange Managed Availability`.

### Análisis Eventos 1 al 179 (Lote Agrupado por Identidad de Patrón)
*Nota del analista: Los 179 eventos contenidos en este volcado comparten exactamente la misma huella técnica, origen, destino, y código de error. Se analizan de forma conjunta para identificar la causa raíz de la saturación estadística.*

### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Threat Names:** `cloud_account_login_failure`, `credential_stuffing`, `internal_cloud_account_login_failure`
* **Host IP (Origen):** `172.16.201.4` (`VM-MARANDU`)
* **Host IP (Destino DC):** `172.16.201.8` (`VMBASE8`)
* **User Name:** `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6@cajaande.gov.py`
* **Description:** In internal traffic... the target domain "CAJAANDE.LOCAL" has been observed executing an anomalously large number of username/password authentication combinations. The observed rate of login failures... is 32.98.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-22T07:51:29Z | N/A | Kerberos Auth Failure | 146 fails | 0 | N/A | Fallos constantes y cíclicos de autenticación Kerberos (EventID 4768) cada 5 minutos. |

### 🔬 Desglose Técnico y Disección Forense
* El servidor `VM-MARANDU` (`172.16.201.4`) está enviando continuamente solicitudes de Ticket-Granting Ticket (TGT) Kerberos al Controlador de Dominio `VMBASE8` (`172.16.201.8`).
* Todas las solicitudes utilizan la misma cuenta: `HealthMailbox0ab06aa4d6694324a4ef2ee8dfd51dc6`.
* El Domain Controller rechaza las peticiones con el Status Code `0x6` (Client not found in Kerberos database).
* El motor analítico de Stellar Cyber observa el alto volumen de rechazos (146+ fallos por bloque de 25 minutos) y lo escala automáticamente como `Credential Stuffing` (Fuerza Bruta / T1110).
* **Cruce de Memoria Institucional:** Según `SOC_GEM_v2.md`, las cuentas "HealthMailbox" son generadas automáticamente por el componente `Managed Availability` de Microsoft Exchange para monitorear la salud de las bases de datos.
* El servidor `VM-MARANDU` presenta "deuda técnica" (migración de Exchange incompleta o mal purgada). Como resultado, el servicio de Exchange sigue intentando validar el estado del sistema utilizando `HealthMailboxes` que ya no existen en el Active Directory, generando un bucle infinito de fallos Kerberos `0x6`.

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo de Ataque**. No existe un atacante intentando adivinar contraseñas (Fuerza Bruta) ni inyectando credenciales robadas (Credential Stuffing). Se trata de un servicio interno de Microsoft Exchange (`Managed Availability`) funcionando mal y saturando los logs de auditoría (Event ID 4768) debido a un error de configuración o limpieza post-migración. La cuenta no existe, por lo que no hay riesgo de compromiso (impacto nulo).

### ⚖️ Análisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Intacta.",
  "Integridad": "Intacta.",
  "Disponibilidad": "Intacta. El volumen de logs es molesto, pero no llega a constituir una Denegación de Servicio (DoS) para el KDC."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo de Ataque (Ruido Administrativo / Deuda Técnica)",
  "Confianza": "100%",
  "Justificacion": "El patrón cíclico, el nombre de cuenta (HealthMailbox) y el código de error (0x6) concuerdan con la firma documentada de deuda técnica en servidores Exchange, descartando actividad adversaria."
}
```

### 🥱 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Crítica",
  "Motivo": "La generación de 179 alertas redundantes por el mismo fallo técnico inunda la consola del SOC, ocultando potencialmente alertas legítimas de fuerza bruta."
}
```

### 🛡️ Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Eradication & Recovery | El equipo de Infraestructura debe detener el servicio de Exchange en `VM-MARANDU` o recrear/purgar correctamente las HealthMailboxes para silenciar la alerta de raíz. |

### 📘 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-OPS-03 | Ruido de Infraestructura Obsoleta | Aplicable a sistemas internos que generan altos volúmenes de telemetría de fallos por desconfiguración (no maliciosos). |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Falla de sistema / Ruido administrativo de Exchange.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-22 07:51 | Antigravity | technoma | 12499 | new_ml | N/A | Medium | credential_stuffing | FP Kerberos Fails (HealthMailbox) | VM-MARANDU (172.16.201.4), VMBASE8 (172.16.201.8) | Lote masivo de 179 fallos de autenticación 4768 (Status 0x6) generados por HealthMailbox de Exchange obsoleto. Mapeado a Credential Stuffing erróneamente | Logs KDC | Exclusión en SIEM y purga en Infra | Cerrado | N/A | NO | N/A | PB-OPS-03 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:**
Falso Positivo de ciberataque. El lote masivo de alertas de `Credential Stuffing` y `Login Failure Anomaly` (179 eventos) corresponde a ruido administrativo puro, generado por deuda técnica en el servidor `VM-MARANDU` (`172.16.201.4`). Este servidor está ejecutando el servicio `Managed Availability` de Exchange, intentando validar cíclicamente cuentas de monitoreo interno (`HealthMailbox...`) contra el controlador de dominio `VMBASE8`. Dado que estas cuentas ya no existen en el directorio (Status `0x6`), se generan cientos de fallos de autenticación (EventID 4768) por hora. Stellar Cyber interpreta estadísticamente este volumen como un ataque de fuerza bruta (MITRE T1110), pero la intencionalidad es nula. Se cierra el caso.
> [!TIP]
> Esta firma está documentada en SOC_GEM_v2.md bajo el apartado "Ruido del Exchange Residual". Se recomienda aplicar una regla de supresión (silencing rule) en Stellar Cyber para este par IP Origen-Destino si Infraestructura no corrige el servicio.
```
