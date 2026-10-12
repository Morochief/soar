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

payload = {
    'cust_id': 'all-tenants',
    'name': 'Test_Hunt_SOC_Query',
    'conditions': {
        'modifier': 'and',
        'conditions': [
            {'type': 'query_string', 'value': ['_index: aella-ser-* AND srcip: "192.168.15.27"']}
        ]
    }
}
r = requests.post(f'https://{host}/connect/api/v1/queries', headers=auth_headers, json=payload, timeout=15)
print('POST /queries status:', r.status_code)
print(r.text[:800])
