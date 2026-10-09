# Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (CJPPA070 - mleiva)

**Tenant:** CAJAANDE | **Host:** CJPPA070 (`172.16.202.121`) | **Usuario:** `CAJAANDE\mleiva`  
**XDR Event:** Sophos Event: User Execution (`sophos_event-execution-user_execution`) | **Subtipo:** `Event::Endpoint::WebControlViolation` | **MITRE:** T1204 (User Execution) / TA0002 (Execution)

---

## Declaración de Conteo Inicial
Se ha detectado **1 evento individual** en el volcado JSON proporcionado:
- **Evento 1 (ID Anomaly: `iTcFkKABI3UnQyDOu0FG`):** Registro emitido por Sophos Endpoint en la estación de trabajo `CJPPA070` (`172.16.202.121`), operada por `CAJAANDE\mleiva`. Refleja el bloqueo preventivo de navegación web hacia `https://translate.google.com` bajo la categoría `Proxies & Translators`.

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#WebControlViolation` `#SophosCentral` `#CAJAANDE` `#CJPPA070` `#ProxiesAndTranslators` `#FiltradoWeb`

---

## Análisis Evento 1 (Bloqueo WebControlViolation: translate.google.com)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** La estación de trabajo `CJPPA070` con IP `172.16.202.121`, bajo la sesión de `CAJAANDE\mleiva`, generó una petición web hacia `https://translate.google.com`.
* **Acción de Seguridad:** Bloqueo preventivo en capa de endpoint ejecutado por el componente de control web de Sophos Central (`type: Event::Endpoint::WebControlViolation`).
* **Clasificación del Contenido:** Categoría de filtrado `Proxies & Translators`, restringida de acuerdo con la directiva corporativa de navegación de CAJAANDE.
* **Mapeo en SIEM (Stellar Cyber):** Stellar Cyber asoció la alerta a la técnica `T1204 (User Execution)` bajo la táctica `TA0002 (Execution)` y fase `Persistent Foothold`. Este mapeo constituye una sobreclasificación analítica del SIEM, dado que no hubo ejecución de archivos ejecutables, scripts ni compromiso de persistencia en el sistema.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-4) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 10:29:24 | 2026-09-11 06:29:24 | Sophos WebControl | `https://translate.google.com` | 1 | 0 | Bloqueo preventivo en endpoint por política de filtrado web (`Proxies & Translators`). |
| 2026-09-11 10:29:24 | 2026-09-11 06:29:24 | Ingesta Syslog | `iTcFkKABI3UnQyDOu0FG` | - | - | Ingestión del log en índice `aella-syslog` (`event_score: 15`). |
| 2026-09-11 10:32:56 | 2026-09-11 06:32:56 | Indexación Stellar | Alerta procesada | - | - | Indexación en índice `aella-ser` (`threat_score: 0`). |

### Desglose Técnico y Disección Forense
* **Mecanismo de Detección:** El agente Sophos Endpoint interceptó la conexión antes de permitir la transferencia del payload HTTP/HTTPS, aplicando la política de filtrado de URL.
* **Comportamiento del Endpoint:** La conexión fue denegada localmente. El dominio `translate.google.com` es una herramienta pública de traducción de Google.
* **Evaluación de Amenaza:** No se observó actividad maliciosa, descarga de ejecutables ni comunicación con servidores de Comando y Control (C2). Corresponde a la aplicación de una política corporativa interna.

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
| H1 | Infección o compromiso en el endpoint | Descartada | Sin procesos anómalos ni persistencia; bloqueo preventivo efectivo a nivel web. |
| H2 | Ejecución de técnica ofensiva T1204 | Descartada | Mapeo heurístico automático del conector Interflow; no hubo ejecución de código. |
| H3 | Bloqueo administrativo por filtrado de navegación | Confirmada | El usuario intentó acceder a Google Translate, servicio no permitido por política de CAJAANDE. |

---

## Cierre Maestro Unificado del Caso

### Análisis de Impacto CIA Triad
```json
{
  "confidencialidad": "C0",
  "integridad": "I0",
  "disponibilidad": "A0",
  "justificacion": "No existio compromiso de informacion confidencial, alteracion de sistemas ni afectacion a la operatividad del equipo tras el bloqueo preventivo."
}
```

### Veredicto y Confianza Analítica
```json
{
  "veredicto": "Falso Positivo",
  "confianza": "100%",
  "clasificacion_soc": "Ruido Operativo / Filtrado Web (WebControlViolation)",
  "justificacion": "El evento base de Sophos Central es un bloqueo de navegacion web corporativo. Sobreclasificacion de T1204 en Stellar Cyber."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Alta",
  "frecuencia": "Patron recurrente en tenant CAJAANDE",
  "razon": "Mapeo sistematico de WebControlViolation hacia T1204 en Stellar Cyber.",
  "accion_recomendada": "Aplicar regla de supresion o reduccion de severidad para subtipo 'event_endpoint_webcontrolviolation'."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Verificación del log de Interflow y validación de la categoría web de filtrado. |
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
| 11/09/2026 06:29 | Analista SOC | CAJAANDE | iTcFkKABI3UnQyDOu0FG | Sophos Events (Stellar Cyber) | - | Baja | Sophos User Execution (WebControlViolation) | Bloqueo preventivo de filtrado web hacia translate.google.com | CJPPA070 (172.16.202.121) | Falso Positivo. El agente Sophos en CJPPA070 bloqueo el intento de acceso del usuario CAJAANDE\mleiva hacia https://translate.google.com por categoria Proxies & Translators. Sin impacto en el endpoint ni ejecucion de codigo malicioso. | Sophos Central / Interflow | Ninguna | Cierre | - | No | - | PB-006 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro (Plantilla 5 adaptada):**
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo (https://translate.google.com bajo categoría Proxies & Translators) en el equipo CJPPA070 (172.16.202.121). No hubo ejecución de código malicioso ni intención ofensiva hacia la infraestructura. Mapeo exagerado de técnica T1204 en el SIEM.
