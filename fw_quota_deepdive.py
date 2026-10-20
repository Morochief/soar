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

auth_str = f"{EMAIL}:{TOKEN}"
auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
jwt = r.json().get("access_token")
h = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

now_ms = int(time.time() * 1000)
start_ms = now_ms - (24 * 3600 * 1000)

print("=" * 90)
print("🎯 ANÁLISIS DE IMPACTO BRUTO DE CUOTA: FIREWALL SYSLOG (ÚLTIMAS 24 HORAS)")
print(f"⏱️ {datetime.fromtimestamp(start_ms/1000).strftime('%Y-%m-%d %H:%M')} -> {datetime.fromtimestamp(now_ms/1000).strftime('%Y-%m-%d %H:%M')}")
print("=" * 90)

url = f"https://{HOST}/connect/api/data/*adr*{TENANT_ID}*/_search"

# 1. Total eventos firewall
payload_base = {
    "track_total_hits": True,
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
        "by_action": {
            "terms": {"field": "action.keyword", "size": 15}
        },
        "by_policy": {
            "terms": {"field": "policy_name.keyword", "size": 15}
        },
        "by_port": {
            "terms": {"field": "dstport", "size": 15}
        },
        "by_subtype": {
            "terms": {"field": "engid_type.keyword", "size": 10}
        }
    }
}

res = requests.get(url, headers=h, json=payload_base, verify=False).json()
total_fw = res.get("hits", {}).get("total", {}).get("value", 0)
print(f"📊 Total Eventos Firewall en 24h: {total_fw:,} logs")

# Calcular tamaño promedio de un log de firewall
sample_payload = {
    "size": 20,
    "query": {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"msg_class.keyword": "firewall"}}
            ]
        }
    }
}
r_sample = requests.get(url, headers=h, json=sample_payload, verify=False).json()
sample_hits = r_sample.get("hits", {}).get("hits", [])
sizes = [len(json.dumps(s["_source"]).encode("utf-8")) for s in sample_hits]
avg_bytes = sum(sizes) / len(sizes) if sizes else 1200
total_gb_fw = (total_fw * avg_bytes) / (1024**3)
print(f"⚖️ Peso estimado total en ingesta: ~{total_gb_fw:.2f} GB de cuota consumida (avg: {avg_bytes:.0f} bytes/log)\n")

print("--- 🔴 1. DESGLOSE POR ACCIÓN (DÓNDE SE VA EL PESO) ---")
for b in res.get("aggregations", {}).get("by_action", {}).get("buckets", []):
    cnt = b["doc_count"]
    pct = (cnt / total_fw * 100) if total_fw else 0
    gb = (cnt * avg_bytes) / (1024**3)
    print(f"  {b['key']:<15}: {cnt:>10,} logs ({pct:>5.1f}%) ➔ ~{gb:.2f} GB")

print("\n--- 🔴 2. TOP POLÍTICAS DE FIREWALL GENERADORAS DE LOGS ---")
for b in res.get("aggregations", {}).get("by_policy", {}).get("buckets", []):
    cnt = b["doc_count"]
    pct = (cnt / total_fw * 100) if total_fw else 0
    gb = (cnt * avg_bytes) / (1024**3)
    print(f"  {b['key']:<30}: {cnt:>10,} logs ({pct:>5.1f}%) ➔ ~{gb:.2f} GB")

print("\n--- 🔴 3. TOP PUERTOS DESTINO ---")
for b in res.get("aggregations", {}).get("by_port", {}).get("buckets", []):
    cnt = b["doc_count"]
    pct = (cnt / total_fw * 100) if total_fw else 0
    gb = (cnt * avg_bytes) / (1024**3)
    print(f"  Puerto {str(b['key']):<15}: {cnt:>10,} logs ({pct:>5.1f}%) ➔ ~{gb:.2f} GB")
