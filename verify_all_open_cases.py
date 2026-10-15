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

def is_dpapi_storage_candidate(case: dict) -> bool:
    name = str(case.get("name", "")).lower()
    src_user = str(case.get("srcip_username") or "").lower()
    user = str(case.get("username") or case.get("user") or "").lower()
    tags = " ".join(str(t).lower() for t in case.get("tags", []))
    desc = str(case.get("description") or "").lower()
    combined = f"{name} {src_user} {user} {tags} {desc}"

    return (
        "protected_storage" in combined or
        "sensitive windows network share" in combined or
        ("network share" in combined and "ipc$" in combined) or
        "windows_security_5145" in combined or
        ("5145" in combined and "share" in combined)
    )

def is_healthmailbox_candidate(case: dict) -> bool:
    name = str(case.get("name", "")).lower()
    src_user = str(case.get("srcip_username") or "").lower()
    user = str(case.get("username") or case.get("user") or "").lower()
    tags = " ".join(str(t).lower() for t in case.get("tags", []))
    desc = str(case.get("description") or "").lower()
    combined = f"{name} {src_user} {user} {tags} {desc}"
    return "healthmailbox" in combined

def main():
    host, email, token = get_credentials()
    jwt = get_jwt(host, email, token)
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    url = f"https://{host}/connect/api/v1/cases?limit=15"
    r = requests.get(url, headers=headers, verify=False, timeout=20)
    data = r.json()
    casos = data.get("data", {}).get("cases", []) or data.get("data", []) or data.get("cases", [])
    
    print(f"[*] Evaluando los {len(casos)} casos mas recientes con la nueva logica:")
    for c in casos[:8]:
        tid = c.get("ticket_id")
        name = c.get("name")
        status = c.get("status")
        match_dpapi = is_dpapi_storage_candidate(c)
        print(f"  - Caso #{tid} [{status}]: {name[:60]}")
        print(f"    -> Match DPAPI: {match_dpapi}")

if __name__ == "__main__":
    main()
