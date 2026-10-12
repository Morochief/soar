import os
import time
import base64
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path('G:/SOC/soar/.env'))
host = os.environ.get('STELLAR_HOST')
email = os.environ.get('STELLAR_EMAIL')
token = os.environ.get('STELLAR_TOKEN')

url = f'https://{host}/connect/api/v1/access_token'
pair = f'{email}:{token}'
b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {b64}', 'Content-Type': 'application/json'}
res = requests.post(url, headers=headers, json={}, verify=True, timeout=10)
jwt = res.json().get('access_token')
auth_headers = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

now_ms = int(time.time() * 1000)
day_ago_ms = now_ms - (24 * 3600 * 1000)
params = {'start_time': day_ago_ms, 'end_time': now_ms}

print("=== SENSORS ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/sensor', headers=auth_headers, params=params, timeout=15)
for s in sorted(r.json().get('data', []), key=lambda x: x.get('total_ingestion', 0), reverse=True):
    gb = s.get('total_ingestion', 0) / (1024**3)
    print(f"Sensor: {s.get('entry_identifier')} | Tenant: {s.get('tenant_name')} | {gb:.3f} GB")

print("\n=== LOG TYPES ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/log-type', headers=auth_headers, params=params, timeout=15)
for lt in sorted(r.json().get('data', []), key=lambda x: x.get('total_ingestion', 0), reverse=True):
    gb = lt.get('total_ingestion', 0) / (1024**3)
    print(f"LogType: {lt.get('entry_identifier')} | Tenant: {lt.get('tenant_name')} | {gb:.3f} GB")

print("\n=== LOG SOURCES ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/log-source', headers=auth_headers, params=params, timeout=15)
for ls in sorted(r.json().get('data', []), key=lambda x: x.get('total_ingestion', 0), reverse=True):
    gb = ls.get('total_ingestion', 0) / (1024**3)
    print(f"Source: {ls.get('entry_identifier')} ({ls.get('source_ip')}:{ls.get('port')}) | Tenant: {ls.get('tenant_name')} | {gb:.3f} GB")

print("\n=== CONNECTORS ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/connector', headers=auth_headers, params=params, timeout=15)
for c in sorted(r.json().get('data', []), key=lambda x: x.get('total_ingestion', 0), reverse=True):
    gb = c.get('total_ingestion', 0) / (1024**3)
    print(f"Connector: {c.get('entry_identifier')} | Tenant: {c.get('tenant_name')} | {gb:.3f} GB")
