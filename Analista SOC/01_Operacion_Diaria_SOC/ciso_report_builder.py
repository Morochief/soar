import datetime
import json
import os
import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURACION ---
# Tiempos
hoy = datetime.datetime.now(datetime.timezone.utc)
ayer = hoy - datetime.timedelta(days=1)
str_inicio = ayer.strftime("%Y-%m-%dT%H:%M:%S.000")
str_fin = hoy.strftime("%Y-%m-%dT%H:%M:%S.000")

# API Keys y Accesos
NVD_API_KEY = "ce79f233-34e5-4445-a3fd-84a8cd00beb6"
OTX_API_KEY = "b6ec3460ec6ed672422e0e8f22367db162a03428b33e0b67f57276d385f9819c"
SO_IP = "172.17.10.25"
SO_API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

OUTPUT_FILE = "Reporte_Diario_CISO.md"

def fetch_cves():
    print("[+] Extrayendo vulnerabilidades del NVD (Ultimas 24h)...")
    headers = {"User-Agent": "CISO-Report-Builder", "apiKey": NVD_API_KEY}
    vulnerabilidades = []
    
    for severidad in ["CRITICAL", "HIGH"]:
        url = (f"https://services.nvd.nist.gov/rest/json/cves/2.0?"
               f"pubStartDate={str_inicio}&pubEndDate={str_fin}&cvssV3Severity={severidad}")
        
        try:
            resp = requests.get(url, headers=headers, timeout=20)
            if resp.status_code == 200:
                data = resp.json()
                vulnerabilidades.extend(data.get("vulnerabilities", []))
            time.sleep(2)
        except Exception as e:
            print(f"Error NVD ({severidad}): {e}")
            
    return vulnerabilidades

def fetch_otx():
    print("[+] Consultando AlienVault OTX (Ultimas campanas)...")
    headers = {"X-OTX-API-KEY": OTX_API_KEY}
    url = "https://otx.alienvault.com/api/v1/pulses/subscribed?limit=5"
    
    try:
        resp = requests.get(url, headers=headers, timeout=20)
        if resp.status_code == 200:
            return resp.json().get("results", [])
    except Exception as e:
        print(f"Error OTX: {e}")
    return []

def fetch_security_onion():
    print("[+] Consultando telemetria interna (Security Onion / Sophos)...")
    headers = {"Authorization": f"ApiKey {SO_API_KEY}", "Content-Type": "application/json"}
    url = f"https://{SO_IP}:9200/_search"
    
    # Filtramos por las ultimas 24h y exclusivamente datos de Sophos Central
    payload = {
        "size": 5,
        "sort": [{"@timestamp": {"order": "desc"}}],
        "query": {
            "bool": {
                "must": [
                    {"query_string": {"query": "data_stream.dataset:\"sophos_central.event\" OR tags:\"sophos\""}}
                ],
                "filter": [
                    {"range": {"@timestamp": {"gte": "now-24h", "lte": "now"}}}
                ]
            }
        }
    }
    
    try:
        resp = requests.post(url, headers=headers, json=payload, verify=False, timeout=10)
        if resp.status_code == 200:
            return resp.json().get("hits", {}).get("hits", [])
    except Exception as e:
        print(f"Error Security Onion: {e}")
    return []

def generar_reporte(cves, otx_pulses, so_alerts):
    print("[+] Generando documento Markdown...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 🛡️ Reporte Ejecutivo Diario - Centro de Operaciones de Seguridad (SOC)\n\n")
        f.write(f"**Fecha de Generación:** {hoy.strftime('%Y-%m-%d %H:%M UTC')}\n")
        f.write(f"**Período Evaluado:** Últimas 24 Horas\n\n")
        
        f.write("## 1. 📊 Resumen Ejecutivo\n")
        f.write("| Métrica | Valor |\n")
        f.write("|---|---|\n")
        f.write(f"| **Nuevas Vulnerabilidades (Críticas/Altas)** | {len(cves)} |\n")
        f.write(f"| **Nuevas Campañas de Amenazas Activas (OTX)** | {len(otx_pulses)} |\n")
        f.write(f"| **Incidentes de Endpoint / Antivirus (Sophos)** | {len(so_alerts)} |\n\n")
        
        f.write("---\n\n")
        
        f.write("## 2. 🚨 Telemetría Interna (Sophos Central Endpoint)\n")
        if not so_alerts:
            f.write("> ✅ No se registraron incidentes ni alertas de Sophos en las últimas 24 horas.\n\n")
        else:
            for hit in so_alerts:
                src = hit.get("_source", {})
                timestamp = src.get("@timestamp", "N/A")
                host = src.get("agent", {}).get("name", "Desconocido")
                
                # Intentar sacar la accion de sophos_central o event
                accion = src.get("event", {}).get("action", "Evento Desconocido")
                
                f.write(f"- **[{timestamp}]** - Equipo: `{host}` - Acción: `{accion}`\n")
        f.write("\n---\n\n")
        
        f.write("## 3. 🌐 Inteligencia de Amenazas Globales (Top 5)\n")
        if not otx_pulses:
            f.write("Sin datos recientes de OTX.\n\n")
        else:
            for pulse in otx_pulses:
                nombre = pulse.get("name", "N/A")
                iocs = pulse.get("indicator_count", len(pulse.get("indicators", [])))
                f.write(f"- **{nombre}** ({iocs} Indicadores de Compromiso detectados)\n")
        f.write("\n---\n\n")
        
        f.write("## 4. 🔓 Avisos de Ciberseguridad NIST (Nuevos CVEs Críticos)\n")
        if not cves:
            f.write("No se publicaron CVEs de alta criticidad en las últimas 24 horas.\n\n")
        else:
            # Mostrar solo los primeros 5 para no saturar al CISO
            for item in cves[:5]:
                cve_id = item.get("cve", {}).get("id", "N/A")
                f.write(f"- **[{cve_id}](https://nvd.nist.gov/vuln/detail/{cve_id})** - Requiere revisión de parcheo.\n")
            if len(cves) > 5:
                f.write(f"\n*(...y {len(cves) - 5} vulnerabilidades adicionales. Consultar al SOC para el reporte completo).* \n\n")
        
        f.write("---\n\n")
        f.write("*Reporte auto-generado por el sistema de automatización Python-Elasticsearch-API del SOC.*\n")

def main():
    print("=======================================")
    print(" INICIANDO CONSTRUCCION DE REPORTE CISO")
    print("=======================================")
    cves = fetch_cves()
    otx = fetch_otx()
    so = fetch_security_onion()
    
    generar_reporte(cves, otx, so)
    print(f"¡Proceso Terminado! Reporte guardado como: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
