import os
import sys
import json
import base64
import requests
import urllib3

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_credentials():
    host = os.environ.get("STELLAR_HOST")
    email = os.environ.get("STELLAR_EMAIL")
    token = os.environ.get("STELLAR_TOKEN")
    if not (host and email and token):
        try:
            import winreg
            for hive in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
                subkey = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
                try:
                    with winreg.OpenKey(hive, subkey) as reg_key:
                        if not host:
                            try: host = str(winreg.QueryValueEx(reg_key, "STELLAR_HOST")[0]).strip()
                            except Exception: pass
                        if not email:
                            try: email = str(winreg.QueryValueEx(reg_key, "STELLAR_EMAIL")[0]).strip()
                            except Exception: pass
                        if not token:
                            try: token = str(winreg.QueryValueEx(reg_key, "STELLAR_TOKEN")[0]).strip()
                            except Exception: pass
                except Exception:
                    pass
        except Exception:
            pass
    return host, email, token

def get_jwt(host, email, token):
    url = f"https://{host}/connect/api/v1/access_token"
    pair = f"{email}:{token}"
    b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
    headers = {"Authorization": f"Basic {b64}", "Content-Type": "application/json"}
    res = requests.post(url, headers=headers, json={}, verify=False, timeout=10)
    res.raise_for_status()
    return res.json().get("access_token")

def evaluate_candidate(case: dict):
    src = case.get("_source", case)
    name = str(src.get("name") or src.get("title") or "").lower()
    src_user = str(src.get("srcip_username") or "").lower()
    user = str(src.get("username") or src.get("user") or "").lower()
    tags = " ".join(str(t).lower() for t in src.get("tags", []))
    desc = str(src.get("description") or "").lower()
    combined = f"{name} {src_user} {user} {tags} {desc}"

    # HM
    is_hm = "healthmailbox" in combined
    # Translate
    is_translate = (
        "translate.google.com" in combined or
        "webcontrolviolation" in combined or
        ("user execution" in combined and "sophos" in combined)
    )
    # Sati
    is_sati = "sati" in combined and (
        "firewall denial" in combined or 
        "internal firewall denial" in combined or 
        "denial anomaly" in combined or 
        "policyid" in combined or
        "denial" in combined or
        "10.212.134" in combined or 
        "dns" in combined
    )
    # DPAPI
    is_dpapi = (
        "protected_storage" in combined or
        "sensitive windows network share" in combined or
        ("network share" in combined and "ipc$" in combined) or
        ("windows_security_5145" in combined) or
        ("5145" in combined and "vmbase8" in combined)
    ) and ("vmbase8" in combined or "172.16.201.8" in combined or "protected_storage" in combined)

    # Google Drive / AppSheet
    is_gdrive = (
        "cloud drive" in combined or
        "cloud_drive_data_exfiltration_anomaly" in combined or
        "google workspace" in combined or
        "drive.files.get" in combined or
        "appsheet" in combined or
        "appscript" in combined or
        "exfiltration anomaly" in combined
    )

    matches = []
    if is_hm: matches.append("HealthMailbox")
    if is_translate: matches.append("Sophos Translate")
    if is_sati: matches.append("SATI VPN")
    if is_dpapi: matches.append("DPAPI Storage")
    if is_gdrive: matches.append("Google Drive / AppSheet (GSuite)")
    return matches

def check_open_cases():
    host, email, token = get_credentials()
    if not (host and email and token):
        print(f"[!] Faltan credenciales: host={bool(host)}, email={bool(email)}, token={bool(token)}")
        return

    try:
        jwt = get_jwt(host, email, token)
        print(f"[+] JWT obtenido exitosamente.")
    except Exception as e:
        print(f"[!] Error obteniendo JWT: {e}")
        return

    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    url = f"https://{host}/connect/api/v1/cases?status=Open&limit=50"
    print(f"\n[*] Consultando casos abiertos en {url} ...")
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=15)
        if r.status_code != 200:
            print(f"[!] Error {r.status_code}: {r.text[:300]}")
            return
        
        data = r.json()
        cases = []
        if isinstance(data, list):
            cases = data
        elif isinstance(data, dict):
            cases = data.get("data", {}).get("docs", []) or data.get("cases", []) or data.get("docs", [])
        
        print(f"[+] Casos abiertos encontrados: {len(cases)}")
        for idx, c in enumerate(cases, 1):
            c_id = c.get("_id") or c.get("id") or c.get("case_id")
            src = c.get("_source", c)
            name = src.get("name") or src.get("title") or "Sin Nombre"
            status = src.get("status")
            severity = src.get("severity")
            score = src.get("score")
            created_at = src.get("created_at") or src.get("timestamp") or src.get("start_time")
            matches = evaluate_candidate(c)
            
            print(f"\n--- CASO #{idx}: ID={c_id} ---")
            print(f"Nombre: {name}")
            print(f"Status: {status} | Severidad: {severity} | Score: {score} | Creado: {created_at}")
            print(f"Coincidencias SOAR: {matches if matches else 'NINGUNA'}")
            
            a_url = f"https://{host}/connect/api/v1/cases/{c_id}/alerts"
            try:
                ar = requests.get(a_url, headers=headers, verify=False, timeout=10)
                if ar.status_code == 200:
                    adata = ar.json()
                    adocs = []
                    if isinstance(adata, list):
                        adocs = adata
                    elif isinstance(adata, dict):
                        adocs = adata.get("data", {}).get("docs", []) or adata.get("alerts", []) or adata.get("docs", [])
                    print(f"Alertas en caso ({len(adocs)}):")
                    for a in adocs[:5]:
                        asrc = a.get("_source", a)
                        aname = asrc.get("xdr_event", {}).get("display_name") or asrc.get("event_name") or asrc.get("name")
                        srcip = asrc.get("srcip")
                        user = asrc.get("srcip_username") or asrc.get("user", {}).get("name")
                        msg = asrc.get("message") or asrc.get("event_description") or ""
                        print(f"  - [{aname}] user={user} src={srcip} msg={str(msg)[:80]}")
            except Exception as e_a:
                print(f"  Error obteniendo alertas: {e_a}")
                
    except Exception as e:
        print(f"[!] Error consultando casos: {e}")

def check_process():
    print("\n[*] Verificando procesos command_center.py...")
    import subprocess
    cmd = 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like \'*command_center*\' } | Select-Object ProcessId, CommandLine, CreationDate"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors='replace')
    print(res.stdout if res.stdout else "No se encontraron procesos activos de command_center.py.")

def check_recent_logs():
    paths = [
        r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\historial_caidas.log",
        r"c:\Users\kevinmoraes\Documents\soc-env\historial_caidas.log"
    ]
    print("\n=== ULTIMAS LINEAS DE LOGS ===")
    for p in paths:
        if os.path.exists(p):
            print(f"\n--- Log: {p} (Ultimas 25 lineas) ---")
            with open(p, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
                for line in lines[-25:]:
                    print(line.rstrip())
        else:
            print(f"Log no encontrado: {p}")

if __name__ == "__main__":
    check_process()
    check_open_cases()
    check_recent_logs()
