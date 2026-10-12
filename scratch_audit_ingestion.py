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

print("=== INGESTION STATS: SENSOR (LAST 24H) ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/sensor', headers=auth_headers, params=params, timeout=15)
sensors_data = r.json().get('data', [])
for s in sensors_data:
    gb = s.get('total_ingestion', 0) / (1024**3)
    print(f"Sensor ID: {s.get('entry_identifier')} | Tenant: {s.get('tenant_name')} | Ingest: {gb:.3f} GB ({s.get('total_ingestion')} bytes)")

print("\n=== INGESTION STATS: LOG TYPE (LAST 24H) ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/log-type', headers=auth_headers, params=params, timeout=15)
log_types = r.json().get('data', [])
for lt in log_types:
    gb = lt.get('total_ingestion', 0) / (1024**3)
    print(f"Log Type: {lt.get('entry_identifier')} | Tenant: {lt.get('tenant_name')} | Ingest: {gb:.3f} GB ({lt.get('total_ingestion')} bytes)")

print("\n=== INGESTION STATS: CONNECTOR (LAST 24H) ===")
r = requests.get(f'https://{host}/connect/api/v1/ingestion-stats/connector', headers=auth_headers, params=params, timeout=15)
connectors = r.json().get('data', [])
for c in connectors:
    gb = c.get('total_ingestion', 0) / (1024**3)
    print(f"Connector: {c.get('entry_identifier')} | Tenant: {c.get('tenant_name')} | Ingest: {gb:.3f} GB ({c.get('total_ingestion')} bytes)")

print("\n=== LOG FILTERS CONFIGURED ===")
r = requests.get(f'https://{host}/connect/api/v1/log_filters', headers=auth_headers, timeout=15)
filters = r.json().get('data', [])
print(f"Total Log Filters configured: {len(filters)}")
for idx, f in enumerate(filters):
    fid = f.get('_id')
    raw_content = f.get('content', '{}')
    try:
        content = json.loads(raw_content)
    except:
        content = {}
    print(f"Filter #{idx+1} [ID: {fid}]:")
    print(f"  Description / Dev Type: {content.get('dev_type')} ({content.get('dev_type_label')})")
    print(f"  Tenant: {f.get('tenant_name', content.get('tenant_name'))}")
    print(f"  Rules: {json.dumps(content.get('rules', {}), indent=2)}")
