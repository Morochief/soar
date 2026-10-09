### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `Cloud Drive`, `Data Exfiltration`, `UBA`, `True Positive (Benigno)`, `Shadow IT`.

### 📊 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Threat Name:** `cloud_drive_data_exfiltration_anomaly`
* **Actor / Usuario Externo:** `mcaceresvillanueva55@gmail.com` (Marcos Caceres, empleado interno)
* **Propietario del Recurso:** `manuelazcona@technoma.com.py` (Usuario Interno de AD)
* **Description:** An unusual number of Google Workspace file downloads (10074) was observed from the user mcaceresvillanueva55@gmail.com in a 24-hour interval.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Observación Forense |
| :--- | :--- | :--- | :--- |
| 2026-07-23T02:05:33Z | N/A | Pico Volumétrico Detectado | El modelo de UBA detectó la descarga masiva y disparó la alerta. |
| 2026-07-24T08:14:00-03:00 | 08:14 AM | Confirmación del Usuario | Manuel Azcona confirma por WhatsApp que compartió los instaladores de TEDs (app KAL) con el empleado Marcos Caceres a su correo personal por problemas de bloqueo en la notebook corporativa de este último. |

### 🏛️ El Concilio SOC ha deliberado
> **Problema a analizar:** El SIEM alertó sobre la descarga de 10.074 archivos desde la unidad compartida de Google Drive de `manuelazcona` hacia una cuenta externa de Gmail. Los archivos tienen extensiones `.sqlite`, `.wasm`, `.png`, `.woff2`.

🔴 **Perspectiva Red Team:**
Inicialmente evaluado como exfiltración. Tras la confirmación, se observa el uso de canales no corporativos (Gmail personal) para evadir controles corporativos (Shadow IT) debido a fricciones tecnológicas (bloqueos en la notebook).

🔵 **Perspectiva Blue Team:**
Sincronización legítima de archivos de desarrollo / instaladores (KAL / TEDs). No hay robo de datos por parte de terceros externos. 

🟢 **Perspectiva Threat Intel:**
Riesgo de fuga de datos por uso de cuentas personales. Es un incidente de Gobernanza, no un ciberataque.

---

### 🧠 Síntesis y Decisión Final (Antigravity Mentor)
El incidente es un **True Positive (Benigno)**. La exfiltración fue real en el sentido de que los datos corporativos salieron hacia una cuenta de correo de terceros (Gmail), pero fue autorizada y ejecutada por empleados legítimos como "workaround" (solución alternativa) ante un bloqueo tecnológico en el equipo del receptor. 
El veredicto para el SIEM es **Cerrado - Actividad Confirmada (Excepción Autorizada)**. Internamente se deberá notificar a Infraestructura que hay problemas con la descarga de instaladores en las notebooks que fomenta prácticas de Shadow IT.

### ⚖️ Análisis de Impacto CIA Triad
```json
{
  "Confidencialidad": "Baja (Código fuente a cuenta personal de empleado legítimo)",
  "Integridad": "Intacta.",
  "Disponibilidad": "Intacta."
}
```

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "True Positive Benigno (Excepción de Operaciones / Shadow IT)",
  "Confianza": "100%",
  "Justificacion": "Confirmación directa del propietario del archivo (Manuel Azcona). Indicó que el destinatario externo es el empleado Marcos Caceres usando su correo personal para evadir un bloqueo corporativo que le impedía descargar instaladores."
}
```

### 🛡️ Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Análisis de archivos y verificación Out-of-Band (WhatsApp) con el usuario. |
| Erradicación y Recuperación | Se toma conocimiento del evento. Se recomienda a Infraestructura revisar los bloqueos en las notebooks para evitar el uso de correos personales. |

### 📘 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-DLP-01 | Cloud Data Loss Prevention | Monitoreo de compartición a dominios externos. |

### 🏷️ Resolution Tag para Stellar Cyber
`True Positive` (o `Authorized Exception` según disponibilidad en consola) - Actividad legítima (Workaround operativo).

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 | Antigravity | technoma | 12545 | gsuite_Workspace-THN | N/A | High | Data Exfiltration | TP Exfiltración Benigna (Shadow IT autorizado) | manuelazcona@technoma.com.py | Confirmado por Manuel Azcona vía WhatsApp: se compartió instaladores de la app KAL (TEDs) al empleado Marcos Caceres a su Gmail personal porque su notebook corporativa bloqueaba la descarga. | Captura de WhatsApp de Azcona. | Ninguna (Evento en conocimiento). | Cerrado | N/A | NO | N/A | PB-DLP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** True Positive / Authorized Exception
**Comentario:**
Actividad Confirmada Benigna (Excepción Autorizada / Shadow IT). Tras contactar al usuario `manuelazcona` vía Out-of-Band (WhatsApp), confirmó ser el responsable de la acción. Indicó que compartió los instaladores de desarrollo (app KAL para TEDs) al compañero Marcos Caceres utilizando su correo personal de Gmail (`mcaceresvillanueva55@gmail.com`), debido a que la notebook corporativa de este último presentaba bloqueos que le impedían descargar los recursos internamente. Se cierra el evento al tratarse de una operación legítima de trabajo, pero se deja constancia del riesgo de fuga de datos asociado al uso de correos personales para evadir restricciones de infraestructura.
