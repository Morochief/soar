# 🧠 CATÁLOGO UNIFICADO DE MEMORIA Y MARKDOWNS — TECHNOMA SOC

- **Total de documentos indexados en memoria activa:** `2086` archivos (divididos en `14138` bloques BM25 en `.rag_index_cache.pkl`).
- **Tiempo de consulta en RAM/Disco:** `< 15 ms` (0 tokens consumidos al buscar).

## Resumen por Capa de Conocimiento

| Capa / Categoría | Archivos | Peso de Prioridad | Propósito en el SOAR |
| :--- | :---: | :---: | :--- |
| **`MEMORIA_SOC`** | 42 | `1.65x` | Fuente de la verdad (`SOC_GEM_v2.md`, `plantillas_cierre_soc.md`, `stellar_alerts.md`, `SMB_Rosetta_Stone.md`, inventarios AD/Red) |
| **`CASO_HISTORICO`** | 426 | `1.5x` | Los +35 casos reales ya investigados en `Analista SOC/Casos/` + `Bitacora_Personal_Casos_SOC.md` |
| **`PLAYBOOK`** | 19 | `1.45x` | Catálogo maestro de 28 playbooks IR (`00_Playbooks/`) y playbooks específicos de remediación |
| **`PROCEDIMIENTO_ARQ`** | 664 | `1.3x` | Guías de filtros Lucene/Pre-DPI, Security Onion 3, sensores NDR, ZeroTier, informes y procedimientos |
| **`SKILL_SOC`** | 124 | `1.25x` | Las 60 Skills operativas y técnicas del SOC (`SKILLS_SOC/` y `.agent/skills/`) |
| **`ACADEMIA_SOC`** | 250 | `0.9x` | Apuntes y laboratorios de Google SecOps y Google Cybersecurity Certification |
| **`DOC_STELLAR`** | 561 | `1.0x` | Manuales oficiales de reglas y conectores de Stellar Cyber (`Markdown_Output/`) |

---

## 📂 Capa `MEMORIA_SOC` (42 documentos)

| Archivo | Tamaño | Función / Título Detectado |
| :--- | :---: | :--- |
| `CHANGELOG.md` | 7.0 KB | Registro de Cambios y Control de Versiones (CHANGELOG) |
| `COMO_TRABAJAR_CON_TU_SOAR.md` | 11.2 KB | 🛡️ MANUAL OPERATIVO: CÓMO TRABAJA TU SOAR + CEREBRO DE MEMORIA + ANTIGRAVITY / HERMES |
| `ARQUITECTURA_SUITE_THREAT_HUNTING_360.md` | 7.5 KB | 🚀 ARQUITECTURA DE SUITE DE INVESTIGACIÓN AUTOMATIZADA: THREAT HUNTING 360° |
| `INFORME_HUNTING_PHISHING_NETLIFY_20261020.md` | 5.8 KB | 🛡️ INFORME FORENSE SOC & THREAT HUNTING: CAMPAÑA PHISHING NETLIFY SUBDOMAINS |
| `INDICE_MAESTRO_DOCUMENTACION_SOC.md` | 15.2 KB | 🗺️ ÍNDICE MAESTRO DE DOCUMENTACIÓN Y ARTEFACTOS SOC (KNOWLEDGE MAP) |
| `README.md` | 3.2 KB | 🛡️ Technoma SOC — OpenXDR Master Cockpit & Forensic Suite |
| `Analista SOC/Imagen de Check Point_ IA.md` | 101.3 KB | Imagen de Check Point: IA |
| `Analista SOC/Network Fundamentals.md` | 23.3 KB | Curso: Network Fundamentals |
| `Analista SOC/Registro_IPs_Reportadas_Abuso.md` | 4.5 KB | 🛡️ Registro Oficial de IPs Reportadas por Abuso y Ataques Perimetrales |
| `Analista SOC/Respaldo_Reglas_PreDPI_Stellar.md` | 2.9 KB | Respaldo de Reglas Pre-DPI - Sensor Profile: profile-modular-sensor-technoma |
| `Analista SOC/borrador.md` | 25.6 KB | **INDEL** |
| `Analista SOC/computers_and_servers.md` | 15.4 KB | / Health / Name / Type / Operating System / Last active / IP address / Tamper protection / Last user / Tags /  |
| `Analista SOC/indice_soc.md` | 3.1 KB | 🗺️ Índice Curado de Documentación SOC |
| `Analista SOC/informe-indel.docx.md` | 11.8 KB | **INDEL** |
| `Analista SOC/resumen_ejecutivo_checkpoint.md` | 5.6 KB | Resumen Ejecutivo: Capacitación Check Point – Estrategia y Portafolio |
| `Analista SOC/walkthrough.md` | 1.5 KB | Reorganización del Workspace SOC (Walkthrough) |
| `Analista SOC/02_Base_de_Conocimiento/Informe-preliminar-GR.md` | 16.9 KB | www.technoma.com.py / #SomosTechnoma |
| `Analista SOC/02_Base_de_Conocimiento/Inventario_equipos_de_red_THN.md` | 1.6 KB | 🌐 Inventario de Equipos de Red - Technoma (THN) |
| `Analista SOC/02_Base_de_Conocimiento/Investigacion Healthmailbox .md` | 590.8 KB | 0\. Inicialización Obligatoria en PowerShell (Carga del Módulo de Exchange) |
| `Analista SOC/02_Base_de_Conocimiento/Resumen_Reunion_CheckPoint.md` | 5.5 KB | Resumen Ejecutivo: Reunión Check Point - AI Transformation |
| `Analista SOC/02_Base_de_Conocimiento/SAMR.md` | 5.9 KB | Excelente pregunta de ingeniería. Aquí está el mapa completo de qué puede estar pasando en la PC para que eso  |
| `Analista SOC/02_Base_de_Conocimiento/SMB_Rosetta_Stone.md` | 7.2 KB | 🪨 Piedra de Rosetta: Diccionario Maestro de Comandos SMB (v1, v2 y v3) |
| `Analista SOC/02_Base_de_Conocimiento/SOC_GEM_v2.md` | 67.5 KB | ðŸ“‹ INSTRUCCIONES DE EJECUCIÃ“N OBLIGATORIA: ANALISTA SOC N3 Y MENTOR DFIR |
| `Analista SOC/02_Base_de_Conocimiento/Sophos_Logs_Reference.md` | 4.9 KB | Referencia de Logs de Sophos Endpoint y Server |
| `Analista SOC/02_Base_de_Conocimiento/ad_users_inventory.md` | 7.1 KB | Inventario de Cuentas de Usuario - Active Directory (technoma.local) |
| `Analista SOC/02_Base_de_Conocimiento/cve_criticos.md` | 108.1 KB | Reporte de CVEs Críticos Recientes |
| `Analista SOC/02_Base_de_Conocimiento/cve_reporte_completo.md` | 714.8 KB | Reporte de CVEs (Críticos y Altos) |
| `Analista SOC/02_Base_de_Conocimiento/gemini_prompts.md` | 12.0 KB | 📋 INSTRUCCIONES DE EJECUCIÓN OBLIGATORIA (IDIOMA EXCLUSIVO: ESPAÑOL) |
| `Analista SOC/02_Base_de_Conocimiento/guia_integracion_feeds_tweetfeed_soar.md` | 5.8 KB | Guía de Integración: Feeds de IOCs en Vivo (TweetFeed) en el SOAR |
| `Analista SOC/02_Base_de_Conocimiento/guia_triaje_7_etapas_stellar.md` | 12.1 KB | Guia Operativa de Triaje de Alertas en 7 Etapas (SOC Analyst Standard) |
| `Analista SOC/02_Base_de_Conocimiento/otx_amenazas_recientes.md` | 23.2 KB | 👽 Inteligencia de Amenazas Activas (AlienVault OTX) |
| `Analista SOC/02_Base_de_Conocimiento/plantillas_cierre_soc.md` | 19.2 KB | Plantillas de Cierre SOC (Stellar Cyber) |
| `Analista SOC/02_Base_de_Conocimiento/prompt_stellar_python.md` | 14.8 KB | SYSTEM PROMPT: GENERADOR DE RESUMEN EJECUTIVO (STELLAR CYBER) |
| `Analista SOC/02_Base_de_Conocimiento/securityonion-docs-ES.md` | 689.7 KB | Cebolla de seguridad |
| `Analista SOC/02_Base_de_Conocimiento/securityonion-docs.md` | 591.9 KB | Security Onion |
| `Analista SOC/02_Base_de_Conocimiento/stellar_alerts.md` | 44.3 KB | Diccionario Global de Alertas de Stellar Cyber XDR |
| `Analista SOC/02_Base_de_Conocimiento/stellar_cyber_api_reference.md` | 11.4 KB | 🛡️ Stellar Cyber Open XDR — API Reference v6.5.0 |
| `Analista SOC/02_Base_de_Conocimiento/Noticias/wp2shell_payload_analysis.md` | 1.4 KB | WordPress "wp2shell" exploit payload analyzed: AI developed this attack |
| `Analista SOC/02_Base_de_Conocimiento/Noticias/wp2shell_vulnerability.md` | 15.8 KB | Vulnerabilidad crítica RCE wp2shell: cobertura, PoC y explotación activa |
| `Analista SOC/soc_gem_graph/SOC_GEM_v2.md` | 48.8 KB | 📋 INSTRUCCIONES DE EJECUCIÓN OBLIGATORIA: ANALISTA SOC N3 Y MENTOR DFIR |
| `ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_ESTANDAR_CONSULTA_CASOS_MCP.md` | 3.7 KB | 📖 LECCIÓN APRENDIDA Y PROCEDIMIENTO ESTÁNDAR: CONSULTA DE CASOS VÍA MCP STELLAR CYBER |
| `ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_ESTANDAR_QUERIES_Y_FILTROS_STELLAR.md` | 5.6 KB | 🔍 PROCEDIMIENTO ESTÁNDAR DE INSPECCIÓN DE QUERIES, LOG FILTERS Y ATH (STELLAR CYBER) |
| `ARQUITECTURA_SOC_DOCUMENTACION/PROCEDIMIENTO_THREAT_HUNTING_DATA_LAKE.md` | 2.7 KB | 🎯 PROCEDIMIENTO ESTÁNDAR: THREAT HUNTING DIRECTO EN DATA LAKE DE STELLAR CYBER |
| `Caso cortex/Informe_Seguridad_Uso_No_Autorizado_ProtonDrive_Fabio_Mora.md` | 6.0 KB | 🔒 INFORME TÉCNICO DE SEGURIDAD DE LA INFORMACIÓN |

---

## 📂 Capa `CASO_HISTORICO` (426 documentos)

| Archivo | Tamaño | Función / Título Detectado |
| :--- | :---: | :--- |
| `Analista SOC/Bitacora_Personal_Casos_SOC.md` | 132.3 KB | 🛡️ Bitácora Personal de Casos e Investigaciones — Analista SOC |
| `Analista SOC/01_Operacion_Diaria_SOC/bitacora.md` | 18.2 KB | Walkthrough de ContenciÃ³n TÃ©cnica y OptimizaciÃ³n del SOC Command Center |
| `Analista SOC/Casos/12661_External_Firewall_Denial_Anomaly_and_7_others.md` | 58.3 KB | ========================================================================= |
| `Analista SOC/Casos/12893_Internal_SMB_Write_Anomaly_and_4_others.md` | 69.7 KB | ========================================================================= |
| `Analista SOC/Casos/12896.md` | 16.2 KB | ========================================================================= |
| `Analista SOC/Casos/13070_Internal_Credential_Stuffing_and_93_others.md` | 52.7 KB | ========================================================================= |
| `Analista SOC/Casos/13071_Exploit_Attempt_(Low_Severity)_and_1_other.md` | 29.4 KB | ========================================================================= |
| `Analista SOC/Casos/13840_External_Firewall_Denial_Anomaly_and_2_others.md` | 35.5 KB | ========================================================================= |
| `Analista SOC/Casos/13841_External_Firewall_Denial_Anomaly_and_1_other.md` | 23.5 KB | ========================================================================= |
| `Analista SOC/Casos/3402_Sophos_Event_Impair_Defenses_and_1_other.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3403_Sophos_Event_Impair_Defenses_and_1_other.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3404_Sophos_Event_Impair_Defenses_and_1_other.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3427_Sophos_Event_User_Execution_and_3_others.md` | 28.7 KB | ========================================================================= |
| `Analista SOC/Casos/3644_Sophos_Event_User_Execution_and_1_other.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/SecurityOnion_Memoria_Institucional.md` | 17.8 KB | Security Onion 3: Memoria Institucional y Guía Operativa |
| `Analista SOC/Casos/global-verdict-report.md` | 8.1 KB | WildFire Analysis Report |
| `Analista SOC/Casos/wildfire-appliance-es-es.md` | 395.0 KB | Administración de dispositivos |
| `Analista SOC/Casos/11792_Uncommon_Process_Anomaly_and_12_others/alerta_original.md` | 101.9 KB | ========================================================================= |
| `Analista SOC/Casos/11805_Private_to_Private_Exploit_Anomaly_and_4_others/alerta_original.md` | 87.4 KB | ========================================================================= |
| `Analista SOC/Casos/11809_Internal_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 20.7 KB | ========================================================================= |
| `Analista SOC/Casos/11811_Internal_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 21.6 KB | ========================================================================= |
| `Analista SOC/Casos/11812_Exploited_C&C_Connection_and_3_others/alerta_original.md` | 128.2 KB | ========================================================================= |
| `Analista SOC/Casos/11813_Palo_Alto_Networks_Cortex_XDR_(XDR_Analytics/alerta_original.md` | 47.4 KB | ========================================================================= |
| `Analista SOC/Casos/11816_Internal_SMB_Write_Anomaly_and_1_other/alerta_original.md` | 26.2 KB | ========================================================================= |
| `Analista SOC/Casos/11818_Recently_Registered_Domains_and_1_other/alerta_original.md` | 23.2 KB | ========================================================================= |
| `Analista SOC/Casos/11819_Private_to_Private_Exploit_Anomaly_and_24_ot/alerta_original.md` | 224.8 KB | ========================================================================= |
| `Analista SOC/Casos/11822_Recently_Registered_Domains_and_2_others/alerta_original.md` | 33.4 KB | ========================================================================= |
| `Analista SOC/Casos/11829_Exploited_C&C_Connection_and_1_other/alerta_original.md` | 56.9 KB | ========================================================================= |
| `Analista SOC/Casos/11886_Application_Usage_Anomaly_and_5_others/alerta_original.md` | 45.1 KB | ========================================================================= |
| `Analista SOC/Casos/11887_Internal_Firewall_Denial_Anomaly_and_38_others/alerta_original.md` | 51.4 KB | ========================================================================= |
| `Analista SOC/Casos/11888_Internal_Credential_Stuffing_and_99_others/alerta_original.md` | 54.3 KB | ========================================================================= |
| `Analista SOC/Casos/11893_Internal_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 31.0 KB | ========================================================================= |
| `Analista SOC/Casos/11898_Uncommon_Top-Level_Domain_Anomaly_and_1_other/alerta_original.md` | 17.5 KB | ========================================================================= |
| `Analista SOC/Casos/11904_Exploited_C&C_Connection_and_9_others/alerta_original.md` | 98.1 KB | ========================================================================= |
| `Analista SOC/Casos/11907_Palo_Alto_Networks_Cortex_XDR_(XDR_Analytics/alerta_original.md` | 75.1 KB | ========================================================================= |
| `Analista SOC/Casos/11910_Command_Anomaly_and_2_others/alerta_original.md` | 24.6 KB | ========================================================================= |
| `Analista SOC/Casos/11914_Internal_SMB_Write_Anomaly_and_4_others/alerta_original.md` | 72.0 KB | ========================================================================= |
| `Analista SOC/Casos/11920_Exploited_C&C_Connection_and_3_others/alerta_original.md` | 143.9 KB | ========================================================================= |
| `Analista SOC/Casos/11961_Application_Usage_Anomaly_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/11962_Internal_Credential_Stuffing_and_11_others/alerta_original.md` | 50.7 KB | ========================================================================= |
| `Analista SOC/Casos/11964_Sensitive_Windows_Network_Share_File_or_Fold/alerta_original.md` | 40.6 KB | ========================================================================= |
| `Analista SOC/Casos/11966_Private_to_Private_Exploit_Anomaly_and_1_other/alerta_original.md` | 22.1 KB | ========================================================================= |
| `Analista SOC/Casos/11976_Private_to_Private_Exploit_Anomaly_and_1_other/alerta_original.md` | 22.9 KB | ========================================================================= |
| `Analista SOC/Casos/11980_Exploited_C&C_Connection_and_6_others/alerta_original.md` | 101.7 KB | ========================================================================= |
| `Analista SOC/Casos/11984_Exploit_Attempt_(Low_Severity)_and_1_other/alerta_original.md` | 33.4 KB | ========================================================================= |
| `Analista SOC/Casos/11987_Scanner_Reputation_Anomaly_and_1_other/alerta_original.md` | 17.6 KB | ========================================================================= |
| `Analista SOC/Casos/12028_Private_to_Public_Exploit_Anomaly_and_3_others/alerta_original.md` | 88.6 KB | ========================================================================= |
| `Analista SOC/Casos/12035_Application_Usage_Anomaly_and_12_others/alerta_original.md` | 98.3 KB | ========================================================================= |
| `Analista SOC/Casos/12037_Exploited_C&C_Connection_and_1_other/alerta_original.md` | 53.2 KB | ========================================================================= |
| `Analista SOC/Casos/12040_Uncommon_Process_Anomaly_and_3_others/alerta_original.md` | 32.4 KB | ========================================================================= |
| `Analista SOC/Casos/12041_Palo_Alto_Networks_Cortex_XDR_(XDR_Analytics/alerta_original.md` | 50.0 KB | ========================================================================= |
| `Analista SOC/Casos/12042_Internal_SMB_Write_Anomaly_and_1_other/alerta_original.md` | 26.6 KB | ========================================================================= |
| `Analista SOC/Casos/12043_Login_Time_Anomaly_and_1_other/alerta_original.md` | 17.5 KB | ========================================================================= |
| `Analista SOC/Casos/12044_Application_Usage_Anomaly_and_1_other/alerta_original.md` | 16.0 KB | ========================================================================= |
| `Analista SOC/Casos/12051_Palo_Alto_Networks_Cortex_XDR_(XDR_Analytics/alerta_original.md` | 68.7 KB | ========================================================================= |
| `Analista SOC/Casos/12167_Application_Usage_Anomaly_and_1_other/alerta_original.md` | 20.8 KB | ========================================================================= |
| `Analista SOC/Casos/12171_Uncommon_Process_Anomaly_and_24_others/alerta_original.md` | 117.8 KB | ========================================================================= |
| `Analista SOC/Casos/12172_Internal_SMB_Read_Anomaly_and_1_other/alerta_original.md` | 26.5 KB | ========================================================================= |
| `Analista SOC/Casos/12175_Exploit_Attempt_(Low_Severity)_and_1_other/alerta_original.md` | 27.0 KB | ========================================================================= |
| `Analista SOC/Casos/12177_Exploited_C&C_Connection_and_11_others/alerta_original.md` | 184.3 KB | ========================================================================= |
| `Analista SOC/Casos/12181_External_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 34.0 KB | ========================================================================= |
| `Analista SOC/Casos/12183_Uncommon_Top-Level_Domain_Anomaly_and_1_other/alerta_original_12183.md` | 24.4 KB | ========================================================================= |
| `Analista SOC/Casos/12183_Uncommon_Top-Level_Domain_Anomaly_and_1_other/analisis_12183.md` | 12.8 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12184_Internal_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 28.2 KB | ========================================================================= |
| `Analista SOC/Casos/12184_Internal_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 16.5 KB | Reporte SOC - Caso 12184: Internal Firewall Denial Anomaly (nb-mazcona) |
| `Analista SOC/Casos/12187_External_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 34.2 KB | ========================================================================= |
| `Analista SOC/Casos/12187_External_Firewall_Denial_Anomaly_and_2_others/analisis_12187.md` | 8.1 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12188_Internal_SMB_Write_Anomaly_and_5_others/alerta_original.md` | 79.3 KB | ========================================================================= |
| `Analista SOC/Casos/12188_Internal_SMB_Write_Anomaly_and_5_others/analisis_soc.md` | 4.5 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12191_Exploit_Attempt_(Low_Severity)_and_1_other/alerta_original.md` | 28.0 KB | ========================================================================= |
| `Analista SOC/Casos/12191_Exploit_Attempt_(Low_Severity)_and_1_other/analisis_soc.md` | 4.0 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12198_Internal_SMB_Read_Anomaly_and_2_others/alerta_original.md` | 44.3 KB | ========================================================================= |
| `Analista SOC/Casos/12198_Internal_SMB_Read_Anomaly_and_2_others/analisis_soc.md` | 15.2 KB | Reporte del SOC: Análisis de Alertas - Caso 12198 |
| `Analista SOC/Casos/12203_Exploit_Attempt_(Low_Severity)_and_1_other/alerta_original.md` | 28.5 KB | ========================================================================= |
| `Analista SOC/Casos/12203_Exploit_Attempt_(Low_Severity)_and_1_other/analisis_soc.md` | 10.9 KB | Reporte del SOC: Análisis de Alertas - Caso 12203 |
| `Analista SOC/Casos/12204_Exploited_C&C_Connection_and_1_other/alerta_original.md` | 96.3 KB | ========================================================================= |
| `Analista SOC/Casos/12204_Exploited_C&C_Connection_and_1_other/analisis_soc.md` | 12.3 KB | Reporte del SOC: Análisis de Alertas - Caso 12204 |
| `Analista SOC/Casos/12241_Internal_SMB_Write_Anomaly_and_1_other/alerta_original.md` | 25.7 KB | ========================================================================= |
| `Analista SOC/Casos/12241_Internal_SMB_Write_Anomaly_and_1_other/analisis_soc.md` | 9.8 KB | Reporte del SOC: Análisis de Alertas - Caso 12241 |
| `Analista SOC/Casos/12243_Public_to_Private_Exploit_Anomaly/alerta_original.md` | 13.0 KB | ========================================================================= |
| `Analista SOC/Casos/12243_Public_to_Private_Exploit_Anomaly/analisis_soc.md` | 7.9 KB | Reporte del SOC: Análisis de Alertas - Caso 12243 |
| `Analista SOC/Casos/12244_Internal_User_Login_Failure_Anomaly_and_1_other/alerta_original.md` | 20.5 KB | ========================================================================= |
| `Analista SOC/Casos/12244_Internal_User_Login_Failure_Anomaly_and_1_other/analisis_soc.md` | 8.9 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12245_Internal_Credential_Stuffing_and_48_others/alerta_original.md` | 50.4 KB | ========================================================================= |
| `Analista SOC/Casos/12245_Internal_Credential_Stuffing_and_48_others/analisis_soc.md` | 6.2 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12249_Private_to_Private_Exploit_Anomaly_and_1_other/alerta_original.md` | 21.2 KB | ========================================================================= |
| `Analista SOC/Casos/12249_Private_to_Private_Exploit_Anomaly_and_1_other/analisis_soc.md` | 7.9 KB | Analisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12252_Recently_Registered_Domains_and_2_others/12252_Recently_Registered_Domains_and_2_others.md` | 29.4 KB | ========================================================================= |
| `Analista SOC/Casos/12252_Recently_Registered_Domains_and_2_others/analisis_soc.md` | 7.6 KB | Analisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12263_Internal_SMB_Read_Anomaly_and_1_other/alerta_original.md` | 26.3 KB | ========================================================================= |
| `Analista SOC/Casos/12263_Internal_SMB_Read_Anomaly_and_1_other/analisis_soc.md` | 8.1 KB | Analisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12265_DNS_Tunneling_Anomaly_and_1_other/alerta_original.md` | 26.4 KB | ========================================================================= |
| `Analista SOC/Casos/12265_DNS_Tunneling_Anomaly_and_1_other/analisis_soc.md` | 9.6 KB | Analisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12267_Exploited_C&C_Connection_and_1_other/alerta_original.md` | 78.7 KB | ========================================================================= |
| `Analista SOC/Casos/12267_Exploited_C&C_Connection_and_1_other/analisis_soc.md` | 7.1 KB | Analisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12319_Sensitive_Windows_Network_Share_File_or_Fold/alerta_original.md` | 40.6 KB | ========================================================================= |
| `Analista SOC/Casos/12319_Sensitive_Windows_Network_Share_File_or_Fold/analisis_soc.md` | 6.5 KB | He detectado 4 eventos independientes en tu volcado. Procederé a analizarlos de manera secuencial y emitiré un |
| `Analista SOC/Casos/12320_Internal_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 21.5 KB | ========================================================================= |
| `Analista SOC/Casos/12320_Internal_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 7.5 KB | He detectado 2 eventos independientes en tu volcado. Procederé a analizarlos de manera secuencial y emitiré un |
| `Analista SOC/Casos/12321_External_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 23.2 KB | ========================================================================= |
| `Analista SOC/Casos/12321_External_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 7.5 KB | He detectado 2 eventos independientes en tu volcado. Procederé a analizarlos de manera secuencial y emitiré un |
| `Analista SOC/Casos/12322_Internal_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 21.5 KB | ========================================================================= |
| `Analista SOC/Casos/12322_Internal_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 8.0 KB | He detectado 2 eventos independientes en tu volcado correspondientes al caso 12322. Procederé a analizarlos de |
| `Analista SOC/Casos/12329_Internal_SMB_Write_Anomaly_and_3_others/alerta_original.md` | 54.1 KB | ========================================================================= |
| `Analista SOC/Casos/12329_Internal_SMB_Write_Anomaly_and_3_others/analisis_soc.md` | 8.6 KB | He detectado 4 eventos en el lote de alertas asociadas al caso 12329. Procederé a analizarlos detalladamente y |
| `Analista SOC/Casos/12330_DNS_Tunneling_Anomaly_and_1_other/alerta_original.md` | 24.6 KB | ========================================================================= |
| `Analista SOC/Casos/12330_DNS_Tunneling_Anomaly_and_1_other/analisis_soc.md` | 6.9 KB | He detectado 2 eventos asociados al caso 12330. A continuación, presento el análisis forense unificado y la ju |
| `Analista SOC/Casos/12334_Exploited_C&C_Connection_and_8_others/alerta_original.md` | 184.4 KB | ========================================================================= |
| `Analista SOC/Casos/12334_Exploited_C&C_Connection_and_8_others/analisis_soc.md` | 6.7 KB | He detectado 9 eventos asociados al caso 12334. A continuación, presento el análisis forense unificado y la ju |
| `Analista SOC/Casos/12335_Uncommon_Top-Level_Domain_Anomaly_and_1_other/alerta_original.md` | 17.3 KB | ========================================================================= |
| `Analista SOC/Casos/12335_Uncommon_Top-Level_Domain_Anomaly_and_1_other/analisis_soc.md` | 5.3 KB | He detectado 2 eventos asociados al caso 12335. A continuación, presento el análisis forense unificado y la ju |
| `Analista SOC/Casos/12367_Exploited_C&C_Connection_and_3_others/alerta_original.md` | 107.1 KB | ========================================================================= |
| `Analista SOC/Casos/12367_Exploited_C&C_Connection_and_3_others/analisis_soc.md` | 6.0 KB | He detectado 4 eventos consolidados bajo el caso 12367. A continuación, presento el análisis forense unificado |
| `Analista SOC/Casos/12374_Public_to_Private_Exploit_Anomaly_and_1_other/alerta_original.md` | 20.4 KB | ========================================================================= |
| `Analista SOC/Casos/12374_Public_to_Private_Exploit_Anomaly_and_1_other/analisis_soc.md` | 6.0 KB | He detectado 2 eventos asociados al caso 12374. A continuación, presento el análisis forense unificado y la ju |
| `Analista SOC/Casos/12383_Internal_Firewall_Policy_Anomaly_and_1_other/alerta_original.md` | 21.5 KB | ========================================================================= |
| `Analista SOC/Casos/12383_Internal_Firewall_Policy_Anomaly_and_1_other/analisis_soc.md` | 6.0 KB | He detectado 2 eventos asociados al caso 12383. A continuación, presento el análisis forense unificado y la ju |
| `Analista SOC/Casos/12499_Internal_Credential_Stuffing_and_178_others/alerta_original.md` | 159.2 KB | ========================================================================= |
| `Analista SOC/Casos/12499_Internal_Credential_Stuffing_and_178_others/analisis_soc.md` | 6.6 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12500_Internal_SMB_Write_Anomaly_and_1_other/alerta_original.md` | 26.8 KB | ========================================================================= |
| `Analista SOC/Casos/12500_Internal_SMB_Write_Anomaly_and_1_other/analisis_soc.md` | 7.9 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12504_Internal_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 21.6 KB | ========================================================================= |
| `Analista SOC/Casos/12504_Internal_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 7.6 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12506_Exploited_C&C_Connection_and_12_others/alerta_original.md` | 263.6 KB | ========================================================================= |
| `Analista SOC/Casos/12506_Exploited_C&C_Connection_and_12_others/analisis_soc.md` | 5.8 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12545_Cloud_Drive_Data_Exfiltration_Anomaly/alerta_original.md` | 15.6 KB | ========================================================================= |
| `Analista SOC/Casos/12545_Cloud_Drive_Data_Exfiltration_Anomaly/analisis_soc.md` | 5.7 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12546_Internal_SMB_Read_Anomaly_and_1_other/alerta_original.md` | 27.0 KB | ========================================================================= |
| `Analista SOC/Casos/12546_Internal_SMB_Read_Anomaly_and_1_other/analisis_soc.md` | 6.0 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12551_Internal_SMB_Read_Anomaly_and_1_other/alerta_original.md` | 26.1 KB | ========================================================================= |
| `Analista SOC/Casos/12551_Internal_SMB_Read_Anomaly_and_1_other/analisis_soc.md` | 5.3 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12560_Uncommon_Process_Anomaly_and_1_other/alerta_original.md` | 19.8 KB | ========================================================================= |
| `Analista SOC/Casos/12560_Uncommon_Process_Anomaly_and_1_other/analisis_soc.md` | 5.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12563_Palo_Alto_Networks_Cortex_XDR_XDR_Analytics/alerta_original.md` | 51.7 KB | ========================================================================= |
| `Analista SOC/Casos/12563_Palo_Alto_Networks_Cortex_XDR_XDR_Analytics/analisis_soc.md` | 6.4 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12588_Internal_Credential_Stuffing_and_133_others/alerta_original.md` | 52.9 KB | ========================================================================= |
| `Analista SOC/Casos/12588_Internal_Credential_Stuffing_and_133_others/analisis_soc.md` | 2.9 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12589_Emerging_Threat_and_1_other/alerta_original.md` | 26.3 KB | ========================================================================= |
| `Analista SOC/Casos/12589_Emerging_Threat_and_1_other/analisis_soc.md` | 8.1 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12590_Internal_SMB_Read_Anomaly_and_1_other/alerta_original.md` | 30.1 KB | ========================================================================= |
| `Analista SOC/Casos/12590_Internal_SMB_Read_Anomaly_and_1_other/analisis_soc.md` | 8.3 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12593_Sensitive_Windows_Network_Share_File_or_Fold/alerta_original.md` | 151.7 KB | ========================================================================= |
| `Analista SOC/Casos/12593_Sensitive_Windows_Network_Share_File_or_Fold/analisis_soc.md` | 2.6 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12595_Recently_Registered_Domains_and_4_others/alerta_original.md` | 71.2 KB | ========================================================================= |
| `Analista SOC/Casos/12595_Recently_Registered_Domains_and_4_others/analisis_soc.md` | 3.6 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12597_Internal_SMB_Read_Anomaly_and_3_others/alerta_original.md` | 66.1 KB | ========================================================================= |
| `Analista SOC/Casos/12597_Internal_SMB_Read_Anomaly_and_3_others/analisis_soc.md` | 2.8 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12598_Internal_SMB_Write_Anomaly_and_3_others/alerta_original.md` | 51.0 KB | ========================================================================= |
| `Analista SOC/Casos/12598_Internal_SMB_Write_Anomaly_and_3_others/analisis_soc.md` | 3.4 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12600_Exploited_C&C_Connection_and_1_other/alerta_original.md` | 56.5 KB | ========================================================================= |
| `Analista SOC/Casos/12600_Exploited_C&C_Connection_and_1_other/analisis_soc.md` | 3.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12632_Internal_SMB_Write_Anomaly_and_2_others/alerta_original.md` | 45.8 KB | ========================================================================= |
| `Analista SOC/Casos/12632_Internal_SMB_Write_Anomaly_and_2_others/analisis_soc.md` | 7.8 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12634_Emerging_Threat_and_2_others/alerta_original.md` | 39.2 KB | ========================================================================= |
| `Analista SOC/Casos/12634_Emerging_Threat_and_2_others/analisis_soc.md` | 6.7 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12637_Private_to_Private_Exploit_Anomaly_and_1_other/alerta_original.md` | 29.4 KB | ========================================================================= |
| `Analista SOC/Casos/12637_Private_to_Private_Exploit_Anomaly_and_1_other/analisis_soc.md` | 8.6 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12647_Internal_Credential_Stuffing_and_458_others/alerta_original.md` | 52.6 KB | ========================================================================= |
| `Analista SOC/Casos/12647_Internal_Credential_Stuffing_and_458_others/analisis_soc.md` | 7.4 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12653_External_Firewall_Denial_Anomaly_and_5_others/alerta_original.md` | 70.5 KB | ========================================================================= |
| `Analista SOC/Casos/12653_External_Firewall_Denial_Anomaly_and_5_others/analisis_soc.md` | 6.9 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12654_Internal_SMB_Read_Anomaly_and_1_other/alerta_original.md` | 26.0 KB | ========================================================================= |
| `Analista SOC/Casos/12654_Internal_SMB_Read_Anomaly_and_1_other/analisis_soc.md` | 6.7 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12655_External_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 35.5 KB | ========================================================================= |
| `Analista SOC/Casos/12655_External_Firewall_Denial_Anomaly_and_2_others/analisis_soc.md` | 6.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12830_Internal_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 45.4 KB | ========================================================================= |
| `Analista SOC/Casos/12830_Internal_Firewall_Denial_Anomaly_and_2_others/analisis_soc.md` | 7.4 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12844_Internal_SMB_Write_Anomaly_and_3_others/alerta_original.md` | 52.3 KB | ========================================================================= |
| `Analista SOC/Casos/12844_Internal_SMB_Write_Anomaly_and_3_others/analisis_soc.md` | 6.7 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12848_Palo_Alto_Networks_Cortex_XDR_Analytics/alerta_original.md` | 34.5 KB | ========================================================================= |
| `Analista SOC/Casos/12848_Palo_Alto_Networks_Cortex_XDR_Analytics/analisis_soc.md` | 6.8 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12851_DNS_Tunneling_Anomaly_and_2_others/alerta_original.md` | 35.2 KB | ========================================================================= |
| `Analista SOC/Casos/12851_DNS_Tunneling_Anomaly_and_2_others/analisis_soc.md` | 5.9 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12892_Internal_Credential_Stuffing_and_26_others/alerta_original.md` | 157.0 KB | ========================================================================= |
| `Analista SOC/Casos/12892_Internal_Credential_Stuffing_and_26_others/analisis_soc.md` | 8.8 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12893_Internal_SMB_Write_Anomaly_and_4_others/analisis_soc.md` | 8.0 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12895_Exploit_Attempt_(Low_Severity)_and_2_others/alerta_original.md` | 34.7 KB | ========================================================================= |
| `Analista SOC/Casos/12895_Exploit_Attempt_(Low_Severity)_and_2_others/analisis_soc.md` | 7.0 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12897_Exploited_C&C_Connection_and_2_others/alerta_original.md` | 68.1 KB | ========================================================================= |
| `Analista SOC/Casos/12897_Exploited_C&C_Connection_and_2_others/analisis_soc.md` | 7.3 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12899_Exploited_C&C_Connection_and_5_others/alerta_original.md` | 105.1 KB | ========================================================================= |
| `Analista SOC/Casos/12899_Exploited_C&C_Connection_and_5_others/analisis_soc.md` | 8.2 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12901_Palo_Alto_Networks_Cortex_XDR_(XDR_Analytics/alerta_original.md` | 34.9 KB | ========================================================================= |
| `Analista SOC/Casos/12901_Palo_Alto_Networks_Cortex_XDR_(XDR_Analytics/analisis_soc.md` | 7.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12902_Public_to_Private_Exploit_Anomaly_and_1_other/alerta_original.md` | 25.4 KB | ========================================================================= |
| `Analista SOC/Casos/12902_Public_to_Private_Exploit_Anomaly_and_1_other/analisis_soc.md` | 7.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12903_External_Firewall_Denial_Anomaly_and_4_others/alerta_original.md` | 58.4 KB | ========================================================================= |
| `Analista SOC/Casos/12903_External_Firewall_Denial_Anomaly_and_4_others/analisis_soc.md` | 7.6 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12906_External_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 35.5 KB | ========================================================================= |
| `Analista SOC/Casos/12906_External_Firewall_Denial_Anomaly_and_2_others/analisis_soc.md` | 7.3 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12907_External_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 35.0 KB | ========================================================================= |
| `Analista SOC/Casos/12907_External_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 7.3 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12908_External_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 23.8 KB | ========================================================================= |
| `Analista SOC/Casos/12908_External_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 6.8 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12909_External_Firewall_Denial_Anomaly_and_2_others/alerta_original.md` | 35.5 KB | ========================================================================= |
| `Analista SOC/Casos/12909_External_Firewall_Denial_Anomaly_and_2_others/analisis_soc.md` | 7.4 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12910_External_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 23.2 KB | ========================================================================= |
| `Analista SOC/Casos/12910_External_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 7.1 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12910_External_Firewall_Denial_Anomaly_and_3_others/alerta_original.md` | 46.6 KB | ========================================================================= |
| `Analista SOC/Casos/12910_External_Firewall_Denial_Anomaly_and_3_others/analisis_soc.md` | 7.9 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/12912_External_Firewall_Denial_Anomaly_and_1_other/alerta_original.md` | 23.6 KB | ========================================================================= |
| `Analista SOC/Casos/12912_External_Firewall_Denial_Anomaly_and_1_other/analisis_soc.md` | 6.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/13013_Internal_Credential_Stuffing_and_24_others/alerta_original.md` | 54.3 KB | ========================================================================= |
| `Analista SOC/Casos/13013_Internal_Credential_Stuffing_and_24_others/analisis_soc.md` | 6.6 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/13014_Internal_SMB_Read_Anomaly_and_2_others/alerta_original.md` | 44.1 KB | ========================================================================= |
| `Analista SOC/Casos/13014_Internal_SMB_Read_Anomaly_and_2_others/analisis_soc.md` | 6.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/13016_Internal_SMB_Write_Anomaly_and_3_others/alerta_original.md` | 50.8 KB | ========================================================================= |
| `Analista SOC/Casos/13016_Internal_SMB_Write_Anomaly_and_3_others/analisis_soc.md` | 6.6 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/145120_Palo_Alto_Networks_Cortex_XDR_route_exe_NB-RBARRETO/alerta_original.md` | 30.5 KB | ========================================================================= |
| `Analista SOC/Casos/145120_Palo_Alto_Networks_Cortex_XDR_route_exe_NB-RBARRETO/analisis_soc.md` | 18.2 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/145384_Palo_Alto_Cortex_XDR_PowerShell_claude_exe_NB-JMARIN/alerta_original.md` | 104.3 KB | Lote Completo de Alertas Nativas de Interflow - Stellar Cyber / Cortex XDR |
| `Analista SOC/Casos/145384_Palo_Alto_Cortex_XDR_PowerShell_claude_exe_NB-JMARIN/analisis_soc.md` | 4.1 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR / Palo Alto Cortex XDR |
| `Analista SOC/Casos/19002_Internal_Firewall_Denial_sati_and_IDS_INFO_checkip/alerta_original.md` | 71.1 KB | <USER_REQUEST> |
| `Analista SOC/Casos/19002_Internal_Firewall_Denial_sati_and_IDS_INFO_checkip/analisis_soc.md` | 19.5 KB | Informe Técnico de Análisis Forense Digital e Incident Response (DFIR) |
| `Analista SOC/Casos/19004_VPN_Policy_289_and_Firefox_Portal_10.212.134.204/alerta_original.md` | 45.0 KB | Alertas Originales Interflow / Stellar Cyber - Lote de 4 Eventos |
| `Analista SOC/Casos/19004_VPN_Policy_289_and_Firefox_Portal_10.212.134.204/analisis_soc.md` | 4.5 KB | Informe de Análisis SOC - Lote Interflow (4 Eventos) |
| `Analista SOC/Casos/19025_WUDO_Firewall_Denial_and_Firefox_Portal_Detection_192.168.169.107/alerta_original.md` | 22.0 KB | Alertas Originales Interflow / Stellar Cyber |
| `Analista SOC/Casos/19025_WUDO_Firewall_Denial_and_Firefox_Portal_Detection_192.168.169.107/analisis_soc.md` | 5.6 KB | Informe de Análisis SOC - Lote Interflow (2 Eventos) |
| `Analista SOC/Casos/19072_Lote10_AD_DNS_Tunnel_sati_VPN_and_ET_cc_TLD/alerta_original.md` | 108.1 KB | Alertas Originales Interflow / Stellar Cyber - Lote de 10 Eventos |
| `Analista SOC/Casos/19072_Lote10_AD_DNS_Tunnel_sati_VPN_and_ET_cc_TLD/analisis_soc.md` | 6.8 KB | Informe de Análisis SOC - Lote Completo Interflow (10 Eventos) |
| `Analista SOC/Casos/19079_Sophos_ServiceNotRunning_dmz_CAJAANDE/alerta_original.md` | 13.6 KB | Alertas Originales Interflow / Stellar Cyber |
| `Analista SOC/Casos/19079_Sophos_ServiceNotRunning_dmz_CAJAANDE/analisis_soc.md` | 4.6 KB | Informe de Análisis SOC - Lote Interflow (2 Eventos) |
| `Analista SOC/Casos/19224_Recently_Registered_Domains_nb-ecanete_firefox-portal/alerta_original.md` | 23.2 KB | Lote de Alertas Originales - Stellar Cyber Interflow |
| `Analista SOC/Casos/19224_Recently_Registered_Domains_nb-ecanete_firefox-portal/analisis_soc.md` | 3.3 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/19306_DNS_Tunnel_Webex_and_Firefox_Portal_nb-jdurand/alerta_original.md` | 21.4 KB | Lote de Alertas Originales - Stellar Cyber Interflow |
| `Analista SOC/Casos/19306_DNS_Tunnel_Webex_and_Firefox_Portal_nb-jdurand/analisis_soc.md` | 3.8 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/19343_WUDO_Firewall_Denial_and_Policy_190_NB-EVERA/alerta_original.md` | 21.3 KB | Alertas Originales Interflow / Stellar Cyber - Lote de 2 Eventos |
| `Analista SOC/Casos/19343_WUDO_Firewall_Denial_and_Policy_190_NB-EVERA/analisis_soc.md` | 5.5 KB | Informe de Análisis SOC - Lote Interflow (2 Eventos) |
| `Analista SOC/Casos/19360_Internal_Firewall_Denial_sati_SSLVPN_DNS_ad2/alerta_original.md` | 61.4 KB | Alerta Original - Raw JSON Interflow (Lote de 5 Eventos) |
| `Analista SOC/Casos/19360_Internal_Firewall_Denial_sati_SSLVPN_DNS_ad2/analisis_soc.md` | 4.7 KB | Informe de Análisis SOC - Lote Interflow (5 Eventos) |
| `Analista SOC/Casos/19383_Recently_Registered_Domains_nb-aprette_firefox-portal/alerta_original.md` | 96.7 KB | Lote de Alertas Originales - Stellar Cyber Interflow |
| `Analista SOC/Casos/19383_Recently_Registered_Domains_nb-aprette_firefox-portal/analisis_soc.md` | 3.6 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/19395_Internal_Firewall_Denial_WUDO_7680_VLAN15_WiFiCorp/alerta_original.md` | 20.5 KB | Alerta Original - Raw JSON Interflow (Lote de 2 Eventos) |
| `Analista SOC/Casos/19395_Internal_Firewall_Denial_WUDO_7680_VLAN15_WiFiCorp/analisis_soc.md` | 4.1 KB | Informe de Análisis SOC - Lote Interflow (2 Eventos) |
| `Analista SOC/Casos/19402_Internal_Firewall_Denial_WUDO_7680_VLAN15_VLAN20/alerta_original.md` | 30.9 KB | Alerta Original - Raw JSON Interflow (Lote de 3 Eventos) |
| `Analista SOC/Casos/19402_Internal_Firewall_Denial_WUDO_7680_VLAN15_VLAN20/analisis_soc.md` | 4.1 KB | Informe de Análisis SOC - Lote Interflow (3 Eventos) |
| `Analista SOC/Casos/19437_Windows_Update_pripub_appid_adm-fs/alerta_original.md` | 11.8 KB | Alertas Originales Interflow / Stellar Cyber - Lote de 4 Eventos |
| `Analista SOC/Casos/19437_Windows_Update_pripub_appid_adm-fs/analisis_soc.md` | 3.8 KB | Informe de Análisis SOC - Lote Interflow (4 Eventos) |
| `Analista SOC/Casos/19445_Internal_Firewall_Denial_WUDO_7680_VLAN15_nb-odacosta/alerta_original.md` | 20.6 KB | Lote Completo de Alertas Nativas de Interflow - Stellar Cyber |
| `Analista SOC/Casos/19445_Internal_Firewall_Denial_WUDO_7680_VLAN15_nb-odacosta/analisis_soc.md` | 3.7 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/19478_Internal_Firewall_Denial_NB-JTORALES_DNS_VPN/alerta_original.md` | 42.2 KB | Alerta Original - Raw JSON Interflow (Lote de 4 Eventos) |
| `Analista SOC/Casos/19478_Internal_Firewall_Denial_NB-JTORALES_DNS_VPN/analisis_soc.md` | 4.8 KB | Informe de Análisis SOC - Lote Interflow (4 Eventos) |
| `Analista SOC/Casos/19558_AD_DNS_Tunnel_Telegram_and_Firefox_Portal/alerta_original.md` | 127.4 KB | Alerta Original - Raw JSON Interflow (Lote de 11 Eventos) |
| `Analista SOC/Casos/19558_AD_DNS_Tunnel_Telegram_and_Firefox_Portal/analisis_soc.md` | 6.8 KB | Informe de Análisis SOC - Lote Interflow (11 Eventos) |
| `Analista SOC/Casos/19610_AD_DNS_Tunnel_and_Internal_FW_Denial_sati/alerta_original.md` | 153.5 KB | Lote de Alertas Originales - Stellar Cyber Interflow |
| `Analista SOC/Casos/19610_AD_DNS_Tunnel_and_Internal_FW_Denial_sati/analisis_soc.md` | 4.0 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/19624_Internal_Firewall_Denial_NB-JTORALES_DNS_VPN_Batch2/alerta_original.md` | 42.1 KB | Lote Completo de Alertas Nativas de Interflow - Stellar Cyber |
| `Analista SOC/Casos/19624_Internal_Firewall_Denial_NB-JTORALES_DNS_VPN_Batch2/analisis_soc.md` | 3.8 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/24319_AD_DNS_Tunnel_and_Internal_FW_Denial_sati/alerta_original.md` | 0.5 KB | Alerta Original - Interflow RAW JSON |
| `Analista SOC/Casos/24319_AD_DNS_Tunnel_and_Internal_FW_Denial_sati/analisis_soc.md` | 11.4 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/27810_Internal_SMB_Write_and_Read_Anomaly_GPO/alerta_original.md` | 0.5 KB | Alerta Original - Interflow RAW JSON |
| `Analista SOC/Casos/27810_Internal_SMB_Write_and_Read_Anomaly_GPO/analisis_soc.md` | 8.3 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/3074_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3090_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3097_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 1.3 KB | Resumen Ejecutivo del Caso (Formato Nativo Stellar) |
| `Analista SOC/Casos/3098_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3099_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3100_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3101_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3117_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3118_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3156_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3157_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3158_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3159_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3160_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3161_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3162_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3164_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3166_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 42.6 KB | ========================================================================= |
| `Analista SOC/Casos/3166_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 4.0 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3166_Sophos_Event_User_Execution_and_5_others/alerta_original.md` | 42.7 KB | ========================================================================= |
| `Analista SOC/Casos/3166_Sophos_Event_User_Execution_and_5_others/analisis_soc.md` | 4.0 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3166_Sophos_Event_User_Execution_and_9_others/alerta_original.md` | 70.8 KB | ========================================================================= |
| `Analista SOC/Casos/3166_Sophos_Event_User_Execution_and_9_others/analisis_soc.md` | 3.9 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3171_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.1 KB | ========================================================================= |
| `Analista SOC/Casos/3171_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 7.6 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3172_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3172_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.0 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3173_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 16.2 KB | ========================================================================= |
| `Analista SOC/Casos/3173_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.2 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3174_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.1 KB | ========================================================================= |
| `Analista SOC/Casos/3174_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3175_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3175_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.6 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3186_Sophos_Event_Impair_Defenses_and_1_other/3186_Sophos_Event_Impair_Defenses_and_1_other.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3186_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 96.6 KB | ========================================================================= |
| `Analista SOC/Casos/3186_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 7.2 KB | He detectado 2 eventos independientes en tu volcado. Procederé a analizarlos de manera secuencial y emitiré un |
| `Analista SOC/Casos/3187_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.1 KB | ========================================================================= |
| `Analista SOC/Casos/3187_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.6 KB | He detectado 2 eventos independientes en tu volcado. Procederé a analizarlos de manera secuencial y emitiré un |
| `Analista SOC/Casos/3189_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.1 KB | ========================================================================= |
| `Analista SOC/Casos/3189_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 7.5 KB | He detectado 2 eventos independientes en tu volcado. Procederé a analizarlos de manera secuencial y emitiré un |
| `Analista SOC/Casos/3190_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3190_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.2 KB | He detectado 3 eventos idénticos en tu volcado correspondientes al caso 3190. Procederé a analizarlos y emitir |
| `Analista SOC/Casos/3194_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3194_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.7 KB | He detectado 2 eventos asociados al caso 3194. A continuación, presento el análisis forense unificado y la jus |
| `Analista SOC/Casos/3196_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3196_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.3 KB | He detectado 2 eventos asociados al caso 3196. A continuación, presento el análisis forense unificado y la jus |
| `Analista SOC/Casos/3225_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3225_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.7 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3226_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3226_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.0 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3227_Sophos_Event_User_Execution_and_11_others/alerta_original.md` | 93.6 KB | ========================================================================= |
| `Analista SOC/Casos/3227_Sophos_Event_User_Execution_and_11_others/analisis_soc.md` | 5.8 KB | He detectado 12 eventos asociados al caso 3227. A continuación, presento el análisis forense unificado y la ju |
| `Analista SOC/Casos/3228_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3228_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.5 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3229_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3229_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 6.8 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3230_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.1 KB | ========================================================================= |
| `Analista SOC/Casos/3230_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.7 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3231_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3231_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.3 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3235_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.4 KB | ========================================================================= |
| `Analista SOC/Casos/3235_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.1 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3236_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3236_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3237_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 13.2 KB | ========================================================================= |
| `Analista SOC/Casos/3237_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3238_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3238_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3239_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3239_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3244_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3244_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.1 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3245_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3245_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.1 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3248_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3248_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 2.0 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3249_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3249_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 2.0 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3250_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3250_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 2.1 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3251_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3251_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 2.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3252_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3252_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 2.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3253_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3253_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 2.2 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3256_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3256_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 2.6 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3257_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3257_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 2.6 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3258_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.1 KB | ========================================================================= |
| `Analista SOC/Casos/3258_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 2.8 KB | 🔍 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3321_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3321_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 4.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3322_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3322_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 6.2 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3323_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3323_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.8 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3324_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.1 KB | ========================================================================= |
| `Analista SOC/Casos/3324_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 6.0 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3325_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.5 KB | ========================================================================= |
| `Analista SOC/Casos/3325_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 4.7 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3326_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3326_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3327_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3327_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.1 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3328_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3328_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3338_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3338_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3339_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3339_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 5.5 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3384_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.2 KB | ========================================================================= |
| `Analista SOC/Casos/3384_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 7.8 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3385_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3385_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 7.2 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3386_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 14.2 KB | ========================================================================= |
| `Analista SOC/Casos/3386_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 7.2 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3387_Sophos_Event_Impair_Defenses_and_1_other/alerta_original.md` | 15.3 KB | ========================================================================= |
| `Analista SOC/Casos/3387_Sophos_Event_Impair_Defenses_and_1_other/analisis_soc.md` | 8.2 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3388_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3388_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 6.3 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/3389_Sophos_Event_User_Execution_and_1_other/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/3389_Sophos_Event_User_Execution_and_1_other/analisis_soc.md` | 5.7 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/43573_AD_DNS_Tunnel_Internal_FW_Denial_and_GPO_Sync/alerta_original.md` | 191.3 KB | <USER_REQUEST> |
| `Analista SOC/Casos/43573_AD_DNS_Tunnel_Internal_FW_Denial_and_GPO_Sync/analisis_soc.md` | 14.4 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/43665_AD_DNS_Tunnel_and_Internal_FW_Denial_sati/alerta_original.md` | 20.4 KB | Evidencia Cruda - Lote de Alertas de Interflow (Secuencia 43665) |
| `Analista SOC/Casos/43665_AD_DNS_Tunnel_and_Internal_FW_Denial_sati/analisis_soc.md` | 18.7 KB | Informe Técnico de Análisis SOC - Stellar Cyber OpenXDR |
| `Analista SOC/Casos/CajaAnde_HealthMailbox/diagnostico_soc.md` | 8.5 KB | Resumen técnico — Diagnóstico de alertas de Brute Force (falsos positivos HealthMailbox) |
| `Analista SOC/Casos/CajaAnde_HealthMailbox/resumen_dpapi_backup_key_sync.md` | 5.6 KB | Resumen Ejecutivo — Alerta "Sensitive Windows Network Share Accessed" (protected_storage) |
| `Analista SOC/Casos/Cloud_Drive_Data_Exfiltration_Anomaly_eliasorlandini/alerta_original.md` | 36.2 KB | "data": { |
| `Analista SOC/Casos/Cloud_Drive_Data_Exfiltration_Anomaly_eliasorlandini/analisis_soc.md` | 22.5 KB | Reporte SOC - Caso: Cloud Drive Data Exfiltration Anomaly (eliasorlandini) |
| `Analista SOC/Casos/Cloud_Drive_Data_Exfiltration_Anomaly_josemarin/alerta_original.md` | 183.3 KB | ========================================================================= |
| `Analista SOC/Casos/Cloud_Drive_Data_Exfiltration_Anomaly_josemarin/analisis_soc.md` | 26.7 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/Cloud_Drive_Data_Exfiltration_Anomaly_josepaez/alerta_original.md` | 33.0 KB | "data": { |
| `Analista SOC/Casos/Cloud_Drive_Data_Exfiltration_Anomaly_josepaez/analisis_soc.md` | 16.2 KB | Reporte SOC - Caso: Cloud Drive Data Exfiltration Anomaly (josepaez) |
| `Analista SOC/Casos/Exploit_Attempt_and_SMB_Cluster_2026-09-03/analisis_soc.md` | 20.9 KB | Reporte SOC Maestro - Cluster de Alertas IDS / SMB / Correlacion C2 (Technoma) |
| `Analista SOC/Casos/gsuite_user_suspended_d72JYJ8BI3UnQyDOCipp/analisis_soc.md` | 5.6 KB | 📘 Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/INCIDENT-529_Rare_unsigned_binary/analisis_soc.md` | 6.4 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/INCIDENT-533_WildFire_Malware/analisis_soc.md` | 6.3 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/INCIDENT-534_WildFire_Malware_CryptoTab/analisis_soc.md` | 6.7 KB | Analisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/Internal_Account_Login_Failure_Anomaly_HealthMailbox_VMBASE8/analisis_soc.md` | 15.5 KB | Reporte SOC - Caso: Internal Account Login Failure Anomaly (HealthMailbox - VMBASE8) |
| `Analista SOC/Casos/Internal_Firewall_Denial_Anomaly_sati_10.212.134.204/alerta_original.md` | 20.8 KB | ========================================================================= |
| `Analista SOC/Casos/Internal_Firewall_Denial_Anomaly_sati_10.212.134.204/analisis_soc.md` | 13.2 KB | Reporte SOC - Caso: Internal Firewall Denial Anomaly (sati - 10.212.134.204) |
| `Analista SOC/Casos/Internal_Firewall_Denial_Anomaly_sati_10.212.134.204_ad2/alerta_original.md` | 30.9 KB | ========================================================================= |
| `Analista SOC/Casos/Internal_Firewall_Denial_Anomaly_sati_10.212.134.204_ad2/analisis_soc.md` | 13.4 KB | Reporte SOC - Caso: Internal Firewall Denial Anomaly (sati - 10.212.134.204 -> ad2) |
| `Analista SOC/Casos/Internal_Firewall_Denial_Anomaly_sati_10.212.134.206/alerta_original.md` | 20.5 KB | "data": { |
| `Analista SOC/Casos/Internal_Firewall_Denial_Anomaly_sati_10.212.134.206/analisis_soc.md` | 13.2 KB | Reporte SOC - Caso: Internal Firewall Denial Anomaly (sati - 10.212.134.206) |
| `Analista SOC/Casos/Internal_SMB_Anomaly_nb-jrivarola_192.168.169.8/alerta_original.md` | 26.1 KB | "data": { |
| `Analista SOC/Casos/Internal_SMB_Anomaly_nb-jrivarola_192.168.169.8/analisis_soc.md` | 5.4 KB | ﻿# Reporte de Análisis SOC: Internal SMB Anomaly & Internal SMB Read Anomaly |
| `Analista SOC/Casos/Login_Time_Anomaly_2296189_CJPPA20150819/alerta_original.md` | 107.4 KB | <USER_REQUEST> |
| `Analista SOC/Casos/Login_Time_Anomaly_2296189_CJPPA20150819/analisis_soc.md` | 19.1 KB | Informe Técnico de Análisis Forense Digital e Incident Response (DFIR) |
| `Analista SOC/Casos/Login_Time_Anomaly_bdominguez_CJPPA056/alerta_original.md` | 54.3 KB | <USER_REQUEST> |
| `Analista SOC/Casos/Login_Time_Anomaly_bdominguez_CJPPA056/analisis_soc.md` | 17.7 KB | Informe Técnico de Análisis Forense Digital e Incident Response (DFIR) |
| `Analista SOC/Casos/Recently_Registered_Domains_nb-fcaceres_firefox-portal-detection/alerta_original.md` | 24.0 KB | ========================================================================= |
| `Analista SOC/Casos/Recently_Registered_Domains_nb-fcaceres_firefox-portal-detection/analisis_soc.md` | 12.5 KB | Reporte SOC - Caso: Recently Registered Domains (nb-fcaceres - firefox-portal-detection.com) |
| `Analista SOC/Casos/Sophos_Blocked_Driver_IntcDAud_CJPPA20170828/alerta_original.md` | 15.6 KB | "data": { |
| `Analista SOC/Casos/Sophos_Blocked_Driver_IntcDAud_CJPPA20170828/analisis_soc.md` | 11.1 KB | Reporte SOC - Caso: Sophos CoreBlockedDriverDetection (IntcDAud.sys - CJPPA20170828) |
| `Analista SOC/Casos/Sophos_Event_User_Execution_CJPPA048_rvalenzuela/alerta_original.md` | 4.3 KB | "aella_tuples": "null.null.null.null", |
| `Analista SOC/Casos/Sophos_Event_User_Execution_CJPPA048_rvalenzuela/analisis_soc.md` | 7.9 KB | Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (CJPPA048 - rvalenzuela) |
| `Analista SOC/Casos/Sophos_Event_User_Execution_CJPPA070_mleiva/alerta_original.md` | 4.3 KB | "aella_tuples": "null.null.null.null", |
| `Analista SOC/Casos/Sophos_Event_User_Execution_CJPPA070_mleiva/analisis_soc.md` | 7.8 KB | Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (CJPPA070 - mleiva) |
| `Analista SOC/Casos/Sophos_Event_User_Execution_CJPPA20120902_MP6236932/alerta_original.md` | 14.1 KB | "data": { |
| `Analista SOC/Casos/Sophos_Event_User_Execution_CJPPA20120902_MP6236932/analisis_soc.md` | 8.5 KB | Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (CJPPA20120902 - MP6236932) |
| `Analista SOC/Casos/Sophos_Event_User_Execution_cjppa_hp_26001_agaray/alerta_original.md` | 14.4 KB | ========================================================================= |
| `Analista SOC/Casos/Sophos_Event_User_Execution_cjppa_hp_26001_agaray/analisis_soc.md` | 13.3 KB | Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (cjppa_hp_26001 - agaray) |
| `Analista SOC/Casos/Sophos_Event_User_Execution_NBCJPPA20260818_jrodriguez/alerta_original.md` | 4.3 KB | "aella_tuples": "null.null.null.null", |
| `Analista SOC/Casos/Sophos_Event_User_Execution_NBCJPPA20260818_jrodriguez/analisis_soc.md` | 11.7 KB | Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (NBCJPPA20260818 - jrodriguez) |
| `Analista SOC/Casos/Sophos_Event_User_Execution_NBCJPPA25003_vescobar/alerta_original.md` | 14.2 KB | "data": { |
| `Analista SOC/Casos/Sophos_Event_User_Execution_NBCJPPA25003_vescobar/analisis_soc.md` | 13.0 KB | Reporte SOC - Caso: Sophos Event: User Execution / WebControlViolation (NBCJPPA25003 - vescobar) |
| `Analista SOC/Casos/Sophos_WebControl_CJPPA20260811_egamarra/analisis_soc.md` | 8.3 KB | ﻿### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/Sophos_WebFiltering_CJPPA20260814_lortellado/analisis_soc.md` | 11.2 KB | ﻿### 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/Stellar_133997_WildFire_Malware/analisis_soc.md` | 6.1 KB | 🕵️‍♂️ Análisis en Profundidad (Estilo Mentor DFIR) |
| `Analista SOC/Casos/Stellar_133997_WildFire_Malware/informe_tecnico_wildfire.md` | 2.0 KB | Resumen del análisis de WepaConfig.exe |

---

## 📂 Capa `PLAYBOOK` (19 documentos)

| Archivo | Tamaño | Función / Título Detectado |
| :--- | :---: | :--- |
| `.agent/skills/attack-tree-construction/resources/implementation-playbook.md` | 22.1 KB | Attack Tree Construction Implementation Playbook |
| `.agent/skills/incident-response-smart-fix/resources/implementation-playbook.md` | 31.7 KB | Intelligent Issue Resolution with Multi-Agent Orchestration Implementation Playbook |
| `.agent/skills/threat-mitigation-mapping/resources/implementation-playbook.md` | 26.6 KB | Threat Mitigation Mapping Implementation Playbook |
| `00_Playbooks/SOC_Incident_Response_Playbooks_Master.md` | 118.1 KB | SOC Incident Response Playbooks Compendium |
| `Analista SOC/Playbook_Remediacion_Sophos_WMI.md` | 2.7 KB | Playbook: Remediación de Sophos UpdateFailure (Error 80041f00) |
| `Analista SOC/playbooks_espec__ficos__2_.docx.md` | 441.0 KB | Ransomware: |
| `Analista SOC/02_Base_de_Conocimiento/Playbook_Sophos_AutoUpdate.md` | 3.7 KB | Playbook de Troubleshooting: Sophos AutoUpdate |
| `Analista SOC/02_Base_de_Conocimiento/Playbook_Sophos_ServiceNotRunning.md` | 6.3 KB | ﻿# Playbook SOC: Diagnostico y Remediacion de Sophos Event::Endpoint::ServiceNotRunning |
| `Analista SOC/Casos/playbooks_espec__ficos__2_.docx.md` | 441.0 KB | Ransomware: |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/02 - Phases of an incident response playbook.md` | 7.0 KB | Phases of an incident response playbook |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/03 - module-4-more-about-playbooks.en.md` | 7.2 KB | More about playbooks |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/04 - Zack Incident response and the value of playbooks.md` | 6.7 KB | Zack: Incident response and the value of playbooks |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/06 - Use a playbook to respond to threats, risks, or vulnerabilities.md` | 6.1 KB | Use a playbook to respond to threats, risks, or vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/08 - Playbooks, SIEM tools, and SOAR tools.md` | 4.1 KB | Playbooks, SIEM tools, and SOAR tools |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/09 - Practice Quiz Test your knowledge Use a playbook to respond to an incident.md` | 2.1 KB | Practice Quiz: Test your knowledge: Use a playbook to respond to an incident |
| `Analista SOC/Investigacion/playbooks_espec__ficos__2_.docx.md` | 441.0 KB | Ransomware: |
| `SKILLS_SOC/attack-tree-construction/resources/implementation-playbook.md` | 22.1 KB | Attack Tree Construction Implementation Playbook |
| `SKILLS_SOC/incident-response-smart-fix/resources/implementation-playbook.md` | 31.7 KB | Intelligent Issue Resolution with Multi-Agent Orchestration Implementation Playbook |
| `SKILLS_SOC/threat-mitigation-mapping/resources/implementation-playbook.md` | 26.6 KB | Threat Mitigation Mapping Implementation Playbook |

---

## 📂 Capa `PROCEDIMIENTO_ARQ` (664 documentos)

| Archivo | Tamaño | Función / Título Detectado |
| :--- | :---: | :--- |
| `MAPA_MAESTRO_PROCEDIMIENTOS_SOAR.md` | 14.5 KB | 🧭 MAPA MAESTRO DE PROCEDIMIENTOS Y ARQUITECTURA PYTHON (SOAR TECHNOMA) |
| `Analista SOC/01_Operacion_Diaria_SOC/Nuevo Documento de texto..md` | 24.5 KB | ========================================================================= |
| `Analista SOC/01_Operacion_Diaria_SOC/Reporte_Diario_CISO.md` | 2.3 KB | 🛡️ Reporte Ejecutivo Diario - Centro de Operaciones de Seguridad (SOC) |
| `Analista SOC/01_Operacion_Diaria_SOC/caso_nissei_ ip-192-168-3-65.md` | 15.1 KB | A s u n t o :   [ I n f e c c i  n   p o r   M a l w a r e ]   -   A n  l i s i s   c r o n o l  g i c o   d e |
| `Analista SOC/01_Operacion_Diaria_SOC/caso_nissei_utf8.md` | 7.7 KB | ﻿Asunto: [Infecci¾n por Malware] - Anßlisis cronol¾gico de trß?co malicioso en |
| `Analista SOC/01_Operacion_Diaria_SOC/ste_assetTab.md` | 62.8 KB | / Friendly Name / Risk / State / Status / IP / Sensor / Sensor ID / Data Sources / Type / Vulnerability / Loca |
| `Analista SOC/03_Arquitectura_y_Despliegue/Arquitectura_OpenDNS_Sinkhole.md` | 2.9 KB | Arquitectura del Incidente: Cómo OpenDNS bloqueó al Malware |
| `Analista SOC/03_Arquitectura_y_Despliegue/Guia_Despliegue_SO3_Distribuido.md` | 5.0 KB | Guía de Migración y Despliegue: Security Onion 3 (Arquitectura Distribuida) |
| `Analista SOC/03_Arquitectura_y_Despliegue/Guia_Despliegue_SO3_Distribuido_Endp.md` | 4.1 KB | Guía de Migración y Despliegue: Security Onion 3 (Distribuido + Endpoints) |
| `Analista SOC/03_Arquitectura_y_Despliegue/Guia_Despliegue_SO3_Standalone_Endp.md` | 3.7 KB | Guía de Migración y Despliegue: Security Onion 3 (Standalone + Endpoints) |
| `Analista SOC/03_Arquitectura_y_Despliegue/Guia_Despliegue_SO3_standalone.md` | 4.9 KB | Guía de Migración y Despliegue: Security Onion 3 |
| `Analista SOC/03_Arquitectura_y_Despliegue/Guia_Instalacion_Stellar_AD.md` | 6.2 KB | 📘 Guía Oficial de Instalación: Stellar Cyber Windows Server Sensor en Active Directory |
| `Analista SOC/03_Arquitectura_y_Despliegue/cheatsheet_mantenimiento_soc_zerotier.md` | 12.5 KB | 🛠️ Cheat Sheet Maestro: Operaciones, Mantenimiento y Consultas |
| `Analista SOC/03_Arquitectura_y_Despliegue/deep_dive_soc_gateway.md` | 6.2 KB | Dossier Técnico y Arquitectura de Control: `command_center.py` |
| `Analista SOC/03_Arquitectura_y_Despliegue/guia_conexion_nodos_remotos_zerotier.md` | 26.8 KB | Procedimiento Operativo Estándar (SOP) |
| `Analista SOC/03_Arquitectura_y_Despliegue/guia_despliegue_elastic_agent_valores_sophos.md` | 11.8 KB | Guía Maestra de Despliegue y Enrolamiento: Elastic Agent — Clientes VALORES & CAJA ANDE |
| `Analista SOC/03_Arquitectura_y_Despliegue/guia_despliegue_sensor_ndr_valores.md` | 29.8 KB | Guía de Despliegue y Enrolamiento: Sensor NDR - Cliente VALORES |
| `Analista SOC/03_Arquitectura_y_Despliegue/informe_tecnico_despliegue_secops_vascol.md` | 18.1 KB | INFORME TÉCNICO Y EJECUTIVO DE ARQUITECTURA |
| `Analista SOC/Investigacion/CTF_Byte_Lotus_Solution.md` | 2.2 KB | Resolución CTF: Hacker Holidays - The Byte Lotus Hotel |
| `Analista SOC/Investigacion/CTF_Complimentary_Solution.md` | 3.4 KB | Resolución CTF: Hacker Holidays - Complimentary (AWS Cognito Misconfiguration) |
| `Analista SOC/Investigacion/Reporte_Forense_Phishing_90540.md` | 21.7 KB | Reporte de Incidente: Intento de Spear Phishing (Ticket #90540) |
| `Analista SOC/Investigacion/guia_live_response_investigacion_bloqueo_smb.md` | 38.1 KB | 🔍 Guía Maestra y Evidencia Forense Live Response — Bloqueo SMB y Descarte de Sophos |
| `Analista SOC/Investigacion/phishing gisselle.md` | 15.4 KB |  #   H o j a   1  |
| `Analista SOC/Investigacion/phishing usuarios.md` | 86.7 KB | /   F e c h a   /   I D   d e   m e n s a j e   /   A s u n t o   /   E v e n t o   /   D e   ( d i r e c c i  |
| `Analista SOC/Investigacion/reporte_ejecutivo_incidente_smb_final.md` | 8.1 KB | 📋 INFORME FORENSE EJECUTIVO — CIERRE DE INCIDENTE SMB |
| `Analista SOC/Novedades/correo_azcona.md` | 1.6 KB | **Asunto:** [Seguridad] Consulta sobre compartición de archivos en Google Drive (Alerta SOC) |
| `Analista SOC/Novedades/correo_yeniperez.md` | 1.9 KB | **Asunto:** [ACCIÓN REQUERIDA] Notificación de Seguridad y Cambio de Contraseñas Obligatorio |
| `Analista SOC/Novedades/reporte_20260724_06a14.md` | 1.3 KB | Reporte de Guardia SOC |
| `Analista SOC/Novedades/reporte_20261007_06a14.md` | 3.2 KB | Reporte de Guardia SOC — Cierre de Turno |
| `Analista SOC/Novedades/reporte_20261010_guardia.md` | 1.5 KB | Reporte de Guardia SOC — Sábado 10/10/2026 |
| `Analista SOC/Novedades/reporte_20261011_guardia.md` | 1.5 KB | Reporte de Guardia SOC — Domingo 11/10/2026 |
| `Analista SOC/Novedades/ticket_rfa_yeniperez.md` | 2.5 KB | Ticket RFA: Reinstalación de SO por Riesgo Persistente de Seguridad |
| `Analista SOC/Procedimientos/Manual_Operativo_Soporte_VASCOL_RDS_Zimbra.md` | 26.2 KB | Manual Operativo de Soporte y Triaje Técnico: VASCOL S.A.C.I. |
| `Analista SOC/Procedimientos/guia_metodologia_triaje_phishing_y_bypass_cdn.md` | 28.1 KB | 🛡️ Manual Operativo SOC: Triaje de Phishing y Auditoría de Origen (Bypass CDN / Cloudflare) |
| `Analista SOC/Procedimientos/guia_operativa_triaje_threat_hunting.md` | 17.6 KB | 🛡️ Manual Operativo SOC: Triaje Forense & Arsenal Threat Hunting |
| `Analista SOC/Reportes/Auditoria_Seguridad_Log_Filters_Cegueras_SOC.md` | 8.6 KB | Auditoría Forense de Seguridad: Análisis de Cegueras en Log Filters — Stellar Cyber |
| `Analista SOC/Reportes/CVE_Report_20260912_1129.md` | 9.0 KB | Reporte de CVEs (Vulnerabilidades NVD NIST 2.0) |
| `Analista SOC/Reportes/Informe_Ejecutivo_Causa_Raiz_Ingesta_DNS_Grafana.md` | 9.3 KB | 📋 INFORME TÉCNICO EJECUTIVO: CAUSA RAÍZ DE EXCESO DE CUOTA Y SATURACIÓN DNS |
| `Analista SOC/Reportes/Informe_Plan_Maestro_Reduccion_Ingesta_y_Queries.md` | 14.5 KB | Plan Maestro de Auditoría y Reducción Quirúrgica de Ingesta — Stellar Cyber OpenXDR |
| `Analista SOC/Reportes/Informe_Seguridad_Uso_No_Autorizado_ProtonDrive_Fabio_Mora.md` | 6.0 KB | 🔒 INFORME TÉCNICO DE SEGURIDAD DE LA INFORMACIÓN |
| `Analista SOC/Reportes/Matriz_Correlacion_Stellar_vs_Cortex.md` | 53.2 KB | Matriz de Correlación de Casos: Stellar Cyber vs Palo Alto Cortex XDR |
| `Analista SOC/Reportes/Reporte_Casos_Cortex_XDR_Palo_Alto.md` | 4.6 KB | Informe Ejecutivo y Técnico de Casos Analizados: Palo Alto Cortex XDR |
| `Analista SOC/Reportes/Reporte_Consolidado_Cortex_XDR_Issues.md` | 639.5 KB | Reporte de Alertas e Issues — Palo Alto Cortex XDR |
| `Analista SOC/Reportes/Reporte_Consolidado_Cortex_XDR_Technoma.md` | 89.6 KB | Reporte de Incidentes — Cortex XDR |
| `Analista SOC/Reportes/Resolucion_Alertas_Cortex_BIOC_Python_SOAR.md` | 5.2 KB | 📘 Ficha Forense de Resolución: Alertas BIOC por Scripts de Python en Cortex XDR |
| `Analista SOC/Security_Onion/01_Guia_Traduccion_Filtros_Stellar_a_Security_Onion_SO3.md` | 18.0 KB | 🧅 SECURITY ONION 3.1.0 (SO3) — ARQUITECTURA DISTRIBUIDA & GESTIÓN DE FILTROS |
| `Analista SOC/Security_Onion/02_Cheatsheet_Comandos_Operativos_SO3.md` | 18.4 KB | 📜 CHEATSHEET OPERATIVO: SECURITY ONION 3.1.0 (SO3) — GRID DISTRIBUIDA |
| `Analista SOC/Security_Onion/03_Caso_Estudio_Rescate_Infraestructura_Security_Onion_SO3.md` | 16.1 KB | Caso de Estudio y Memoria Técnica: Rescate de Infraestructura y Desobstrucción de Recursos en Security Onion 3 |
| `Analista SOC/Stellar Documentacion/GUIA_STELLAR_MCP_Y_CLI_UNIFICADO.md` | 6.1 KB | Manual Operativo: Stellar Cyber MCP Server & CLI Unificado (`stellar_cli.py`) |
| `Analista SOC/Stellar Documentacion/Stellar_Cyber_7.0.0s_Novedades_y_Cambios_API.md` | 5.0 KB | 🚀 Stellar Cyber 7.0.0s — Novedades, Cambios de API e Impacto en el SOC |
| `Analista SOC/Stellar Documentacion/guia_stellar_cyber_log_filtering.md` | 52.6 KB | Guía Maestra de Filtrado Integral — Stellar Cyber OpenXDR v7.0.0s |
| `Analista SOC/Stellar Documentacion/Markdown_Output/1Password Connector.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AI Assistant.md` | 16.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ Half-Opened Sessions.md` | 3.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ Log Source Inactivity.md` | 5.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ No Data From Sensor.md` | 3.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ Blocking a Port Scanning Source IP.md` | 4.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ Notifications for Case Scores.md` | 7.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ Pass the Hash.md` | 4.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ATH Example_ Reset TCP Connections after Detecting Threats.md` | 14.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AWS CloudTrail Connector.md` | 29.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AWS CloudWatch Connector.md` | 21.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AWS Connectors Authentication with IAM Role.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AWS Firewall Connector.md` | 7.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AWS GuardDuty Connector.md` | 21.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/AWS Inspector Connector.md` | 10.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Abnormal Security Email Security Connector.md` | 8.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/About Receivers.md` | 0.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/About the Threat Intelligence Platform.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/About the Threat Intelligence Platform1.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Acronis Cyber Protect Cloud Connector.md` | 16.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Active Directory Connector.md` | 15.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Adding a Table to Display IP Address Pairs with the Most Events.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Adding a Table to Display Sensors with the Most Events.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Adding a Table to Display Source IP Addresses by Average Fidelity & Severity.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Adding a Table to Display Source IP Addresses by Events_Day.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Adding a Table to Group Source IP Addresses by Event Fidelity.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Akamai Connector.md` | 7.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Alert Auto Triage.md` | 19.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Alert Scoring and Categories in Stellar Cyber.md` | 8.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Alert Types New in this Release.md` | 0.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Alert Types with a Detection Time of Timestamp.md` | 3.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Alert Types with a Detection Time of Write Time.md` | 8.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/All Alert Types Model Summary.md` | 690.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/All Alert Types by Name.md` | 615.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/All Alert Types by Name1.md` | 615.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/All Alert Types by XDR Event Name.md` | 683.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/All Rules.md` | 902.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Amazon Security Lake Connector.md` | 10.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Analyst View.md` | 0.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Analyzing Assets.md` | 2.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Armis Connector.md` | 8.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Aruba Central Connector.md` | 10.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Asset Details.md` | 5.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Assets Overview.md` | 0.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Auto-Triage Overview.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Automated Threat Hunting.md` | 75.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Automox Connector.md` | 10.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Azure AD B2C Information Worksheet.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Azure Event Hub Connector.md` | 15.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Azure NSG Connector.md` | 9.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Barracuda Email Connector.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Barracuda Firewall Connector.md` | 6.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Barracuda WAF Connector.md` | 8.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Best Practices and System Design Guidance.md` | 3.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Best Practices for Coverage.md` | 3.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Best Practices for Coverage1.md` | 3.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Best Practices for File Integrity Monitoring (FIM).md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Best Practices for NTP and Timezones.md` | 2.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Best Practices for the System Action Center.md` | 6.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/BeyondTrust Connector.md` | 8.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Bitdefender Connector.md` | 18.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/BlackBerry Cylance Connector.md` | 14.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Box Connector.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Broadcom (Blue Coat _ Symantec) WSS Connector.md` | 6.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Broadcom (Symantec) Cloud Workload Protection Connector.md` | 6.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Broadcom (Symantec) Email Security.cloud Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Broadcom Symantec Endpoint Security (SES) Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/CODA Footprint Connector.md` | 10.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/CYRISMA Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cato Networks Connectors.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Certificates.md` | 0.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Check Point Firewall Connector.md` | 8.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Check Point Harmony Email Connector.md` | 8.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Check Point Smart-1 Cloud Connector.md` | 10.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Check Point Smart-1 Cloud Connector1.md` | 10.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cisco AMP Connector.md` | 7.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cisco Firewall Management Center (FMC) Connector.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cisco Meraki Firewall Connector.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cisco Secure Access Connector.md` | 7.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cloning Windows Server Sensor VMs.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cloudflare Connector.md` | 9.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Common Log Formats.md` | 12.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Complete Configurations on Stellar Cyber.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuration Overview.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configure & Upload Policies _ Keys.md` | 206.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring API Authentication.md` | 12.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring AWS Port Mirroring.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Active Directory Federation Services SSO.md` | 13.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Authentication.md` | 12.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Azure AD B2C SSO.md` | 0.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Bitdefender Log Ingestion.md` | 11.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Certificates for AD Connectors with LDAPS.md` | 5.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Certificates for AD Connectors with LDAPS1.md` | 5.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Connectors.md` | 5.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Corelight Sensor Log Ingestion.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring CyberArk CEF Log Ingestion.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Data Enrichment.md` | 13.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring ERSPAN Ingestion.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring F5 BIG-IP Telemetry.md` | 9.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring F5 BIG-IP Telemetry1.md` | 9.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Feeds in the Threat Intelligence Platform.md` | 26.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Feeds in the Threat Intelligence Platform1.md` | 26.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring GCP Packet Mirroring.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Generic Log Capture.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Global Shared Resources.md` | 1.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Microsoft Entra ID SSO.md` | 25.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Modular Sensor Profiles.md` | 38.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring NXLog for HostIP Field.md` | 11.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Object-Level Sharing and Access Control.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Okta SSO.md` | 15.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring OneLogin SSO.md` | 14.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring RSPAN Ingestion.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Recipients.md` | 4.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Recipients2.md` | 4.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Rippling SSO.md` | 13.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Role-Based Access Control.md` | 10.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Sensor Profiles.md` | 5.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Sensors and Log Sources.md` | 1.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring SentinelOne Log Ingestion.md` | 1.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Standard Sensor Profiles.md` | 71.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Third-Party Authentication.md` | 0.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Users, Roles and Authentication.md` | 1.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring Windows to Identify Who Deleted Files.md` | 3.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring a Central Windows Log Collector.md` | 5.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Configuring a Data Aggregator.md` | 5.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ConnectSecure V4 Connector.md` | 11.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connector Details Page.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connector Types & Functions.md` | 60.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connector Types & Functions1.md` | 60.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connector Types & Functions2.md` | 60.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connectors and Integrations Summary.md` | 61.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connectors and Integrations Summary1.md` | 61.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Connectors and Integrations Summary2.md` | 49.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Converting Sensor Storage to Use Encryption in AWS.md` | 2.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Coro Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Create & Schedule Reports.md` | 41.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Creating New Alert Types.md` | 10.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Creating Saved Scripts.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Credential Management.md` | 3.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/CrowdStrike (Hosts_Events) Connector.md` | 12.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/CrowdStrike FDR Connector.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Custom Dashboard Components.md` | 19.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/CyberArk EPM Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/CyberCNS Connector.md` | 7.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cybereason Connector.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cyble Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Cynet Connector.md` | 8.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Dashboard Actions.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Dashboard Builder (EAP).md` | 27.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Dashboard Examples.md` | 0.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Dashboards Hub (EAP).md` | 6.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Dashboards Hub.md` | 4.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Data Durability and Availability in Stellar Cyber.md` | 9.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Deep Instinct Connector.md` | 9.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Deploying Linux Server Sensors Using Ansible.md` | 14.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Detection Timing Summary.md` | 2.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Detection and Correlation Overview.md` | 4.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Duo Security Connector.md` | 8.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ESET Responder Connector.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Editing Your User Profile.md` | 8.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Email Action Templates.md` | 16.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Enabling SSSE3 for Linux-Based Sensors.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Encrypted Traffic.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Update Tags, Status, and Comments for Events.md` | 15.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Download Sensor Images.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Perform an ElasticSearch Query.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Retrieve Case Details.md` | 18.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Retrieve Case Observables.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Retrieve Connector Details.md` | 11.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Retrieve Sensor Details.md` | 20.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API to Update Case Details.md` | 6.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API with Tenant Groups.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Examples_ Using the API with Tenants.md` | 9.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ExtraHop Reveal(x) 360 Connector.md` | 8.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/F5 BIG-IP ASM Connector.md` | 6.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/F5 BIG-IP Firewall Connector.md` | 7.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/F5 Silverline Connector.md` | 5.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/File Integrity Monitoring Dashboard.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Filter Options.md` | 0.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Firewall Requirements.md` | 0.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Firewall Requirements1.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Firewall Requirements2.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Firewall Requirements3.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Firewalla Managed Security Portal Connector.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Forescout Connector.md` | 12.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/FortiEDR Connector.md` | 7.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/FortiManager Connector.md` | 11.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Fortigate Firewall Connector.md` | 10.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Fortra Frontline Connector.md` | 8.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Forwarding Malware to an External HTTPS Server.md` | 14.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Generating Server Certificates.md` | 3.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Generic S3 Connector.md` | 22.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Getting Started.md` | 3.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Google Cloud Audit Log Connector.md` | 11.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Google Cloud Security Command Center Connector.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Google Workspace Connector.md` | 12.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Group-IB Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/HIBUN Connector.md` | 6.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/HYAS Protect Connector.md` | 9.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Halcyon Connector.md` | 7.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/HanDreamnet Security Switch Connector.md` | 5.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Hillstone Firewall Connector.md` | 5.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Hoxhunt Connector.md` | 7.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Huntress Connector.md` | 9.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Imperva Incapsula Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Importing Assets.md` | 3.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Index Definitions & Details.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Index Definitions & Details1.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Indusface Connector.md` | 6.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Ingesting Logs over TLS.md` | 10.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Ingesting Logs.md` | 4.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Ingestion Dashboard.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installation Overview.md` | 2.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Linux Server Sensor.md` | 25.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in AWS.md` | 14.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in Azure.md` | 28.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in GCP.md` | 14.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in Hyper-V.md` | 20.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in KVM (SaaS).md` | 49.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in OCI.md` | 24.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor in VMware.md` | 22.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Modular Sensor.md` | 1.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Server Sensor.md` | 0.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Installing a Windows Server Sensor.md` | 33.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Integrating with an IdP.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Integration of Third Party Native Alerts.1pdf.md` | 123.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Integration of Third Party Native Alerts.md` | 123.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Integration of Third Party Native Alerts1.md` | 123.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Introducing the Stellar Cyber API.md` | 9.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Introducing the Stellar Cyber API3.md` | 9.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Introduction to Stellar Cyber.md` | 13.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Intrusion Signatures.md` | 4.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Investigate Overview.md` | 4.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Ironscales Connector.md` | 7.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Ironscales Connector1.md` | 7.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Jamf Pro Connector.md` | 7.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Jamf Protect Connector.md` | 7.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/JumpCloud Connector.md` | 7.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Juniper Mist Connector.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Key Fields for Alert Types.md` | 170.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Key Fields for Alert Types1.md` | 170.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/LastPass Connector.md` | 6.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/LimaCharlie Connector.md` | 8.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Liongard Connector.md` | 8.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Liongard Connector1.md` | 8.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Log Parser Ports.md` | 244.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Log Parser Ports1.md` | 244.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Log Parser Ports3.md` | 244.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Logging In.md` | 9.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/M05 Open XDR Windows Server Sensor Installation and Configuration.md` | 130.5 KB | WINDOWS SERVER SENSOR TRANSCRIPT |
| `Analista SOC/Stellar Documentacion/Markdown_Output/MAC or IP-Identified Assets.md` | 5.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Machine Learning Alert Types by Index.md` | 0.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Machine Learning Model Summary.md` | 7.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Machine Learning Only Alert Types.md` | 463.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Mailprotector Connector.md` | 8.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Malware Sandbox.md` | 5.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Manage Engine Endpoint Central Connector.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Certificates.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Firewall Actions.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing IoCs in the Threat Intelligence Platform.md` | 15.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing IoCs in the Threat Intelligence Platform1.md` | 15.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Licenses.md` | 0.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Log Filters.md` | 9.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Scheduled Reports.md` | 7.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Security Switch Actions.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Settings.md` | 6.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Tenants.md` | 0.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Tenants1.md` | 11.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Tenants2.md` | 11.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Traffic Filters_ Application Groups.md` | 2.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Traffic Filters_ Applications.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Managing Users.md` | 14.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Memcyco Connector.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Metadata Dictionary Subset.md` | 21.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Defender for Cloud Apps Connector.md` | 8.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Defender for Endpoint Connector.md` | 12.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Entra ID (formerly Azure Active Directory) Connector.md` | 16.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Graph Intune Connector.md` | 11.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Graph Message Trace Connector.md` | 9.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Graph Security API Connector.md` | 19.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft Graph Security API Connector1.md` | 19.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Microsoft SQL Server Connector.md` | 7.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Mimecast API 1.0 Connector.md` | 9.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Mimecast API 2.0 Connector.md` | 9.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/MySQL Connector.md` | 7.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Nessus Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/NetFoundry Connector.md` | 9.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Netskope Connector.md` | 16.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Network Visibility.md` | 5.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/New & Updated Articles.md` | 1.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/NodeZero Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Nodeware Connector.md` | 7.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/NordStellar Connector.md` | 7.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Notifications Overview.md` | 0.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/OT Deployment.md` | 30.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Office 365 Connector.md` | 13.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Office 365 Connector1.md` | 13.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Office 365 Reporting Web Service Connector.md` | 11.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Okta Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/OneLogin Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Operational View.md` | 0.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Oracle Cloud Infrastructure (OCI) Streaming Connector.md` | 13.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Overview of New User Interface.md` | 12.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Overview of the Knowledge Base.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/PDF Installation Guides.md` | 0.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Palo Alto Networks CORTEX XDR Connector.md` | 11.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Palo Alto Networks Firewall Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Palo Alto Networks Panorama Connector.md` | 10.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Panoramic View.md` | 4.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Parser Studio – Log Sources.md` | 5.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Parser Studio – Parsers.md` | 35.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/People Risk Explorer Connector.md` | 8.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Perception Point X-Ray Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Performing Field Actions.md` | 3.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Performing Field Actions1.md` | 3.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Phishing Auto Triage.md` | 22.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Photon-160-Installation-Quick-Start-SaaS.md` | 9.6 KB | September, 2024 |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Photon-250-Installation-Quick-Start-SaaS.md` | 6.5 KB | September, 2024 |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Photon-400-Installation-Quick-Start-SaaS.md` | 7.2 KB | September, 2024 |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Physical Photon Sensor Specifications.md` | 4.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Pre-DPI Filters.md` | 8.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Predefined Dashboards.md` | 0.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Prepare Details for Policy _ Key Configuration.md` | 18.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Prepare _ Configure Users in Azure AD B2C.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Prisma Cloud (Palo Alto Networks) Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Product Security Overview.md` | 5.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Proofpoint TAP Connector.md` | 9.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Proofpoint on Demand Connector.md` | 14.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Provisioning Disk Space for Virtual Modular Sensors.md` | 2.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Qualys Connector.md` | 7.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Qualys FIM Connector.md` | 8.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Queries and Filters.md` | 115.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Queries and Filters2.md` | 115.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Quick Start_ Administrators.md` | 5.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Quick Start_ Analysts.md` | 2.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rapid7 Connector.md` | 6.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Recorded Future Connector.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Related Events for Alert Types.md` | 5.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Remote SSH Host Connector.md` | 5.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Removing Tenants.md` | 4.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Reporting Menu Overview.md` | 0.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Reputation Definitions.md` | 7.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Reserving Resources for Virtual Modular Sensors.md` | 4.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Resetting a Device Sensor's Password.md` | 2.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Respond Menu Overview.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Routers.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rule Framework Summary.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rule-Based Alert Type Details.md` | 5.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rule-Based Alert Types.md` | 21.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rule-Based Alert Types1.md` | 21.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rule-Based Only Alert Types.md` | 162.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to AWS Default VPC Configuration Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to AWS EC2 Security Group Deleted Alert.md` | 1.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to AWS High-Risk Ports Exposed to Internet Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to AWS IAM Policy with Wildcard Privileges Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to AWS S3 Bucket Missing Server-Side Encryption Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to AWS S3 Bucket Policy with Public Access Alert.md` | 0.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Azure Application Gateway Changed Alert.md` | 0.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Azure DNS Zone Changed Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Azure New CloudShell Created Alert.md` | 1.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Azure Security Configuration Changed Alert.md` | 4.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to BloodHound Enumeration Activity.md` | 4.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to DCERPC SMB Spoolss Named Pipe Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to DNS Query to Anonymous File Upload Domains.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to DNS Query to External Service Interaction Domains.md` | 2.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to DNS Query to Monero Crypto Coin Mining Pool Domains.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to DNS Query to TOR Proxy Domain.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Impacket PsExec Execution Alert.md` | 1.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft 365 Rare Operations Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Application Configuration Changes Alert.md` | 5.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Application Deleted Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Application Permission Changes Alert.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Bitlocker Key Retrieval Alert.md` | 1.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Changes to Conditional Access Policy Alert.md` | 5.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Changes to Device Registration Policy Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Changes to Privileged Account Alert.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Changes to Privileged Role Assignment Alert.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Federation Modified Alert.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Guest User Invited by Non-Approved Inviters Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Hybrid Health AD FS New Server Alert.md` | 2.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Hybrid Health AD FS Service Deleted Alert.md` | 2.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra ID Discovery using Azurehound Alert.md` | 1.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra ID MFA Disabled Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Owner Removed from Application Alert.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra PIM Setting Changed Alert.md` | 2.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Privileged Account Assignment or Elevation Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Microsoft Entra Sign-in Failure Alert.md` | 4.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to OCI Discovery Activity Alert.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to OCI Insecure Metadata Endpoint Alert.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to OCI Insecure NFS Export Configuration Alert.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to OCI Instance Metadata Access Alert.md` | 1.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to OCI Unexpected User Agent Alert.md` | 1.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Parent_Child-based Suspicious Process Creation Alert.md` | 76.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Password Reset By User Account Alert.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Persistence and Execution at Scale via GPO Scheduled Task Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Phishing Domain with File Extension TLD.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Possible Impacket SecretDump Remote Activity Alert.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Possible PetitPotam Coerce Authentication Attempt Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Potentially Malicious AWS Activity Alert.md` | 34.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Potentially Malicious Windows Event Alerts.md` | 45.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Protected Storage Service Access Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Remote Service Activity via SVCCTL Named Pipe Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Remote Task Creation via ATSVC Named Pipe Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Sensitive Windows Active Directory Attribute Modification Alerts.md` | 3.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Sensitive Windows Network Share File or Folder Accessed Alerts.md` | 15.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Startup_Logon Script Added to Group Policy Object Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Steal or Forge Kerberos Tickets Alert.md` | 4.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AD Machine Account Creation Alert.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS Bucket Enumeration Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS EBS Activity Alert.md` | 1.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS EC2 Activity Alert.md` | 14.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS ELB Activity Alert.md` | 1.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS IAM Activity Alert.md` | 21.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS Login Failure.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS RDS Event.md` | 12.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS Root Account Activity Alert.md` | 3.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS Route 53 Activity Alert.md` | 4.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS SSL Certificate Activity Alert.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS VPC Flow Logs Modification Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious AWS VPC Mirror Session Activity.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Access Attempt to Windows Object Alerts.md` | 12.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Activity Related to Security-Enabled Group Alerts.md` | 5.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Account Permission Elevation Alert.md` | 2.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Deployment Activity Alert.md` | 3.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Firewall Activity Alert.md` | 6.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Key Vault Activity Alert.md` | 5.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Kubernetes Activity_ Credential Access Alert.md` | 2.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Kubernetes Activity_ Defense Evasion Alert.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Kubernetes Activity_ Impact Alert.md` | 7.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Kubernetes Activity_ Persistence Alert.md` | 2.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Kubernetes Activity_ Privilege Escalation Alert.md` | 5.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Azure Network Activity Alert.md` | 4.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Connection to Another Process Alerts.md` | 3.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Handle Request to Sensitive Object Alerts.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Kerberos Authentication from Golden Certificate Alert.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious LSASS Process Access Alert.md` | 11.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Microsoft 365 Inbox Rule Alert.md` | 5.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Microsoft 365 Mail Transport Rule Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Microsoft Entra Device Activity Alert.md` | 2.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Microsoft Entra Service Principal Activity Alert.md` | 3.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Microsoft Entra Sign-in Activity Alert.md` | 5.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Modification of AWS CloudTrail Logs Alert.md` | 5.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Modification of AWS Route Table Alert.md` | 3.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Modification of S3 Bucket Alert.md` | 5.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Bucket Enumeration Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Bucket Public Access Type Configuration Alert.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Configuration Change to Network Security Group Alert.md` | 2.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Event Rule Deletion Alert.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI IAM Activity_ Impact Alert.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI IAM Activity_ Persistence Alert.md` | 5.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Inbound SSH Connection Alert.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Instance Activity Alert.md` | 2.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Instance Image Export Alert.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Kubernetes Activity Alert.md` | 1.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Logging Activity Alert.md` | 4.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Modification of Route Table Alert.md` | 3.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Object Storage Activity Alert.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Scanning Activity Alert.md` | 1.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious OCI Security Service Impairment Alert.md` | 3.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious PowerShell Script Alert Type.md` | 156.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Process Creation Commandline Alert.md` | 262.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious PsExec Execution Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Windows Active Directory Operation Alerts.md` | 5.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Windows Logon Event Alerts.md` | 8.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Windows Network Connection Alert.md` | 5.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Windows Registry Event_ Impact Alert.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Windows Registry Event_ Persistence Alert.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Suspicious Windows Service Installation Alert.md` | 21.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to T1047 Wmiprvse Wbemcomn DLL Hijack Alert.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Windows Network Access Suspicious desktop.ini Action Alert.md` | 1.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to Windows Suspicious Process Creation Alert.md` | 26.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Rules Contributing to certutil.exe Certificate Extraction Alert.md` | 2.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/SLA (Service Level Agreements).md` | 2.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/SOCRadar Connector.md` | 8.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Salesforce Connector.md` | 17.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Searching the Knowledge Base.md` | 3.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Searching.md` | 11.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Security Monitoring with Stellar Cyber.md` | 0.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sensor CLI Access Window.md` | 42.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sensor CLI Access Window1.md` | 42.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sensor Details.md` | 9.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sensor Installation Summary.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/SentinelOne Connector.md` | 22.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Server Sensor Sizing Specifications.md` | 1.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Server Sensor Update Behavior through an Aggregator.md` | 8.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Service Visibility.md` | 3.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Setting the Home Page.md` | 1.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Single Sensor Multi-Tenant Log Ingestion.md` | 9.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/SonicWall Capture Client Connector.md` | 8.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/SonicWall Endpoint Security Connector.md` | 11.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/SonicWall Firewall Connector.md` | 12.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sophos Central Connector.md` | 11.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sophos XG Firewall Connector.md` | 9.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Standard Metadata Dictionary.md` | 29.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber 6.6.0s Release Notes.md` | 60.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Architecture.md` | 21.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Architecture2.md` | 21.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Connector.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Feature and API Deprecation Policy.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Glossary.md` | 30.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Overview.md` | 3.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Product Support and End of Life Policies.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber SaaS Availability and Architecture.md` | 3.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Security Development Lifecycle.md` | 6.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stellar Cyber Default Credentials.md` | 0.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Stormshield Network Security (SNS) Firewall Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Streaming Data to a Snowflake Data Lake.md` | 3.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Sucuri Security Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Supported Sensor Operating Systems.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Supported Sensor Operating Systems1.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Swagger UI.md` | 46.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Swagger UI1.md` | 46.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/System (Management) Overview.md` | 0.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/TLS Version and Cipher Suites.md` | 0.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/TLS Version and Cipher Suites1.md` | 0.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Templates for Windows Server Sensors.md` | 13.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Tenable Cloud Security Connector.md` | 7.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Tenable.io Connector.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Tenable.sc Connector.md` | 7.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Tenant Mapping.md` | 9.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Thinkst Canary Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Threat Hunting.md` | 37.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/ThreatDown OneView (formerly Malwarebytes OneView) Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Threatlocker Connector.md` | 7.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trellix (FireEye) Endpoint Security HX Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trellix MVISION Connector.md` | 8.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trend Micro Apex Central Connector.md` | 9.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trend Micro Cloud App Security Connector.md` | 10.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trend Micro Cloud One Security Connector.md` | 8.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trend Micro Email Security Connector.md` | 8.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Trend Micro Vision One Connector.md` | 15.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Types of Stellar Cyber Sensors.md` | 6.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Alert Auto Triage Performance.md` | 5.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Asset-Based Licensing.md` | 15.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Cases.md` | 28.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Cases1.md` | 28.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Cases3.md` | 28.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Casesj1.md` | 28.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Event Details.md` | 41.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Event Details1.md` | 41.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Interflow.md` | 8.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Interflow1.md` | 8.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding License Compliance.md` | 6.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Tenants.md` | 6.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding Volume-Based Licensing.md` | 2.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding the Stellar Cyber Risk Model.md` | 6.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding the XDR Kill Chain.md` | 14.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Understanding the XDR Kill Chain2.md` | 14.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Universal Webhook Responder Connector.md` | 18.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Universal Webhook Responder Connector1.md` | 18.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Upload a Custom Parser Provided by Customer Success.md` | 4.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/User Behavior Analytics.md` | 9.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/User Reported Phishing Email Alerts.md` | 19.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using AI Investigator.md` | 24.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using Chart Builder.md` | 21.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using InSyncs.md` | 26.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using Tables.md` | 17.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using Tenant Groups.md` | 3.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using Toolbar Filters.md` | 15.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using Toolbar Filters1.md` | 15.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using a Modular Sensor with Azure Virtual Network TAP (VTAP).md` | 39.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Alert Details.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Alerts Page.md` | 30.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Analysis Tab in the Case Detail View.md` | 18.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Detection Management System.md` | 37.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Detection Management System1.md` | 37.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Detection Management System2.md` | 37.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Detection Tab in the Case Details View.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Detection Tab in the Case Details View1.md` | 7.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Kibana Plugin.md` | 2.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Notification Center.md` | 5.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Response Tab in the Case Details View.md` | 24.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Sensor Installation Page.md` | 22.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Sensor Overview.md` | 33.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the Sensor Overview2.md` | 33.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the System Action Center.md` | 100.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the System Action Center2.md` | 100.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the XDR Kill Chain (Home Page).md` | 26.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the XDR Kill Chain (Home Page)1.md` | 26.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Using the XDR Kill Chain (Home Page)2.md` | 26.1 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/VMware Carbon Black Cloud Connector.md` | 16.7 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/VMware Workspace ONE Connector.md` | 6.4 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/VadeSecure Connector.md` | 7.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Vendor-Related Metadata.md` | 1.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Verkada Connector.md` | 10.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Versa Networks Concerto Connector.md` | 7.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Versa Networks Firewall Connector.md` | 8.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Vicarius Connector.md` | 7.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Viewing Email Actions.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Viewing Endpoint Actions.md` | 2.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Viewing Response Action History.md` | 1.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Viewing Script Actions.md` | 1.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Viewing User Actions.md` | 1.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Viewing Webhook Actions.md` | 1.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Virtual Modular Sensor Provisioning and Performance.md` | 6.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/WatchGuard Firebox Responder Connector.md` | 10.0 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Webroot Connector.md` | 9.5 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/WithSecure Elements Connector.md` | 14.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Wiz Connector.md` | 10.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Case Details.md` | 19.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Case Details1.md` | 19.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Cases (Including Case Queues).md` | 35.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Cases.md` | 28.9 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Dashboards.md` | 17.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Dashboards1.md` | 17.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Queries and Filters.1pdf.md` | 7.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Queries and Filters.md` | 7.6 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with Watchlists.md` | 11.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/Working with the Connectors Table.md` | 15.3 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/XDR Connector.md` | 13.8 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `Analista SOC/Stellar Documentacion/Markdown_Output/iManage Threat Manager Connector.md` | 9.2 KB | Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes! |
| `auditoria_cuota_stellar/GUIA_FILTROS_Y_ALERT_CUSTOMIZATIONS.md` | 5.2 KB | Guía Maestra de Filtros y Supresión en Stellar Cyber OpenXDR |
| `auditoria_cuota_stellar/README.md` | 4.0 KB | Suite de Auditoría de Cuota y Telemetría Stellar Cyber (SOC Technoma) |

---

## 📂 Capa `SKILL_SOC` (124 documentos)

| Archivo | Tamaño | Función / Título Detectado |
| :--- | :---: | :--- |
| `.agent/skills/active-directory-attacks/SKILL.md` | 9.9 KB | name: active-directory-attacks |
| `.agent/skills/active-directory-attacks/references/advanced-attacks.md` | 9.8 KB | Advanced Active Directory Attacks Reference |
| `.agent/skills/analyze_cortex_alert/SKILL.md` | 5.6 KB | name: analyze_cortex_alert |
| `.agent/skills/analyze_stellar_alert/SKILL.md` | 4.0 KB | name: analyze_stellar_alert |
| `.agent/skills/api-design/SKILL.md` | 13.3 KB | name: api-design |
| `.agent/skills/attack-tree-construction/SKILL.md` | 1.5 KB | name: attack-tree-construction |
| `.agent/skills/burp-suite-testing/SKILL.md` | 11.2 KB | name: burp-suite-testing |
| `.agent/skills/burpsuite-project-parser/SKILL.md` | 12.6 KB | name: burpsuite-project-parser |
| `.agent/skills/cisco-ios-patterns/SKILL.md` | 5.2 KB | name: cisco-ios-patterns |
| `.agent/skills/deep-research/SKILL.md` | 4.8 KB | name: deep-research |
| `.agent/skills/error-handling/SKILL.md` | 11.0 KB | name: error-handling |
| `.agent/skills/ethical-hacking-methodology/SKILL.md` | 11.2 KB | name: ethical-hacking-methodology |
| `.agent/skills/firmware-analyst/SKILL.md` | 8.0 KB | name: firmware-analyst |
| `.agent/skills/google_cyber_transcriber/SKILL.md` | 6.6 KB | name: google_cyber_transcriber |
| `.agent/skills/html-injection-testing/SKILL.md` | 13.5 KB | name: html-injection-testing |
| `.agent/skills/human_writer/SKILL.md` | 1.4 KB | name: human_writer |
| `.agent/skills/incident-responder/SKILL.md` | 10.2 KB | name: incident-responder |
| `.agent/skills/incident-response-incident-response/SKILL.md` | 10.7 KB | name: incident-response-incident-response |
| `.agent/skills/incident-response-smart-fix/SKILL.md` | 3.3 KB | name: incident-response-smart-fix |
| `.agent/skills/incident-runbook-templates/SKILL.md` | 11.1 KB | name: incident-runbook-templates |
| `.agent/skills/linux-privilege-escalation/SKILL.md` | 12.1 KB | name: linux-privilege-escalation |
| `.agent/skills/malware-analyst/SKILL.md` | 6.6 KB | name: malware-analyst |
| `.agent/skills/memory-forensics/SKILL.md` | 11.2 KB | name: memory-forensics |
| `.agent/skills/metasploit-framework/SKILL.md` | 14.1 KB | name: metasploit-framework |
| `.agent/skills/netmiko-ssh-automation/SKILL.md` | 6.0 KB | name: netmiko-ssh-automation |
| `.agent/skills/network-101/SKILL.md` | 7.7 KB | name: network-101 |
| `.agent/skills/network-bgp-diagnostics/SKILL.md` | 5.6 KB | name: network-bgp-diagnostics |
| `.agent/skills/network-config-validation/SKILL.md` | 7.7 KB | name: network-config-validation |
| `.agent/skills/network-engineer/SKILL.md` | 9.6 KB | name: network-engineer |
| `.agent/skills/network-interface-health/SKILL.md` | 5.7 KB | name: network-interface-health |
| `.agent/skills/powershell-windows/SKILL.md` | 3.7 KB | name: powershell-windows |
| `.agent/skills/python-patterns/SKILL.md` | 17.2 KB | name: python-patterns |
| `.agent/skills/python-testing/SKILL.md` | 19.2 KB | name: python-testing |
| `.agent/skills/red-team-tactics/SKILL.md` | 4.8 KB | name: red-team-tactics |
| `.agent/skills/red-team-tools/SKILL.md` | 8.1 KB | name: red-team-tools |
| `.agent/skills/security-audit/SKILL.md` | 5.3 KB | name: security-audit |
| `.agent/skills/security-auditor/SKILL.md` | 10.0 KB | name: security-auditor |
| `.agent/skills/security-bluebook-builder/SKILL.md` | 2.3 KB | name: security-bluebook-builder |
| `.agent/skills/security-bounty-hunter/SKILL.md` | 3.6 KB | name: security-bounty-hunter |
| `.agent/skills/security-review/SKILL.md` | 12.7 KB | name: security-review |
| `.agent/skills/security-review/cloud-infrastructure-security.md` | 10.3 KB | / name / description / |
| `.agent/skills/security-scan/SKILL.md` | 4.5 KB | name: security-scan |
| `.agent/skills/security-scanning-security-hardening/SKILL.md` | 10.7 KB | name: security-scanning-security-hardening |
| `.agent/skills/shodan-reconnaissance/SKILL.md` | 13.9 KB | name: shodan-reconnaissance |
| `.agent/skills/soc-bitacora/SKILL.md` | 6.9 KB | name: soc-bitacora |
| `.agent/skills/soc-council/SKILL.md` | 3.6 KB | name: soc_council |
| `.agent/skills/soc-incidencias/SKILL.md` | 5.3 KB | name: soc-incidencias |
| `.agent/skills/soc_shift_handover/SKILL.md` | 3.9 KB | name: soc_shift_handover |
| `.agent/skills/soc_swarm_response/SKILL.md` | 2.5 KB | name: soc_swarm_response |
| `.agent/skills/sql-injection-testing/SKILL.md` | 11.7 KB | name: sql-injection-testing |
| `.agent/skills/stellar-api-interaction/SKILL.md` | 4.5 KB | name: stellar-api-interaction |
| `.agent/skills/stellar-soc-playbooks/SKILL.md` | 8.0 KB | name: stellar-soc-playbooks |
| `.agent/skills/stellar-soc-triage/SKILL.md` | 4.3 KB | name: stellar-soc-triage |
| `.agent/skills/threat-mitigation-mapping/SKILL.md` | 1.1 KB | name: threat-mitigation-mapping |
| `.agent/skills/threat-modeling-expert/SKILL.md` | 2.1 KB | name: threat-modeling-expert |
| `.agent/skills/update_soc_memory/SKILL.md` | 1.1 KB | name: update_soc_memory |
| `.agent/skills/vulnerability-scanner/SKILL.md` | 7.8 KB | name: vulnerability-scanner |
| `.agent/skills/vulnerability-scanner/checklists.md` | 2.8 KB | Security Checklists |
| `.agent/skills/web-security-testing/SKILL.md` | 4.1 KB | name: web-security-testing |
| `.agent/skills/windows-desktop-e2e/SKILL.md` | 30.6 KB | name: windows-desktop-e2e |
| `.agent/skills/wireshark-analysis/SKILL.md` | 12.3 KB | name: wireshark-analysis |
| `.agent/skills/xss-html-injection/SKILL.md` | 13.6 KB | name: xss-html-injection |
| `SKILLS_SOC/README_SKILLS.md` | 6.1 KB | Inventario de Skills - Proyecto SOC & OpenXDR |
| `SKILLS_SOC/active-directory-attacks/SKILL.md` | 9.9 KB | name: active-directory-attacks |
| `SKILLS_SOC/active-directory-attacks/references/advanced-attacks.md` | 9.8 KB | Advanced Active Directory Attacks Reference |
| `SKILLS_SOC/analyze_cortex_alert/SKILL.md` | 5.6 KB | name: analyze_cortex_alert |
| `SKILLS_SOC/analyze_stellar_alert/SKILL.md` | 4.0 KB | name: analyze_stellar_alert |
| `SKILLS_SOC/api-design/SKILL.md` | 13.3 KB | name: api-design |
| `SKILLS_SOC/attack-tree-construction/SKILL.md` | 1.5 KB | name: attack-tree-construction |
| `SKILLS_SOC/burp-suite-testing/SKILL.md` | 11.2 KB | name: burp-suite-testing |
| `SKILLS_SOC/burpsuite-project-parser/SKILL.md` | 12.6 KB | name: burpsuite-project-parser |
| `SKILLS_SOC/cisco-ios-patterns/SKILL.md` | 5.2 KB | name: cisco-ios-patterns |
| `SKILLS_SOC/deep-research/SKILL.md` | 4.8 KB | name: deep-research |
| `SKILLS_SOC/error-handling/SKILL.md` | 11.0 KB | name: error-handling |
| `SKILLS_SOC/ethical-hacking-methodology/SKILL.md` | 11.2 KB | name: ethical-hacking-methodology |
| `SKILLS_SOC/firmware-analyst/SKILL.md` | 8.0 KB | name: firmware-analyst |
| `SKILLS_SOC/google_cyber_transcriber/SKILL.md` | 6.6 KB | name: google_cyber_transcriber |
| `SKILLS_SOC/html-injection-testing/SKILL.md` | 13.5 KB | name: html-injection-testing |
| `SKILLS_SOC/human_writer/SKILL.md` | 1.4 KB | name: human_writer |
| `SKILLS_SOC/incident-responder/SKILL.md` | 10.2 KB | name: incident-responder |
| `SKILLS_SOC/incident-response-incident-response/SKILL.md` | 10.7 KB | name: incident-response-incident-response |
| `SKILLS_SOC/incident-response-smart-fix/SKILL.md` | 3.3 KB | name: incident-response-smart-fix |
| `SKILLS_SOC/incident-runbook-templates/SKILL.md` | 11.1 KB | name: incident-runbook-templates |
| `SKILLS_SOC/linux-privilege-escalation/SKILL.md` | 12.1 KB | name: linux-privilege-escalation |
| `SKILLS_SOC/malware-analyst/SKILL.md` | 6.6 KB | name: malware-analyst |
| `SKILLS_SOC/memory-forensics/SKILL.md` | 11.2 KB | name: memory-forensics |
| `SKILLS_SOC/metasploit-framework/SKILL.md` | 14.1 KB | name: metasploit-framework |
| `SKILLS_SOC/netmiko-ssh-automation/SKILL.md` | 6.0 KB | name: netmiko-ssh-automation |
| `SKILLS_SOC/network-101/SKILL.md` | 7.7 KB | name: network-101 |
| `SKILLS_SOC/network-bgp-diagnostics/SKILL.md` | 5.6 KB | name: network-bgp-diagnostics |
| `SKILLS_SOC/network-config-validation/SKILL.md` | 7.7 KB | name: network-config-validation |
| `SKILLS_SOC/network-engineer/SKILL.md` | 9.6 KB | name: network-engineer |
| `SKILLS_SOC/network-interface-health/SKILL.md` | 5.7 KB | name: network-interface-health |
| `SKILLS_SOC/powershell-windows/SKILL.md` | 3.7 KB | name: powershell-windows |
| `SKILLS_SOC/python-patterns/SKILL.md` | 17.2 KB | name: python-patterns |
| `SKILLS_SOC/python-testing/SKILL.md` | 19.2 KB | name: python-testing |
| `SKILLS_SOC/red-team-tactics/SKILL.md` | 4.8 KB | name: red-team-tactics |
| `SKILLS_SOC/red-team-tools/SKILL.md` | 8.1 KB | name: red-team-tools |
| `SKILLS_SOC/security-audit/SKILL.md` | 5.3 KB | name: security-audit |
| `SKILLS_SOC/security-auditor/SKILL.md` | 10.0 KB | name: security-auditor |
| `SKILLS_SOC/security-bluebook-builder/SKILL.md` | 2.3 KB | name: security-bluebook-builder |
| `SKILLS_SOC/security-bounty-hunter/SKILL.md` | 3.6 KB | name: security-bounty-hunter |
| `SKILLS_SOC/security-review/SKILL.md` | 12.7 KB | name: security-review |
| `SKILLS_SOC/security-review/cloud-infrastructure-security.md` | 10.3 KB | / name / description / |
| `SKILLS_SOC/security-scan/SKILL.md` | 4.5 KB | name: security-scan |
| `SKILLS_SOC/security-scanning-security-hardening/SKILL.md` | 10.7 KB | name: security-scanning-security-hardening |
| `SKILLS_SOC/shodan-reconnaissance/SKILL.md` | 13.9 KB | name: shodan-reconnaissance |
| `SKILLS_SOC/soc-bitacora/SKILL.md` | 6.9 KB | name: soc-bitacora |
| `SKILLS_SOC/soc-council/SKILL.md` | 3.6 KB | name: soc_council |
| `SKILLS_SOC/soc-incidencias/SKILL.md` | 5.3 KB | name: soc-incidencias |
| `SKILLS_SOC/soc_shift_handover/SKILL.md` | 3.9 KB | name: soc_shift_handover |
| `SKILLS_SOC/soc_swarm_response/SKILL.md` | 2.5 KB | name: soc_swarm_response |
| `SKILLS_SOC/sql-injection-testing/SKILL.md` | 11.7 KB | name: sql-injection-testing |
| `SKILLS_SOC/stellar-soc-playbooks/SKILL.md` | 8.0 KB | name: stellar-soc-playbooks |
| `SKILLS_SOC/stellar-soc-triage/SKILL.md` | 4.3 KB | name: stellar-soc-triage |
| `SKILLS_SOC/threat-mitigation-mapping/SKILL.md` | 1.1 KB | name: threat-mitigation-mapping |
| `SKILLS_SOC/threat-modeling-expert/SKILL.md` | 2.1 KB | name: threat-modeling-expert |
| `SKILLS_SOC/update_soc_memory/SKILL.md` | 1.1 KB | name: update_soc_memory |
| `SKILLS_SOC/vulnerability-scanner/SKILL.md` | 7.8 KB | name: vulnerability-scanner |
| `SKILLS_SOC/vulnerability-scanner/checklists.md` | 2.8 KB | Security Checklists |
| `SKILLS_SOC/web-security-testing/SKILL.md` | 4.1 KB | name: web-security-testing |
| `SKILLS_SOC/windows-desktop-e2e/SKILL.md` | 30.6 KB | name: windows-desktop-e2e |
| `SKILLS_SOC/wireshark-analysis/SKILL.md` | 12.3 KB | name: wireshark-analysis |
| `SKILLS_SOC/xss-html-injection/SKILL.md` | 13.6 KB | name: xss-html-injection |

---

## 📂 Capa `ACADEMIA_SOC` (250 documentos)

| Archivo | Tamaño | Función / Título Detectado |
| :--- | :---: | :--- |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 1/01 - Graded Quiz Module 1 challenge.md` | 5.2 KB | Graded Quiz: Module 1 challenge |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 2/01 - Practice Quiz Safeguard information.md` | 2.5 KB | Practice Quiz: Test your knowledge: Safeguard information |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 2/02 - Lab Exemplar Decrypt an encrypted message.md` | 6.3 KB | Laboratorio: Decrypt an encrypted message |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 2/03 - Lab Exemplar Create hash values.md` | 5.7 KB | Laboratorio: Create hash values |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 2/04 - Practice Quiz Encryption methods.md` | 2.5 KB | Practice Quiz: Test your knowledge: Encryption methods |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 2/05 - Practice Quiz Authentication authorization and accounting.md` | 2.8 KB | Practice Quiz: Test your knowledge: Authentication, authorization, and accounting |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 2/06 - Graded Quiz Module 2 challenge.md` | 7.1 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 3/01 - Practice Quiz Flaws in the system.md` | 2.5 KB | Practice Quiz: Test your knowledge: Flaws in the system |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 3/02 - Practice Quiz Identify system vulnerabilities.md` | 2.4 KB | Practice Quiz: Test your knowledge: Identify system vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 3/03 - Practice Quiz Self reflection Approach cybersecurity with an attacker mindset.md` | 4.4 KB | Practice Quiz: Self-reflection: Approach cybersecurity with an attacker mindset |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 3/04 - Practice Quiz Cyber attacker mindset.md` | 2.9 KB | Practice Quiz: Test your knowledge: Cyber attacker mindset |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 3/05 - Graded Quiz Module 3 challenge.md` | 8.1 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 4/01 - Practice Quiz Social engineering.md` | 2.7 KB | Practice Quiz: Test your knowledge: Social engineering |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 4/02 - Practice Quiz Activity Filter malicious emails.md` | 4.5 KB | Practice Quiz: Activity: Filter malicious emails |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 4/03 - Practice Quiz Malware.md` | 2.1 KB | Practice Quiz: Test your knowledge: Malware |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 4/04 - Practice Quiz Web-based exploits.md` | 3.1 KB | Practice Quiz: Test your knowledge: Web-based exploits |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 4/05 - Practice Quiz Threat modeling.md` | 2.5 KB | Practice Quiz: Test your knowledge: Threat modeling |
| `Analista SOC/Google Cybersecurity Certification/Assets, Threats, and Vulnerabilities/Modulo 4/06 - Graded Quiz Module 4 challenge.md` | 6.3 KB | Graded Quiz: Module 4 challenge |
| `Analista SOC/Google Cybersecurity Certification/Automate Cybersecurity Tasks with Python/Modulo 1/01 - Graded Quiz Module 1 challenge.md` | 4.8 KB | Graded Quiz: Module 1 challenge |
| `Analista SOC/Google Cybersecurity Certification/Automate Cybersecurity Tasks with Python/Modulo 2/01 - Graded Quiz Module 2 challenge.md` | 4.3 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Automate Cybersecurity Tasks with Python/Modulo 3/01 - Graded Quiz Module 3 challenge.md` | 3.9 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Automate Cybersecurity Tasks with Python/Modulo 4/01 - Graded Quiz Module 4 challenge.md` | 5.4 KB | Graded Quiz: Module 4 challenge |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/01 - Introduction to Course 3.md` | 4.0 KB | Introduction to Course 3 |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/02 - module-1-course-3-overview.en.md` | 9.5 KB | Course 3 overview |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/03 - Welcome to module 1.md` | 2.9 KB | Welcome to module 1 |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/04 - Chris My path to cybersecurity.md` | 5.7 KB | Chris: My path to cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/05 - What are networks.md` | 4.6 KB | What are networks? |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/06 - Tina Working in network security.md` | 4.7 KB | Tina: Working in network security |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/07 - Emmanuel Useful skills for network security.md` | 5.8 KB | Emmanuel: Useful skills for network security |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/08 - Network tools.md` | 4.9 KB | Network tools |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/09 - module-1-network-components-devices-and-diagrams.en.md` | 12.4 KB | Network components, devices, and diagrams |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/10 - Cloud networks.md` | 5.3 KB | Cloud networks |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/11 - module-1-cloud-computing-and-software-defined-networks.en.md` | 11.1 KB | Reading: Cloud computing and software-defined networks |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/12 - Practice Quiz Test your knowledge Introduction to networks.md` | 1.7 KB | Practice Quiz: Test your knowledge: Introduction to networks |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/13 - Introduction to network communication.md` | 6.1 KB | Introduction to network communication |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/14 - The TCP-IP model.md` | 6.4 KB | The TCP/IP model |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/15 - The four layers of the TCP-IP model.md` | 5.4 KB | The four layers of the TCP/IP model |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/16 - module-1-learn-more-about-the-tcp-ip-model.en.md` | 11.9 KB | Reading: Learn more about the TCP/IP model |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/17 - module-1-the-osi-model.en.md` | 9.8 KB | Reading: The OSI model |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/18 - Practice Quiz Test your knowledge Network communication.md` | 3.1 KB | Practice Quiz: Test your knowledge: Network communication |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/19 - IP addresses and network communication.md` | 6.0 KB | IP addresses and network communication |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/20 - module-1-components-of-network-layer-communication.en.md` | 11.4 KB | Components of network layer communication |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/21 - Practice Quiz Test your knowledge Local and wide network communication.md` | 1.7 KB | Practice Quiz: Test your knowledge: Local and wide network communication |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/22 - Wrap-up.md` | 3.7 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/23 - Glossary terms from module 1.md` | 6.3 KB | Glossary terms from module 1 |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/24 - Graded Quiz Module 1 Challenge.md` | 5.3 KB | Graded Quiz: Module 1 Challenge |
| `Analista SOC/Google Cybersecurity Certification/Connect and Protect Networks and Network Security/Modulo 1/module-1-glossary-terms-from-module-1.en.md` | 2.4 KB | Reading: Glossary terms from module 1 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/01 - Welcome to the Google Cybersecurity Certificate.md` | 9.6 KB | Welcome to the Google Cybersecurity Certificate |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/03 - module-1-google-cybersecurity-certificate-overview.md` | 4.1 KB | Lectura: Resumen del Certificado de Ciberseguridad de Google |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/05 - module-1-course-1-overview.md` | 7.3 KB | Lectura: Resumen del Curso 1 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/06 - Welcome to module 1.md` | 2.0 KB | Welcome to module 1 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/07 - Get started with your Google Cybersecurity Certificate.md` | 3.3 KB | Get started with your Google Cybersecurity Certificate |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/08 - Introduction to cybersecurity.md` | 5.6 KB | Introduction to cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/09 - Toni My path to cybersecurity.md` | 4.4 KB | Toni: My path to cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/10 - Responsibilities of an entry-level cybersecurity analyst.md` | 4.3 KB | Responsibilities of an entry-level cybersecurity analyst |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/11 - Nikki A day in the life of a security engineer.md` | 4.1 KB | Nikki: A day in the life of a security engineer |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/13 - module-1-common-cybersecurity-terminology.md` | 4.2 KB | Lectura: Terminología común de ciberseguridad |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/14 - Practice Quiz Introduction to cybersecurity.md` | 1.9 KB | Practice Quiz: Introduction to cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/15 - Core skills for cybersecurity professionals.md` | 5.1 KB | Core skills for cybersecurity professionals |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/16 - Veronica My path to working in cybersecurity.md` | 3.2 KB | Veronica: My path to working in cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/18 - module-1-transferable-and-technical-cybersecurity-skills.md` | 4.9 KB | Lectura: Transferable and technical cybersecurity skills |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/19 - The importance of cybersecurity.md` | 4.3 KB | The importance of cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/20 - Practice Quiz Core skills for cybersecurity professionals.md` | 1.8 KB | Practice Quiz: Core skills for cybersecurity professionals |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/21 - Wrap-up.md` | 2.1 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/23 - module-1-glossary-terms-from-module-1.md` | 3.2 KB | Lectura: Glosario de términos del Módulo 1 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/24 - Graded Quiz Module 1 challenge.md` | 4.1 KB | Graded Quiz: Module 1 challenge |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 1/walkthrough.md` | 1.6 KB | Framework de Transcripción Creado |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/01 - Welcome to module 2.md` | 2.2 KB | Welcome to module 2 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/02 - Past cybersecurity attacks.md` | 4.8 KB | Past cybersecurity attacks |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/03 - Attacks in the digital age.md` | 4.1 KB | Attacks in the digital age |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/05 - module-2-common-attacks-and-their-effectiveness.md` | 5.8 KB | Lectura: Common attacks and their effectiveness |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/06 - Sean Keep your cool during a data breach.md` | 3.5 KB | Sean: Keep your cool during a data breach |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/07 - Practice Quiz The history of cybersecurity.md` | 2.8 KB | Practice Quiz: Test your knowledge: The history of cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/08 - Introduction to the eight CISSP security domains Part 1.md` | 4.1 KB | Introduction to the eight CISSP security domains, Part 1 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/09 - Introduction to the eight CISSP security domains Part 2.md` | 3.9 KB | Introduction to the eight CISSP security domains, Part 2 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/11 - module-2-determine-the-type-of-attack.md` | 4.3 KB | Lectura: Determine the type of attack |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/13 - module-2-understand-attackers.md` | 4.1 KB | Lectura: Understand attackers |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/14 - Practice Quiz The eight CISSP security domains.md` | 2.8 KB | Practice Quiz: Test your knowledge: The eight CISSP security domains |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/15 - Wrap-up.md` | 2.8 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/17 - module-2-glossary-terms-from-module-2.md` | 4.0 KB | Glosario: Términos del Módulo 2 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 2/18 - Graded Quiz Module 2 challenge.md` | 6.0 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/01 - Welcome to module 3.md` | 3.3 KB | Welcome to module 3 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/02 - Introduction to security frameworks and controls.md` | 4.3 KB | Introduction to security frameworks and controls |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/03 - Secure design.md` | 4.5 KB | Secure design |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/04 - module-3-controls-frameworks-and-compliance.md` | 5.1 KB | Lectura: Controls, frameworks, and compliance |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/05 - Heather Protect sensitive data and information.md` | 3.0 KB | Heather: Protect sensitive data and information |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/06 - Practice Quiz Frameworks and controls.md` | 2.3 KB | Practice Quiz: Test your knowledge: Frameworks and controls |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/07 - Ethics in cybersecurity.md` | 4.8 KB | Ethics in cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/08 - module-3-ethical-concepts-that-guide-cybersecurity-decisions.md` | 4.1 KB | Lectura: Ethical concepts that guide cybersecurity decisions |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/09 - Holly The importance of ethics as a cybersecurity professional.md` | 3.9 KB | Holly: The importance of ethics as a cybersecurity professional |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/10 - Practice Quiz Ethics in cybersecurity.md` | 4.1 KB | Practice Quiz: Test your knowledge: Ethics in cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/11 - Wrap-up.md` | 1.9 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/12 - module-3-glossary-terms-from-module-3.md` | 3.4 KB | Glosario del Módulo 3 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 3/13 - Graded Quiz Module 3 challenge.md` | 6.0 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/01 - Welcome to module 4.md` | 2.4 KB | Welcome to module 4 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/02 - Common cybersecurity tools.md` | 3.4 KB | Common cybersecurity tools |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/03 - module-4-tools-for-protecting-business-operations.md` | 5.2 KB | Lectura: Tools for protecting business operations |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/04 - Practice Quiz Important cybersecurity tools.md` | 2.2 KB | Practice Quiz: Test your knowledge: Important cybersecurity tools |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/05 - Introduction to Linux SQL and Python.md` | 3.2 KB | Introduction to Linux, SQL, and Python |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/06 - module-4-use-tools-to-protect-business-operations.md` | 5.6 KB | Lectura: Use tools to protect business operations |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/07 - Practice Quiz Core cybersecurity knowledge.md` | 2.1 KB | Practice Quiz: Test your knowledge: Core cybersecurity knowledge and skills |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/08 - module-4-create-a-cybersecurity-portfolio.md` | 3.6 KB | Lectura: Create a cybersecurity portfolio |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/09 - Graded Quiz Draft a professional statement.md` | 3.5 KB | Actividad del Portafolio: Redactar una declaración profesional |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/10 - Professional statement outline.md` | 2.5 KB | Material de Apoyo: Professional statement outline |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/11 - Refine your professional statement.md` | 1.7 KB | Material de Apoyo: Refine your professional statement |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/12 - module-4-portfolio-activity-exemplar-draft-a-professional-statement.md` | 1.4 KB | Lectura: Portfolio Activity Exemplar: Draft a professional statement |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/13 - Wrap-up.md` | 1.4 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/14 - Glossary terms from module 4.md` | 2.8 KB | Glosario: Términos del Módulo 4 |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/15 - Graded Quiz Module 4 challenge.md` | 5.6 KB | Graded Quiz: Module 4 challenge |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/16 - Course wrap-up.md` | 2.2 KB | Course wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/17 - Course 1 glossary.md` | 10.7 KB | Glosario Maestro del Curso 1: Fundamentos de Ciberseguridad |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/18 - module-4-get-started-on-the-next-course.md` | 3.0 KB | Lectura: Get started on the next course |
| `Analista SOC/Google Cybersecurity Certification/Foundations of Cybersecurity/Modulo 4/19 - module-4-course-1-resources-and-citations.md` | 3.1 KB | Recursos y Citas del Curso 1 |
| `Analista SOC/Google Cybersecurity Certification/Google Security Operations - Fundamentals/Assessment_Google_Security_Operations_Fundamentals.md` | 3.7 KB | Assessment: Google Security Operations - Fundamentals |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/01 - Introduction to Course 2.md` | 2.4 KB | Introduction to Course 2 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/02 - module-1-course-2-overview.md` | 4.1 KB | Lectura: Course 2 overview |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/03 - Welcome to module 1.md` | 1.7 KB | Welcome to module 1 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/04 - Explore the CISSP security domains, Part 1.md` | 4.7 KB | Explore the CISSP security domains, Part 1 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/05 - Explore the CISSP security domains, Part 2.md` | 5.3 KB | Explore the CISSP security domains, Part 2 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/06 - module-1-security-domains-cybersecurity-analysts-need-to-know.md` | 6.8 KB | Lectura: Security domains cybersecurity analysts need to know |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/07 - Ashley My path to cybersecurity.md` | 4.4 KB | Ashley: My path to cybersecurity |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/08 - Practice Quiz More about the CISSP security domains.md` | 2.8 KB | Practice Quiz: Test your knowledge: More about the CISSP security domains |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/09 - Threats, risks, and vulnerabilities.md` | 5.0 KB | Threats, risks, and vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/10 - Key impacts of threats, risks, and vulnerabilities.md` | 4.8 KB | Key impacts of threats, risks, and vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/11 - Herbert Manage threats, risks, and vulnerabilities.md` | 2.9 KB | Herbert: Manage threats, risks, and vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/12 - NISTs Risk Management Framework.md` | 5.0 KB | NIST’s Risk Management Framework |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/13 - module-1-manage-common-threats-risks-and-vulnerabilities.md` | 6.0 KB | Lectura: Manage common threats, risks, and vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/14 - Practice Quiz Navigate threats, risks, and vulnerabilities.md` | 2.3 KB | Practice Quiz: Test your knowledge: Navigate threats, risks, and vulnerabilities |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/15 - Wrap-up.md` | 2.0 KB | Wrap-up (Resumen del Módulo 1) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/16 - module-1-glossary-terms-from-module-1.md` | 3.3 KB | Glosario: Términos del Módulo 1 (Manage Security Risks) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 1/17 - Graded Quiz Module 1 challenge.md` | 6.2 KB | Graded Quiz: Module 1 challenge |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/01 - Welcome to module 2.md` | 1.7 KB | Welcome to module 2 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/02 - Frameworks.md` | 3.2 KB | Frameworks |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/03 - Controls.md` | 4.7 KB | Controls |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/04 - module-2-the-relationship-between-frameworks-and-controls.md` | 4.7 KB | Lectura: The relationship between frameworks and controls |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/05 - Practice Quiz More about frameworks and controls.md` | 2.5 KB | Practice Quiz: Test your knowledge: More about frameworks and controls |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/06 - Explorando la Triada CIA.md` | 5.3 KB | Explorando la Tríada CIA |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/07 - module-2-use-the-cia-triad-to-protect-organizations.en.md` | 4.8 KB | Lectura: Uso de la Tríada CIA para Proteger Organizaciones |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/08 - Practice Quiz Test your knowledge The CIA triad.md` | 2.4 KB | Practice Quiz: Test your knowledge: The CIA triad |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/09 - Frameworks de NIST.md` | 5.9 KB | Frameworks de NIST (NIST Frameworks) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/10 - Explore the six functions of the NIST Cybersecurity Framework.md` | 5.0 KB | Explorando las Funciones Core del Marco de Ciberseguridad de NIST |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/11 - Practice Quiz Test your knowledge NIST frameworks.md` | 3.2 KB | Practice Quiz: Test your knowledge: NIST frameworks |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/12 - OWASP security principles.md` | 6.5 KB | Principios de Seguridad de OWASP (OWASP Security Principles) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/13 - module-2-more-about-owasp-security-principles.en.md` | 5.8 KB | Lectura: Más sobre los Principios de Seguridad de OWASP |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/14 - Wajih Stay up-to-date on the latest cybersecurity threats.md` | 4.3 KB | Wajih: Mantente al Día sobre las Últimas Amenazas de Ciberseguridad |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/15 - Plan a security audit.md` | 6.8 KB | Planificación de una Auditoría de Seguridad (Plan a Security Audit) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/16 - Complete a security audit.md` | 7.2 KB | Completando una Auditoría de Seguridad (Complete a Security Audit) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/17 - module-2-more-about-security-audits.en.md.md` | 8.3 KB | Lectura: Más sobre las Auditorías de Seguridad (More about security audits) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/18 - Practice Quiz Test your knowledge OWASP principles and security audits.md` | 2.9 KB | Practice Quiz: Test your knowledge: OWASP principles and security audits |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/19 - Graded Quiz Portfolio Activity Conduct a security audit.md` | 4.1 KB | Graded Quiz: Portfolio Activity: Conduct a security audit |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/20 - Botium Toys Scope, goals, and risk assessment report.md` | 10.4 KB | Botium Toys: Informe de Alcance, Objetivos y Evaluación de Riesgos (Botium Toys: Scope, goals, and risk assess |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/21 - Control categories.md` | 7.9 KB | Lectura: Categorías y Tipos de Controles de Seguridad (Control Categories) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/22 - Controls and compliance checklist.md` | 8.7 KB | Botium Toys: Lista de Verificación de Controles y Cumplimiento (Controls and Compliance Checklist) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/23 - module-2-portfolio-activity-exemplar-conduct-a-security-audit.en..md` | 3.9 KB | Lectura: Ejemplar de la Actividad de Portafolio: Realizar una Auditoría de Seguridad (Portfolio Activity Exemp |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/24 - Wrap-up.md` | 4.5 KB | Cierre del Módulo: Resumen de Conceptos de Seguridad (Wrap-up) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/25 - module-2-glossary-terms-from-module-2.en.md` | 7.3 KB | Lectura: Glosario de Términos del Módulo 2 (Glossary terms from module 2) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 2/26 - Graded Quiz Module 2 challenge.md` | 7.7 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/01 - Welcome to Module 3.md` | 3.7 KB | Bienvenido al Módulo 3 (Welcome to Module 3) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/02 - Logs and SIEM tools.md` | 5.3 KB | Registros de Actividad y Herramientas SIEM (Logs and SIEM tools) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/03 - SIEM dashboards.md` | 5.7 KB | SIEM dashboards |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/04 - module-3-the-future-of-siem-tools.en.md` | 7.5 KB | Lectura: El Futuro de las Herramientas SIEM (The future of SIEM tools) |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/05 - Parisa The parallels of accessibility and security.md` | 5.3 KB | Parisa: The parallels of accessibility and security |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/06 - Practice Quiz Test your knowledge Security information and event management (SIEM) dashboards.md` | 2.0 KB | Practice Quiz: Test your knowledge: Security information and event management (SIEM) dashboards |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/07 - Explore common SIEM tools.md` | 5.8 KB | Explore common SIEM tools |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/08 - module-3-more-about-cybersecurity-tools.en.md` | 7.9 KB | More about cybersecurity tools |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/09 - Talya Myths about the cybersecurity field.md` | 5.0 KB | Talya: Myths about the cybersecurity field |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/10 - module-3-use-siem-tools-to-protect-organizations.en.md` | 11.1 KB | Use SIEM tools to protect organizations |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/11 - Practice Quiz Test your knowledge Identify threats and vulnerabilities with SIEM tools.md` | 2.1 KB | Practice Quiz: Test your knowledge: Identify threats and vulnerabilities with SIEM tools |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/12 - Wrap-up.md` | 3.5 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/13 - module-3-glossary-terms-from-module-3.en.md` | 5.3 KB | Reading: Glossary terms from module 3 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 3/14 - Graded Quiz Module 3 challenge.md` | 4.7 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/01 - Welcome to module 4.md` | 3.2 KB | Welcome to module 4 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/05 - Practice Quiz Test your knowledge Incident response.md` | 2.8 KB | Practice Quiz: Test your knowledge: Incident response |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/07 - Erin The importance of diversity of perspective on a security team.md` | 5.8 KB | Erin: The importance of diversity of perspective on a security team |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/10 - Wrap-up.md` | 3.9 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/11 - module-4-glossary-terms-from-module-4.en.md` | 2.4 KB | Reading: Glossary terms from module 4 |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/12 - Graded Quiz Module 4 challenge.md` | 5.5 KB | Graded Quiz: Module 4 challenge |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/13 - Course wrap-up.md` | 4.7 KB | Course wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/14 - module-4-course-2-glossary.en.md` | 2.8 KB | Reading: Course 2 glossary |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/15 - Course 2 glossary.md` | 13.6 KB | Reading: Course 2 glossary |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/16 - Get started on the next course.md` | 5.1 KB | Reading: Get started on the next course |
| `Analista SOC/Google Cybersecurity Certification/Play It Safe Manage Security Risks/Modulo 4/17 - module-4-course-2-resources-and-citations.en.md` | 12.1 KB | Reading: Course 2 resources and citations |
| `Analista SOC/Google Cybersecurity Certification/Put It to Work Prepare for Cybersecurity Jobs/Modulo 1/01 - Graded Quiz Module 1 challenge.md` | 4.8 KB | Graded Quiz: Module 1 challenge |
| `Analista SOC/Google Cybersecurity Certification/Put It to Work Prepare for Cybersecurity Jobs/Modulo 2/01 - Graded Quiz Module 2 challenge.md` | 5.6 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Put It to Work Prepare for Cybersecurity Jobs/Modulo 3/01 - Graded Quiz Module 3 challenge.md` | 5.5 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Put It to Work Prepare for Cybersecurity Jobs/Modulo 4/01 - Graded Quiz Module 4 challenge.md` | 5.7 KB | Graded Quiz: Module 4 challenge |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 1/01 - Graded Quiz Module 1 challenge.md` | 5.9 KB | Graded Quiz: Module 1 challenge |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 1/02 - Practice Quiz Test your knowledge The incident response lifecycle.md` | 1.8 KB | Practice Quiz: Test your knowledge: The incident response lifecycle |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 1/03 - Practice Quiz Test your knowledge Incident response operations.md` | 2.1 KB | Practice Quiz: Test your knowledge: Incident response operations |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 1/04 - Practice Quiz Test your knowledge Detection and documentation tools.md` | 1.6 KB | Practice Quiz: Test your knowledge: Detection and documentation tools |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 1/05 - Practice Quiz Test your knowledge Management tools.md` | 1.8 KB | Practice Quiz: Test your knowledge: Management tools |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 2/01 - Graded Quiz Module 2 challenge.md` | 4.7 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 2/02 - Exemplar Analyze your first packet with Wireshark.md` | 4.4 KB | Exemplar: Analyze your first packet with Wireshark |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 2/03 - Practice Quiz Test your knowledge Capture and view network traffic.md` | 1.4 KB | Practice Quiz: Test your knowledge: Capture and view network traffic |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 2/04 - Exemplar Capture your first packet.md` | 3.8 KB | Exemplar: Capture your first packet |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 2/05 - Practice Quiz Test your knowledge Packet inspection.md` | 1.2 KB | Practice Quiz: Test your knowledge: Packet inspection |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 3/01 - Graded Quiz Module 3 challenge.md` | 5.0 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 3/02 - Practice Quiz Test your knowledge Incident detection and verification.md` | 1.4 KB | Practice Quiz: Test your knowledge: Incident detection and verification |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 3/03 - Practice Quiz Test your knowledge Response and recovery.md` | 1.8 KB | Practice Quiz: Test your knowledge: Response and recovery |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 3/04 - Practice Quiz Activity Review a final report.md` | 1.5 KB | Practice Quiz: Activity: Review a final report |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 3/05 - Practice Quiz Test your knowledge Post-incident actions.md` | 2.2 KB | Practice Quiz: Test your knowledge: Post-incident actions |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/01 - Graded Quiz Module 4 challenge.md` | 3.8 KB | Graded Quiz: Module 4 challenge |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/02 - Practice Quiz Test your knowledge Overview of logs.md` | 1.6 KB | Practice Quiz: Test your knowledge: Overview of logs |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/03 - Practice Quiz Test your knowledge Log components and formats.md` | 1.5 KB | Practice Quiz: Test your knowledge: Log components and formats |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/04 - Exemplar Examine alerts, logs, and rules with Suricata.md` | 4.7 KB | Exemplar: Examine alerts, logs, and rules with Suricata |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/05 - Practice Quiz Test your knowledge Overview of intrusion detection systems (IDS).md` | 2.0 KB | Practice Quiz: Test your knowledge: Overview of intrusion detection systems (IDS) |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/06 - Practice Quiz Activity Perform a query with Wazuh.md` | 1.5 KB | Practice Quiz: Activity: Perform a query with Wazuh |
| `Analista SOC/Google Cybersecurity Certification/Sound the Alarm Detection and Response/Modulo 4/07 - Practice Quiz Test your knowledge Overview of SIEM tools.md` | 1.6 KB | Practice Quiz: Test your knowledge: Overview of SIEM tools |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/01 - Introduction to the shell.md` | 3.7 KB | Introduction to the shell |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/02 - module-2-different-types-of-shells.en.md` | 4.5 KB | Reading: Different types of shells |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/03 - Input and output in the shell.md` | 3.9 KB | Input and output in the shell |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/04 - module-2-exemplar-examine-input-and-output-in-the-shell.en.md` | 5.9 KB | Exemplar: Examine input and output in the shell |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/05 - Practice Quiz Test your knowledge The shell.md` | 2.8 KB | Practice Quiz: Test your knowledge: The shell |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/06 - Wrap-up.md` | 2.6 KB | Wrap-up |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/07 - module-2-glossary-terms-from-module-2.en.md` | 5.7 KB | Reading: Glossary terms from module 2 |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/09 - module-2-more-linux-distributions.en..md` | 5.6 KB | Reading: More Linux distributions |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/10 - module-2-package-managers-for-installing-applications.en.md` | 5.4 KB | Reading: Package managers for installing applications |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/11 - module-2-resources-for-completing-linux-labs.en.md` | 8.1 KB | Reading: Resources for completing Linux labs |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/12- module-2-lab-tips-and-troubleshooting-steps.en.md` | 4.9 KB | Reading: Lab tips and troubleshooting steps |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/13 - module-2-exemplar-install-software-in-a-linux-distribution.en.md` | 7.2 KB | Exemplar: Install software in a Linux distribution |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/14 - Practice Quiz Test your knowledge Linux distributions.md` | 1.9 KB | Practice Quiz: Test your knowledge: Linux distributions |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 2/16 - Graded Quiz Module 2 challenge.md` | 4.7 KB | Graded Quiz: Module 2 challenge |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/01 - Welcome to module 3.md` | 2.7 KB | Welcome to module 3 |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/02 - Linux commands via the Bash shell.md` | 4.1 KB | Linux commands via the Bash shell |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/04 - module-3-navigate-linux-and-read-file-content.en.md` | 8.6 KB | Reading: Navigate Linux and read file content |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/06 - Practice Quiz Test your knowledge Navigate the Linux file system in Bash.md` | 3.1 KB | Practice Quiz: Test your knowledge: Navigate the Linux file system in Bash |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/09 - Practice Quiz Test your knowledge Manage file content in Bash.md` | 2.9 KB | Practice Quiz: Test your knowledge: Manage file content in Bash |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/13 - Practice Quiz Test your knowledge Authenticate and authorize users.md` | 3.3 KB | Practice Quiz: Test your knowledge: Authenticate and authorize users |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/15 - Practice Quiz Test your knowledge Get help in Linux.md` | 2.8 KB | Practice Quiz: Test your knowledge: Get help in Linux |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/16 - Graded Quiz Module 3 challenge.md` | 5.2 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/17 - Graded Quiz Module 3 challenge.md` | 5.6 KB | Graded Quiz: Module 3 challenge |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/Current file permissions.md` | 0.9 KB | Current file permissions |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/File permissions in Linux exemplar.md` | 204.6 KB | File permissions in Linux |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/Instructions for including Linux commands.md` | 0.9 KB | Instructions for including Linux commands |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-exemplar-add-and-manage-users-with-linux-commands.en.md` | 4.8 KB | Reading: Exemplar: Add and manage users with |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-exemplar-filter-with-grep.en.md` | 4.3 KB | Reading: Exemplar: Filter with grep |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-exemplar-manage-authorization.en.md` | 8.6 KB | Reading: Exemplar: Manage authorization |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-exemplar-manage-files-with-linux-commands.en.md` | 7.7 KB | Reading: Exemplar: Manage files with Linux |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-filter-content-in-linux.en.md` | 6.0 KB | Reading: Filter content in Linux |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-manage-directories-and-files.en.md` | 5.9 KB | Reading: Manage directories and files |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-permission-commands.en.md` | 6.8 KB | Reading: Permission commands |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 3/module-3-responsible-use-of-sudo.en.md` | 7.0 KB | Reading: Responsible use of sudo |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 4/13 - Practice Quiz Test your knowledge SQL queries.md` | 1.7 KB | Practice Quiz: Test your knowledge: SQL queries |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 4/14 - Lab Apply more filters in SQL.md` | 7.1 KB | Lab: Apply more filters in SQL |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 4/16 - Lab Complete a SQL join.md` | 7.1 KB | Lab: Complete a SQL join |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 4/Apply filters to SQL queries.md` | 0.6 KB | Apply filters to SQL queries |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 4/Instructions for including SQL queries.md` | 0.9 KB | Instructions for including SQL queries |
| `Analista SOC/Google Cybersecurity Certification/Tools of the Trade Linux and SQL/Modulo 4/Table formats.md` | 11.8 KB | Table formats |
| `Analista SOC/Google SecOPS/Google_SecOps_Anki_Flashcards.md` | 30.5 KB | Google Security Operations (SIEM) - Flashcards de Estudio & Anki |
| `Analista SOC/Google SecOPS/Google_SecOps_Resumenes.md` | 279.8 KB | Google Security Operations (SecOps) - Resúmenes de Estudio |

---

## 📘 Capa `DOC_STELLAR` (561 manuales únicos de Stellar Cyber en `Markdown_Output/`)

> Todos los manuales de reglas, conectores y arquitectura de Stellar Cyber están indexados y deduplicados en `.rag_index_cache.pkl`.
