# Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (NBCJPPA20260818 - jrodriguez)

**Tenant:** CAJAANDE | **Host:** NBCJPPA20260818 (`172.16.202.43`) | **Usuario:** `CAJAANDE\jrodriguez`  
**XDR Event:** Sophos Event: User Execution (`sophos_event-execution-user_execution`) | **Subtipo:** `Event::Endpoint::WebControlViolation` | **MITRE:** T1204 (User Execution) / TA0002 (Execution)

---

## Declaración de Conteo Inicial
Se ha detectado **1 evento individual** en el volcado JSON proporcionado:
- **Evento 1 (ID Anomaly: `8TSzj6ABI3UnQyDOU6Tv`):** Evento originado por Sophos Endpoint en la estación de trabajo portátil `NBCJPPA20260818` (`172.16.202.43`), asignada al usuario `CAJAANDE\jrodriguez`. Corresponde al bloqueo preventivo de navegación hacia `https://translate.google.com` bajo la categoría de filtrado web `Proxies & Translators`.

---

### Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `#FalsoPositivo` `#WebControlViolation` `#SophosCentral` `#CAJAANDE` `#NBCJPPA20260818` `#ProxiesAndTranslators` `#FiltradoWeb`

---

## Análisis Evento 1 (Bloqueo WebControlViolation: translate.google.com)

### Resumen Ejecutivo del Caso (Formato Nativo Stellar)
* **Actividad Observada:** El endpoint `NBCJPPA20260818` con dirección IP `172.16.202.43`, operado por el usuario `CAJAANDE\jrodriguez`, intentó conectarse a la URL `https://translate.google.com`.
* **Acción de Seguridad:** Bloqueo preventivo inmediato en el host ejecutado por el componente de filtrado web de Sophos Central Endpoint (`type: Event::Endpoint::WebControlViolation`).
* **Clasificación del Contenido:** La categoría de filtrado web aplicada por Sophos fue `Proxies & Translators`, directiva restringida por la política corporativa de navegación de CAJAANDE.
* **Mapeo en SIEM (Stellar Cyber):** Stellar Cyber correlacionó automáticamente el evento con la técnica `T1204 (User Execution)` dentro de la táctica `TA0002 (Execution)` y fase `Persistent Foothold`. Este mapeo es una sobreclasificación analítica del SIEM, ya que no existió ejecución de binarios, scripts ni actividad maliciosa en el sistema.

### Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local GMT-4) | Evento Detectado | Actual | Typical | Ratio | Observación Forense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-09-11 08:59:58 | 2026-09-11 04:59:58 | Sophos WebControl | `https://translate.google.com` | 1 | 0 | Bloqueo preventivo en endpoint por política de filtrado web (`Proxies & Translators`). |
| 2026-09-11 09:00:18 | 2026-09-11 05:00:18 | Ingesta Syslog | `8TSzj6ABI3UnQyDOU6Tv` | - | - | Ingestión del evento en índice `aella-syslog` (`event_score: 15`). |
| 2026-09-11 09:03:36 | 2026-09-11 05:03:36 | Indexación Stellar | Alerta procesada | - | - | Indexación en índice `aella-ser` (`threat_score: 0`). |

### Desglose Técnico y Disección Forense
* **Mecanismo de Detección:** El controlador de red local de Sophos Endpoint interceptó la resolución y establecimiento de sesión HTTP/HTTPS antes de permitir el intercambio de datos, aplicando la regla de control web.
* **Comportamiento del Endpoint:** La conexión fue abortada de inmediato en la estación de trabajo. El destino `translate.google.com` es un servicio legítimo de traducción de Google que muchas organizaciones restringen dentro de la categoría `Proxies & Translators` para prevenir la fuga de información mediante traducción de textos confidenciales o su uso como proxy.
* **Evaluación de Amenaza:** No existe indicio de compromiso, infección por malware, descarga de payloads ni comunicación con infraestructura adversaria. Se trata estrictamente de la aplicación de una directiva de navegación web.

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

#### Comandos de Diagnóstico Recomendados
```powershell
# Verificación de sockets de red y estado de procesos de navegación en el host NBCJPPA20260818
Get-NetTCPConnection -OwningProcess (Get-Process msedge, chrome, firefox -ErrorAction SilentlyContinue).Id | Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State
```

#### Hipótesis Formuladas
| ID | Hipótesis | Evaluación | Justificación Forense |
| :--- | :--- | :--- | :--- |
| H1 | Infección o actividad maliciosa ejecutada por usuario | Descartada | No existen binarios creados, procesos anómalos ni persistencia; el log nativo es puramente un bloqueo web. |
| H2 | Ejecución de exploit o técnica ofensiva T1204 | Descartada | Mapeo predeterminado e inflado por el conector de Interflow en Stellar Cyber; no hubo ejecución de código. |
| H3 | Bloqueo legítimo por política administrativa de filtrado | Confirmada | El usuario intentó acceder a Google Translate, servicio bloqueado por la directiva de seguridad de CAJAANDE. |

---

## ¿Por qué es (o no es) una Amenaza?
No constituye una amenaza para el entorno corporativo. El agente Sophos Endpoint realizó la contención preventiva en el host de manera eficaz. El sitio `translate.google.com` es un servicio público de traducción de Google. La clasificación de MITRE ATT&CK `T1204 (User Execution)` bajo `Persistent Foothold` en Stellar Cyber es una distorsión sistemática del conector Interflow, que mapea eventos de control web (`WebControlViolation`) como eventos de ejecución sospechosa.

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
  "justificacion": "El log base de Sophos Central es un bloqueo administrativo de navegacion hacia translate.google.com. Sobredimensionamiento heuristico de T1204 en Stellar Cyber."
}
```

### Indicador de Fatiga de Alertas
```json
{
  "fatiga_detectada": "Alta",
  "frecuencia": "Patron recurrente documentado en tenant CAJAANDE",
  "razon": "Stellar Cyber asigna la tecnica T1204 (User Execution) a bloqueos rutinarios de navegacion web hacia translate.google.com, saturando la bandeja de entrada del SOC.",
  "accion_recomendada": "Configurar una regla de ajuste o supresion en Stellar Cyber para descartar automaticamente eventos de Sophos con subtype 'event_endpoint_webcontrolviolation'."
}
```

### Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
| :--- | :--- |
| Detección y Análisis | Análisis de la telemetría de Interflow, verificación de la categoría web (`Proxies & Translators`) y confirmación de ausencia de artefactos ejecutables. |
| Contención, Erradicación y Recuperación | Contención preventiva ejecutada de forma local por Sophos Endpoint. No se requieren acciones de remediación ni aislamiento del host. |
| Post-Incidente | Documentación y cierre del caso en la bitácora unificada del SOC bajo el playbook PB-006. |

### Playbook Asignado
| ID Playbook | Nombre | Justificación Estratégica |
| :--- | :--- | :--- |
| PB-006 | Descarte de Falsos Positivos por Filtrado Web y Ruido Operativo | Procedimiento estándar para la gestión y cierre de alertas generadas por políticas de filtrado web corporativo. |

### Resolution Tag para Stellar Cyber
* **Resolution Tag:** `False Positive`
* **Descripción:** Alerta descartada debido a que corresponde a un bloqueo administrativo de navegación web sin impacto ni actividad maliciosa en el endpoint.

### Datos para Bitácora de Excel (UNA SOLA LÍNEA EN TABLA)
| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia (Logs, etc. Puede ser el mismo del Case Evidence ) | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 11/09/2026 04:59 | Analista SOC | CAJAANDE | 8TSzj6ABI3UnQyDOU6Tv | Sophos Events (Stellar Cyber) | - | Baja | Sophos User Execution (WebControlViolation) | Bloqueo preventivo de filtrado web hacia translate.google.com | NBCJPPA20260818 (172.16.202.43) | Falso Positivo. El agente Sophos en NBCJPPA20260818 bloqueo el intento de acceso del usuario CAJAANDE\jrodriguez hacia https://translate.google.com por categoria Proxies & Translators. Sin impacto en el endpoint ni ejecucion de codigo malicioso. | Sophos Central / Interflow | Ninguna | Cierre | - | No | - | PB-006 |

### Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario de Cierre Maestro (Plantilla 5 adaptada):**
> Alerta descartada como falso positivo. Tras revisar la telemetría base, se confirma que el evento original de Sophos es un simple WebControlViolation debido a que el usuario intentó acceder a una URL bloqueada por política de filtrado corporativo (https://translate.google.com bajo categoría Proxies & Translators) en el equipo NBCJPPA20260818 (172.16.202.43). No hubo ejecución de código malicioso ni intención ofensiva hacia la infraestructura. Mapeo exagerado de técnica T1204 en el SIEM.

---

### Desglose Ultra Quirúrgico
* **Capa de Red y Enrutamiento:**
  * `hostip`: `172.16.202.43` (Dirección IP privada asignada a la estación de trabajo dentro de la LAN de `CAJAANDE`).
  * `computer_name`: `NBCJPPA20260818` (Notebook corporativa de la entidad).
  * `user.name`: `CAJAANDE\jrodriguez` (Cuenta de usuario de dominio de Active Directory).
* **Capa de Transporte y Conexión:**
  * `aella_tuples`: `null.null.null.null` (Indica que el registro fue recolectado a nivel de log de endpoint por la API de Sophos y no capturado por un sensor DPI de red).
  * `totalbytes`: `0`, `totalpackets`: `0` (Sesión TCP interrumpida por el proxy/driver local antes de la transmisión de datos).
* **Capa de Aplicación y DPI / Endpoint:**
  * `msg_class / dms_job_id`: `sophos_events` (Conector Interflow de ingesta de eventos de Sophos Central).
  * `threat.name / sophos.type`: `Event::Endpoint::WebControlViolation` (Violación de la directiva de navegación web).
  * `sophos.name`: `'https://translate.google.com' blocked due to category 'Proxies & Translators'`.
  * `sophos.id`: `ec17c7b4-f650-4601-9e1d-7575d5e53e91` (Identificador único asignado por Sophos Central).
* **Capa de Detección XDR y Motor ML:**
  * `threat_score`: `0` (Sin puntuación de riesgo calculada).
  * `severity`: `15` / `severity_str: low` (Severidad baja asignada por Interflow).
  * `xdr_event.name`: `sophos_event-execution-user_execution` (Regla genérica del catálogo de Stellar Cyber).
  * `technique`: `T1204` / `tactic: TA0002` (Asignación táctica incorrecta; no existió ejecución de binarios).

**Resumen Quirúrgico Final:**  
El usuario `CAJAANDE\jrodriguez`, desde el equipo portátil `NBCJPPA20260818` (`172.16.202.43`), intentó ingresar a `https://translate.google.com` a las 04:59:58 hora local. El agente Sophos Endpoint abortó la conexión en cumplimiento de la directiva corporativa de filtrado web para la categoría `Proxies & Translators`. Stellar Cyber procesó el log mediante su conector de Sophos Central y lo categorizó erróneamente bajo la técnica MITRE T1204 (User Execution). El incidente se resuelve como Falso Positivo / Ruido Operativo de Filtrado Web.
