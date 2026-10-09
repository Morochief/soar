### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Windows Update`, `RPC`, `SMB`, `Active Directory`

### Análisis Evento 1

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Internal SMB Write Anomaly
* **Activos Involucrados:** `192.168.169.127` -> `ad.technoma.local` (`10.11.1.1`)
* **Comportamiento Anómalo:** Motor ML detecta 11 solicitudes de escritura SMB (cuando el típico es 2) en 5 mins.
* **Causalidad Probable:** Diálogo de protocolo RPC (Remote Procedure Call) contra el controlador de dominio.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Observación Forense |
|---|---|---|---|---|---|
| 2026-07-25T07:10:55 | 2026-07-25 04:10:55 | Internal SMB Write Anomaly | 11 | 2 | Flujo SMB/RPC hacia el DC primario. |

### 🔬 Desglose Técnico y Disección Forense
* **Flujo de Tráfico:** Origen privado `192.168.169.127` hacia el DC `10.11.1.1` en el puerto `445` (SMB).
* **Inspección de Metadatos:** Los metadatos muestran comandos SMB como `8` (Tree Connect) y `9` (Tree Disconnect) y `16`.
* Según nuestra Memoria Institucional, Stellar marca cada petición RPC al DC (SAM) como un "Write".

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "SMB Metadata",
  "payload_value": "Command 8, Command 9, Command 16",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Autenticación / Consulta GPO",
  "payload_destino": "ad.technoma.local"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza.** Tal como documenta nuestra memoria (`SOC_GEM_v2.md`), las lecturas y escrituras SMB hacia la IP `10.11.1.1` (DC Primario) son en realidad peticiones RPC normales de los endpoints de la red para autenticarse, consultar políticas (GPOs) o dialogar con el Security Account Manager (SAM). El motor de Machine Learning de Stellar se confunde y los cuenta volumétricamente como si fueran escrituras masivas de archivos (Ransomware), lo cual es falso.

---

### Análisis Evento 2

### 🎯 Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Alerta Detectada:** Application Usage Anomaly (pripub_appid)
* **Activos Involucrados:** `ad.technoma.local` (`10.11.1.1`) -> `45.161.239.50` (AS61512 - GIG@NET)
* **Comportamiento Anómalo:** 103 conexiones en 5 mins usando `windows_update`.
* **Causalidad Probable:** Descarga de actualizaciones de Windows desde nodos CDN.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local) | Evento Detectado | Actual | Typical | Observación Forense |
|---|---|---|---|---|---|
| 2026-07-25T10:09:59 | 2026-07-25 07:09:59 | Application Usage Anomaly | 103 | 31 (threshold) | Conexiones HTTP GET a `3.tlu.dl.delivery.mp.microsoft.com`. |

### 🔬 Desglose Técnico y Disección Forense
* **Aplicación Identificada:** `windows_update` (HTTP sobre puerto 80).
* **URI Solicitada:** `/filestreamingservice/files/ee36ea64...`
* **User Agent:** `Microsoft-Delivery-Optimization/10.0`
* **Destino Público:** `45.161.239.50` (IP de un CDN local de Microsoft Delivery Optimization en la red GIG@NET, Paraguay).

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "HTTP Request",
  "payload_value": "GET /filestreamingservice/files/ee36ea64...",
  "payload_hash": "N/A",
  "payload_firma": "N/A",
  "payload_accion": "Descarga de Parches Windows",
  "payload_destino": "3.tlu.dl.delivery.mp.microsoft.com"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza.** Se trata del servicio nativo de Microsoft (Delivery Optimization) descargando actualizaciones del sistema operativo (Parches). Windows utiliza CDNs geográficamente cercanos (en este caso una IP de Paraguay, GIGANET) para agilizar las descargas, y para ello abre docenas de conexiones TCP simultáneas (Partial Contents `HTTP 206`), lo cual rompe el umbral volumétrico de Stellar Cyber, disparando la alerta de "Anomalía de Aplicación".

---

### Análisis Evento 3

**El Evento 3 es un duplicado exacto del Evento 2**, correspondiendo a otro intervalo de 5 minutos (Hora: 10:10:03 UTC) donde el DC `10.11.1.1` continuó descargando paquetes de Windows Update desde la misma IP pública `45.161.239.50` utilizando el mismo User Agent `Microsoft-Delivery-Optimization/10.0`.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto. Flujos normales de AD y WSUS.",
  "Integrity": "Sin impacto.",
  "Availability": "Sin impacto."
}
```

### ⚖️ Veredicto y Confianza Analítica
```json
{
  "Veredicto": "False Positive",
  "Confianza": "100%",
  "Motivo": "Comportamientos documentados y firmados por OS (RPC de AD y Windows Update via MS Delivery Optimization)."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Alta",
  "Razón": "El Machine Learning sin sintonizar detona falsos positivos por comportamientos base de Windows (SMB y Updates)."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| Detección y Análisis | Inspección de metadatos SMB y URIs HTTP. |
| Erradicación y Recuperación | N/A (Falso Positivo) |
| Actividad Post-Incidente | Cierre del ticket. |

### 📚 Playbook Asignado
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| PB-002 | Manejo de Falsos Positivos | Cierre documentado de alertas generadas por tráfico legítimo. |

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior.

### 📝 Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
`25/07/2026 11:27 | Analista | technoma | 12632 | Stellar Cyber | - | Baja | Internal SMB Write Anomaly & Application Anomaly | Tráfico RPC a DC y Descarga de Windows Update | 192.168.169.127, 10.11.1.1 | Falsos positivos por peticiones RPC normales al Controlador de Dominio y descargas volumétricas de parches de Windows desde CDN de Microsoft. | Metadatos SMB y User-Agent MS Delivery Optimization | Ninguna | Cerrado | - | No | - | PB-002`

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:** Falso positivo. Las alertas corresponden a dos flujos legítimos de la infraestructura: 1) Tráfico RPC/SMB normal hacia el DC (10.11.1.1) para consultas y empuje de GPOs. 2) Múltiples conexiones (App: windows_update) del DC hacia nodos CDN de Microsoft (GIGANET, PY) para descarga segmentada de actualizaciones de sistema operativo (User-Agent: Microsoft-Delivery-Optimization). No hay indicios de amenaza.

> [!TIP]
> Proponer añadir una regla en Stellar Cyber para elevar el umbral (threshold) de conexiones simultáneas para la App `windows_update` hacia el AS61512, a fin de reducir el ruido administrativo de estas descargas de parches, y documentar el AS61512 como CDN válido en `SOC_GEM_v2.md`.

### 🔬 Desglose Ultra Quirúrgico
* **Red/Enrutamiento:** Conexiones LAN-to-LAN y LAN-to-WAN desde endpoints hacia el DC, y del DC hacia IPs de Paraguay (AS61512).
* **Transporte/Conexión:** Picos volumétricos de paquetes TCP (3762 paquetes en 5 minutos para Windows Update), superando perfiles base (`typical`).
* **Aplicación/DPI:** DPI de Stellar extrae comandos SMB 8 (Tree Connect) y HTTP GET requests con URI de Microsoft File Streaming y códigos de respuesta `206 Partial Content`.
* **Resumen Quirúrgico Final:** El motor ML volumétrico de Stellar Cyber es muy sensible a ráfagas de paquetes. En el primer caso (SMB), malinterpreta un burst de consultas RPC como "escrituras", y en el segundo caso (App Anomaly), se alarma por la arquitectura de descarga multiparte (múltiples flujos GET HTTP 206) utilizada por el servicio Delivery Optimization de Microsoft. Ambos flujos son 100% benignos y esperados en un entorno de red Windows saludable.
