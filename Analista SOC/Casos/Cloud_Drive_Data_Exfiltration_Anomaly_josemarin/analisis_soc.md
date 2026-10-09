### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR)
**Tags:** `False Positive`, `Benign True Positive`, `Google Workspace`, `Cloud Drive`, `Data Exfiltration Anomaly`, `UBA`, `AppSheet`, `Apps Script`, `Servicio Tecnico`, `Jose Marin`, `TA0010`, `T1567.002`

He detectado **10 eventos completos e independientes** en tu volcado (junto con un 11.° evento recibido parcialmente en el búfer debido a truncamiento de terminal). Todos los eventos corresponden a la alerta de Machine Learning `cloud_drive_data_exfiltration_anomaly` de Google Workspace (`gsuite_Workspace-THN`) asociada a la cuenta del usuario `josemarin@technoma.com.py`. A continuación se presenta la disección forense secuencial e individual de cada uno de los eventos, concluyendo con una correlación integral y un cierre maestro unificado para el caso.

---

### Análisis Evento 1 (Anomaly ID: 8FYhzqABI3UnQyDOxwMz)

### 🎯 Resumen Ejecutivo del Evento 1 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `36`, Severidad `70`, Fidelidad `9.66`).
* **Activos Involucrados:** Cuenta corporativa Google Workspace `josemarin@technoma.com.py` (Profile ID `105470296121996656711`, Customer ID `C02am33mw`).
* **Comportamiento Anómalo:** Detección de una tasa acumulada de `451` descargas de archivos en Google Drive en un intervalo de 24 horas, frente a una línea base típica de `29`. El evento puntual registró la descarga (`drive.files.get`) del archivo de imagen `5d8affbd.firma_tecnico.113215.png` (Doc ID `1Yy7L6KhzPqw4kull3r3wEmhiC9OzMQwB`).
* **Causalidad Probable:** Operación benigna automatizada generada por la aplicación interna `POC Servicio Tecnico AppScript` (OAuth Client ID `1043972006487-k6fk24kqf8u5rhohg85e245aafvpq3ms.apps.googleusercontent.com`). El script consulta y descarga firmas digitales de técnicos y clientes para la compilación automática de actas de servicio técnico.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T11:43:39.000Z | 2026-09-23 08:43:39 | `drive.files.get` (download) | 451 | 29 | `POC Servicio Tecnico AppScript` | `5d8affbd.firma_tecnico.113215.png` | Invocación de API de Google Drive para renderizar firma de técnico en reporte de servicio. |

### 🔬 Desglose Técnico y Disección Forense
* **Identidad y Contexto del Actor:**
  - Actor: `josemarin@technoma.com.py`.
  - Aplicación Conectora: `POC Servicio Tecnico AppScript` (`originating_app_id`: `1043972006487`).
  - Propietario del Documento: `josemarin@technoma.com.py` (propietario directo, `owner_is_shared_drive`: `false`).
  - Permisos y Visibilidad: `private` (alojado dentro del propio Drive del usuario).
* **Naturaleza de los Archivos en la Ráfaga:**
  - En el sumario de la anomalía (`downloaded_files_summary`, 361 archivos) destacan patrones estrictamente operacionales:
    - Firmas de Clientes: `*.firma_cliente.*.png` (ej. `01f2303f.firma_cliente.174048.png`, `0273b5b2.firma_cliente.135719.png`).
    - Firmas de Técnicos: `*.firma_tecnico.*.png` (ej. `01f2303f.firma_tecnico.174048.png`, `0273b5b2.firma_tecnico.135006.png`).
    - Fotografías de Servicio Técnico: `*.imagen.*.jpg` (ej. `051a206d.imagen.195936.jpg`, `0683399e.imagen.144830.jpg`).

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "google_workspace_drive_api_download",
  "payload_value": "5d8affbd.firma_tecnico.113215.png (doc_id: 1Yy7L6KhzPqw4kull3r3wEmhiC9OzMQwB)",
  "payload_hash": "N/A - Llamada autenticada OAuth2 Google Drive API",
  "payload_firma": "OAuth Client ID: 1043972006487-k6fk24kqf8u5rhohg85e245aafvpq3ms.apps.googleusercontent.com",
  "payload_accion": "drive.files.get (Lectura/Descarga de activo privado)",
  "payload_destino": "Motor de ejecución de Apps Script institucional de Technoma"
}
```

**Comandos de Diagnóstico y Validación Forense:**
```powershell
# 1. Auditoría de tokens OAuth2 corporativos de Google Workspace mediante GAM / CLI
gam user josemarin@technoma.com.py show tokens

# 2. Filtrado de actividad de la aplicación en los registros de auditoría de Drive
gam report drive user josemarin@technoma.com.py app_id 1043972006487
```

**Tabla de Hipótesis Formuladas:**
| ID | Hipótesis | Evaluación Forense | Estado |
|---|---|---|---|
| H1 | Exfiltración masiva de datos corporativos a la nube personal (T1567.002). | Descartada. Los archivos consultados permanecen en el tenant institucional y son consumidos por una App interna registrada. | Descartada |
| H2 | Compromiso de credenciales del usuario `josemarin`. | Descartada. Las solicitudes no provienen de navegadores web anónimos ni IPs sospechosas, sino del Client ID de Google Apps Script. | Descartada |
| H3 | Procesamiento benigno de actas de servicio técnico mediante AppScript. | Confirmada. El nombre de los archivos y la aplicación (`POC Servicio Tecnico AppScript`) validan la generación automatizada de informes. | **Confirmada** |

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza.** La alerta responde a la desviación cuantitativa que percibe el algoritmo de Machine Learning de Stellar Cyber (`new_ml`). Al contrastar 451 descargas contra el promedio histórico de 29, infiere una fuga de información masiva. Sin embargo, no se trata de documentos confidenciales (PDFs financieros, bases de datos o código fuente) sino de imágenes de firmas digitales requeridas por la aplicación móvil de soporte técnico para incrustarlas en los reportes de visita.

---

### Análisis Evento 2 (Anomaly ID: G1pGzqABI3UnQyDOae7t)

### 🎯 Resumen Ejecutivo del Evento 2 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `35`, Severidad `70`, Fidelidad `8.54`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** Registro acumulado de `443` descargas en 24h. Evento puntual: descarga de `9a6939e9.firma_tecnico.121953.png` (Doc ID `1REHFIQnjfz8vCdpc0g6RH2cfcXWpejb9`).
* **Causalidad Probable:** Continuidad del lote de procesamiento de Apps Script (`POC Servicio Tecnico AppScript`) 40 minutos después del Evento 1, al procesar una nueva orden de servicio técnico.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T12:23:43.000Z | 2026-09-23 09:23:43 | `drive.files.get` | 443 | 29 | `POC Servicio Tecnico AppScript` | `9a6939e9.firma_tecnico.121953.png` | Procesamiento secuencial de firmas de intervención técnica. |

### 🔬 Desglose Técnico y Disección Forense
* **Detalle del Proceso:** La ventana móvil de 24 horas recalcula 443 descargas (`typical: 29`). El identificador de cliente OAuth es idéntico (`1043972006487`), confirmando la misma rutina de software. El archivo `9a6939e9.firma_tecnico.121953.png` fue generado y consultado con visibilidad privada por el propio usuario.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "google_workspace_drive_api_download",
  "payload_value": "9a6939e9.firma_tecnico.121953.png (doc_id: 1REHFIQnjfz8vCdpc0g6RH2cfcXWpejb9)",
  "payload_hash": "N/A - API Call",
  "payload_firma": "POC Servicio Tecnico AppScript (1043972006487)",
  "payload_accion": "drive.files.get",
  "payload_destino": "Servicio de compilación de órdenes de trabajo"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza.** Se verifica la misma dinámica legítima de compilación de actas de campo para clientes de Technoma.

---

### Análisis Evento 3 (Anomaly ID: 01pGzqABI3UnQyDOae3t)

### 🎯 Resumen Ejecutivo del Evento 3 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `35`, Severidad `70`, Fidelidad `8.40`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `442` descargas acumuladas. Descarga de `a88f7034.firma_tecnico.122317.png` (Doc ID `18Huf-VafCS8ipalE7-IgFdbI0gPtTcpg`).
* **Causalidad Probable:** Invocación originada por **Google AppSheet** (OAuth Client ID `953348912797-h2fo9tmk42mnrkk0kc6gula9i8ipv3re.apps.googleusercontent.com`). Demuestra que la aplicación de servicio técnico está construida sobre AppSheet, la cual interactúa con Google Drive para recuperar los anexos multimedia cargados desde el dispositivo móvil.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T12:25:29.000Z | 2026-09-23 09:25:29 | `drive.files.get` | 442 | 29 | `Google AppSheet` | `a88f7034.firma_tecnico.122317.png` | Sincronización de registros de AppSheet leyendo firmas en Google Drive. |

### 🔬 Desglose Técnico y Disección Forense
* **Transición de Aplicación:** Este evento introduce la integración con `Google AppSheet` (`953348912797`). La arquitectura se aclara por completo: los técnicos en campo utilizan una App de AppSheet ("Servicio Técnico") que captura firmas y fotos; AppSheet se comunica con Apps Script para la generación de reportes y almacenamiento de datos en Drive.

**Payload / Evidencia Principal:**
```json
{
  "payload_type": "google_workspace_appsheet_download",
  "payload_value": "a88f7034.firma_tecnico.122317.png (doc_id: 18Huf-VafCS8ipalE7-IgFdbI0gPtTcpg)",
  "payload_hash": "N/A - AppSheet Sync",
  "payload_firma": "Google AppSheet (953348912797)",
  "payload_accion": "drive.files.get",
  "payload_destino": "Plataforma Google AppSheet Enterprise"
}
```

### 🧠 ¿Por qué es (o no es) una Amenaza?
**No es una amenaza.** AppSheet es una plataforma empresarial oficial de Google (aprobada y gestionada dentro del ecosistema de Workspace). El acceso a archivos mediante su Client ID es un comportamiento intrínseco de su operativa.

---

### Análisis Evento 4 (Anomaly ID: s1xPzqABI3UnQyDOji6u)

### 🎯 Resumen Ejecutivo del Evento 4 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `35`, Severidad `70`, Fidelidad `8.96`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `446` descargas acumuladas. Descarga de `04c8769e.firma_tecnico.122947.png` (Doc ID `1pY4YmQQUWp76wdRh_aYtknI2zTaUptoC`).
* **Causalidad Probable:** Invocación de Apps Script vinculada a la orden de trabajo finalizada a las 12:29 UTC.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T12:34:05.000Z | 2026-09-23 09:34:05 | `drive.files.get` | 446 | 29 | `POC Servicio Tecnico AppScript` | `04c8769e.firma_tecnico.122947.png` | Descarga de firma de técnico por Apps Script. |

### 🔬 Desglose Técnico y Disección Forense
* **Correlación de Nombres:** Obsérvese que en el sumario aparecen emparejados `04c8769e.firma_cliente.122947.png` y `04c8769e.firma_tecnico.122947.png`, reflejando exactamente el cierre de una misma orden técnica con el prefijo GUID `04c8769e`.

---

### Análisis Evento 5 (Anomaly ID: Q15YzqABI3UnQyDOtRJc)

### 🎯 Resumen Ejecutivo del Evento 5 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `36`, Severidad `70`, Fidelidad `9.52`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `450` descargas acumuladas. Descarga de `a26cd05c.firma_tecnico.123519.png` (Doc ID `1jBFVYk-0XxnLNV_L1Ql_0e18vffrjNr2`).
* **Causalidad Probable:** Procesamiento de la orden de servicio identificada con el GUID `a26cd05c`.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T12:43:35.000Z | 2026-09-23 09:43:35 | `drive.files.get` | 450 | 29 | `POC Servicio Tecnico AppScript` | `a26cd05c.firma_tecnico.123519.png` | Descarga de firma técnica en nuevo ticket de soporte. |

---

### Análisis Evento 6 (Anomaly ID: oWBhzqABI3UnQyDO3xwX)

### 🎯 Resumen Ejecutivo del Evento 6 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `36`, Severidad `70`, Fidelidad `9.52`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `450` descargas acumuladas. Descarga de `d3e58d47.firma_tecnico.124459.png` (Doc ID `1hF9zWel29Pg4GsjIpaK6kCDIV96PEQat`).
* **Causalidad Probable:** Procesamiento automatizado de la orden de servicio `d3e58d47`.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T12:53:36.000Z | 2026-09-23 09:53:36 | `drive.files.get` | 450 | 29 | `POC Servicio Tecnico AppScript` | `d3e58d47.firma_tecnico.124459.png` | Procesamiento secuencial de orden `d3e58d47`. |

---

### Análisis Evento 7 (Anomaly ID: X2FmzqABI3UnQyDOcCnS)

### 🎯 Resumen Ejecutivo del Evento 7 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `36`, Severidad `70`, Fidelidad `9.80`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `452` descargas acumuladas. Descarga de `2b9ba513.firma_cliente.124301.png` (Doc ID `1sU6Tb6O3XhxlpUW59Oy9zzbLePSDceMa`).
* **Causalidad Probable:** Google AppSheet consultando la firma del cliente capturada en la orden `2b9ba513`.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T12:58:28.000Z | 2026-09-23 09:58:28 | `drive.files.get` | 452 | 29 | `Google AppSheet` | `2b9ba513.firma_cliente.124301.png` | AppSheet sincronizando firma de conformidad de cliente. |

---

### Análisis Evento 8 (Anomaly ID: YWJrzqABI3UnQyDOAxcG)

### 🎯 Resumen Ejecutivo del Evento 8 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `38`, Severidad `70`, Fidelidad `11.34`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `463` descargas acumuladas. Descarga de `e6be1c6c.firma_tecnico.125751.png` (Doc ID `1Ij4wh0PaR312Cgkz4NX5XRLXXt53vKOs`).
* **Causalidad Probable:** Invocación de Apps Script para la orden técnica `e6be1c6c`. El incremento a 463 descargas refleja la acumulación de sincronizaciones durante la mañana.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T13:04:04.000Z | 2026-09-23 10:04:04 | `drive.files.get` | 463 | 29 | `POC Servicio Tecnico AppScript` | `e6be1c6c.firma_tecnico.125751.png` | Apps Script procesando firma de orden `e6be1c6c`. |

---

### Análisis Evento 9 (Anomaly ID: o2JrzqABI3UnQyDOMx3a)

### 🎯 Resumen Ejecutivo del Evento 9 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `38`, Severidad `70`, Fidelidad `11.34`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `463` descargas acumuladas. Descarga de `3b887043.firma_tecnico.125840.png` (Doc ID `1gWGqFeaqIH8OYrEYr26DPR3ReelnnDTS`).
* **Causalidad Probable:** Sincronización concurrente de Google AppSheet apenas 1 minuto después del Evento 8, al actualizar la interfaz de usuario con la orden `3b887043`.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T13:05:14.000Z | 2026-09-23 10:05:14 | `drive.files.get` | 463 | 29 | `Google AppSheet` | `3b887043.firma_tecnico.125840.png` | AppSheet sincronizando vista de técnicos. |

---

### Análisis Evento 10 (Anomaly ID: 5mR0zqABI3UnQyDOLDk4)

### 🎯 Resumen Ejecutivo del Evento 10 (Formato Nativo Stellar)
* **Alerta Detectada:** Cloud Drive Data Exfiltration Anomaly (Score `38`, Severidad `70`, Fidelidad `11.06`).
* **Activos Involucrados:** `josemarin@technoma.com.py` | Google Workspace.
* **Comportamiento Anómalo:** `461` descargas acumuladas. Descarga de `717f444a.firma_tecnico.130740.png` (Doc ID `1OPEE5pq8uEPMUYSZPlHAl5hmPvEalJkq`).
* **Causalidad Probable:** Cierre del ciclo matutino de órdenes técnicas por parte de Apps Script para la orden `717f444a`.

### ⏱️ Línea de Tiempo Temporal
| Hora (UTC) | Hora (Local UTC-3) | Evento Detectado | Actual | Typical | Aplicación Actora | Archivo Consultado | Observación Forense |
|---|---|---|---|---|---|---|---|
| 2026-09-23T13:13:59.000Z | 2026-09-23 10:13:59 | `drive.files.get` | 461 | 29 | `POC Servicio Tecnico AppScript` | `717f444a.firma_tecnico.130740.png` | Descarga de firma de orden `717f444a`. |

> [!NOTE]
> **Nota de Cobertura sobre Evento 11 (Fragmento Truncado):** El archivo original contenía un fragmento de un 11.° evento (Anomaly ID `PmV9zqABI3UnQyDOVPSy` / Doc Title `302c2300.firma_cliente.132613.png`), el cual confirma exactamente la misma secuencia operacional de consultas a firmas digitales generadas por la solución móvil.

---

### Cierre Maestro Unificado

### 🛡️ Análisis de Impacto CIA Triad
```json
{
  "Confidentiality": "Sin impacto. Los archivos consultados permanecen dentro del tenant institucional de Google Workspace y corresponden a anexos operativos de órdenes de trabajo (firmas y fotos de servicio técnico) gestionados por aplicaciones internas autorizadas.",
  "Integrity": "Sin impacto. Las llamadas registradas corresponden a operaciones de lectura ('drive.files.get'). No hubo alteración ni corrupción de archivos en Google Drive.",
  "Availability": "Sin impacto. El almacenamiento de Google Drive y la operatividad de AppSheet y Apps Script se mantuvieron plenamente funcionales."
}
```

### ⚖️ Veredicto y Confianza Analítica (Metodología de 7 Etapas)
```json
{
  "Veredicto": "Benign True Positive",
  "Confianza": "100%",
  "Motivo": "La totalidad de las descargas en Google Drive fueron ejecutadas mediante APIs OAuth autorizadas de Google AppSheet y Apps Script corporativo ('POC Servicio Tecnico AppScript') para la sincronización de firmas digitales e imágenes asociadas a órdenes de trabajo de Technoma. La alerta deriva exclusivamente de la sensibilidad del modelo de Machine Learning ante la volumetría atípica generada por la automatización."
}
```

### 📉 Indicador de Fatiga de Alertas
```json
{
  "Fatiga": "Alta",
  "Razón": "El modelo de UBA de Stellar Cyber dispara alertas consecutivas cada pocos minutos (buckets móviles de 24h) mientras la aplicación móvil sincroniza lotes de fotos y firmas, generando decenas de eventos redundantes para un único proceso legítimo."
}
```

### 📘 Fase del Ciclo NIST 800-61
| Fase NIST | Acción Técnica |
|---|---|
| **Detección y Análisis** | Correlación de eventos de Google Workspace Audit (`gsuite_Workspace-THN`), extracción de OAuth Client IDs y análisis de contenido de los archivos (`*.firma_tecnico.*`, `*.firma_cliente.*`). |
| **Contención, Erradicación y Recuperación** | No requerida. Tráfico corporativo completamente esperado y autorizado. |
| **Actividad Post-Incidente** | Documentar los OAuth Client IDs de `Google AppSheet` y `POC Servicio Tecnico AppScript` en la base de conocimiento para configurar reglas de exclusión/tuning en Stellar Cyber y evitar alertas repetitivas de exfiltración. |

### 📚 Playbook Asignado y Escalación CERT-PY
| ID | Nombre | Justificación Estratégica |
|---|---|---|
| **PB-002** | Manejo de Falsos Positivos y Ruido Operativo de UBA | Descarte de alertas de Machine Learning provocadas por integraciones de software empresarial legítimo (AppSheet/Apps Script). |
| **CERT-PY** | No Aplica Escalación | Actividad netamente interna, benigna y autorizada sin compromiso de credenciales ni exfiltración fuera del perímetro corporativo. |

> [!NOTE]
> **Mecanismo Human-In-The-Loop (HITL):** Al confirmarse la naturaleza benigna del caso, no se requiere autorización para acciones de bloqueo. Si se desea formular una regla de afinamiento en Stellar Cyber para suprimir alertas de este Client ID, responda `"dame los pasos"`.

### 🏷️ Resolution Tag para Stellar Cyber
`False Positive` - Normal Administrative Behavior / Legitimate Application Sync (Google AppSheet & Apps Script).

### 📝 Datos para Bitácora de Excel (Apoyo Visual y 1-Clic TSV)

| Fecha y Hora | Analista | Tenant | ID del caso | Fuente de Detección | Nro. Ticket | Prioridad | Tipo de evento | Asunto | Activos | Descripción | Evidencia | Solicitud de Accion | Estado | URL | Generación de Ticket | TICKET | Playbook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 23/09/2026 13:50 | Analista SOC | technoma | Cloud_Drive_Data_Exfiltration_Anomaly_josemarin | Stellar Cyber (new_ml) | - | Media | Cloud Drive Exfiltration Anomaly | Sincronización masiva de firmas técnicas mediante AppSheet y Apps Script | josemarin@technoma.com.py | Benign True Positive / Falso Positivo. Detección heurística de exfiltración en Google Drive (440-463 descargas vs línea base de 29) en la cuenta de josemarin@technoma.com.py. La investigación forense determinó que las solicitudes 'drive.files.get' fueron emitidas por las aplicaciones corporativas Google AppSheet y 'POC Servicio Tecnico AppScript' para la sincronización y compilación de firmas digitales y fotografías de órdenes de servicio técnico. No existe compromiso ni exfiltración externa. | Google Workspace Audit / OAuth AppSheet | Ninguna (Tuning sugerido en SIEM) | Cerrado | - | No | - | PB-002 |

**Fila Cruda para Copiar (1-Clic TSV):**
```tsv
23/09/2026 13:50	Analista SOC	technoma	Cloud_Drive_Data_Exfiltration_Anomaly_josemarin	Stellar Cyber (new_ml)	-	Media	Cloud Drive Exfiltration Anomaly	Sincronización masiva de firmas técnicas mediante AppSheet y Apps Script	josemarin@technoma.com.py	"Benign True Positive / Falso Positivo. Detección heurística de exfiltración en Google Drive (440-463 descargas vs línea base de 29) en la cuenta de josemarin@technoma.com.py. La investigación forense determinó que las solicitudes 'drive.files.get' fueron emitidas por las aplicaciones corporativas Google AppSheet y 'POC Servicio Tecnico AppScript' para la sincronización y compilación de firmas digitales y fotografías de órdenes de servicio técnico. No existe compromiso ni exfiltración externa."	Google Workspace Audit / OAuth AppSheet	Ninguna (Tuning sugerido en SIEM)	Cerrado	-	No	-	PB-002
```

### 💻 Instrucción para Cierre en Stellar Cyber
* **Estado:** Closed
* **Resolution Tag:** False Positive
* **Comentario final:**
Tras realizar una minuciosa inspección de la telemetría de auditoría de Google Workspace (`gsuite_Workspace-THN`), se concluye que el lote de alertas de anomalía por exfiltración en Google Drive asociadas al usuario `josemarin@technoma.com.py` corresponde a un falso positivo operacional derivado de procesos legítimos de sincronización (Benign True Positive). La volumetría atípica registrada por el motor analítico de Machine Learning (`442` a `463` descargas frente a la cota base de `29`) fue originada exclusivamente por las herramientas corporativas Google AppSheet (OAuth Client ID `953348912797`) y Apps Script (`POC Servicio Tecnico AppScript`, Client ID `1043972006487`). Estas aplicaciones realizan llamadas masivas al método de API `drive.files.get` para compilar e incrustar las firmas digitales de clientes y técnicos, así como fotografías de respaldo, en las actas de servicio técnico del área de operaciones de Technoma. Los recursos involucrados permanecen bajo la custodia del propio usuario dentro del almacenamiento institucional, descartándose rotura de confidencialidad, compromiso de cuenta o exfiltración hacia destinos externos. Se da por concluida la investigación y se cierra formalmente el ticket.

> [!TIP]
> **Propuesta de Mejora Institucional:** Se recomienda documentar los OAuth Client IDs de AppSheet y Apps Script en la Memoria Institucional (`SOC_GEM_v2.md`) y agregar la Plantilla 16 en `plantillas_cierre_soc.md` para estandarizar el triaje rápido de alertas generadas por soluciones low-code/AppSheet en Google Workspace.

---

### 🔬 Desglose Ultra Quirúrgico
* **Capa 1: Red y Conectividad Cloud**
  - Origen: Servicios Cloud de Google Workspace e infraestructura SaaS de Google AppSheet.
  - Contexto de Identidad: `josemarin@technoma.com.py`, perteneciente a la organización corporativa (`customerId`: `C02am33mw`).
* **Capa 2: Aplicación y API de Almacenamiento (`gsuite.events` / `event_detail`)**
  - Método API: `drive.files.get` (descarga/lectura autenticada).
  - Tipo de Recurso: Archivos binarios de imagen privada (`type: png` y `jpg`).
  - Nomenclatura Forense: Archivos con marcas de tiempo y hashes identificativos de orden técnica (ej. `<hash>.firma_tecnico.<hhmmss>.png` y `<hash>.firma_cliente.<hhmmss>.png`).
* **Capa 3: Autenticación OAuth2 y Actores (`applicationInfo`)**
  - Aplicación 1: `POC Servicio Tecnico AppScript` (OAuth Client ID `1043972006487-k6fk24kqf8u5rhohg85e245aafvpq3ms.apps.googleusercontent.com`).
  - Aplicación 2: `Google AppSheet` (OAuth Client ID `953348912797-h2fo9tmk42mnrkk0kc6gula9i8ipv3re.apps.googleusercontent.com`).
  - Suplantación de Identidad (`impersonation`): `false` (ejecución directa bajo el contexto del usuario autenticado).
* **Capa 4: Motor de Machine Learning / UBA (`stellar` / `xdr_event`)**
  - Modelo de Detección: `new_ml` (`cloud_drive_data_exfiltration_anomaly`).
  - Ratio de Disparo: ~15x sobre la línea base histórica del usuario (450 descargas vs 29 esperadas en 24h).
  - Mapeo MITRE: TA0010 (Exfiltration) / T1567.002 (Exfiltration to Cloud Storage).

**Resumen Quirúrgico Final:** La alerta surge de una discrepancia puramente estadística calculada por el motor de comportamiento de Stellar Cyber al registrar cientos de transacciones de API en una cuenta que normalmente tiene baja actividad de descarga directa. La inspección forense a nivel de metadatos OAuth y la semántica de los nombres de archivo certifican que no existe exfiltración adversaria, sino una rutina automatizada de la solución móvil de servicio técnico de Technoma basada en Google AppSheet y Apps Script.
