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
    res = requests.post(url, headers=headers, json={}, verify=False, timeout=10)
    res.raise_for_status()
    return res.json().get("access_token")

def main():
    host, email, token = get_credentials()
    jwt = get_jwt(host, email, token)
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    url = f"https://{host}/connect/api/v1/cases?limit=50"
    print(f"[*] Consultando {url}...")
    r = requests.get(url, headers=headers, verify=False, timeout=25)
    r.raise_for_status()
    data = r.json()

    # Stellar API structure: data -> cases or docs or list
    casos = []
    if isinstance(data, list):
        casos = data
    elif isinstance(data, dict):
        if "data" in data:
            d = data["data"]
            if isinstance(d, dict):
                casos = d.get("cases", []) or d.get("docs", [])
            elif isinstance(d, list):
                casos = d
        if not casos:
            casos = data.get("cases", []) or data.get("docs", [])

    print(f"[+] Total casos recibidos: {len(casos)}")
    for c in casos:
        cid = c.get("_id") or c.get("id")
        tid = c.get("ticket_id") or c.get("id")
        name = c.get("name") or c.get("title")
        status = c.get("status")
        created = c.get("created_at") or c.get("timestamp") or c.get("start_time")
        status_str = str(status)
        # Check if case is open/in progress
        # Usually 0=Open, 1=In Progress, 2=Closed or 'Open', 'Closed'
        print(f"\nCaso #{tid} | ID: {cid} | Status: {status} | Creado: {created}")
        print(f"  Nombre: {name}")
        
        # Check alerts inside this case
        a_url = f"https://{host}/connect/api/v1/cases/{cid}/alerts"
        try:
            ar = requests.get(a_url, headers=headers, params={"limit": 5}, verify=False, timeout=10)
            if ar.status_code == 200:
                adata = ar.json()
                adocs = []
                if isinstance(adata, dict):
                    inner = adata.get("data", adata)
                    if isinstance(inner, dict):
                        adocs = inner.get("docs", [])
                    elif isinstance(inner, list):
                        adocs = inner
                elif isinstance(adata, list):
                    adocs = adata
                for a in adocs[:3]:
                    asrc = a.get("_source", a)
                    aname = asrc.get("xdr_event", {}).get("display_name") or asrc.get("event_name")
                    srcuser = asrc.get("srcip_username") or asrc.get("user", {}).get("name")
                    print(f"    Alert: {aname} | user={srcuser}")
        except Exception as e_al:
            print(f"    Error alerts: {e_al}")

if __name__ == "__main__":
    main()
