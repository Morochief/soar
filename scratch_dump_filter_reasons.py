import os
import sys
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(Path('G:/SOC/soar/.env'))

host = os.environ.get('STELLAR_HOST')
email = os.environ.get('STELLAR_EMAIL')
token = os.environ.get('STELLAR_TOKEN')

import base64
url = f'https://{host}/connect/api/v1/access_token'
pair = f'{email}:{token}'
b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {b64}', 'Content-Type': 'application/json'}
res = requests.post(url, headers=headers, json={}, verify=True, timeout=10)
jwt = res.json().get('access_token')
auth_headers = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

r = requests.get(f'https://{host}/connect/api/v1/log_filters', headers=auth_headers, timeout=15)
filters = r.json().get('data', [])

print(f"=== INVENTARIO COMPLETO DE LOS {len(filters)} FILTROS CON NOMBRES Y AUTORES ===")
for i, f in enumerate(filters[:30], 1):
    fid = f.get('_id', '')
    fname = f.get('name', 'SIN NOMBRE')
    creator = f.get('created_by', 'Desconocido')
    mod_by = f.get('modified_by', creator)
    profiles = f.get('in_use', {}).get('sensor_profile', [])
    raw = f.get('content', '{}')
    try:
        content = json.loads(raw) if isinstance(raw, str) else raw
    except:
        content = {}
    dev_type = content.get('dev_type', 'all')
    rules = content.get('rules', {})
    rules_summary = []
    for k, v in rules.items():
        val = v.get('value') if isinstance(v, dict) else v
        op = v.get('op', '=') if isinstance(v, dict) else '='
        rules_summary.append(f"{k} {op} {val}")
    r_str = ' AND '.join(rules_summary)
    print(f"#{i:02d} | [{dev_type}] \"{fname}\" | Creado por: {creator} | Regla: {r_str}")
