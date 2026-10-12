import os
import requests
import base64
import json
import time
import sys
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()
host = os.environ.get("STELLAR_HOST")
email = os.environ.get("STELLAR_EMAIL")
token = os.environ.get("STELLAR_TOKEN")

url_token = f"https://{host}/connect/api/v1/access_token"
pair = f"{email}:{token}"
b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
jwt = requests.post(url_token, headers={"Authorization": f"Basic {b64}", "Content-Type": "application/json"}, json={}, timeout=15).json().get("access_token")
headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

now_ms = int(time.time() * 1000)
start_ms = now_ms - (7 * 24 * 3600 * 1000)

p = {"aggr_type": "tenant_index", "start_time": start_ms, "end_time": now_ms}
r = requests.get(f"https://{host}/connect/api/v1/storage-usages", headers=headers, params=p, timeout=15)
print("Status tenant_index:", r.status_code)
if r.status_code == 200:
    data = r.json().get("data", [])
    print(f"Total puntos temporales: {len(data)}")
    if data:
        last = data[-1]
        print(f"Última fecha: {last.get('time')}")
        print(f"Total usage en ese punto: {last.get('total_usage')} GB")
        usages = last.get("usages", [])
        # Ordenar por usage descendente
        usages.sort(key=lambda x: x.get("usage", 0), reverse=True)
        print("Top 10 índices con mayor ingesta:")
        for u in usages[:10]:
            print(f"   {u.get('tenant_name'):15s} | Index: {u.get('index'):25s} | Ingesta: {u.get('usage'):8.4f} GB")
