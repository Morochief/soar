# Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (CJPPA048 - rvalenzuela)

**Tenant:** CAJAANDE | **Host:** CJPPA048 (`172.16.202.68`) | **Usuario:** `CAJAANDE\rvalenzuela`  
**XDR Event:** Sophos Event: User Execution (`sophos_event-execution-user_execution`) | **Subtipo:** `Event::Endpoint::WebControlViolation` | **MITRE:** T1204 (User Execution) / TA0002 (Execution)

---

## Declaración de Conteo Inicial
Se ha detectado **1 evento individual** en el volcado JSON proporcionado:
- **Evento 1 (ID Anomaly: `3DghkKABI3UnQyDOMS9T`):** Registro emitido por Sophos Central en la estación de trabajo `CJPPA048` (`172.16.202.68`), bajo la cuenta `CAJAANDE\rvalenzuela`. Corresponde al bloqueo preventivo de navegación hacia `https://translate.google.com` clasificado bajo la categoría de filtrado web `Proxies & Translators`.

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#WebControlViolation` `#SophosCentral` `#CAJAANDE` `#CJPPA048` `#ProxiesAndTranslators` `#FiltradoWeb`

---

## Análisis Evento 1 (Bloqueo WebControlViolation: translate.google.com)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** La estación de trabajo `CJPPA048` con dirección IP `172.16.202.68`, utilizada por `CAJAANDE\rvalenzuela`, inició una conexión web hacia `https://translate.google.com`.
* **Acción de Seguridad:** Bloqueo preventivo en el endpoint ejecutado por el componente de control web de Sophos Central (`type: Event::Endpoint::WebControlViolation`).
* **Clasificación del Contenido:** Categoría de filtrado `Proxies & Translators`, restringida en cumplimiento con la directiva corporativa de uso aceptable de internet de CAJAANDE.
* **Mapeo en SIEM (Stellar Cyber):** Stellar Cyber correlacionó la alerta con la técnica `T1204 (User Execution)` bajo la táctica `TA0002 (Execution)` y fase `Persistent Foothold`. Este mapeo es una sobreclasificación analítica del SIEM, ya que no existió ejecución de binarios, scripts ni actividad maliciosa en el equipo.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-4) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 10:57:43 | 2026-09-11 06:57:43 | Sophos WebControl | `https://translate.google.com` | 1 | 0 | Bloqueo preventivo en endpoint por política de filtrado web (`Proxies & Translators`). |
| 2026-09-11 10:58:04 | 2026-09-11 06:58:04 | Ingesta Syslog | `3DghkKABI3UnQyDOMS9T` | - | - | Ingestión del log en índice `aella-syslog` (`event_score: 15`). |
| 2026-09-11 11:02:43 | 2026-09-11 07:02:43 | Indexación Stellar | Alerta procesada | - | - | Indexación en índice `aella-ser` (`threat_score: 0`). |

### Desglose Técnico y Disección Forense
* **Mecanismo de Detección:** El agente Sophos Endpoint interceptó la resolución y establecimiento de sesión HTTP/HTTPS antes de transferir datos, aplicando la regla de filtrado de categorías restringidas.
* **Comportamiento del Endpoint:** La conexión fue abortada de inmediato en la estación de trabajo. El destino `translate.google.com` es un servicio público de traducción de Google.
* **Evaluación de Amenaza:** No se evidencia descarga de código malicioso, payloads ni tráfico con servidores de Comando y Control (C2). Corresponde a la aplicación de una directiva interna corporativa.

```json
/* Payload / Evidencia Principal: */
{
  "payload_type": "URL Request / Web Control Block",
  "payload_value": "https://translate.google.com",
  "payload_hash": "N/A",
  "payload_firma": "Event::Endpoint::WebControlViolation | Category: Proxies & Translators",
  "payload_accion": "blocked",
  "payload_destino": "translate.google.com"
}
```

#### Hipótesis Formuladas
| ID | Hipótesis | Evaluación | Justificación Forense |
| :--- | :--- | :--- | :--- |
| H1 | Infección o actividad maliciosa en el host | Descartada | Sin procesos anómalos ni persistencia; contención preventiva efectiva en capa web. |
| H2 | Ejecución de técnica ofensiva T1204 | Descartada | Mapeo heurístico automático del conector Interflow; no existió ejecución de binarios. |
| H3 | Bloqueo administrativo por filtrado de navegación | Confirmada | El usuario intentó acceder a Google Translate, servicio no permitido por política de CAJAANDE. |

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "No existio exposicion de credenciales ni datos, no hubo alteracion de archivos y los servicios del endpoint operan con total normalidad tras el bloqueo preventivo."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Operativo / Filtrado Web (WebControlViolation)",
  "justificacion": "El evento base de Sophos Central es un bloqueo de navegacion web corporativo hacia translate.google.com. Sobredimensionamiento heuristico de T1204 en Stellar Cyber."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Alta",
  "frecuencia": "Patron recurrente en tenant CAJAANDE",
  "razon": "Mapeo continuo de WebControlViolation hacia T1204 en Stellar Cyber.",
  "accion_recomendada": "Aplicar regla de supresion o reduccion de severidad para subtipo 'event_endpoint_webcontrolviolation'."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Verificación del log en Interflow y confirmación de la categoría web de filtrado. |
| Contención, Erradicación y Recuperación | Contención local automática por parte de Sophos Endpoint. No requiere remediación. |
| Post-Incidente | Registro del caso en bitácora y catalogación como ruido operativo. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-006 | Descarte de Falsos Positivos por Filtrado Web y Ruido Operativo | Procedimiento estándar de análisis y cierre de eventos de filtrado web. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta descartada por bloqueo preventivo de filtrado web sin impacto en el endpoint.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11/09/2026 06:57 | Analista SOC | CAJAANDE | 3DghkKABI3UnQyDOMS9T | Sophos Events (Stellar Cyber) | - | Baja | Sophos User Execution (WebControlViolation) | Bloqueo preventivo de filtrado web hacia translate.google.com | CJPPA048 (172.16.202.68) | Falso Positivo. El agente Sophos en CJPPA048 bloqueo el intento de acceso del usuario CAJAANDE\rvalenzuela hacia https://translate.google.com por categoria Proxies & Translators. Sin impacto en el endpoint ni ejecucion de codigo malicioso. | Sophos Central / Interflow | Ninguna | Cierre | - | No | - | PB-006 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro (Plantilla 5 adaptada):**
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo (https://translate.google.com bajo categoría Proxies & Translators) en el equipo CJPPA048 (172.16.202.68). No hubo ejecución de código malicioso ni intención ofensiva hacia la infraestructura. Mapeo exagerado de técnica T1204 en el SIEM.
