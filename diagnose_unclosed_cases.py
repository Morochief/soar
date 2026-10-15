import os
import sys
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_stellar_config():
    candidates = [
        os.path.join(r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar", "config.json"),
        os.path.join(r"c:\Users\kevinmoraes\Documents\soc-env", "config.json"),
        "config.json"
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error reading {p}: {e}")
    return None

def query_open_cases():
    cfg = get_stellar_config()
    if not cfg:
        print("[!] No se encontro config.json")
        return

    host = cfg.get("stellar_host", "172.16.201.20")
    api_key = cfg.get("stellar_api_key", "")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print(f"[*] Consultando Stellar Cyber ({host}) para casos abiertos...")
    # Try the cases endpoint used by command_center.py
    # In command_center.py, let's see how cases are fetched:
    url = f"https://{host}/connect/api/v1/cases?status=Open&limit=25"
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=15)
        print(f"HTTP Status: {r.status_code}")
        if r.status_code != 200:
            print(f"Response: {r.text[:500]}")
            return
        
        data = r.json()
        cases = []
        if isinstance(data, list):
            cases = data
        elif isinstance(data, dict):
            cases = data.get("data", {}).get("docs", []) or data.get("cases", []) or data.get("docs", [])
        
        print(f"[*] Total casos abiertos recibidos: {len(cases)}")
        for idx, c in enumerate(cases, 1):
            c_id = c.get("_id") or c.get("id") or c.get("case_id")
            src = c.get("_source", c)
            name = src.get("name") or src.get("title") or "Sin Nombre"
            status = src.get("status")
            severity = src.get("severity")
            score = src.get("score")
            print(f"\n--- CASO #{idx} ---")
            print(f"ID: {c_id}")
            print(f"Nombre: {name}")
            print(f"Status: {status} | Severidad: {severity} | Score: {score}")
            
            # Print candidate check against all known workers
            n_lower = name.lower()
            matches = []
            if "exchange healthmailbox" in n_lower or "healthmailbox" in n_lower:
                matches.append("HealthMailbox")
            if "sophos ssl vpn" in n_lower or "translation failed" in n_lower:
                matches.append("Sophos SSL VPN")
            if "sati vpn" in n_lower or "sati" in n_lower:
                matches.append("SATI VPN")
            if "protected_storage" in n_lower or "dpapi" in n_lower or "5145" in n_lower or ("vmbase8" in n_lower and "ipc$" in n_lower):
                matches.append("DPAPI")
            if "exfiltration" in n_lower or "google" in n_lower or "drive" in n_lower or "appsheet" in n_lower:
                matches.append("Google Drive / AppSheet Anomaly")
            
            print(f"Posibles Matches SOAR: {matches if matches else 'NINGUNO'}")
            
            # Query alerts inside the case if available
            alerts_url = f"https://{host}/connect/api/v1/cases/{c_id}/alerts"
            try:
                ar = requests.get(alerts_url, headers=headers, verify=False, timeout=10)
                if ar.status_code == 200:
                    adata = ar.json()
                    adocs = []
                    if isinstance(adata, list):
                        adocs = adata
                    elif isinstance(adata, dict):
                        adocs = adata.get("data", {}).get("docs", []) or adata.get("alerts", []) or adata.get("docs", [])
                    print(f"Alertas asociadas ({len(adocs)}):")
                    for a in adocs[:3]:
                        asrc = a.get("_source", a)
                        aname = asrc.get("xdr_event", {}).get("display_name") or asrc.get("event_name") or asrc.get("name")
                        srcip = asrc.get("srcip")
                        dstip = asrc.get("dstip")
                        user = asrc.get("srcip_username") or asrc.get("user", {}).get("name")
                        print(f"  - Alerta: {aname} | User: {user} | Src: {srcip} -> Dst: {dstip}")
            except Exception as e_a:
                print(f"  [!] Error consultando alertas del caso: {e_a}")

    except Exception as e:
        print(f"[!] Excepcion al consultar casos: {e}")

def check_log_tail():
    for base in [r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar", r"c:\Users\kevinmoraes\Documents\soc-env"]:
        log_path = os.path.join(base, "historial_caidas.log")
        if os.path.exists(log_path):
            print(f"\n[*] Ultimas 20 lineas de {log_path}:")
            try:
                with open(log_path, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()
                for line in lines[-20:]:
                    print("  " + line.rstrip())
            except Exception as e:
                print(f"  [!] Error: {e}")

if __name__ == "__main__":
    query_open_cases()
    check_log_tail()
