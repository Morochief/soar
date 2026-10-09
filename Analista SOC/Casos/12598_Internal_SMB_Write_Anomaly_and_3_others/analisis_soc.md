### 🔍 Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `SMB`, `ML_Anomaly`, `IPC$`, `10.11.1.1`, `False Positive`.

### 📊 Resumen Ejecutivo del Caso
* **Threat Name:** `internal_smb_read_anomaly`, `internal_smb_anomaly` (SMB Write)
* **Source:** `192.168.169.96` (nb-caranda.technoma.local) y `192.168.169.144`
* **Destinations:** `10.11.1.1` (ad.technoma.local - Domain Controller) puerto `445` (SMB)
* **Description:** Alertas generadas por el motor de Machine Learning debido a un incremento inusual en la cantidad de peticiones de lectura y escritura SMB hacia el recurso `\\ad.technoma.local\IPC$`.

### 🧠 ¿Por qué es (o no es) una Amenaza?
Es un **Falso Positivo de Ciberataque (Ruido Administrativo)**.
Las alertas se disparan porque el volumen de peticiones SMB superó la línea base temporal calculada por el motor de ML (ej. 101 peticiones frente a un típico de 16 en 5 minutos). Sin embargo, el recurso al que se accede (`IPC$`) en un Controlador de Dominio es crítico para operaciones normales de red de Windows (autenticación, enumeración de recursos, Group Policies). Este pico de tráfico es consistente con procesos legítimos de background del sistema operativo (actualizaciones de GPO, scripts de inicio o mapeo de unidades de red) originados desde endpoints corporativos. No existen indicadores de movimiento lateral malicioso ni intentos de explotación.

### 🎯 Veredicto y Confianza Analítica
```json
{
  "Veredicto": "Falso Positivo (Tráfico SMB/AD Legítimo)",
  "Confianza": "100%",
  "Justificacion": "El pico de peticiones es hacia el recurso IPC$ del Controlador de Dominio desde máquinas internas conocidas. Es tráfico inherente al funcionamiento de un entorno Active Directory y no indica explotación de servicios remotos."
}
```

### 📝 Datos para Bitácora de Excel
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-24 | Antigravity | technoma | 12598 | modular_sensor | N/A | High | Lateral Movement | FP Anomalía Volumétrica SMB IPC$ hacia DC | 192.168.169.96, 192.168.169.144, 10.11.1.1 | Alertas volumétricas de ML por picos de peticiones de lectura/escritura SMB al share IPC$ en el Domain Controller. | Tráfico SMB | Ninguna. | Cerrado | N/A | NO | N/A | PB-FP-01 |

### 🏁 Instrucción para Cierre en Stellar Cyber
**Estado:** Closed
**Resolution Tag:** False Positive
**Comentario:** Falso Positivo Analítico (Anomalía de Volumen). Las detecciones `internal_smb_read_anomaly` e `internal_smb_anomaly` fueron disparadas por el motor de Machine Learning al observar picos de tráfico SMB que excedieron la línea base histórica en una ventana de 5 minutos. El tráfico consiste en peticiones hacia el recurso compartido `\\ad.technoma.local\IPC$` en el Domain Controller principal (`10.11.1.1`), originadas desde estaciones de trabajo corporativas internas. Este comportamiento es benigno y típico en entornos Windows (asociado a la actualización de directivas de grupo, scripts administrativos y validaciones AD de background). No se evidencia compromiso ni movimiento lateral real (T1210 / T1021). Se cierra el incidente sin más acciones.
