# 🗺️ ÍNDICE MAESTRO DE DOCUMENTACIÓN Y ARTEFACTOS SOC (KNOWLEDGE MAP)

> **PROPÓSITO PARA EL ANALISTA Y AGENTES IA:**  
> Este es el mapa central de navegación del entorno SOC. **Antes de realizar búsquedas a ciegas (`grep`, scripts ad-hoc o conjeturar rutas)**, consulta este índice para identificar exactamente qué documento o herramienta resuelve la necesidad actual.

---

## ⚡ 1. Herramientas de Ejecución Rápida y Automatización

| Herramienta | Ubicación | Propósito y Comandos Clave |
| :--- | :--- | :--- |
| **CLI Unificado Stellar** | [**`stellar_cli.py`**](file:///c:/Users/kevinmoraes/Documents/soc-env/stellar_cli.py) | **Herramienta permanente única** para Casos, Alertas, Tenants, Cuota, Data Lake Hunting y Filtros.<br>`.\Scripts\python.exe stellar_cli.py --case <ID>`<br>`.\Scripts\python.exe stellar_cli.py --list-cases --status "In Progress"`<br>`.\Scripts\python.exe stellar_cli.py --quota`<br>`.\Scripts\python.exe stellar_cli.py --search "<LUCENE>"` |
| **Cockpit GUI del SOC** | [**`command_center.py`**](file:///c:/Users/kevinmoraes/Documents/soc-env/command_center.py) | Interfaz visual en PySide6 para monitoreo en vivo, visualización de alertas, mitigaciones SOAR y generación de reportes. |
| **Scripts de Auditoría Cuota**| [**`auditoria_cuota_stellar/`**](file:///c:/Users/kevinmoraes/Documents/soc-env/auditoria_cuota_stellar/) | Scripts modulares `01_...` a `10_...` para inspección profunda de índices, consumo de licencia, políticas FortiGate y auditoría de log filters. |

---

## 🧠 2. Memoria Institucional y Criterios de Triaje (Fuentes de la Verdad)

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Memoria Institucional SOC** | [**`SOC_GEM_v2.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/SOC_GEM_v2.md) | **[CRÍTICO - Fuente de la Verdad]** Falsos positivos validados, deuda técnica documentada (HealthMailboxes, escáneres Nessus), activos críticos y comportamientos legítimos de Technoma y clientes. |
| **Plantillas de Cierre SOC** | [**`plantillas_cierre_soc.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/plantillas_cierre_soc.md) | **[CRÍTICO]** Justificaciones humanizadas estandarizadas para cierre de casos en Stellar Cyber (Falsos Positivos, Pruebas Autorizadas, Remedición Validada). |
| **Guía Triaje 7 Etapas** | [**`guia_triaje_7_etapas_stellar.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/guia_triaje_7_etapas_stellar.md) | Procedimiento formal en 7 pasos para análisis metódico de alertas OpenXDR. |
| **Inventario de Usuarios AD** | [**`ad_users_inventory.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/ad_users_inventory.md) | Volcado completo de cuentas de usuario válidas del dominio `technoma.local` para validar ataques de fuerza bruta o suplantación. |
| **Diccionario Alertas Stellar** | [**`stellar_alerts.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/stellar_alerts.md) | Catálogo de tipos de alertas analíticas de Stellar Cyber, severidades, umbrales y mapeo MITRE ATT&CK. |
| **Rosetta Stone de SMB** | [**`SMB_Rosetta_Stone.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/02_Base_de_Conocimiento/SMB_Rosetta_Stone.md) | Guía de decodificación de comandos y códigos de retorno SMB para análisis de tráfico lateral y anomalías de archivos compartidos. |

---

## 📘 3. Stellar Cyber: Protocolos, MCP, Filtros y Alert Customizations

| Documento | Ubicación | Cuándo Consultar |
| :--- | :--- | :--- |
| **Manual MCP y CLI** | [**`GUIA_STELLAR_MCP_Y_CLI_UNIFICADO.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Stellar%20Documentacion/GUIA_STELLAR_MCP_Y_CLI_UNIFICADO.md) | Instrucciones técnicas del endpoint MCP (`/mcp`), validación de parámetros (`ticket_id` string), flujo JWT y comandos del CLI unificado. |
| **Guía Maestra de Filtros** | [**`guia_stellar_cyber_log_filtering.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Stellar%20Documentacion/guia_stellar_cyber_log_filtering.md) | Sintaxis completa Lucene, campos soportados, operadores de Alert Customizations (`is`, `contains`, `starts with`, etc.), mejores prácticas y reducción de ingesta. |
| **Filtros y Alert Customizations**| [**`GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/auditoria_cuota_stellar/GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md) | Resumen rápido de reglas Pre-DPI, filtros de ingesta y estándares de notas de exclusión. |
| **Novedades y Cambios API 7.0.0s**| [**`Stellar_Cyber_7.0.0s_Novedades_y_Cambios_API.md`**](file:///c:/Users/kevinmoraes/Documents/soc-env/Analista%20SOC/Stellar%20Documentacion/Stellar_Cyber_7.0.0s_Novedades_y_Cambios_API.md) | **[VERSIÓN 7.0.0s]** Breaking changes de API (`request_id`, RBAC sensores), nuevas acciones FortiGate (bloqueo URL/Dominio), métricas de SLA y nuevas detecciones ML. |
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
