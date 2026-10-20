# 🧭 MAPA MAESTRO DE PROCEDIMIENTOS Y ARQUITECTURA PYTHON (SOAR TECHNOMA)
> **Directiva de Operación para la IA (Antigravity)**: Este documento es la referencia definitiva de qué hace cada script en `g:\Hermes + Antigravity\soar`.  
> **REGLA DE ORO**: Cuando el usuario solicite una tarea (consultar cuota, analizar un caso, investigar un observable, revisar filtros o correr la interfaz), **NO busques en el workspace ni leas archivos a ciegas**. Usá directamente el script y comando indicado en esta guía.

---

## ⚡ TABLA RÁPIDA: QUÉ EJECUTAR SEGÚN LO QUE PIDA EL USUARIO

| Cuando el usuario te pida... | Qué comando o script usar | Qué hace exactamente |
| :--- | :--- | :--- |
| **"Control cruzado / Verificar casos de Cortex en Stellar"** | `python sync_cortex_cases.py --month YYYY-MM` *(o `--dry-run`)* | Rastrea alertas de Cortex con `case_id`, crea los casos faltantes en Stellar y vincula su telemetría forense. |
| **"Cerrar masivamente casos / resolver incidentes"** | `python close_cases_bulk.py --cortex-cases <LISTA> --resolution <Benign/False Positive>` *(o `--month YYYY-MM`)* | Cierra casos masivamente aplicando estado oficial `Resolved` y resolución estandarizada en Stellar Cyber. |
| **"Auditar hits de alertas en el Data Lake (vista web hits)"** | `python stellar_alerts_checker.py --hours 12` *(o `--today`, `--type <STR>`)* | Replica la vista `/alerts?view=hits`, audita anomalías (arp.exe, LOLBINs) e inspecciona payload IDS. |
| **"Auditar tarjetas de Threat Hunting / Interflow (por qué arroja esos números)"** | `python threat_hunting_exact_auditor.py` *(o `threat_hunting_auditor.py --hours 24`)* | Reconcilia 1:1 las cards de Threat Hunting Library (Firewall 2.1M, Network Apps 3.3M, Windows Logins, DNS, etc.) con sus índices y queries nativas. |
| **"Citar / listar / resumir casos abiertos y cierres"** | `python stellar_case_fetcher.py --open` *(abiertos)* o `python stellar_case_fetcher.py --closed --today` *(cerrados de hoy)* | Consulta vía MCP oficial de Stellar Cyber sin fallos de encoding ni de ID. |
| **"Auditar si los cierres de casos corresponden"** | `python stellar_case_fetcher.py --audit-closures --today` | Extrae y audita dictámenes forenses de analistas y concordancia con alertas. |
| **"Verificá / analizá el caso #XXXXX"** | `python stellar_case_fetcher.py --case XXXXX` *(o `python soar_cli.py analyze XXXXX`)* | Trae el detalle vía MCP traduciendo automáticamente el Ticket ID a Hex ID y analizando con RAG. |
| **"Escaneá esta IP / Dominio / Hash"** | `python soar_cli.py cti <OBSERVABLE>` | Corre Tri-Scan en paralelo (VirusTotal + AbuseIPDB + URLScan) con caché en RAM. |
| **"¿Qué tenemos documentado de X tema / cliente?"** | `python soar_cli.py rag "<QUERY>" --top-k 5` | Consulta el índice de 2.084 Markdowns en 8 ms y devuelve los 5 fragmentos más relevantes con score y capa. |
| **"¿Cómo viene el consumo de Syslog / Licencia / Cuota?"** | `python auditoria_cuota_stellar/01_consultar_consumo_licencia.py` *(o `03_auditoria_fortigate_deep_dive.py`)* | Consulta el pozo global (10 GB), desglose por tenant y top políticas/puertos. |
| **"¿Qué queries guardadas / filtros de logs / reglas ATH tenemos?"** | `python stellar_query_inspector.py --queries` *(o `--filters`, `--filter-detail X`, `--ath`, `--in-use`)* | Inspecciona las 72+ Saved Queries, uso en ATH/Charts, y desglosa el JSON real de los 51 Log Filters. |
| **"Auto-Investigar 360° / Threat Hunting automatizado en 1 clic"** | Botón `🚀 Auto-Investigar 360°` en Cockpit *(o doc [ARQUITECTURA_SUITE_THREAT_HUNTING_360.md](file:///g:/Hermes%20+%20Antigravity/soar/ARQUITECTURA_SUITE_THREAT_HUNTING_360.md))* | Orquestador unificado que detecta IP (Privada/Pública) o Dominio (PaaS/Propio) y dispara en paralelo la batería CTI y forense exacta. |
| **"Consultar informe de la campaña de phishing Netlify"** | Leer [INFORME_HUNTING_PHISHING_NETLIFY_20261020.md](file:///g:/Hermes%20+%20Antigravity/soar/INFORME_HUNTING_PHISHING_NETLIFY_20261020.md) | Dictamen forense completo de las firmas IDS de Netlify (`nb-sdoncell`, `nb-wgonzalez`), URLScan y takedowns. |
| **"Hacé Threat Hunting / buscá logs de X IP, usuario o puerto"** | `python stellar_threat_hunter.py --ip <IP>` *(o `--user <USER>` o `--query "<LUCENE>"`)* | Caza en vivo en Data Lake de Interflow, Firewall y WinEvent con agregaciones forenses. |
| **"Buscá en el Data Lake / Interflow (crudo)"** | `python stellar_cli.py --search "<LUCENE_QUERY>"` | Ejecuta queries en el Data Lake (ej: `srcip:192.168.1.1`). |
| **"Abrir el Cockpit"** | Doble clic en `INICIAR_COMMAND_CENTER.bat` *(o `Start-Process pythonw -ArgumentList "command_center.py"`)* | Lanza la GUI completa (10.425 líneas) desacoplada de la terminal. |
| **"Abrir el Copiloto Forense autónomo"** | `python soc_agent_gui.py` | Abre la ventana independiente de chat forense con Gemini 3.8 + RAG. |
| **"Inspeccionar endpoints / MDR Sophos (CAJAANDE)"** | `python sophos_mdr_cli.py --summary` *(o `--host <NAME>`, `--suspicious`, `--alerts`)* | Consulta postura, alertas activas y telemetría de 123 endpoints en Sophos Central (100% Read-Only, sin remediación intrusiva). |

---

## 📂 CATÁLOGO EXHAUSTIVO DE SCRIPTS PYTHON (.py)

### 1. 🎛️ NÚCLEO Y COCKPIT DESKTOP (GUI)
* [**`command_center.py`**](file:///g:/Hermes%20+%20Antigravity/soar/command_center.py) (10.425 líneas)
  * **Qué hace**: Es la aplicación central de escritorio del SOC (PySide6). Monitorea casos en vivo, gestiona SLA/SLO (MTTD/MTTR), analiza alertas con Gemini 3.8 Flash + RAG con streaming SSE, extrae Interflow, tiene analizador de phishing, reporte masivo AbuseIPDB, generador de tickets Technoma, pre-DPI validator y alertas push a móviles vía `ntfy.sh`.
  * **Cuándo se toca**: Solo cuando se requiera mejorar o arreglar funciones de la interfaz gráfica principal.

* [**`soc_agent_gui.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soc_agent_gui.py) & [**`soc_agent.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soc_agent.py)
  * **Qué hace**: Copiloto forense conversacional. Permite chatear con Gemini 3.8 Flash inyectando casos crudos, logs de Suricata o eventos de Windows, consultando siempre el RAG local.

* [**`ui_theme.py`**](file:///g:/Hermes%20+%20Antigravity/soar/ui_theme.py) & [**`cyber_telemetry_widgets.py`**](file:///g:/Hermes%20+%20Antigravity/soar/cyber_telemetry_widgets.py)
  * **Qué hace**: Estilos cyberpunk / oscuro de la interfaz, widgets de top protocolos de red y monitoreo de salud de sensores.

---

### 2. 🧠 INTELIGENCIA ARTIFICIAL Y MEMORIA (RAG DE 2.086 MARKDOWNS)
* [**`rag_engine.py`**](file:///g:/Hermes%20+%20Antigravity/soar/rag_engine.py)
  * **Qué hace**: Motor de recuperación BM25 local sobre **2.086 archivos Markdown** (`14.150+` chunks) estructurado en 7 capas con pesos diferenciales (`MEMORIA_SOC`, `CASO_HISTORICO`, `PLAYBOOK`, `PROCEDIMIENTO_ARQ`, `SKILL_SOC`, `DOC_STELLAR`, `ACADEMIA_SOC`).
  * **Almacenamiento**: Persiste en [`.rag_index_cache.pkl`](file:///g:/Hermes%20+%20Antigravity/soar/.rag_index_cache.pkl) (tiempo de consulta: 8.69 ms). Se auto-actualiza solo si detecta archivos modificados.

* [**`soar_ai_client.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_ai_client.py)
  * **Qué hace**: Cliente unificado de Inteligencia Artificial. Conecta a Google Antigravity OAuth (`gemini-3.8-flash-high`) con rotación automática de credenciales y streaming SSE. Fallbacks transparentes a Gemini REST API, NVIDIA NIM (`Llama-3.2`) u OpenAI.

* [**`stellar_gemini_orchestrator.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_gemini_orchestrator.py)
  * **Qué hace**: Orquestador forense. Limpia telemetría cruda ([`forensic_utils.py`](file:///g:/Hermes%20+%20Antigravity/soar/forensic_utils.py)), aplica anonimización PII reversible opcional en RAM (`SecurityMaskingEngine`), inyecta los hits del RAG de 2.086 Markdowns, controla el tope de 80 KB y transmite el dictamen en streaming.

* [**`playbook_engine.py`**](file:///g:/Hermes%20+%20Antigravity/soar/playbook_engine.py) & [**`integrate_playbooks.py`**](file:///g:/Hermes%20+%20Antigravity/soar/integrate_playbooks.py)
  * **Qué hace**: Mapeo estricto de eventos de Stellar Cyber contra los 57 Playbooks oficiales del SOC (PB 1.1 al PB 6.4).

---

### 3. 🌐 CONECTORES STELLAR CYBER, SECURITY ONION Y CTI
* [**`sync_cortex_cases.py`**](file:///g:/Hermes%20+%20Antigravity/soar/sync_cortex_cases.py)
  * **Qué hace**: Motor de control cruzado y sincronización bidireccional Cortex XDR ➔ Stellar Cyber. Rastrea en `aella-ser-*` los eventos con `palo_alto_networks.case_id`, crea los casos faltantes vía `POST /connect/api/v1/cases` y vincula automáticamente sus alertas forenses mediante `POST /connect/api/v1/cases/{id}/alerts`.
  * **Parámetros**: `--month YYYY-MM`, `--limit N`, `--dry-run`.

* [**`close_cases_bulk.py`**](file:///g:/Hermes%20+%20Antigravity/soar/close_cases_bulk.py)
  * **Qué hace**: Remediador y cerrador masivo de casos en Stellar Cyber vía API REST. Aplica de forma estricta el estado `status: "Resolved"` y la resolución (`"Benign"`, `"False Positive"`, `"True Positive"`).
  * **Parámetros**: `--cortex-cases 610,604`, `--stellar-cases <HEX>`, `--month YYYY-MM`, `--resolution <TIPO>`, `--dry-run`.

* [**`stellar_alerts_checker.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_alerts_checker.py)
  * **Qué hace**: Auditor forense de hits de alertas crudas en el Data Lake (`aella-ser-*`). Replica exactamente la vista web `/alerts?view=hits`, analiza procesos no comunes (`arp.exe`, PowerShell, LOLBINs) y extrae payload IDS.

* [**`stellar_case_fetcher.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_case_fetcher.py)
  * **Qué hace**: Consultor y auditor MCP de casos de Stellar Cyber. Traduce automáticamente Ticket ID (`#17858`) a Hex ID, lista casos abiertos (`--open`), cerrados (`--closed --today`) y audita si las justificaciones de cierre corresponden (`--audit-closures`).

* [**`stellar_query_inspector.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_query_inspector.py)
  * **Qué hace**: Inspector rápido de Saved Queries (`--queries`, `--in-use`, `--query-detail`), Log Filters desglosados (`--filters`, `--filter-detail`), reglas ATH (`--ath`) y limpiador de queries huérfanas de prueba (`--cleanup-orphans`).

* [**`stellar_threat_hunter.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_threat_hunter.py)
  * **Qué hace**: Motor directo de Threat Hunting sobre Elasticsearch/Data Lake (`/connect/api/data/*/_search`) sin ensuciar las Saved Queries. Soporta búsqueda bidireccional por IP, usuario, puerto y query Lucene con agregaciones.

* [**`stellar_cli.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_cli.py)
  * **Qué hace**: La herramienta CLI multi-función para hablar con la API y MCP de Stellar Cyber (`technoma.stellarcyber.cloud`). Permite consultar casos, alertas, tenants, cuota, buscar en Data Lake y gestionar log filters.

* [**`soar_cli.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_cli.py)
  * **Qué hace**: La navaja suiza unificada creada para el agente. Agrupa comandos `cti`, `rag`, `memory`, `catalog`, `sla` y `triage` en una sola línea de comandos.

* [**`cti_engine.py`**](file:///g:/Hermes%20+%20Antigravity/soar/cti_engine.py)
  * **Qué hace**: Motor de Cyber Threat Intelligence. Consulta en hilos paralelos VirusTotal, AbuseIPDB y URLScan con caché TTL de 15 minutos en memoria.

* [**`threat_hunting_exact_auditor.py`**](file:///g:/Hermes%20+%20Antigravity/soar/threat_hunting_exact_auditor.py) & [**`threat_hunting_auditor.py`**](file:///g:/Hermes%20+%20Antigravity/soar/threat_hunting_auditor.py)
  * **Qué hace**: Reconciliación forense y matemática 1:1 de la pantalla **Threat Hunting Library / Interflow Search** de Stellar Cyber. Mapea exactamente cada una de las tarjetas visibles (`Firewall 2.1M`, `Network Applications 3.3M`, `DNS Analysis 717.1k`, `Google Workspace 59.7k`, `Windows Logins 22.4k`, `All Login Failures 60.2k`, etc.) consultando sus índices nativos (`adr`, `wineventlog`, `audit`, `syslog`, `ser`) y explica el origen técnico de cada número.
  * **Comandos**: `python threat_hunting_exact_auditor.py` *(o con `--hours 24`)*.

* [**`so_engine.py`**](file:///g:/Hermes%20+%20Antigravity/soar/so_engine.py)
  * **Qué hace**: Motor de conexión con el Grid de Security Onion 3 (`https://172.17.10.25:9200`). Ejecuta consultas elásticas a Suricata, Zeek y correlaciona alertas de red.

* [**`sophos_mdr_cli.py`**](file:///g:/Hermes%20+%20Antigravity/soar/sophos_mdr_cli.py)
  * **Qué hace**: Cliente e inspector MDR de solo lectura para Sophos Central (CAJAANDE / Multi-tenant). Consulta estado de salud del parque (123 endpoints), identifica hosts en riesgo (`suspicious`/`bad`), lista alertas activas de seguridad, extrae la ficha forense completa (interfaces, servicios de seguridad, tamper protection) y recupera eventos SIEM sin ejecutar acciones intrusivas.
  * **Comandos**: `python sophos_mdr_cli.py --summary`, `python sophos_mdr_cli.py --suspicious`, `python sophos_mdr_cli.py --host <HOSTNAME>`, `python sophos_mdr_cli.py --alerts`, `python sophos_mdr_cli.py --events`.

---

### 4. 📋 TICKETS, REPORTES Y MÓDULOS FORENSES ESPECIALIZADOS
* [**`thn_ticket_generator.py`**](file:///g:/Hermes%20+%20Antigravity/soar/thn_ticket_generator.py)
  * **Qué hace**: Generador de reportes Technoma. Produce la fila exacta de 40 columnas para la planilla **FL-THN-POS-01 Rev. 03**, la bitácora de turno TSV (18 columnas) y reportes ejecutivos en HTML/PDF.

* [**`email_header_analyzer.py`**](file:///g:/Hermes%20+%20Antigravity/soar/email_header_analyzer.py)
  * **Qué hace**: Forense de cabeceras de correos de phishing (`Received:`, hops SMTP, validación SPF/DKIM/DMARC y bypass de CDN).

* [**`abuse_report_dialog.py`**](file:///g:/Hermes%20+%20Antigravity/soar/abuse_report_dialog.py) & [**`generar_reportes_abuso.py`**](file:///g:/Hermes%20+%20Antigravity/soar/generar_reportes_abuso.py)
  * **Qué hace**: Reporte automático de IPs maliciosas atacantes hacia AbuseIPDB y registro en `registro_ips_reportadas.json`.

* [**`predpi_validator_module.py`**](file:///g:/Hermes%20+%20Antigravity/soar/predpi_validator_module.py) & [**`stellar_log_filter_manager.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_log_filter_manager.py)
  * **Qué hace**: Validación y despliegue de filtros de descarte Pre-DPI y expresiones Lucene en sensores de Stellar Cyber.

* [**`feeds_intel_module.py`**](file:///g:/Hermes%20+%20Antigravity/soar/feeds_intel_module.py), [**`feeds_engine.py`**](file:///g:/Hermes%20+%20Antigravity/soar/feeds_engine.py) & [**`feeds_ai_orchestrator.py`**](file:///g:/Hermes%20+%20Antigravity/soar/feeds_ai_orchestrator.py)
  * **Qué hace**: Descarga feeds RSS de ciberseguridad (`feeds_intel.db`), enriquece CVEs con NVD y redacta boletines para clientes con IA.

* [**`whois_recon.py`**](file:///g:/Hermes%20+%20Antigravity/soar/whois_recon.py) & [**`dnstwist_recon.py`**](file:///g:/Hermes%20+%20Antigravity/soar/dnstwist_recon.py)
  * **Qué hace**: Reconocimiento OSINT de dominios sospechosos, DNS typosquatting y homógrafos.

---

### 5. 📊 AUDITORÍA DE CUOTA Y LICENCIAS (`auditoria_cuota_stellar/` & Suite Forense)
* [**`01_consultar_consumo_licencia.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/01_consultar_consumo_licencia.py): Estado del pozo de 10 GB y consumos por cliente.
* [**`02_resumen_diario_indices.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/02_resumen_diario_indices.py): Muestra qué índices y tipos de dispositivos (`fw_fortigate`, etc.) consumieron más gigas en el día.
* [**`03_auditoria_fortigate_deep_dive.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/03_auditoria_fortigate_deep_dive.py): Desglose forense de FortiGate: qué políticas, interfaces (`WiFi_Corp`) y puertos (443, 53) generan los logs.
* [**`05_auditar_log_filters_existentes.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/05_auditar_log_filters_existentes.py): Inspección de los 51 filtros de log para verificar reglas `Drop`.
* [**`09_verificar_filtro_en_vivo.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/09_verificar_filtro_en_vivo.py): Comprueba si un filtro recién creado está descartando tráfico en tiempo real.
* [**`threat_hunting_exact_auditor.py`**](file:///g:/Hermes%20+%20Antigravity/soar/threat_hunting_exact_auditor.py): Reconciliación matemática 1:1 de las tarjetas de la UI de Threat Hunting con los índices reales (`adr`, `wineventlog`, `audit`, `syslog`, `ser`).
* [**`deep_dive_loaded_events.py`**](file:///g:/Hermes%20+%20Antigravity/soar/deep_dive_loaded_events.py): Diagnóstico forense profundo de las 4 tarjetas más cargadas de Stellar Cyber (acciones, puertos, usuarios ruidosos de AD/Google).
* [**`fw_quota_deepdive.py`**](file:///g:/Hermes%20+%20Antigravity/soar/fw_quota_deepdive.py): Análisis de impacto bruto de cuota en logs de firewall: desglose de los ~2 millones de eventos en gigabytes reales por acción, política y puerto.
* [**`audit_yesterday_domains.py`**](file:///g:/Hermes%20+%20Antigravity/soar/audit_yesterday_domains.py) & [**`audit_benign_domains.py`**](file:///g:/Hermes%20+%20Antigravity/soar/audit_benign_domains.py): Extracción y auditoría de dominios recurrentes en tráfico `passthrough` para saneamiento de cuota.
* [**`compare_saturdays.py`**](file:///g:/Hermes%20+%20Antigravity/soar/compare_saturdays.py): Comparador punto a punto entre fines de semana en idéntica franja horaria para aislar la efectividad real de los filtros desplegados.

---

### 6. 🏗️ ARQUITECTURA MODULAR DEL COMMAND CENTER (`soar_app/` v6.5.2)
* [**`command_center.py`**](file:///g:/Hermes%20+%20Antigravity/soar/command_center.py): Entrypoint ligero y fachada 100% retrocompatible que re-exporta todas las clases y lanza [`XdrDashboard`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/main_window.py).
* [**`soar_app/core/infra.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/core/infra.py): Carga segura de `.env`, `LRUCache`, `RestSessionManager` (renovación proactiva JWT), `MobileAlertsNotifier` (ntfy.sh) y sanitización forense.
* [**`soar_app/workers/api_workers.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/workers/api_workers.py): Los 19 workers multihilo (`QThread` y `QRunnable`) de casos, salud, Interflow, IA, CTI, CVE Batch y Security Onion.
* [**`soar_app/workers/auto_remediators.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/workers/auto_remediators.py): Los 6 demonios de auto-remediación y auto-guardia 24/7 (`HealthMailbox`, `SophosTranslate`, `SatiDns`, `DPAPIStorage`, `CaseIdentityProbe`, `AutoAssign`).
* [**`soar_app/ui/window_manager.py`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/window_manager.py): **`SOCWindowManager` y `SOCManagedWindow`**. Estandariza todas las ventanas satélites (`parent=None` con banderas nativas de Windows `Qt.Window | Qt.WindowMinMaxButtonsHint`, eliminando bloqueos `.exec()`), añade soporte de 1 clic para **Acoplar en Pestaña (`📌`) <-> Desacoplar a Ventana Independiente (`↗`)** y provee la barra inferior de ventanas activas/minimizadas en el Cockpit.
* [**`soar_app/ui/tabs/`**](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs):
  * [`triage_ops_mixin.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs/triage_ops_mixin.py): Triaje L1, Cola SOAR, Auto-Remediadores UI y Playbook 6.3.
  * [`analytics_playbooks_mixin.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs/analytics_playbooks_mixin.py): Métricas Ejecutivas SOC, SLA, Catálogo de Playbooks y Anti-Sleep.
  * [`terminal_cti_mixin.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs/terminal_cti_mixin.py): Consola Forense DFIR, 15 Presets de Reconocimiento, FortiGate Block CLI y lanzadores de módulos satélites.
  * [`cve_intel_mixin.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs/cve_intel_mixin.py): Motor NVD NIST 2.0 Batch & CVE Intelligence.
  * [`security_onion_mixin.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs/security_onion_mixin.py): Integración Security Onion Grid, Pre-DPI Validator (Tab 8) e inicializador de Tab 9.
  * [`stellar_hunter_tab.py`](file:///g:/Hermes%20+%20Antigravity/soar/soar_app/ui/tabs/stellar_hunter_tab.py): **Pestaña 9 / Ventana `🔍 Queries, Dominios & Hunter`** que integra visualmente en la GUI a `stellar_query_inspector.py` (cobertura de dominios y gestión de filtros), `stellar_threat_hunter.py` y `stellar_case_fetcher.py` (auditoría de cierres del turno).
* [**`scripts_archivo/`**](file:///g:/Hermes%20+%20Antigravity/soar/scripts_archivo): Archivo ordenado de los 19 scripts históricos de diagnóstico/reportes y el backup íntegro del monolito original (`command_center_monolith_v651_backup.py`).

