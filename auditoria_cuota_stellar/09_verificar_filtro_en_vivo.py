import os
import sys
import requests
import json
import base64
import time
from datetime import datetime, timezone
import urllib3

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "")
CUST_ID = "e511c3fc54cd4d668bb67612c2ef4b04"

def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
    headers_auth = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers_auth, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando: {r.text}")
        exit(1)
    return r.json().get("access_token")

print("=" * 75)
print("   VERIFICACIÓN EN VIVO DEL NUEVO LOG FILTER EN STELLAR CYBER")
print("=" * 75)

jwt = get_jwt()
headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

# 1. Consultar todos los filtros en la API: /log_filters
url = f"https://{HOST}/connect/api/v1/log_filters"
r = requests.get(url, headers=headers, verify=False, timeout=20)

if r.status_code != 200:
    print(f"[-] Error al consultar log_filters: HTTP {r.status_code} - {r.text}")
    exit(1)

data = r.json()
filters = data.get("data", data) if isinstance(data, dict) else data
print(f"[+] Total filtros registrados en el sistema: {len(filters)}")

filters_sorted = sorted(filters, key=lambda x: str(x.get("created_at") or x.get("modified_at") or ""), reverse=True)

print(f"\n[+] Los 6 filtros más recientes en la plataforma:")
for idx, f in enumerate(filters_sorted[:6], 1):
    fid = f.get("_id") or f.get("id")
    name = f.get("name")
    action = f.get("action")
    creator = f.get("created_by")
    c_at = f.get("created_at")
    m_at = f.get("modified_at")
    in_use = f.get("in_use", {})
    profiles = in_use.get("sensor_profile", []) if isinstance(in_use, dict) else []
    
    raw_content = f.get("content", "{}")
    if isinstance(raw_content, str):
        try: content_dict = json.loads(raw_content)
        except Exception: content_dict = {}
    else: content_dict = raw_content or {}
    
    rules = content_dict.get("rules", f.get("rules", {}))
    
    print("-" * 75)
    print(f"[{idx}] NOMBRE: {name}")
    print(f"    ID: {fid}")
    print(f"    Creado por: {creator}")
    print(f"    Sensor Profiles Asignados: {profiles}")
    print(f"    Reglas Técnicas: {json.dumps(rules, ensure_ascii=False)}")
    if not profiles:
        print("    [!] ADVERTENCIA: 'in_use' está vacío. ¡El filtro NO está asignado al Sensor Profile!")
    else:
        print(f"    [OK] ACTIVO: Asignado a {profiles}")

# 2. Consultar telemetría de FortiGate en Data Lake en los últimos 30 minutos
print("\n" + "=" * 75)
print("   EVALUACIÓN DE IMPACTO EN TIEMPO REAL (ÚLTIMOS 30 MINUTOS)")
print("=" * 75)

now_epoch = int(time.time() * 1000)
min30_ago = now_epoch - (30 * 60 * 1000)

today_str = datetime.now().strftime("%Y.%m.%d")
target_index = f"*{today_str}*{CUST_ID}*"

query_benign = {
    "size": 0,
    "query": {
        "bool": {
            "filter": [
                {"term": {"tenantid": CUST_ID}},
                {"term": {"action.keyword": "passthrough"}},
                {"range": {"write_time": {"gte": min30_ago}}}
            ]
        }
    },
    "aggs": {
        "over_time": {
            "date_histogram": {
                "field": "write_time",
                "fixed_interval": "5m"
            }
        }
    }
}

try:
    url_es = f"https://{HOST}/connect/api/data/{target_index}/_search"
    res_es = requests.get(url_es, headers=headers, json=query_benign, timeout=30, verify=False)
    if res_es.status_code == 200:
        es_data = res_es.json()
        total_recent = es_data.get("hits", {}).get("total", {}).get("value", 0)
        print(f"Eventos 'passthrough' ingresados al Data Lake en los últimos 30 min: {total_recent:,}")
        print("\nHistograma de ingesta de passthrough cada 5 minutos:")
        for b in es_data.get("aggregations", {}).get("over_time", {}).get("buckets", []):
            t_str = datetime.fromtimestamp(b.get("key") / 1000, tz=timezone.utc).strftime("%H:%M:%S UTC")
            print(f"  • {t_str}: {b.get('doc_count'):,} eventos")
    else:
        print(f"Error consultando ES: {res_es.status_code}")
except Exception as e:
    print(f"Error: {e}")

print("=" * 75)
