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

    cid = "6ad0bf15a9a3e2ee2766c08a"
    a_url = f"https://{host}/connect/api/v1/cases/{cid}/alerts"
    ar = requests.get(a_url, headers=headers, verify=False, timeout=15)
    ad = ar.json()
    docs = []
    if isinstance(ad, dict):
        inner = ad.get("data", ad)
        if isinstance(inner, dict):
            docs = inner.get("docs", [])
        elif isinstance(inner, list):
            docs = inner
    elif isinstance(ad, list):
        docs = ad

    if docs:
        first = docs[0].get("_source", docs[0])
        # Find all keys containing storage, share, path, target, ipc
        print("Keys in alert:")
        for k, v in first.items():
            s_v = str(v)
            if any(term in s_v.lower() for term in ["ipc", "storage", "protected", "share", "5145", "vmbase"]):
                print(f"  {k}: {s_v[:150]}")

if __name__ == "__main__":
    main()
