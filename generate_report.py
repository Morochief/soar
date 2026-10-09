import csv
import json
import re

cases = []
with open('XDR_Cases_2026-10-02T10_39_42.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        cases.append(row)

total = len(cases)
severities = {}
for c in cases:
    s = c.get('Severity', 'Unknown')
    severities[s] = severities.get(s, 0) + 1

# Classify cases into themes
categories = {
    'bypass_wdac': [],
    'bypass_firewall': [],
    'lolbin_dev': [],
    'network_anomalies': [],
    'malware_bioc_fp': [],
    'policy_violations': [],
    'soc_intel': [],
    'other_resolved': []
}

for c in cases:
    name = c.get('Case Name', '')
    desc = c.get('Case Description', '')
    res = c.get('Resolution Comment', '')
    text = (name + ' ' + desc + ' ' + res).lower()
    
    if 'ci policy' in text or 'vulnerable driver' in text or 'aggregatorhost' in text or '347087060' in text:
        categories['bypass_wdac'].append(c)
    elif 'firewall bypass' in text or 'cameraconfigurationtool' in text or '1993920586' in text:
        categories['bypass_firewall'].append(c)
    elif 'tor connection' in text or 'tweetfeed' in text or 'antigravity' in text:
        categories['soc_intel'].append(c)
    elif 'counter-strike' in text or 'minecraft' in text or 'recreativo' in text or 'pup' in text:
        categories['policy_violations'].append(c)
    elif 'power bi' in text or 'pbidesktop' in text or 'ivms' in text or 'webrtc' in text or 'failed connection' in text or 'large upload' in text or 'nmap' in text or 'ssh' in text:
        categories['network_anomalies'].append(c)
    elif 'powershell' in text or 'lolbin' in text or 'curl' in text or 'winget' in text or 'rundll32' in text or 'vscode' in text or 'dotnet' in text or 'node' in text:
        categories['lolbin_dev'].append(c)
    elif 'cdvap' in text or 'storedesktopextension' in text or 'brservice' in text or 'local analysis malware' in text or 'wildfire malware' in text or '0_.dll' in text or 'reader_es' in text:
        categories['malware_bioc_fp'].append(c)
    else:
        categories['other_resolved'].append(c)

detailed = [c for c in cases if len(c.get('Resolution Comment', '')) > 40 and 'caso ya resuelto' not in c.get('Resolution Comment', '').lower() and 'caso resuelto y escalado' not in c.get('Resolution Comment', '').lower()]

print("Classification summary:")
for k, v in categories.items():
    print(f"  {k}: {len(v)}")

# Generate Comprehensive Report
report = []
report.append("# Informe Maestro Consolidado de Incidentes y Casos: Palo Alto Cortex XDR")
report.append("**Área:** Centro de Operaciones de Seguridad (SOC) — Technoma S.A.E.C.A.")
report.append("**Elaborado por:** Analista SOC (Kevin Moraes)")
report.append("**Destinatario:** SOC Manager / Jefatura de Ciberseguridad")
report.append(f"**Fecha de Emisión:** Octubre 2026 | **Total de Casos Auditados:** {total} Casos")
report.append("**Estado:** 100% Resueltos / Documentados\n")
report.append("---\n")

report.append("## 1. Resumen Ejecutivo y Estadísticas Globales\n")
report.append(f"El presente informe consolida el universo total de **{total} casos** registrados y gestionados en la plataforma **Palo Alto Networks Cortex XDR** dentro del inquilino corporativo de Technoma. Cada uno de los incidentes fue sometido al flujo formal de triaje, enriquecimiento de telemetría (XQL/BIOC/AMSI), validación de causalidad y asignación de veredicto técnico.\n")

report.append("### Distribución por Severidad:")
report.append("| Nivel de Severidad | Total de Casos | Porcentaje | Tratamiento SOC |")
report.append("| :--- | :---: | :---: | :--- |")
for sev in ['High', 'Medium', 'Low']:
    cnt = severities.get(sev, 0)
    pct = (cnt / total) * 100
    trat = "Prioridad 1 - Triaje inmediato / Análisis de proceso y bloqueo" if sev == 'High' else ("Prioridad 2 - Correlación de linaje y actividad de usuario" if sev == 'Medium' else "Prioridad 3 - Análisis estadístico de red / Verificación de falsos positivos")
    report.append(f"| **{sev}** | {cnt} | {pct:.1f}% | {trat} |")

report.append("\n### Distribución Temática de los Incidentes:")
report.append(f"* **Desvíos de Red y Conexiones (Anomalías de Tráfico / Escaneos / Cargas Masivas):** {len(categories['network_anomalies'])} casos")
report.append(f"* **Ejecución de Herramientas del Sistema (LOLBINs / Scripts PowerShell / Herramientas Dev):** {len(categories['lolbin_dev'])} casos")
report.append(f"* **Falsos Positivos de Malware y Detecciones Heurísticas (BIOC / WildFire / Local Analysis):** {len(categories['malware_bioc_fp'])} casos")
report.append(f"* **Técnicas de Evasión de Defensas (Políticas CI WDAC y Bypass de Firewall):** {len(categories['bypass_wdac']) + len(categories['bypass_firewall'])} casos")
report.append(f"* **Uso de Software No Autorizado / Violaciones de Política de TI (PUP / Juegos):** {len(categories['policy_violations'])} casos")
report.append(f"* **Actividades Operativas del SOC / Enriquecimiento CTI:** {len(categories['soc_intel'])} casos")
report.append(f"* **Incidentes Operativos Menores / Casos de Cierre Sistémico:** {len(categories['other_resolved'])} casos\n")

report.append("---\n")
report.append("## 2. Metodología Estandarizada de Investigación de Casos en Cortex XDR\n")
report.append("Para responder con rigurosidad a cada alerta generada por los motores de Cortex XDR (Analytics, BIOC, Behavioral Threat Protection, WildFire y Local Analysis), el SOC aplica una metodología estructurada en 5 fases:\n")
report.append("1. **Fase 1 - Extracción de Telemetría (JSON & XQL):**  ")
report.append("   Inspección exhaustiva de los metadatos brutos del caso: `action` (Blocked/Detected), `causality_id`, `actor_process_id`, marcas temporales, IP de origen/destino y puertos.\n")
report.append("2. **Fase 2 - Análisis de Linaje y Causalidad de Procesos (Process Tree):**  ")
report.append("   Reconstrucción del árbol de ejecución. Se analiza el Proceso Padre (PPID) y el Proceso Actor para verificar si el comando fue ejecutado interactivamente por el usuario, por un servicio del sistema (`SYSTEM`) o por una tarea programada. Se valida la firma digital (*Digital Signature* y *Signer Vendor*).\n")
report.append("3. **Fase 3 - Análisis Forense de Comandos y Payloads (AMSI / Script Block Logging):**  ")
report.append("   Decodificación de cadenas en Base64, análisis de argumentos en línea de comando, verificación de rutas de acceso (carpetas protegidas de sistema vs. `%TEMP%` / `%APPDATA%`) e inspección de scripts `.ps1`, `.bat` o `.vbs`.\n")
report.append("4. **Fase 4 - Enriquecimiento y Correlación de Inteligencia de Amenazas (CTI / WildFire):**  ")
report.append("   Cruce de hashes SHA256 contra WildFire y VirusTotal. Verificación de reputación de dominios e IPs externas. En caso de alertas de red, se comprueba si el tráfico responde a protocolos estándar de aplicaciones legítimas (WebRTC, STUN, APIs públicas de Microsoft/Google) o si muestra características de C2.\n")
report.append("5. **Fase 5 - Determinación del Veredicto, Remediación y Documentación:**  ")
report.append("   Asignación del veredicto formal (*Falso Positivo*, *Comportamiento Benigno*, *Violación de Políticas*, *Verdadero Positivo Mitigado*). En caso de falsos positivos recurrentes, se documenta la recomendación de afinamiento de regla (*Tuning / Exclusion rule*) para optimizar el EDR.\n")

report.append("---\n")
report.append("## 3. Análisis en Profundidad por Familias de Incidentes y Casos Clave\n")

# Section 3.1
report.append("### 3.1 Familia: Evasión de Medidas de Seguridad — Políticas CI de Windows (WDAC)")
report.append("**Técnica MITRE:** `T1562.004 - Impair Defenses: Disable or Modify System Firewall` / `T1562 - Impair Defenses`  ")
report.append("**Módulo Cortex:** `Protection Against Security Measures Bypass Techniques` | **Severidad:** High  ")
report.append("**Casos Representativos:** Case #412, Alerta 347087060 (múltiples hosts: `nb-jtorales`, etc.)\n")
report.append("* **Descripción del Evento:** Cortex XDR alertó de forma repetida por la modificación de archivos de política de integridad de código en la ruta `C:\\windows\\system32\\codeintegrity\\cipolicies\\staged\\{8f9cb695-5d48-48d6-a329-7202b44607e3}.cip`.")
report.append("* **Pasos de Investigación Seguidos:**")
report.append("  1. Extracción de telemetría de endpoint identificando el binario responsable: `AggregatorHost.exe` invocado por `svchost.exe`.")
report.append("  2. Verificación de la firma digital: binario firmado oficialmente por **Microsoft Windows Component Publisher**, ejecutándose bajo privilegios de `NT AUTHORITY\\SYSTEM`.")
report.append("  3. Identificación del GUID `{8f9cb695-5d48-48d6-a329-7202b44607e3}`: Se corroboró en la documentación oficial de Microsoft que corresponde a la lista de bloqueo de controladores vulnerables (*Vulnerable Driver Blocklist*) de Windows Defender Application Control (WDAC).")
report.append("  4. Explicación del comportamiento del EDR: Cortex XDR tiene una regla estricta para prevenir técnicas de inyección de drivers maliciosos (*BYOVD - Bring Your Own Vulnerable Driver*), por lo que bloquea preventivamente cualquier escritura en dicha carpeta, interceptando una actualización rutinaria de parches de Windows.")
report.append("* **Veredicto Oficial:** **Falso Positivo (False Positive / Benign System Activity)**.")
report.append("* **Resolución Técnica:** Se descartó cualquier inyección o técnica LotL. La actividad fue legítima del sistema operativo.\n")

# Section 3.2
report.append("### 3.2 Familia: Evasión de Medidas de Seguridad — Modificación de Firewall por Software Local")
report.append("**Técnica MITRE:** `T1562.004 - Impair Defenses: Modify System Firewall`  ")
report.append("**Módulo Cortex:** `Protection Against Security Measures Bypass Techniques - 1993920586` | **Severidad:** High  ")
report.append("**Host Afectado:** `NB-ABOGADO` (Usuario: `axelbogado`)\n")
report.append("* **Descripción del Evento:** Alerta por intento de evasión de firewall (*firewall bypass attempt*) mediante ejecución de PowerShell.")
report.append("* **Pasos de Investigación Seguidos:**")
report.append("  1. Reconstrucción del árbol de procesos: `CameraConfigurationTool.exe` (Motorola Solutions) ➔ `cmd.exe` ➔ `powershell.exe -Verb runAs -WindowStyle hidden` ➔ `svchost.exe (Appinfo)` ➔ `execute.bat` ➔ `powershell.exe New-NetFirewallRule`.")
report.append("  2. Análisis del script bloqueado: El comando intentó ejecutar `New-NetFirewallRule -DisplayName 'Camera Configuration Tool' -Direction Inbound -Action Allow -Protocol UDP -Program '...CameraConfigurationTool.exe'` para permitir descubrimiento de cámaras CCTV por UDP broadcast.")
report.append("  3. Validación de autenticidad: El ejecutable padre está firmado y verificado por **Motorola Solutions, Inc.** con veredicto WildFire Benign.")
report.append("  4. Causa del bloqueo: Cortex detectó la técnica de ejecutar un script temporal desde `%TEMP%` con ventana oculta y elevación para modificar reglas de red, disparando la regla preventiva de evasión.")
report.append("* **Veredicto Oficial:** **Falso Positivo / Actividad Benigna de Software Autorizado (Benign Positive)**.")
report.append("* **Resolución Técnica:** Se confirmó que la regla está restringida al propio ejecutable de Motorola y no expone el sistema. No hay compromiso.\n")

# Section 3.3
report.append("### 3.3 Familia: Ejecución de LOLBINs en Entornos de Desarrollo y Automatización")
report.append("**Técnica MITRE:** `T1059.001 - PowerShell` / `T1105 - Ingress Tool Transfer` / `T1218 - System Binary Proxy Execution`  ")
report.append("**Módulos Cortex:** `XDR Analytics BIOC`, `EDR Windows C2 Analytics`, `LOLBIN Execution Analytics` | **Severidad:** Medium  ")
report.append("**Hosts Afectados:** `NB-FBENEGAS`, `NB-MGAMARRA`, `NB-AOLIVER`, `NB-RAULM`, `NB-OSCANDIA`\n")
report.append("* **Casos Analizados:**")
report.append("  1. **Winget-AutoUpdate (WAU) en `NB-FBENEGAS`:** Conhost generó un subproceso de PowerShell ejecutando `WAU-Notify.ps1` y modificó claves `RunOnce` con `index.exe` para instalar drivers de Lenovo/Motorola. *Investigación:* Se confirmó que corresponde al software oficial de actualización desatendida de parches bajo contexto `SYSTEM`. Veredicto: **Falso Positivo / Mantenimiento Autorizado**.")
report.append("  2. **Entornos de Desarrollo VS Code (`Code.exe`) / .NET / Node.js:** Ejecución de `powershell.exe` y `curl.exe` contactando dominios como `ci.dot.net`, `gastos-personales-zpar.onrender.com`, `filmagic-demo.web.app` y `itti-digital.app.n8n.cloud`. *Investigación:* Se comprobó que eran desarrolladores de software ejecutando extensiones oficiales (`ms-dotnettools`, OpenAI Codex, npm scripts) realizando pruebas de API en entornos de staging. Veredicto: **Falso Positivo Contextual / Actividad Legítima de Desarrollo**.")
report.append("  3. **Validación de Certificados con `rundll32.exe`:** Conexión hacia `ocsp1.uanataca.com`. *Investigación:* El usuario abrió un documento firmado digitalmente; Windows utilizó Rundll32 para consultar el protocolo OCSP del prestador de certificación Uanataca. Veredicto: **Actividad Benigna del Sistema**.")

# Section 3.4
report.append("### 3.4 Familia: Anomalías de Red, Escaneos y Transferencias Masivas")
report.append("**Técnica MITRE:** `T1041 - Exfiltration Over C2 Channel` / `T1048 - Exfiltration Over Alternative Protocol` / `T1046 - Network Service Discovery`  ")
report.append("**Módulos Cortex:** `XDR Analytics (Network/NDR Insights)` | **Severidad:** Low - Medium\n")
report.append("* **Casos Analizados:**")
report.append("  1. **Large Upload (HTTPS) en `NB-JTORALES` (381.5 MB):** Carga masiva hacia `wabi-south-central-us-c-primary-redirect.analysis.windows.net`. *Investigación:* Se identificó que el proceso fue `PBIDesktop.exe` publicando el informe comercial `PETROCHACO - Modelo Comercial y Operativo V2(1).pbix` en los servidores oficiales de Microsoft Power BI. Veredicto: **Actividad Benigna Operativa**.")
report.append("  2. **Large Upload (SMTP) en `NB-JRIVAROLA` (60.2 MB):** Envío anómalo por correo hacia `smtp.gmail.com`. *Investigación:* Usuario operativo despachando correos con archivos adjuntos pesados en su jornada laboral. Veredicto: **Actividad Benigna**.")
report.append("  3. **Failed Connections masivas (`iVMS-4200` en `NB-GRIVEROS`):** 96 intentos TCP fallidos al puerto 8000. *Investigación:* El software oficial de videovigilancia Hikvision iVMS-4200 realizaba el chequeo rutinario de estado de cámaras IP offline en la red local. Veredicto: **Falso Positivo Operativo**.")
report.append("  4. **Failed Connections por WebRTC (`msedge.exe` en `NB-CGAUTO`):** 42 conexiones UDP fallidas hacia IPs privadas. *Investigación:* Comportamiento nativo de sondeo STUN/ICE del navegador Microsoft Edge para sesiones de videollamadas. Veredicto: **Falso Positivo**.")
report.append("  5. **Suspicious Port Scan en `NB-ALBERTMUNOZ`:** Ejecución de `nmap.exe -T4 -A -v 192.168.1.0/24`. *Investigación:* Tareas autorizadas de relevamiento de infraestructura interna por parte del equipo técnico de Technoma. Veredicto: **Actividad Administrativa Autorizada**.")

# Section 3.5
report.append("### 3.5 Familia: Falsos Positivos de Malware y Empaquetadores Heurísticos")
report.append("**Técnica MITRE:** `T1204 - User Execution` / `T1055 - Process Injection`  ")
report.append("**Módulos Cortex:** `WildFire Malware`, `Local Analysis Malware`, `BIOC` | **Severidad:** High - Medium\n")
report.append("* **Casos Analizados:**")
report.append("  1. **Herramienta Interna `CDVAP.exe` en `NB-ALOVERA`:** Cortex alertó por WildFire Malware y BIOC. *Investigación:* Se auditó el software ubicado en `C:\\CDVAP-Technoma\\` (versiones v1.9.0 y v1.9.1). Es una aplicación interna desarrollada por Technoma, empaquetada con PyInstaller. La alta entropía de empaquetado y la falta de reputación en la nube pública dispararon la heurística estática de Cortex. Veredicto: **Falso Positivo (Software Propietario)**.")
report.append("  2. **Falso Positivo en `StoreDesktopExtension.exe`:** Proceso oficial de Microsoft Store dentro de `C:\\Program Files\\WindowsApps\\` bloqueado por el motor local estático. Veredicto: **Falso Positivo de Plataforma**.")
report.append("  3. **Inyección Heurística en `BrService.exe`:** Alerta de *Process Hollowing*. *Investigación:* Servicio legítimo del sistema interactuando con memoria virtual en operaciones normales de drivers. Veredicto: **Falso Positivo**.")

# Section 3.6
report.append("### 3.6 Familia: Violaciones de Políticas de TI y Software No Autorizado (PUP)")
report.append("**Técnica MITRE:** `T1204 - User Execution` | **Módulo:** `WildFire Malware` / `Agent BIOC` | **Severidad:** Medium - Low\n")
report.append("* **Caso 1: `cd-client-4_33_4-en.exe` (Counter-Strike 1.6):** Archivo ubicado en `C:\\Program Files (x86)\\Counter-Strike 1.6\\C-D\\`. *Investigación:* Cortex bloqueó legítimamente un componente de terceros (anti-cheat de videojuegos) descargado por un empleado. *Veredicto:* **Bloqueo Legítimo / Violación de Políticas de Seguridad de TI (PUP)**. Se notificó al área correspondiente.")
report.append("* **Caso 2: Instalación de `Minecraft`:** Detección de múltiples alertas MITRE por instalación de software recreativo en equipo corporativo. *Veredicto:* **Violación de Políticas de Uso Aceptable**.")

# Section 3.7
report.append("### 3.7 Familia: Tareas Operativas del SOC y Enriquecimiento de Inteligencia")
report.append("**Caso Representativo:** `Tor Connection - 88640603` (Fetching a file from a TOR domain) | **Severidad:** High\n")
report.append("* **Descripción del Evento:** Alerta de conexión hacia un dominio Tor generada por el proceso `Antigravity IDE.exe` ejecutando un comando de PowerShell con Python.")
report.append("* **Investigación:** Se comprobó que el comando ejecutaba una consulta HTTP a la API pública de Threat Intelligence `https://api.tweetfeed.live/v1/ioc/<onion_address>` para verificar la reputación de un IoC de ransomware. Cortex detectó la cadena de texto `.onion` dentro de los argumentos y asumió erróneamente una conexión a la red Tor. El host nunca estableció túneles SOCKS ni contactó nodos Tor.")
report.append("* **Veredicto Oficial:** **Falso Positivo / Enriquecimiento CTI del SOC**.")

report.append("\n---\n")
report.append("## 4. Tabla Maestra de Casos Significativos Analizados y Cerrados\n")
report.append("| Fecha | Severidad | Nombre del Caso | Host / Usuario Involucrado | Veredicto SOC | Justificación / Causa Raíz Resumida |")
report.append("| :--- | :---: | :--- | :--- | :---: | :--- |")

for c in detailed[:35]:
    date = c.get('Last Updated', '').split(' 2026')[0] + ' 2026'
    sev = c.get('Severity', '')
    name = c.get('Case Name', '')[:38]
    desc = c.get('Case Description', '')
    res = c.get('Resolution Comment', '')
    
    # Extract host if present
    m_host = re.search(r'(nb-[a-z0-9_-]+|NB-[A-Z0-9_-]+)', desc + ' ' + res)
    host = m_host.group(1) if m_host else "Varios Hosts"
    
    # Determine verdict label
    res_l = res.lower()
    if 'falso positivo' in res_l or 'false positive' in res_l:
        verdict = "Falso Positivo"
    elif 'bloqueo legítimo' in res_l or 'violación' in res_l or 'recreativo' in res_l:
        verdict = "Violación Política TI"
    elif 'legítim' in res_l or 'benign' in res_l or 'autorizad' in res_l:
        verdict = "Actividad Benigna"
    else:
        verdict = "Resuelto / Descartado"
        
    res_short = res.replace('\n', ' ').strip()
    if len(res_short) > 110:
        res_short = res_short[:107] + "..."
        
    report.append(f"| {date} | **{sev}** | {name} | `{host}` | **{verdict}** | {res_short} |")

report.append("\n---\n")
report.append("## 5. Recomendaciones de Afinamiento (Tuning) para la Consola Cortex XDR\n")
report.append("A partir del análisis sistemático de los 206 casos, se identifican oportunidades clave de optimización en las políticas del agente de Palo Alto para reducir la fatiga de alertas del SOC:")
report.append("1. **Exclusión de Actualizaciones WDAC:** Crear una regla de excepción en el módulo *Protection Against Security Measures Bypass Techniques* para el proceso firmado `AggregatorHost.exe` actuando sobre la ruta `C:\\windows\\system32\\codeintegrity\\cipolicies\\staged\\`. Esto eliminará decenas de falsas alarmas de severidad High recurrentes en las actualizaciones de Windows.")
report.append("2. **Lista Blanca de Binarios Internos Compilados:** Firmar digitalmente los ejecutables internos desarrollados por Technoma (como `CDVAP.exe`) con un certificado corporativo de confianza o agregarlos a la lista de *Hash Exceptions* de WildFire para evitar bloqueos por heurística de PyInstaller.")
report.append("3. **Afinamiento de Detección de Tráfico WebRTC y CCTV:** Ajustar el umbral analítico de *Failed Connections* para puertos UDP efímeros de navegadores (`msedge.exe`) y puertos de videovigilancia interna (`8000` de Hikvision iVMS) hacia subredes de confianza.")
report.append("4. **Reglas para Ambientes de Desarrollo (VS Code / Winget):** Excluir del módulo LOLBIN C2 Analytics las llamadas de `powershell.exe` y `curl.exe` cuando el proceso padre sea `Code.exe` (Visual Studio Code) o `winget.exe`, bajo rutas de extensiones preaprobadas.")

final_md = "\n".join(report)

with open('Analista SOC/Reportes/Reporte_Consolidado_Cortex_XDR_Technoma.md', 'w', encoding='utf-8') as f:
    f.write(final_md)

print("Report successfully generated!")
