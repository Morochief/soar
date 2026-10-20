import sys
import json
import base64
import time
import requests
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOST = 'technoma.stellarcyber.cloud'
EMAIL = 'kevinmoraes@technoma.com.py'
TOKEN = 'rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ'
TENANT_ID = 'e511c3fc54cd4d668bb67612c2ef4b04'

def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    return r.json().get("access_token")

jwt = get_jwt()
headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

now_ms = int(time.time() * 1000)
start_ms = now_ms - (24 * 3600 * 1000)

print("=" * 85)
print("🔬 DEEP DIVE EN LOS EVENTOS MÁS CARGADOS (ÚLTIMAS 24 HORAS)")
print(f"⏱️ {datetime.fromtimestamp(start_ms/1000).strftime('%Y-%m-%d %H:%M')} -> {datetime.fromtimestamp(now_ms/1000).strftime('%Y-%m-%d %H:%M')}")
print("=" * 85)

# 1. DEEP DIVE EN FIREWALL (2.05M eventos)
print("\n🔥 1. ANÁLISIS FORENSE: FIREWALL (2.05M eventos)")
url_adr = f"https://{HOST}/connect/api/data/*adr*{TENANT_ID}*/_search"
payload_fw = {
    "size": 0,
    "query": {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"msg_class.keyword": "firewall"}}
            ]
        }
    },
    "aggs": {
        "by_action": {"terms": {"field": "action.keyword", "size": 8}},
        "by_policy": {"terms": {"field": "policy_name.keyword", "size": 8}},
        "top_dst_ip": {"terms": {"field": "dstip.keyword", "size": 8}},
        "top_dst_port": {"terms": {"field": "dstport", "size": 8}}
    }
}
r_fw = requests.get(url_adr, headers=headers, json=payload_fw, verify=False).json()
print("  Acciones principales:")
for b in r_fw.get("aggregations", {}).get("by_action", {}).get("buckets", []):
    print(f"    - {b['key']:<15}: {b['doc_count']:,} logs")
print("  Top Políticas de Firewall más cargadas:")
for b in r_fw.get("aggregations", {}).get("by_policy", {}).get("buckets", []):
    print(f"    - {b['key']:<30}: {b['doc_count']:,} logs")
print("  Top IPs Destino más impactadas:")
for b in r_fw.get("aggregations", {}).get("top_dst_ip", {}).get("buckets", []):
    print(f"    - {b['key']:<20}: {b['doc_count']:,} logs")
print("  Top Puertos Destino:")
for b in r_fw.get("aggregations", {}).get("top_dst_port", {}).get("buckets", []):
    print(f"    - Puerto {str(b['key']):<12}: {b['doc_count']:,} logs")

# 2. DEEP DIVE EN NETWORK APPLICATIONS (1.23M eventos)
print("\n🌐 2. ANÁLISIS FORENSE: NETWORK APPLICATIONS (1.23M flujos DPI)")
payload_net = {
    "size": 0,
    "query": {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"msg_class.keyword": "interflow_traffic"}}
            ]
        }
    },
    "aggs": {
        "top_apps": {"terms": {"field": "appid_name.keyword", "size": 10}},
        "top_services": {"terms": {"field": "service.keyword", "size": 8}},
        "top_src_ips": {"terms": {"field": "srcip.keyword", "size": 8}}
    }
}
r_net = requests.get(url_adr, headers=headers, json=payload_net, verify=False).json()
print("  Top Aplicaciones detectadas por el Sensor Modular:")
for b in r_net.get("aggregations", {}).get("top_apps", {}).get("buckets", []):
    print(f"    - {b['key']:<25}: {b['doc_count']:,} flujos")
print("  Top IPs Origen generadoras de flujos:")
for b in r_net.get("aggregations", {}).get("top_src_ips", {}).get("buckets", []):
    print(f"    - {b['key']:<20}: {b['doc_count']:,} flujos")

# 3. DEEP DIVE EN ALL LOGIN FAILURES (61.2k eventos en Windows)
print("\n🚨 3. ANÁLISIS FORENSE: ALL LOGIN FAILURES (61.2k fallos)")
url_win = f"https://{HOST}/connect/api/data/*wineventlog*{TENANT_ID}*/_search"
payload_fail = {
    "size": 0,
    "query": {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"login_result.keyword": "fail"}}
            ]
        }
    },
    "aggs": {
        "top_users": {"terms": {"field": "event_data.TargetUserName.keyword", "size": 10}},
        "top_status": {"terms": {"field": "event_data.Status.keyword", "size": 6}},
        "top_hosts": {"terms": {"field": "engid_name.keyword", "size": 5}}
    }
}
r_fail = requests.get(url_win, headers=headers, json=payload_fail, verify=False).json()
print("  Top Cuentas con Fallos de Login:")
for b in r_fail.get("aggregations", {}).get("top_users", {}).get("buckets", []):
    print(f"    - {b['key']:<45}: {b['doc_count']:,} fallos")
print("  Top Servidores donde se registran los fallos:")
for b in r_fail.get("aggregations", {}).get("top_hosts", {}).get("buckets", []):
    print(f"    - {b['key']:<25}: {b['doc_count']:,} fallos")

# 4. DEEP DIVE EN GOOGLE WORKSPACE (58.5k eventos)
print("\n☁️ 4. ANÁLISIS FORENSE: GOOGLE WORKSPACE (58.5k eventos)")
url_audit = f"https://{HOST}/connect/api/data/*audit*{TENANT_ID}*/_search"
payload_gsuite = {
    "size": 0,
    "query": {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"msg_class.keyword": "gsuite"}}
            ]
        }
    },
    "aggs": {
        "top_events": {"terms": {"field": "event_name.keyword", "size": 10}},
        "top_actors": {"terms": {"field": "srcip_username.keyword", "size": 8}}
    }
}
r_gsuite = requests.get(url_audit, headers=headers, json=payload_gsuite, verify=False).json()
print("  Top Tipos de Eventos de Google Workspace:")
for b in r_gsuite.get("aggregations", {}).get("top_events", {}).get("buckets", []):
    print(f"    - {b['key']:<35}: {b['doc_count']:,} eventos")
print("  Top Usuarios más activos en auditoría Google:")
for b in r_gsuite.get("aggregations", {}).get("top_actors", {}).get("buckets", []):
    print(f"    - {b['key']:<35}: {b['doc_count']:,} eventos")

print("\n" + "=" * 85)
