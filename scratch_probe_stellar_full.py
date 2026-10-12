import os
import requests
import base64
import json
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

r = requests.get(f"https://{host}/connect/api/v1/storage-usages/daily_and_monthly", headers=headers, timeout=15)
data = r.json()
print(f"Total Tenants con almacenamiento: {len(data.get('data', []))}")
total_mes = 0
for t in data.get('data', []):
    m = t.get('monthly_usage', 0)
    total_mes += m
    d_list = t.get('daily_usage', [])
    ult_dia = d_list[-1]['usage'] if d_list else 0
    print(f"Tenant: {t.get('tenant_name'):30s} | Mes: {m:8.2f} GB | Último Día: {ult_dia:6.2f} GB")

print(f"\nTOTAL MENSUAL ACUMULADO TODOS LOS TENANTS: {total_mes:.2f} GB")
