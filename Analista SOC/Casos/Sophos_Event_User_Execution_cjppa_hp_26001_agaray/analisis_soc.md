# Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (cjppa_hp_26001 - agaray)

**Tenant:** CAJAANDE | **Host:** cjppa_hp_26001 (`172.16.202.16`) | **Usuario:** `CAJAANDE\agaray`  
**XDR Event:** Sophos Event: User Execution (`sophos_event-execution-user_execution`) | **Subtipo:** `Event::Endpoint::WebControlViolation` | **MITRE:** T1204 (User Execution) / TA0002 (Execution)

---

## Declaración de Conteo Inicial
Se han detectado **2 eventos individuales** en el volcado JSON proporcionado:
- **Evento 1 (ID Anomaly: `vQUWjKABI3UnQyDOU-LY`):** `Event::Endpoint::WebControlViolation` originado por Sophos Endpoint en la estación de trabajo `cjppa_hp_26001` (`172.16.202.16`), usuario `CAJAANDE\agaray`. Bloqueo preventivo de navegación hacia `https://s328.erome.com` categorizado bajo la directiva `Adult/Sexually Explicit`.
- **Evento 2 (ID Anomaly: `yAYajKABI3UnQyDO7CnU`):** Duplicado técnico exacto del Evento 1 (mismo `sophos.id: 454aad1b-5d7e-41b6-b261-272efd36ded1` y misma marca de tiempo `2026-09-10T16:07:30.000Z`), reingestado por el conector de Stellar Cyber aproximadamente 6 minutos después (`write_time: 1789057143547`).

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#WebControlViolation` `#SophosCentral` `#CAJAANDE` `#cjppa_hp_26001` `#AdultSexuallyExplicit` `#FiltradoWeb`

---

## Análisis Evento 1 (Bloqueo WebControlViolation: s328.erome.com)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
- **Actividad Observada:** El endpoint `cjppa_hp_26001` con dirección IP `172.16.202.16`, bajo la sesión de `CAJAANDE\agaray`, intentó establecer conexión HTTP/HTTPS hacia la URL `https://s328.erome.com`.
- **Acción de Seguridad:** Bloqueo preventivo inmediato en el endpoint por parte del motor de filtrado web de Sophos Central (`type: Event::Endpoint::WebControlViolation`).
- **Clasificación del Contenido:** La categoría de filtrado aplicada por Sophos fue `Adult/Sexually Explicit`, directiva denegada por la política de uso aceptable corporativo de CAJAANDE.
- **Mapeo en SIEM (Stellar Cyber):** Stellar Cyber asoció la alerta a la técnica `T1204 (User Execution)` dentro de la táctica `TA0002 (Execution)` y fase `Persistent Foothold`. Se determina que este mapeo es una sobreclasificación analítica del SIEM, ya que no existió ejecución de binarios, scripts, ni compromiso de persistencia en el activo.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-4) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-10 16:07:30 | 2026-09-10 12:07:30 | Sophos WebControl | `https://s328.erome.com` | 1 | 0 | Bloqueo en endpoint por política de filtrado web (Adult/Sexually Explicit). |
| 2026-09-10 16:07:50 | 2026-09-10 12:07:50 | Ingestión Syslog | `vQUWjKABI3UnQyDOU-LY` | - | - | Ingesta de evento en índice aella-syslog (`event_score: 15`). |
| 2026-09-10 16:13:06 | 2026-09-10 12:13:06 | Indexación Stellar | Documento 1 | - | - | Indexación en aella-ser (`threat_score: 0`). |

### Desglose Técnico y Disección Forense
- **Mecanismo de Detección:** El agente local Sophos Endpoint interceptó la solicitud del navegador antes de completar la carga de recursos, aplicando la lista de categorías denegadas en la política de control web.
- **Comportamiento del Endpoint:** El intento de conexión fue abortado localmente. La URL `s328.erome.com` corresponde a una subcarpeta de entrega de contenido multimedia de una plataforma de contenido para adultos.
- **Análisis de Amenaza:** No se observaron descargas de ejecutables maliciosos, exploits de navegador ni peticiones hacia infraestructura de Comando y Control (C2). Se trata de una infracción a la política interna de navegación web laboral.

```json
/* Payload / Evidencia Principal: */
{
  "payload_type": "URL Request / Web Control Block",
  "payload_value": "https://s328.erome.com",
  "payload_hash": "N/A",
  "payload_firma": "Event::Endpoint::WebControlViolation | Category: Adult/Sexually Explicit",
  "payload_accion": "blocked",
  "payload_destino": "s328.erome.com"
}
```

#### Comandos de Diagnóstico Recomendados
```powershell
# Verificar procesos de navegación y conexiones de red en el endpoint (si se requiriese auditoría interna)
Get-NetTCPConnection -OwningProcess (Get-Process chrome, msedge, firefox -ErrorAction SilentlyContinue).Id | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

#### Hipótesis Formuladas
| ID | Hipótesis | Evaluación | Justificación Forense |
| :--- | :--- | :--- | :--- |
| H1 | Infección por malware / troyano descargado | Descartada | La telemetría no registra creación de binarios ni alteración de llaves Run/Servicios; el bloqueo fue efectivo en capa web. |
| H2 | Ejecución de exploit en navegador (T1204) | Descartada | Mapeo heurístico incorrecto del conector Interflow; el tipo nativo es WebControlViolation y no ExploitPrevention. |
| H3 | Infracción de política corporativa de navegación | Confirmada | El usuario `agaray` intentó acceder a un portal de contenido para adultos restringido por las directivas de CAJAANDE. |

---

## Análisis Evento 2 (Duplicado Técnico: Anomaly ID yAYajKABI3UnQyDO7CnU)

### Identificación de Duplicado
El **Evento 2 es un duplicado exacto del Evento 1**.
- **ID de Alerta Stellar:** `786ba681-646e-46f9-90ce-a5febf3f412d1789057143548-YWVsbGEtc2VyLTIwMjYuMDkuMTAtMzkyY2Y3MzE5ZDY5NGQ1Mzg4OTI4MDM0MGZmZjUxZTk=`
- **ID de Anomalía:** `yAYajKABI3UnQyDO7CnU`
- **ID de Sophos Central (`sophos.id`):** `454aad1b-5d7e-41b6-b261-272efd36ded1` (Idéntico al Evento 1).
- **Hora del Evento (`sophos.when`):** `2026-09-10T16:07:30.000Z` (Idéntico al Evento 1).
- **Hora de Creación (`sophos.created_at`):** `2026-09-10T16:07:50.931Z` (Idéntico al Evento 1).
- **Causa Técnica del Duplicado:** Reemisión del conector de Sophos Central hacia Stellar Cyber con `write_time: 1789057143547` (2026-09-10 16:19:03 UTC). No representa un segundo intento de navegación, sino una doble ingesta del mismo registro en el pipeline del SIEM.

---

## ¿Por qué es (o no es) una Amenaza?
No constituye una amenaza para la infraestructura tecnológica. El agente Sophos Endpoint realizó su labor de contención preventiva bloqueando la solicitud hacia `https://s328.erome.com`. El evento corresponde estrictamente a un desvío administrativo y conductual de la política corporativa de uso de internet (intento de navegación a contenido no laboral). La clasificación de MITRE ATT&CK `T1204 (User Execution)` y `Persistent Foothold` en Stellar Cyber es una severa distorsión de la taxonomía del SIEM, que eleva un log de filtrado web a nivel de incidente de ejecución de código.

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "No existio exposicion de datos sensibles, modificacion de sistemas ni interrupcion de servicios. La conexion fue abortada preventivamente por el agente de endpoint."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Operativo / Infracción de Política de Filtrado Web",
  "justificacion": "El evento base es un Event::Endpoint::WebControlViolation exitosamente bloqueado por Sophos. Mapeo inflado de T1204 por el motor analitico de Stellar Cyber."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Alta",
  "frecuencia": "Recurrente en tenant CAJAANDE",
  "razon": "Stellar Cyber correlaciona indebidamente eventos de tipo WebControlViolation con tecnicas de User Execution, inundando la cola del SOC con falsos incidentes de persistencia.",
  "accion_recomendada": "Ajustar la regla de ingestión o aplicar supresión de severidad en Stellar Cyber para logs de Sophos con subtype 'event_endpoint_webcontrolviolation'."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Correlación de telemetría Sophos Interflow, confirmación de bloqueo en capa de control web e identificación de duplicado técnico. |
| Contención, Erradicación y Recuperación | Contención local automática y exitosa por parte del agente Sophos. No requiere acciones de remediación en el host. |
| Post-Incidente | Documentación de la regla de ruido operativo en la memoria institucional del SOC. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-006 | Descarte de Falsos Positivos por Filtrado Web y Ruido Operativo | Validación de políticas de navegación y descarte de eventos sobreclasificados por el SIEM. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta descartada debido a que corresponde a un bloqueo preventivo de filtrado web corporativo sin impacto ni ejecución maliciosa en el host.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 10/09/2026 12:07 | Analista SOC | CAJAANDE | vQUWjKABI3UnQyDOU-LY | Sophos Events (Stellar Cyber) | - | Baja | Sophos User Execution (WebControlViolation) | Bloqueo preventivo de filtrado web hacia s328.erome.com | cjppa_hp_26001 (172.16.202.16) | Falso Positivo. El agente Sophos en cjppa_hp_26001 bloqueo el intento de acceso del usuario CAJAANDE\agaray hacia https://s328.erome.com por categoria Adult/Sexually Explicit. Se detecta duplicado tecnico (yAYajKABI3UnQyDO7CnU). Sin impacto en endpoint ni ejecucion de codigo. | Sophos Central / Interflow | Ninguna | Cierre | - | No | - | PB-006 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro (Plantilla 5 adaptada):**
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo (https://s328.erome.com bajo categoría Adult/Sexually Explicit) en el equipo cjppa_hp_26001 (172.16.202.16). Se identifica además que el segundo evento del lote corresponde a una duplicación técnica del mismo registro. No hubo ejecución de código malicioso ni intención ofensiva hacia la infraestructura. Mapeo exagerado de técnica T1204 en el SIEM.

> [!TIP]
> Proponer al Administrador de Seguridad la creación de una regla de normalización o supresión de severidad en Stellar Cyber para eventos de origen Sophos con subtipo `event_endpoint_webcontrolviolation`, evitando falsas alarmas de `User Execution` (T1204).

---

### Desglose Ultra Quirúrgico
- **Capa de Red y Enrutamiento:**
  - `hostip`: `172.16.202.16` (Segmento privado de estaciones de trabajo del tenant `CAJAANDE`).
  - `computer_name`: `cjppa_hp_26001` (Activo tipo PC/Notebook HP corporativa).
  - `user.name`: `CAJAANDE\agaray` (Identidad de usuario autenticada en el dominio local).
- **Capa de Transporte y Conexión:**
  - `aella_tuples`: `null.null.null.null` (Indica que el evento proviene de un colector de logs de endpoint y no de un sensor DPI de red con captura de flujo IP/puerto en tiempo real).
  - `totalbytes`: `0`, `totalpackets`: `0` (Coherente con una interrupción a nivel de driver/proxy de endpoint antes de transmitir flujo TCP completo).
- **Capa de Aplicación y DPI / Endpoint:**
  - `msg_class / dms_job_id`: `sophos_events` (Recolectado vía API de Sophos Central hacia Stellar Cyber).
  - `threat.name / sophos.type`: `Event::Endpoint::WebControlViolation` (Identificador del módulo de control web de Sophos Endpoint).
  - `sophos.name`: `'https://s328.erome.com' blocked due to category 'Adult/Sexually Explicit'`.
  - `sophos.id`: `454aad1b-5d7e-41b6-b261-272efd36ded1` (UUID único emitido por Sophos Central, repetido exactamente en ambos documentos).
- **Capa de Detección XDR y Motor ML:**
  - `threat_score`: `0` (Sin puntuación de criticidad activa).
  - `severity`: `15` / `severity_str: low` (Gravedad baja nativa).
  - `xdr_event.name`: `sophos_event-execution-user_execution` (Mapeo estático por catálogo en Interflow).
  - `technique`: `T1204` / `tactic: TA0002` (Atribución indebida a tácticas ofensivas MITRE para una simple política de URL filtering).

**Resumen Quirúrgico Final:**  
El usuario `CAJAANDE\agaray` navegaba desde el host `cjppa_hp_26001` (`172.16.202.16`) e ingresó a la dirección web `https://s328.erome.com` a las 12:07:30 hora local. El agente Sophos Endpoint interceptó la resolución y denegó el tráfico bajo la directiva `Adult/Sexually Explicit`. El evento fue despachado por la API de Sophos Central e ingerido por Stellar Cyber dos veces (`write_time` con 6 minutos de separación), atribuyéndose erróneamente a la técnica MITRE T1204. El incidente queda cerrado como Falso Positivo / Ruido Operativo sin afectación al entorno.
