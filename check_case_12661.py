import os
import sys
import json
import base64
import requests
import urllib3

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

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
    res = requests.post(url, headers=headers, json={}, verify=False, timeout=15)
    res.raise_for_status()
    return res.json().get("access_token")

def check_case_12661():
    host, email, token = get_credentials()
    jwt = get_jwt(host, email, token)
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    # Intentar endpoint por ticket_id o search con timeout de 45s
    url = f"https://{host}/connect/api/v1/cases"
    params = {"ticket_id": "12661"}
    print(f"[*] Consultando caso ticket_id=12661 con timeout 45s...")
    try:
        r = requests.get(url, headers=headers, params=params, verify=False, timeout=45)
        if r.status_code == 200:
            data = r.json()
            casos = []
            if isinstance(data, dict):
                inner = data.get("data", data)
                if isinstance(inner, dict): casos = inner.get("cases", []) or inner.get("docs", [])
                elif isinstance(inner, list): casos = inner
            elif isinstance(data, list):
                casos = data

            if casos:
                c = casos[0]
                cid = c.get("_id")
                print(f"[+] Caso encontrado: ID={cid} | Ticket={c.get('ticket_id')}")
                print(f"    Nombre: {c.get('name')}")
                print(f"    Status: {c.get('status')} | Severidad: {c.get('severity')}")
                print(f"    Tags: {c.get('tags')}")

                # Alertas
                a_url = f"https://{host}/connect/api/v1/cases/{cid}/alerts"
                ar = requests.get(a_url, headers=headers, params={"limit": 15}, verify=False, timeout=30)
                if ar.status_code == 200:
                    adata = ar.json()
                    adocs = []
                    if isinstance(adata, dict):
                        ainner = adata.get("data", adata)
                        if isinstance(ainner, dict): adocs = ainner.get("docs", [])
                        elif isinstance(ainner, list): adocs = ainner
                    elif isinstance(adata, list):
                        adocs = adata
                    print(f"\n[+] Total alertas en caso: {len(adocs)}")
                    for idx, a in enumerate(adocs, 1):
                        asrc = a.get("_source", a)
                        ename = asrc.get("xdr_event", {}).get("display_name") or asrc.get("event_name")
                        pol = asrc.get("fortinet", {}).get("policyname") or asrc.get("policyname")
                        srcip = asrc.get("srcip")
                        dstip = asrc.get("dstip")
                        dstport = asrc.get("dstport")
                        proto = asrc.get("proto_name") or asrc.get("proto")
                        service = asrc.get("fortinet", {}).get("service") or asrc.get("service")
                        print(f"  Alert #{idx}: [{ename}] Pol={pol} | {srcip} -> {dstip}:{dstport} ({proto}) | Svc={service}")
                    return
        print("[-] No devolvio resultados por ticket_id.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    check_case_12661()
