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

def check_hm_cases():
    host, email, token = get_credentials()
    jwt = get_jwt(host, email, token)
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    for cid in ["6ad0bd34a9a3e2ee2766c038", "6ad0bd34a9a3e2ee2766c035"]: # #17761, #17760
        url = f"https://{host}/connect/api/v1/cases/{cid}"
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        c = r.json().get("data", r.json())
        print(f"\nCaso #{c.get('ticket_id')} | Status: {c.get('status')} | Name: {c.get('name')}")
        
        # Check alerts
        a_url = f"https://{host}/connect/api/v1/cases/{cid}/alerts"
        ar = requests.get(a_url, headers=headers, verify=False, timeout=10)
        ad = ar.json()
        docs = []
        if isinstance(ad, dict):
            inner = ad.get("data", ad)
            if isinstance(inner, dict): docs = inner.get("docs", [])
            elif isinstance(inner, list): docs = inner
        elif isinstance(ad, list): docs = ad
        
        users = set()
        protos = set()
        event_ids = set()
        for d in docs:
            asrc = d.get("_source", d)
            u = asrc.get("srcip_username") or asrc.get("user", {}).get("name")
            if u: users.add(str(u).lower())
            p = asrc.get("service") or asrc.get("protocol") or asrc.get("auth_protocol")
            if p: protos.add(str(p))
            eid = asrc.get("event_id") or asrc.get("winlog", {}).get("event_id")
            if eid: event_ids.add(str(eid))
            substatus = asrc.get("sub_status") or asrc.get("status_code") or asrc.get("winlog", {}).get("event_data", {}).get("SubStatus")
            
        print(f"  Total Alertas: {len(docs)}")
        print(f"  Users: {users}")
        print(f"  Event IDs: {event_ids}")
        print(f"  Protos: {protos}")

if __name__ == "__main__":
    check_hm_cases()
