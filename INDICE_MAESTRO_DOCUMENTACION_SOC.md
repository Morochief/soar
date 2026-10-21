# 🗺️ ÍNDICE MAESTRO DE DOCUMENTACIÓN Y ARTEFACTOS SOC (KNOWLEDGE MAP)

> **PROPÓSITO PARA EL ANALISTA Y AGENTES IA:**  
> Este es el mapa central de navegación del entorno SOC. **Antes de realizar búsquedas a ciegas (`grep`, scripts ad-hoc o conjeturar rutas)**, consulta este índice para identificar exactamente qué documento o herramienta resuelve la necesidad actual.

---

## ⚡ 1. Herramientas de Ejecución Rápida y Automatización

| Herramienta | Ubicación | Propósito y Comandos Clave |
| :--- | :--- | :--- |
| **Sync y Control Cruzado Cortex** | [**`sync_cortex_cases.py`**](file:///g:/Hermes%20+%20Antigravity/soar/sync_cortex_cases.py) | **Control cruzado Cortex XDR ➔ Stellar Cyber**. Detecta alertas con `case_id`, crea los casos faltantes y asocia su evidencia forense.<br>`python sync_cortex_cases.py --month 2026-10`<br>`python sync_cortex_cases.py --dry-run` |
| **Cierre Masivo de Casos** | [**`close_cases_bulk.py`**](file:///g:/Hermes%20+%20Antigravity/soar/close_cases_bulk.py) | **Resolución y cierre masivo en Stellar Cyber** aplicando estado estricto `Resolved` y resolución (`Benign`, `False Positive`, `True Positive`).<br>`python close_cases_bulk.py --cortex-cases 610,604 --resolution "Benign"`<br>`python close_cases_bulk.py --month 2026-10 --resolution "Benign"` |
| **Auditor de Hits de Alertas** | [**`stellar_alerts_checker.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_alerts_checker.py) | **Inspección forense de hits crudos en Data Lake** (`aella-ser-*`), emulando la vista web `/alerts?view=hits`.<br>`python stellar_alerts_checker.py --hours 12`<br>`python stellar_alerts_checker.py --type "arp.exe"` |
| **Auditor Threat Hunting Library** | [**`threat_hunting_exact_auditor.py`**](file:///g:/Hermes%20+%20Antigravity/soar/threat_hunting_exact_auditor.py) | **Reconciliación matemática 1:1 de las tarjetas de Threat Hunting Library** (Firewall 2.1M, Network Apps 3.3M, Windows Logins, DNS, etc.) con sus índices y queries nativas.<br>`python threat_hunting_exact_auditor.py`<br>`python threat_hunting_auditor.py --hours 24` |
| **Deep Dive Eventos Cargados** | [**`deep_dive_loaded_events.py`**](file:///g:/Hermes%20+%20Antigravity/soar/deep_dive_loaded_events.py) | **Diagnóstico forense profundo** de las 4 tarjetas con mayor volumen (Firewall, Network Apps, Login Failures, Google Workspace), aislando cuentas ruidosas de AD y Google.<br>`python deep_dive_loaded_events.py` |
| **Deep Dive Cuota de Firewall** | [**`fw_quota_deepdive.py`**](file:///g:/Hermes%20+%20Antigravity/soar/fw_quota_deepdive.py) | **Impacto en Gigabytes de los logs de FortiGate** (~2M eventos/día), desglosando volumen y gigas por acción (`accept`, `close`, `deny`), política y puerto.<br>`python fw_quota_deepdive.py` |
| **Auditoría Diaria Dominios/Syslog** | [**`17_auditoria_dominios_y_syslog_diario.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py) | **Auditoría forense de 24h**: Top Acciones, Top 35 URLs UTM, Top 30 Dominios DNS en NDR, Syslog No-Firewall e inspección de puertos pesados.<br>`python auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py`<br>`python auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py --date 2026-10-17` |
| **Auditor Seguridad Log Filters** | [**`18_auditoria_seguridad_y_efectividad_log_filters.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py) | **Auditoría de los 54+ Log Filters y cruce empírico Firewall vs NDR (`interflow_traffic`)** para detectar puntos ciegos y medir volumen real retenido antes de modificar reglas.<br>`python auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py --verify-effectiveness` |
| **Hot-Reload Log Filters (API PUT)** | [**`19_actualizar_log_filters_en_caliente.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/19_actualizar_log_filters_en_caliente.py) | **Actualización en caliente en el Modular Sensor** vía `PUT /connect/api/v1/log_filters/{id}` sobre filtros ya asociados a `profile-modular-sensor-technoma` o `Profile-CajaAnde`.<br>`python auditoria_cuota_stellar/19_actualizar_log_filters_en_caliente.py --status` |
| **Auditor Top Risky Assets** | [**`20_auditoria_top_risky_assets.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/20_auditoria_top_risky_assets.py) | **Diagnóstico forense del widget Top Risky Assets**: cruza los activos (`*assets*`) contra las alertas (`*ser*`) para desentrañar la causa raíz del Risk Score (falsos positivos, rotación DHCP, LDAP, SMB, o bloqueos por firewall).<br>`python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py`<br>`python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --asset "forestdnszones"` |
| **Workflow Diario SOC Élite** | [**`21_chequeo_diario_analista_soc_elite.py`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/21_chequeo_diario_analista_soc_elite.py) | **Workflow integral de chequeo diario de 6 fases** (Cuota/Licencia, Salud de Sensores/Interflow, Triage de Casos, Matriz XDR Kill Chain, Diagnóstico de Alertas/FP y Top Risky Assets) para inicio de turno.<br>`python auditoria_cuota_stellar/21_chequeo_diario_analista_soc_elite.py`<br>`python auditoria_cuota_stellar/21_chequeo_diario_analista_soc_elite.py --hours 24` |
| **CLI Unificado Stellar** | [**`stellar_cli.py`**](file:///g:/Hermes%20+%20Antigravity/soar/stellar_cli.py) | **Herramienta permanente única** para Casos, Alertas, Tenants, Cuota, Data Lake Hunting y Filtros.<br>`.\Scripts\python.exe stellar_cli.py --case <ID>`<br>`.\Scripts\python.exe stellar_cli.py --list-cases --status "In Progress"`<br>`.\Scripts\python.exe stellar_cli.py --quota`<br>`.\Scripts\python.exe stellar_cli.py --search "<LUCENE>"` |
| **Sophos Central MDR / DFIR Inspector** | [**`sophos_mdr_cli.py`**](file:///g:/Hermes%20+%20Antigravity/soar/sophos_mdr_cli.py) | **MDR Casero de Solo Lectura para Sophos Central (CAJAANDE / Multi-tenant)**. Consulta inventario, estado de salud (good/suspicious/bad), alertas activas, deep dive forense por host/IP y flujo de eventos SIEM sin acciones intrusivas.<br>`python sophos_mdr_cli.py --summary`<br>`python sophos_mdr_cli.py --suspicious`<br>`python sophos_mdr_cli.py --host <HOSTNAME>`<br>`python sophos_mdr_cli.py --alerts`<br>`python sophos_mdr_cli.py --events` |
| **Scripts de Auditoría Cuota**| [**`auditoria_cuota_stellar/`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/) | Scripts modulares `01_...` a `21_...` para inspección profunda de índices, consumo de licencia, políticas FortiGate, log filters, risky assets y workflow diario. |

---

## 🧠 2. Memoria Institucional y Criterios de Triaje (Fuentes de la Verdad)

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Memoria Institucional SOC** | [**`SOC_GEM_v2.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/SOC_GEM_v2.md) | **[CRÍTICO - Fuente de la Verdad]** Falsos positivos validados, deuda técnica documentada (HealthMailboxes, escáneres Nessus), activos críticos y comportamientos legítimos de Technoma y clientes. |
| **Plantillas de Cierre SOC** | [**`plantillas_cierre_soc.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/plantillas_cierre_soc.md) | **[CRÍTICO]** Justificaciones humanizadas estandarizadas para cierre de casos en Stellar Cyber (Falsos Positivos, Pruebas Autorizadas, Remedición Validada). |
| **Guía Triaje 7 Etapas** | [**`guia_triaje_7_etapas_stellar.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/guia_triaje_7_etapas_stellar.md) | Procedimiento formal en 7 pasos para análisis metódico de alertas OpenXDR. |
| **Inventario de Usuarios AD** | [**`ad_users_inventory.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/ad_users_inventory.md) | Volcado completo de cuentas de usuario válidas del dominio `technoma.local` para validar ataques de fuerza bruta o suplantación. |
| **Inventario Activos CAJAANDE (Sophos)** | [**`Inventario_Activos_CajaAnde_Sophos.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/02_Base_de_Conocimiento/Inventario_Activos_CajaAnde_Sophos.md) | **[INVENTARIO OFICIAL]** Catálogo completo de los **123 endpoints** de CAJAANDE (100 PCs/Laptops y 23 Servidores) con IP, SO, estado de salud (Good/Suspicious/Bad), Tamper Protection y última conexión. |
| **Fórmulas y Funciones Sheets SOC** | [**`Formulas_Funciones_GoogleSheets_SOC.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/02_Base_de_Conocimiento/Formulas_Funciones_GoogleSheets_SOC.md) | Catálogo de fórmulas maestras y funciones con nombre (`GENERAR_TICKET_SOC`) para generar automáticamente tarjetas de tickets de escalación en Google Sheets y Excel. |
| **Diccionario Alertas Stellar** | [**`stellar_alerts.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/stellar_alerts.md) | Catálogo de tipos de alertas analíticas de Stellar Cyber, severidades, umbrales y mapeo MITRE ATT&CK. |
| **Rosetta Stone de SMB** | [**`SMB_Rosetta_Stone.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/SMB_Rosetta_Stone.md) | Guía de decodificación de comandos y códigos de retorno SMB para análisis de tráfico lateral y anomalías de archivos compartidos. |

---

## 📘 3. Stellar Cyber: Protocolos, MCP, Filtros y Alert Customizations

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Manual MCP y CLI** | [**`GUIA_STELLAR_MCP_Y_CLI_UNIFICADO.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Stellar%20Documentacion/GUIA_STELLAR_MCP_Y_CLI_UNIFICADO.md) | Instrucciones técnicas del endpoint MCP (`/mcp`), validación de parámetros (`ticket_id` string), flujo JWT y comandos del CLI unificado. |
| **Guía Maestra de Filtros** | [**`guia_stellar_cyber_log_filtering.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Stellar%20Documentacion/guia_stellar_cyber_log_filtering.md) | Sintaxis completa Lucene, campos soportados, operadores de Alert Customizations (`is`, `contains`, `starts with`, etc.), mejores prácticas y reducción de ingesta. |
| **Filtros y Alert Customizations**| [**`GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md`**](file:///g:/Hermes%20+%20Antigravity/soar/auditoria_cuota_stellar/GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md) | Resumen rápido de reglas Pre-DPI, filtros de ingesta y estándares de notas de exclusión. |
| **Curso Oficial Stellar M00 (7 Módulos)**| [**`Curso M00/`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Stellar%20Documentacion/Curso%20M00/) | **[CURSO OFICIAL / TRANSCRIPCIONES MD]** Manuales de arquitectura: M01 Plataforma, M02 Admin Tenants/Usuarios, M03 Modular Sensor Concepts & Config, M04 Modular Sensor Install, M05 Windows Sensor, M06 Linux Sensor, M07 Sophos Connector. |
| **Curso Oficial Stellar J00 (4 Módulos)**| [**`Curso J00/`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Stellar%20Documentacion/Curso%20J00/) | **[SOC ANALYST: INVESTIGATIONS & TOOLS]** J01 Open XDR Explained, J02 UI Features, J03 Investigations & Workflows (Risk Matrix, Case Investigation, Alert Handling), J04 Investigation Tools (Interflow Dictionary, Lucene Search, Regex, Query Tool). |
| **Curso Oficial Stellar F00 (3 Módulos)**| [**`Curso F00/`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Stellar%20Documentacion/Curso%20F00/) | **[FOUNDATIONS: ARCHITECTURE & UI]** F01 Overview of Stellar Cyber, F02 Open XDR Architecture Overview (Data Lake, DP, Sensors), F03 User Interface Overview (Dashboards, Navigation). |
| **Actualización Oficial Stellar 7.0**| [**`7_0_product_update_transcript.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Stellar%20Documentacion/7_0_product_update_transcript.md) | **[TRANSCRIPCIÓN OFICIAL 7.0 GA]** Autonomous SOC on-prem/cloud, Evidence Linkage (queries con trazabilidad 1-clic), asistente de IA con live analytics, MCP General Availability, nuevas detecciones M365 ASN y Pass-the-Ticket, Parser Studio GA. |
| **Novedades y Cambios API 7.0.0s**| [**`Stellar_Cyber_7.0.0s_Novedades_y_Cambios_API.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Stellar%20Documentacion/Stellar_Cyber_7.0.0s_Novedades_y_Cambios_API.md) | **[VERSIÓN 7.0.0s]** Breaking changes de API (`request_id`, RBAC sensores), nuevas acciones FortiGate (bloqueo URL/Dominio), métricas de SLA y nuevas detecciones ML. |
| **Referencia API Stellar** | [**`stellar_cyber_api_reference.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/stellar_cyber_api_reference.md) | Especificación de endpoints REST de Stellar (`/connect/api/v1/cases`, `/queries`, `/storage-usages`). |

---

## 🎯 4. Playbooks Maestros de Respuesta a Incidentes (IR)

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Master IR Playbooks (28 tipos)** | [**`SOC_Incident_Response_Playbooks_Master.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/00_Playbooks/SOC_Incident_Response_Playbooks_Master.md) | **[CATÁLOGO MAESTRO]** Procedimientos de respuesta para: Ransomware, C2, SQLi, XSS, Escaneos, Phishing, Data Leak, Defacement, Fuerza Bruta, Movimiento Lateral, Exfiltración ICMP/DNS, etc. |
| **Catálogo JSON de Playbooks** | [**`playbooks_catalog.json`**](file:///c:/Users/kevinmoraes/Documents/soc-env/00_Playbooks/playbooks_catalog.json) | Estructura indexada programáticamente para el motor SOAR del Cockpit. |
| **Playbook Sophos AutoUpdate** | [**`Playbook_Sophos_AutoUpdate.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/Playbook_Sophos_AutoUpdate.md) | Resolución de fallas del servicio de actualización local de Sophos EDR (Error `80041f00`). |
| **Playbook Sophos ServiceDown** | [**`Playbook_Sophos_ServiceNotRunning.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/Playbook_Sophos_ServiceNotRunning.md) | Reanudación y resolución de servicios detenidos de Sophos Endpoint. |

---

## 🔍 5. Procedimientos de Triaje Especializado y Threat Hunting

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Inspección de Queries y Log Filters** | [**`PROCEDIMIENTO_ESTANDAR_QUERIES_Y_FILTROS_STELLAR.md`**](file:///g:/Hermes%20+%20Antigravity/soar/ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_ESTANDAR_QUERIES_Y_FILTROS_STELLAR.md) | **[PROCEDIMIENTO ESTÁNDAR]** Auditoría de los 54+ Log Filters, cruce empírico Firewall vs NDR (`interflow_traffic`) y actualización en caliente (Hot-Reload `PUT`) en el Modular Sensor. |
| **Control Cruzado Cortex & Cierre Masivo** | [**`PROCEDIMIENTO_CONTROL_CRUZADO_Y_CIERRE_CASOS_CORTEX.md`**](file:///g:/Hermes%20+%20Antigravity/soar/ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_CONTROL_CRUZADO_Y_CIERRE_CASOS_CORTEX.md) | **[PROCEDIMIENTO ESTÁNDAR]** Control cruzado de alertas Cortex XDR con `case_id`, sincronización a Stellar Cyber y cierre masivo con dictamen formal. |
| **Auditoría de Threat Hunting Library** | [**`PROCEDIMIENTO_AUDITORIA_THREAT_HUNTING_LIBRARY.md`**](file:///g:/Hermes%20+%20Antigravity/soar/ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_AUDITORIA_THREAT_HUNTING_LIBRARY.md) | **[PROCEDIMIENTO ESTÁNDAR]** Metodología matemática 1:1 para auditar las 13 tarjetas de Threat Hunting Library, reconciliación de índices del Data Lake y análisis de origen de eventos. |
| **Procedimiento MDR Sophos (CAJAANDE)** | [**`Procedimiento_MDR_Sophos_Central_CajaAnde.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/02_Base_de_Conocimiento/Procedimiento_MDR_Sophos_Central_CajaAnde.md) | **[PROCEDIMIENTO ESTÁNDAR - SOP-SOC-MDR-001]** Metodología operativa de monitoreo, triaje forense e investigación de endpoints de solo lectura (sin acciones intrusivas) en Sophos Central para CAJAANDE vía `sophos_mdr_cli.py`. |
| **Auditoría de Hits de Alertas** | [**`PROCEDIMIENTO_AUDITORIA_HITS_ALERTAS.md`**](file:///g:/Hermes%20+%20Antigravity/soar/ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_AUDITORIA_HITS_ALERTAS.md) | Procedimiento para auditar la vista de Hits de Stellar Cyber (`/alerts?view=hits`), análisis de LOLBINs y payloads IDS. |
| **Suite Automatizada Threat Hunting 360°** | [**ARQUITECTURA_SUITE_THREAT_HUNTING_360.md**](file:///g:/Hermes%20+%20Antigravity/soar/ARQUITECTURA_SUITE_THREAT_HUNTING_360.md) | **[NUEVA SUITE 360°]** Orquestador inteligente de 1-clic: Detección y matriz de decisión automática para IPs (Privada/Pública) y Dominios (PaaS/Propio), integrando VirusTotal, AbuseIPDB, URLScan, DNSBL y correlación Stellar. |
| **Informe Forense Phishing Netlify** | [**INFORME_HUNTING_PHISHING_NETLIFY_20261020.md**](file:///g:/Hermes%20+%20Antigravity/soar/INFORME_HUNTING_PHISHING_NETLIFY_20261020.md) | **[INFORME FORENSE OFICIAL]** Dictamen técnico del incidente de phishing sobre subdominios efímeros de Netlify (unruffled-shannon-1a7413 y sage-crumble-d13d8c), equipos internos afectados (
b-sdoncell, 
b-wgonzalez) y remediación preventiva. |
| **Triaje Threat Hunting** | [**`guia_operativa_triaje_threat_hunting.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Procedimientos/guia_operativa_triaje_threat_hunting.md) | Metodología operativa para cacería proactiva de amenazas en logs de firewall y endpoints. |
| **Triaje Phishing y Bypass CDN** | [**`guia_metodologia_triaje_phishing_y_bypass_cdn.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Procedimientos/guia_metodologia_triaje_phishing_y_bypass_cdn.md) | Análisis de correos maliciosos, extracción de encabezados y descubrimiento de servidores de origen detrás de Cloudflare/CDN. |
| **Operación VASCOL RDS/Zimbra** | [**`Manual_Operativo_Soporte_VASCOL_RDS_Zimbra.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Procedimientos/Manual_Operativo_Soporte_VASCOL_RDS_Zimbra.md) | Manual operativo de soporte técnico e incidentes para entornos Vascol RDS y correo Zimbra. |
| **Investigación HealthMailbox** | [**`Investigacion Healthmailbox .md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/Investigacion%20Healthmailbox%20.md) | Análisis forense de ruidos generados por sondas internas de Exchange (`HealthMailbox*`) y directivas de exclusión. |

---

## 🏗️ 6. Arquitectura, Sensores y Despliegue de Red

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Deep Dive SOC Gateway** | [**`deep_dive_soc_gateway.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/deep_dive_soc_gateway.md) | Arquitectura técnica de la pasarela SOC, zonas de red, sensores de red e interfaces. |
| **Conexión ZeroTier SOC** | [**`guia_conexion_nodos_remotos_zerotier.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/guia_conexion_nodos_remotos_zerotier.md) | Configuración de interconexión cifrada ZeroTier para nodos y sensores remotos. |
| **Mantenimiento ZeroTier** | [**`cheatsheet_mantenimiento_soc_zerotier.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/cheatsheet_mantenimiento_soc_zerotier.md) | Comandos de diagnóstico, reinicio de servicios y verificación de rutas ZeroTier. |
| **Sensor NDR Valores** | [**`guia_despliegue_sensor_ndr_valores.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/guia_despliegue_sensor_ndr_valores.md) | Guía técnica paso a paso para el despliegue del sensor NDR en el cliente Valores Casa de Bolsa. |
| **Elastic Agent Valores Sophos** | [**`guia_despliegue_elastic_agent_valores_sophos.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/guia_despliegue_elastic_agent_valores_sophos.md) | Despliegue de Elastic Agent para correlación y telemetría de Sophos Central. |
| **Despliegues Security Onion** | [**`Guia_Despliegue_SO3_*.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/03_Arquitectura_y_Despliegue/) | Manuales de despliegue de Security Onion 3 (Standalone, Distribuido y Endpoints). |
| **Arquitectura SO3 & Filtros Salt** | [**`01_Guia_Traduccion_Filtros_Stellar_a_Security_Onion_SO3.md`**](file:///c:/Users/kevinmoraes/Documents/SOC_SOAR/soar/Analista%20SOC/Security_Onion/01_Guia_Traduccion_Filtros_Stellar_a_Security_Onion_SO3.md) | Topología Grid de 4 nodos, compilación BPF, supresiones Suricata `threshold.conf`, Logstash drops, catálogo oficial y SOP paso a paso estandarizado. |
| **Cheatsheet Comandos SO3** | [**`02_Cheatsheet_Comandos_Operativos_SO3.md`**](file:///c:/Users/kevinmoraes/Documents/SOC_SOAR/soar/Analista%20SOC/Security_Onion/02_Cheatsheet_Comandos_Operativos_SO3.md) | Cheatsheet de administración, rescate de memoria/disco, purga de índices basura, auditoría SaltStack y Playbook Rápido de filtros Logstash en 4 pasos. |
| **Caso de Estudio Rescate SO3** | [**`03_Caso_Estudio_Rescate_Infraestructura_Security_Onion_SO3.md`**](file:///c:/Users/kevinmoraes/Documents/SOC_SOAR/soar/Analista%20SOC/Security_Onion/03_Caso_Estudio_Rescate_Infraestructura_Security_Onion_SO3.md) | Memoria técnica completa del rescate del nodo Standalone: neutralización de los 4 monstruos de ruido (>17M eventos), desentrañamiento de SaltStack/Logstash y métricas comparativas Antes vs. Después. |

---

## 📊 7. Operación Diaria, Turnos y Bitácoras

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Bitácora Personal de Casos** | [**`Bitacora_Personal_Casos_SOC.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Bitacora_Personal_Casos_SOC.md) | Registro histórico detallado de tickets y casos trabajados por Kevin Moraes con análisis y resoluciones. |
| **Bitácora Operativa General** | [**`bitacora.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/01_Operacion_Diaria_SOC/bitacora.md) | Bitácora de guardia de turno del SOC. |
| **Reporte Diario CISO** | [**`Reporte_Diario_CISO.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/01_Operacion_Diaria_SOC/Reporte_Diario_CISO.md) | Formato ejecutivo de reporte diario de estado e incidentes para la dirección de ciberseguridad. |
| **IPs Reportadas por Abuso** | [**`Registro_IPs_Reportadas_Abuso.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Registro_IPs_Reportadas_Abuso.md) | Histórico de direcciones IP atacantes reportadas en plataformas como AbuseIPDB. |

---

## 📑 8. Informes Ejecutivos y Reportes Forenses

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Auditoría de Cegueras SOC** | [**`Auditoria_Seguridad_Log_Filters_Cegueras_SOC.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Reportes/Auditoria_Seguridad_Log_Filters_Cegueras_SOC.md) | Evaluación de riesgo sobre filtros de logs agresivos que puedan ocultar ataques reales. |
| **Plan Maestro Reducción Cuota**| [**`Informe_Plan_Maestro_Reduccion_Ingesta_y_Queries.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Reportes/Informe_Plan_Maestro_Reduccion_Ingesta_y_Queries.md) | Estrategia de optimización de ingesta en gigabytes y supresión de queries redundantes en Stellar. |
| **Causa Raíz DNS Grafana** | [**`Informe_Ejecutivo_Causa_Raiz_Ingesta_DNS_Grafana.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Reportes/Informe_Ejecutivo_Causa_Raiz_Ingesta_DNS_Grafana.md) | Dictamen técnico sobre picos masivos de ingesta causados por resoluciones de Grafana/Zabbix. |
| **Informe Forense ProtonDrive** | [**`Informe_Seguridad_Uso_No_Autorizado_ProtonDrive_Fabio_Mora.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Reportes/Informe_Seguridad_Uso_No_Autorizado_ProtonDrive_Fabio_Mora.md) | Investigación forense de uso no autorizado de nube personal y exfiltración potencial. |
| **Matriz Stellar vs Cortex** | [**`Matriz_Correlacion_Stellar_vs_Cortex.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Reportes/Matriz_Correlacion_Stellar_vs_Cortex.md) | Cuadro comparativo de visibilidad y correlación entre alertas de Palo Alto Cortex XDR y Stellar Cyber. |

---

## 🤖 9. Reglas y Skills de IA del Entorno

| Skill / Regla | Ubicación | Función |
| :--- | :--- | :--- |
| **Reglas Globales Agent** | [**`.agents/AGENTS.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/.agents/AGENTS.md) | Reglas de oro: inmutabilidad, no uso de `python -c`, cobertura de tests y priorización de skills. |
| **Skill API Stellar** | [**`.agent/skills/stellar-api-interaction/SKILL.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/.agent/skills/stellar-api-interaction/SKILL.md) | Fuerza el uso obligatorio de `stellar_cli.py` y prohíbe one-liners en consola. |
| **Skill Triaje Forense** | [**`.agent/skills/analyze_stellar_alert/SKILL.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/.agent/skills/analyze_stellar_alert/SKILL.md) | Aplica triaje forense estructurado en 4 fases para volcados de alertas Stellar. |
| **Skill Bitácora 18 Cols** | [**`.agent/skills/soc-bitacora/SKILL.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/.agent/skills/soc-bitacora/SKILL.md) | Generador de registros TSV de 1-clic para la planilla oficial de guardia. |
| **Skill Formulario Incidentes**| [**`.agent/skills/soc-incidencias/SKILL.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/.agent/skills/soc-incidencias/SKILL.md) | Generador oficial de las 40 columnas del formulario FL-THN-POS-01 Rev. 03. |

---

## 🧅 8. Arquitectura Security Onion (SO3) & SaltStack

| Documento | Ubicación | Contenido y Alcance |
| :--- | :--- | :--- |
| **Índice Maestro SO3 & SaltStack** | [**`INDICE_MAESTRO_SO3_Y_SALTSTACK.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Security_Onion/INDICE_MAESTRO_SO3_Y_SALTSTACK.md) | **Arquitectura completa de contenedores Docker, capas NDR/EDR/Storage y orquestación con SaltStack.** |
| **Ficha Técnica: `so-dockerregistry`** | [**`01_Contenedor_so-dockerregistry.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Security_Onion/contenedores/01_Contenedor_so-dockerregistry.md) | **Disección profunda del registro privado OCI v2**: almacenamiento `/nsm/docker/registry`, Salt states, comandos curl de API y troubleshooting de disco. |
| **Traducción Filtros Stellar a SO3** | [**`01_Guia_Traduccion_Filtros_Stellar_a_Security_Onion_SO3.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Security_Onion/01_Guia_Traduccion_Filtros_Stellar_a_Security_Onion_SO3.md) | Mapeo de reglas y filtros de Stellar Cyber hacia BPF, Zeek scripts y Suricata thresholds en SO3. |
| **Cheatsheet Comandos SO3** | [**`02_Cheatsheet_Comandos_Operativos_SO3.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Security_Onion/02_Cheatsheet_Comandos_Operativos_SO3.md) | Comandos esenciales `so-...`, docker, salt-call y gestión de servicios. |
| **Caso Estudio Rescate SO3** | [**`03_Caso_Estudio_Rescate_Infraestructura_Security_Onion_SO3.md`**](file:///g:/Hermes%20+%20Antigravity/soar/Analista%20SOC/Security_Onion/03_Caso_Estudio_Rescate_Infraestructura_Security_Onion_SO3.md) | Procedimiento de rescate ante fallas críticas de clúster y discos llenos. |
