import os
import sys
import json
import base64
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")

def get_jwt() -> str:
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    return r.json().get("access_token")

jwt_token = get_jwt()
headers = {"Authorization": f"Bearer {jwt_token}", "Content-Type": "application/json"}

def query_stellar(index_pattern, query_lucene, size=10):
    url = f"https://{HOST}/connect/api/data/{index_pattern}/_search"
    payload = {
        "size": size,
        "query": {
            "query_string": {
                "query": query_lucene
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}]
    }
    r = requests.get(url, headers=headers, json=payload, timeout=20, verify=False)
    if r.status_code == 200:
        return r.json().get("hits", {}).get("hits", [])
    else:
        print(f"Error {r.status_code}: {r.text[:200]}")
        return []

def investigate_ip(ip):
    print(f"\n=======================================================")
    print(f"=== INVESTIGANDO IP: {ip} ===")
    print(f"=======================================================")
    
    # 1. Buscar en assets
    print("--- [1] Consulta en Asset / Device Management ---")
    hits_asset = query_stellar("*asset*", f'ip:"{ip}" OR ip_list:"{ip}"', size=5)
    print(f"Hits en assets: {len(hits_asset)}")
    for h in hits_asset:
        src = h.get("_source", {})
        print(f"  Hostname: {src.get('hostname')}")
        print(f"  Device Name: {src.get('device_name')}")
        print(f"  OS: {src.get('os')} / {src.get('os_version')}")
        print(f"  MAC: {src.get('mac')}")
        print(f"  Tenant: {src.get('tenant_name')}")
        print(f"  Services: {src.get('services')}")

    # 2. Buscar en tráfico / flujos (ADR)
    print("\n--- [2] Muestra de Tráfico Reciente (ADR / Interflow / Firewall) ---")
    hits_traffic = query_stellar("*adr*", f'srcip:"{ip}" OR dstip:"{ip}"', size=10)
    print(f"Hits en tráfico: {len(hits_traffic)}")
    for h in hits_traffic:
        src = h.get("_source", {})
        t_name = src.get("tenant_name", "")
        s_ip = src.get("srcip")
        s_port = src.get("srcport")
        s_host = src.get("srcip_host")
        d_ip = src.get("dstip")
        d_port = src.get("dstport")
        d_host = src.get("dstip_host")
        app = src.get("appid_name")
        proto = src.get("proto_name")
        smac = src.get("srcmac")
        dmac = src.get("dstmac")
        msg_class = src.get("msg_class")
        user = src.get("srcip_username") or src.get("user_name") or ""
        print(f"  [{t_name}] {s_ip}:{s_port} ({s_host}) -> {d_ip}:{d_port} ({d_host}) | Class: {msg_class} | App: {app}/{proto} | MAC: {smac}->{dmac} | User: {user}")

    # 3. Buscar en logs de eventos / syslogs / wineventlog
    print("\n--- [3] Muestra en Registros de Eventos / Syslog / Windows ---")
    hits_ev = query_stellar("*wineventlog*", f'srcip:"{ip}" OR dstip:"{ip}" OR host_ip:"{ip}" OR "{ip}"', size=5)
    print(f"Hits en Windows Events: {len(hits_ev)}")
    for h in hits_ev:
        src = h.get("_source", {})
        print(f"  Host: {src.get('host_name')} | EventID: {src.get('event_id')} | User: {src.get('user_name')} | Msg: {str(src.get('msg'))[:120]}")

investigate_ip("192.168.15.70")
investigate_ip("192.168.9.5")
