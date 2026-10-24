import sys, os, json, requests, urllib3
urllib3.disable_warnings()

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(r'c:\Users\kevinmoraes\Desktop\SOC\soar')
import sync_cortex_cases

HOST = 'technoma.stellarcyber.cloud'
headers = sync_cortex_cases.get_headers()

# Dictámenes técnicos caso por caso
JUSTIFICACIONES = {
    "18168": "Invocación de herramientas de build y comandos locales desde asistente de código/IDE en NB-KMORAEZ. Falso positivo validado.",
    "18169": "Actividad legítima de desarrollo y ejecución de scripts locales vía Node/Wscript en NB-MANUELALM interactuando con repositorio externo reconocido. Sin payload ni anomalías en subprocesos. Resuelto como Falso Positivo.",
    "18170": "Ejecución iniciada por entorno de desarrollo / asistente de código (Codex CLI) en NB-GVERA para comandos de compilación local. Mismo patrón verificado en ticket #18168. Resuelto como Falso Positivo.",
    "18171": "Pruebas de investigación y validación de Threat Intelligence realizadas desde estación de analista SOC (NB-KMORAEZ). No se evidenció compromiso ni persistencia. Resuelto como Falso Positivo.",
    "18172": "Aplicación legítima de productividad personal de código abierto (Super Productivity) en NB-RALEMAN sincronizando notas y tareas con la API de Dropbox del usuario. Tráfico benigno validado por SOC.",
    "18173": "Tareas administrativas de gestión interna y validación de red local entre subredes de soporte/IT desde NB-ODACOSTA. Tráfico operacional legítimo sin propagación maliciosa.",
    "18174": "Petición HTTP legítima de desarrollo/soporte hacia dominio de partner local (www.mastertech.com.py) desde NB-EORLANDINI mediante curl.exe. Tráfico benigno validado.",
    "18175": "Invocación de herramientas de build y scripting automatizado desde IDE / AI CLI local de desarrollo en NB-GVERA. Resuelto como Falso Positivo.",
    "18176": "Descarga de paquetes o artefactos de compilación usando ejecutables nativos desde NB-EORLANDINI hacia host externo benigno de desarrollo. Resuelto como Falso Positivo.",
    "18177": "Sincronización normal de telemetría de proyecto y dependencias de la extensión Google Cloud Code / Antigravity IDE desde NB-KMORAEZ contra infraestructura oficial de Google Cloud. Tráfico benigno validado.",
    "18178": "Sincronización y resguardo de copias de seguridad de archivos mediante el cliente oficial de Proton Drive (fra-storage.proton.me) desde NB-FMORA. Actividad administrativa autorizada.",
    "18179": "Falso positivo originado por concatenación de variables en scripts internos de soporte PowerShell en NB-JTORALES. Verificado libre de ofuscación maliciosa o evasión de defensas.",
    "18180": "Compilación local y empaquetado de utilidad interna de Technoma en NB-GMARTINEZ no indexada previamente en WildFire. Hash verificado y seguro. Resuelto como Falso Positivo.",
    "18181": "Terminal en segundo plano ejecutada por Visual Studio Code / terminal integrado en modo sin cabecera (--headless) en NB-FBENEGAS. Comportamiento estándar de entornos de desarrollo.",
    "18182": "Uso estándar del servicio BITS de Windows para actualización y descarga de paquetes del sistema operativo en NB-EDVELAZQUEZ. Sin anomalías de persistencia.",
    "18183": "Proceso secundario de terminal de desarrollo generado por entorno IDE local en modo headless en NB-RBARRETO. Resuelto como Falso Positivo.",
    "18184": "Instalación/actualización legítima del reproductor multimedia VLC mediante el gestor de paquetes de Windows (winget) en NB-NOC2 conectado al mirror oficial de la Universidad UFPR. Tráfico benigno.",
    "18185": "Descarga legítima de modelos/pesos de Inteligencia Artificial y datasets desde el repositorio oficial de Hugging Face desde NB-EORLANDINI. Tráfico benigno.",
    "18186": "Despliegue de software verificado mediante winget desde el mirror oficial universitario de VideoLAN en NB-FBENEGAS. Tráfico benigno.",
    "18187": "Tarea de automatización y terminal en segundo plano originada por herramientas de desarrollo local en NB-IMAYOR. Resuelto como Falso Positivo.",
    "18188": "Terminal integrado headless de editor de código en NB-FBENEGAS. Resuelto como Falso Positivo.",
    "18189": "Sondeo y verificación de conectividad interna ejecutado por personal de SOC (NB-JTORALES) en monitoreo rutinario de endpoints. Tráfico administrativo benigno.",
    "18190": "Actividad legítima de desarrollo y documentación local desde IDE Antigravity / Python / PowerShell en NB-KMORAEZ hacia Bitacora_Personal_Casos_SOC.md. Falso positivo validado."
}

with open(r'c:\Users\kevinmoraes\Desktop\SOC\soar\cortex_cases_analysis.json', 'r', encoding='utf-8') as f:
    cases = json.load(f)

print(f"[*] Insertando comentarios forenses en {len(cases)} casos...")

success = 0
for c in cases:
    t_id = str(c['ticket_id'])
    hex_id = c['hex_id']
    comment_text = JUSTIFICACIONES.get(t_id, "Actividad operacional y benigna validada por SOC Technoma tras análisis forense.")
    
    url = f"https://{HOST}/connect/api/v1/cases/{hex_id}/comments"
    payload = {"comment": comment_text}
    
    r = requests.post(url, headers=headers, json=payload, verify=False, timeout=15)
    if r.status_code == 200:
        print(f"  [+] Ticket #{t_id} (ID: {hex_id}): Comentario insertado.")
        success += 1
    else:
        print(f"  [-] Ticket #{t_id} ERROR {r.status_code}: {r.text[:120]}")

print(f"\n[✔] Finalizado: {success}/{len(cases)} comentarios agregados con éxito.")
