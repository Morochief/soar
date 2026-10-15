# Inventario de Skills - Proyecto SOC & OpenXDR

Esta carpeta contiene las **60 skills operativas y técnicas** utilizadas para este proyecto, listas para copiar y usar en cualquier otra computadora.

## Cómo instalarlas en otra PC:
Para que Antigravity / Claude / VS Code reconozca todas las skills en otra computadora:
1. Copia la carpeta `SKILLS_PROYECTO_SOC` (o descomprime `SKILLS_SOC.zip`).
2. Pega su contenido dentro de la carpeta `.agents/skills/` o `.agent/skills/` en la raíz de tu proyecto en la otra máquina.

---

## Índice de Skills Incluidas (60 Skills)

### 1. Operación SOC, Guardias & Stellar Cyber
- **`analyze_stellar_alert`**: Triaje forense estructurado en 4 fases para Stellar Cyber/Interflow.
- **`stellar-soc-triage`**: Procedimiento formal de triaje en 7 etapas para alertas en consola Stellar.
- **`stellar-soc-playbooks`**: Playbooks de respuesta a incidentes (Ransomware, Brute Force, Exfiltration, etc.).
- **`analyze_cortex_alert`**: Análisis express y plantillas de resolución de Palo Alto Cortex XDR.
- **`soc-bitacora`**: Generador de registro de 18 columnas para la Bitácora de Turno (TSV 1-clic).
- **`soc-incidencias`**: Formulario oficial FL-THN-POS-01 Rev. 03 (40 columnas TSV).
- **`soc_shift_handover`**: Reporte resumido de entrega de guardia para WhatsApp y relevo de turno.
- **`update_soc_memory`**: Actualización de patrones de falsos positivos en `SOC_GEM_v2.md`.
- **`human_writer`**: Filtro de redacción profesional, humana y directa para reportes.

### 2. Concilio & Enjambre Multi-Agente
- **`soc-council`**: Debate tripartito en paralelo (Red Team, Blue Team, Threat Intel) para casos ambiguos.
- **`soc_swarm_response`**: Despliegue enjambre en paralelo para investigar IoCs en SO, Stellar y CTI simultáneamente.
- **`google_cyber_transcriber`**: Procesamiento y formato estructurado para guías y apuntes Google Cybersecurity.
- **`graphify`**: Generación de grafos de conocimiento y arquitectura de repositorios.

### 3. Análisis Forense, Red & Malware
- **`wireshark-analysis`**: Inspección y análisis forense de paquetes y capturas PCAP.
- **`memory-forensics`**: Análisis forense de volcados de memoria RAM.
- **`malware-analyst`**: Triaje y análisis de comportamiento de malware y binarios sospechosos.
- **`firmware-analyst`**: Análisis de seguridad y reversing en firmware embebido.

### 4. Inteligencia de Amenazas (CTI) & Reconocimiento
- **`shodan-reconnaissance`**: Reconocimiento de servicios e infraestructura expuesta con Shodan.
- **`threat-mitigation-mapping`**: Mapeo de técnicas adversarias a controles defensivos MITRE ATT&CK.
- **`threat-modeling-expert`**: Modelado de amenazas y superficies de ataque.
- **`deep-research`**: Investigación profunda estructurada de indicadores y amenazas.

### 5. Respuesta a Incidentes & Hardening
- **`incident-responder`**: Flujo general de respuesta y contención de incidentes.
- **`incident-response-incident-response`**: Flujo detallado de gestión de incidentes.
- **`incident-response-smart-fix`**: Mitigación rápida y fixes defensivos.
- **`incident-runbook-templates`**: Plantillas estandarizadas de runbooks para incidentes.
- **`security-audit`**: Metodología de auditoría de seguridad integral.
- **`security-auditor`**: Evaluación y checklist de auditoría de seguridad.
- **`security-bluebook-builder`**: Creación de manuales defensivos y políticas SOC.
- **`security-scanning-security-hardening`**: Endurecimiento de sistemas, servidores y red.

### 6. Simulación Ofensiva & Vectores de Ataque (Red Team / TTPs)
- **`active-directory-attacks`**: Detección y simulación de ataques en Active Directory / Kerberos.
- **`attack-tree-construction`**: Construcción de árboles de ataque para visualizar vectores de intrusión.
- **`windows-privilege-escalation`**: Técnicas de elevación de privilegios en Windows.
- **`linux-privilege-escalation`**: Técnicas de elevación de privilegios en Linux.
- **`red-team-tactics`**: Tácticas de adversarios y bypass de controles.
- **`red-team-tools`**: Herramientas y utilidades de ataque para validación de defensas.
- **`vulnerability-scanner`**: Escaneo y análisis de vulnerabilidades CVE / NVD.
- **`web-security-testing`**: Pruebas de seguridad web OWASP.
- **`sql-injection-testing`**: Detección y validación de inyecciones SQL.
- **`xss-html-injection`**: Detección de Cross-Site Scripting (XSS).
- **`html-injection-testing`**: Análisis de inyección HTML.
- **`burp-suite-testing`**: Análisis de tráfico HTTP/HTTPS mediante Burp Suite.
- **`burpsuite-project-parser`**: Extracción y análisis de proyectos Burp.
- **`metasploit-framework`**: Uso y detección de módulos Metasploit.
- **`ethical-hacking-methodology`**: Metodología de hacking ético.

### 7. Redes & Conectividad de Infraestructura
- **`cisco-ios-patterns`**: Comandos y patrones de configuración Cisco IOS/IOS-XE.
- **`netmiko-ssh-automation`**: Automatización segura de tareas SSH en switches y firewalls.
- **`network-bgp-diagnostics`**: Diagnóstico de tablas de rutas y adyacencias BGP.
- **`network-config-validation`**: Validación previa al despliegue de configuraciones de red.
- **`network-interface-health`**: Diagnóstico de errores, CRC, drops y descartes de interfaces.
- **`network-101`**: Fundamentos de protocolos de red.
- **`network-engineer`**: Resolución de problemas avanzados de red.
- **`powershell-windows`**: Scripting y telemetría avanzada con PowerShell en Windows.

### 8. Desarrollo, APIs & Automatización SOAR
- **`python-patterns`**: Mejores prácticas y patrones seguros en Python.
- **`python-testing`**: Pruebas unitarias e integración con pytest.
- **`windows-desktop-e2e`**: Pruebas de aplicaciones GUI Windows (PyQt).
- **`api-design`**: Diseño de APIs REST limpias y resilientes.
- **`error-handling`**: Manejo robusto de errores y reintentos.
- **`security-review`**: Revisión de código enfocado en prevención de vulnerabilidades.
- **`security-scan`**: Detección de problemas de configuración de seguridad.
- **`security-bounty-hunter`**: Análisis de bugs y fallas críticas.
