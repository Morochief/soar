# 🗺️ Índice Curado de Documentación SOC

Este documento es un mapa estructurado de los archivos Markdown más críticos y operativos del workspace. Te ayudará a distinguir entre las herramientas diarias del analista y la documentación masiva de referencia.

---

## 🛡️ Núcleo Operativo (`02_Base_de_Conocimiento\`)
Esta carpeta es el "cerebro" del SOC. Contiene los archivos que dictan las decisiones diarias, inventarios de la infraestructura y guías de investigación. **Son los archivos que más utilizamos y actualizamos.**

*   `SOC_GEM_v2.md`: **[CRÍTICO]** La Memoria Institucional. Aquí documentamos todos los Falsos Positivos validados, deuda técnica (ej. HealthMailboxes), IPs críticas y comportamiento esperado de la red de Technoma/CajaAnde.
*   `plantillas_cierre_soc.md`: **[CRÍTICO]** Respuestas estandarizadas para cerrar tickets y falsos positivos en Stellar Cyber.
*   `ad_users_inventory.md`: Volcado completo de todos los usuarios válidos del Active Directory (`technoma.local`). Útil para validar ataques de fuerza bruta.
*   `stellar_alerts.md`: Diccionario táctico de las reglas analíticas de Stellar Cyber, su mapeo MITRE ATT&CK y campos clave.
*   `SMB_Rosetta_Stone.md`: Tabla de traducción de códigos de comando SMB. Esencial para diseccionar ciberataques en la red interna o tráfico lateral.
*   `Playbook_Sophos_AutoUpdate.md`: Procedimiento maestro para resolver problemas específicos del servicio de actualización de Sophos (ej. Error `80041f00`).
*   `Sophos_Logs_Reference.md`: Referencia técnica de dónde buscar y qué significan los logs locales de Sophos EDR.
*   `cve_criticos.md` / `cve_reporte_completo.md`: Reportes periódicos de vulnerabilidades críticas en la infraestructura.
*   `otx_amenazas_recientes.md`: Feeds de inteligencia de amenazas e IoCs de AlienVault OTX.
*   `stellar_cyber_api_reference.md` / `prompt_stellar_python.md`: Guías técnicas para automatizaciones e interacción programática con el SIEM.
*   `securityonion-docs.md` / `securityonion-docs-ES.md`: Manuales operativos para consultas en Security Onion.
*   `SAMR.md`: Documentación sobre consultas SAMR (Security Account Manager Remote) en contexto de reconocimiento de red.

---

## 📂 Directorio Raíz (`\`)
Contiene playbooks históricos o archivos de control general.

*   `Playbook_Remediacion_Sophos_WMI.md`: Procedimiento inicial de remediación mediante la purga del repositorio WMI (utilizado previamente).
*   `AGENTS.md` (oculto en `.agents`): Contiene las reglas maestras de comportamiento de la IA (formato de entrega de turno, obligación de buscar en la memoria).

---

## 🗃️ Archivo Histórico de Casos (`Casos\`)
Aquí se almacenan estructuradamente todas las alertas procesadas.
*   Cada subcarpeta tiene el nombre exacto de la alerta.
*   Contiene el archivo `alerta_original.md` (JSON crudo) y nuestro `analisis_soc.md` final.

---

## 📚 Bibliotecas de Referencia Masiva (Solo para consultas)
Archivos generados automáticamente que contienen miles de páginas de documentación técnica original. **No necesitas memorizarlos ni revisarlos manualmente.** La Inteligencia Artificial los consultará silenciosamente de fondo cuando se requiera soporte avanzado.

*   `Stellar Documentacion\Markdown_Output\`: Contiene más de 3000 archivos `.md` raspados del sitio oficial de documentación de Stellar Cyber (ej. `Understanding Tenants.md`, `User Behavior Analytics.md`).
*   `graphify-out\`: Mapa de conocimiento y relaciones de tu repositorio.

---

> **Recomendación:** Si alguna vez dudas de un procedimiento, la "Memoria Institucional" (`SOC_GEM_v2.md`) es tu única fuente de la verdad para clasificar alertas.
