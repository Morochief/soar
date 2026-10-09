# Informe de Análisis SOC - Lote Interflow (4 Eventos)
**ID del Caso:** `19437_Windows_Update_pripub_appid_adm-fs`  
**Fecha de Análisis:** 2026-09-24 12:23:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `Technoma` (`cf73a415c8794884a0c35b458b7c73ae`)  
**Sensor:** `technoma-sensor` (`4e3eab0649114a80a089a5d5a078994d`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
Se procesaron **4 eventos de seguridad** correlacionados de anomalía de uso de aplicación (`pripub_appid`):

1. **Evento 1 (`_seq_no: 19437`):** `pripub_appid` (Application Usage Anomaly). 224 conexiones HTTP/80 hacia CDN Fastly (`199.232.214.172`, `bg.microsoft.map.fastly.net`) por `windows_update`.
2. **Evento 2 (`_seq_no: 19449`):** `pripub_appid`. 160 conexiones HTTP/80 hacia CDN Fastly (`199.232.210.172`, `office.microsoft.map.fastly.net`) por `windows_update`.
3. **Evento 3 (`_seq_no: 19465`):** `pripub_appid`. 217 conexiones HTTP/80 hacia CDN Fastly (`199.232.214.172`, `fg.microsoft.map.fastly.net`) por `windows_update`.
4. **Evento 4 (`_seq_no: 19561`):** `pripub_appid`. 196 conexiones HTTP/80 hacia CDN Fastly (`199.232.214.172`, `bg.microsoft.map.fastly.net`) por `windows_update`.

---

## 2. Análisis Técnico Detallado
- **Host de Origen:** `10.11.1.5` (`adm-fs.technoma.local` - Servidor de Archivos institucional)
- **Destino:** Red CDN oficial de Fastly / Microsoft (`199.232.214.172`, `199.232.210.172`) en puerto `80` (HTTP)
- **Dominio y URI de Petición:** `3.tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/47e375ad-a10c-4c90-a161-555d91c9a5ad...`
- **User Agent:** `Microsoft-Delivery-Optimization/10.0`
- **Código de Respuesta:** `206 Partial Content` (descarga segmentada de paquetes y cabinas de actualización mediante HTTP Range requests)
- **Tipo MIME:** `application/octet-stream`
- **Diagnóstico:** El servidor de archivos corporativo `adm-fs` ejecutó descargas legítimas de actualizaciones del sistema operativo mediante el servicio de optimización de entrega de Microsoft. Al tratarse de descargas concurrentes de múltiples bloques binarios, se superó el umbral basal de 76 conexiones en intervalos de 5 minutos, disparando la anomalía de Machine Learning. Tráfico benigno y esperado de mantenimiento del sistema operativo.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Sin fuga de datos ni acceso no autorizado.
- **Integridad (0/10):** Los archivos binarios descargados son firmados digitalmente por Microsoft.
- **Disponibilidad (0/10):** El servicio de archivos y la red operaron con normalidad.
- **Puntuación de Riesgo Global:** **0.0 / 10** (Insignificante / Tráfico Benigno de Actualización).

---

## 4. Veredicto Final y Recomendación
- **Veredicto:** **Falso Positivo** (Ruido Operativo / Descarga Legítima de Windows Update Delivery Optimization).
- **Acciones:**
  1. Cerrar los 4 eventos en Stellar Cyber como Falso Positivo.
  2. Ajustar el umbral analítico de Machine Learning para `pripub_appid` con `appid_name: windows_update` en servidores críticos.

---

## 5. Instrucción de Cierre en Stellar Cyber
* **Estado:** `Closed`
* **Resolution Tag:** `False Positive`
* **Comentario:**
> Alerta descartada como **Falso Positivo**. La telemetría confirma que el clúster de alertas de anomalía de uso de aplicación (`pripub_appid`) corresponde a descargas legítimas y concurrentes de parches de Windows Update por parte del servidor `adm-fs.technoma.local` (`10.11.1.5`). Las peticiones fueron generadas por el agente nativo `Microsoft-Delivery-Optimization/10.0` hacia endpoints y CDNs oficiales de Microsoft (`3.tlu.dl.delivery.mp.microsoft.com` / Fastly), registrando respuestas HTTP 206 (Partial Content) para fragmentos binarios de actualización. No existe actividad maliciosa ni impacto en la tríada CIA.
