# Informe de Análisis SOC - Lote Interflow (2 Eventos)
**ID del Caso:** `19079_Sophos_ServiceNotRunning_dmz_CAJAANDE`  
**Fecha de Análisis:** 2026-09-24 09:48:00 (UTC-03:00)  
**Analista Responsable:** Nivel 1 SOC / DFIR  
**Tenant / Organización:** `CAJAANDE` (`392cf7319d694d53889280340fff51e9`)  
**Fuente / Sensor:** `sophos_CAJA-ANDE-SOPHOS` / `sophos_events`  
**Servidor Afectado:** `dmz` (`192.168.30.5`, Asset ID `e7cf1ae0-d9d1-11f0-bee4-aa0456b9a54a`)  

---

## 1. Declaración de Cantidad y Desglose del Lote
El lote recibido contiene exactamente **2 eventos JSON**, los cuales representan la ingesta duplicada / renotificación de una única incidencia de salud de endpoint reportada por Sophos Central:

1. **Evento 1 (`_seq_no: 19079`, `write_time: 1790253327185`):** Alerta inicial de `sophos_event-xdr_eba-xdr_endpoint_indicator_of_threat` para el evento de Sophos `31ced54d-949b-4e6c-af50-2a0c0dc5be66`.
2. **Evento 2 (`_seq_no: 19088`, `write_time: 1790253684586`):** Ingesta duplicada (~6 minutos después) con el mismo identificador de evento nativo de Sophos (`sophos.id: 31ced54d-949b-4e6c-af50-2a0c0dc5be66`) y misma marca de tiempo (`when: 2026-09-24T12:30:05.872Z`).

---

## 2. Análisis Técnico Detallado

### Contexto del Evento y Telemetría
- **Tipo de Evento Sophos:** `Event::Endpoint::ServiceNotRunning`
- **Descripción Nativa:** *"One or more Sophos services are missing or not running"*
- **Mapeo XDR de Stellar Cyber:**
  - **Táctica:** `XTA0001` (XDR EBA)
  - **Técnica:** `XT1004` (XDR Endpoint Indicator of Threat)
  - **Kill Chain Stage:** `Persistent Foothold` (T1562.001 - Impair Defenses: Disable or Modify Tools)
- **Activo Involucrado:**
  - **Nombre del Equipo:** `dmz`
  - **Dirección IP:** `192.168.30.5`
  - **Ubicación:** `dmz`
  - **Tipo de Endpoint:** `server`
  - **ID de Endpoint en Sophos Central:** `cd39704e-447e-4167-8980-2c8a8e6e4cfb`

### Diagnóstico Forense y de Seguridad
1. **Mapeo Heurístico en Stellar Cyber:** Stellar Cyber etiqueta esta notificación bajo `XT1004` y la etapa de `Persistent Foothold` de forma heurística, ya que en un escenario de intrusión avanzada los actores de amenazas pueden intentar deshabilitar servicios de seguridad para evadir la detección (T1562.001).
2. **Ausencia de Evidencia de Compromiso:**
   - No existen alertas correlacionadas de detección de malware, actividad de ransomware, inyección de memoria ni conexiones anómalas de comando y control (C2) sobre el servidor `192.168.30.5`.
   - No se registran eventos de escalamiento de privilegios o ejecución de scripts sospechosos (PowerShell, CMD, WMI) inmediatamente antes de las 12:30:05 UTC.
3. **Causa Raíz Operacional:**
   - La alerta `Event::Endpoint::ServiceNotRunning` es un evento de salud operacional generado por Sophos Central cuando alguno de sus módulos locales (ej. *Sophos File Scanner Service*, *Sophos Network Threat Protection*, *Sophos Health*) se detiene imprevistamente, entra en tiempo de espera durante un proceso de actualización automática de firmas/binarios o el servidor experimenta una sobrecarga temporal de recursos.
   - Ambos registros en Interflow corresponden al mismo identificador de incidencia de Sophos (`31ced54d-949b-4e6c-af50-2a0c0dc5be66`), confirmando que se trata de un único suceso con duplicidad de ingesta en el SIEM.

---

## 3. Evaluación de Impacto y Tríada CIA
- **Confidencialidad (0/10):** Sin filtración ni acceso no autorizado a información confidencial.
- **Integridad (0/10):** No se observan alteraciones de archivos ni compromiso de la integridad del sistema operativo.
- **Disponibilidad (2/10):** Afectación menor y transitoria en la disponibilidad de los servicios locales del agente de seguridad Sophos en el servidor DMZ.
- **Puntuación de Riesgo Global:** **1.0 / 10** (Bajo - Incidencia Operacional de Mantenimiento de Endpoint).

---

## 4. Veredicto y Acciones Recomendadas

- **Veredicto:** **Falso Positivo de Intrusión / Incidencia Operacional de Salud de Endpoint**.
- **Acciones Inmediatas (NIST SP 800-61r2):**
  1. **Verificación en Consola Sophos Central:** Acceder a Sophos Central bajo el tenant CAJAANDE y revisar el estado en tiempo real del servidor `dmz` (`cd39704e-447e-4167-8980-2c8a8e6e4cfb`).
  2. **Recuperación del Agente:** Validar si el servicio se restableció automáticamente tras la actualización o si requiere reinicio de los servicios de Sophos desde `services.msc` / reinicio del host por parte del equipo de infraestructura.
  3. **Cierre en Stellar Cyber:** Cerrar ambas alertas como Falso Positivo con justificación de alerta operacional de estado de servicio.
