import sys
import json
import base64
import time
import requests

HOST = 'technoma.stellarcyber.cloud'
EMAIL = 'kevinmoraes@technoma.com.py'
TOKEN = 'rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ'
auth_str = f'{EMAIL}:{TOKEN}'
auth_b64 = base64.b64encode(auth_str.encode()).decode()
headers = {'Authorization': f'Basic {auth_b64}', 'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.post(f'https://{HOST}/connect/api/v1/access_token', headers=headers, json={}, verify=False)
jwt = r.json()['access_token']
h = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

now_ms = int(time.time() * 1000)
start_ms = now_ms - (24 * 3600 * 1000)

payload = {
    'track_total_hits': True,
    'size': 0,
    'query': {
        'bool': {
            'filter': [{'term': {'tenantid': 'e511c3fc54cd4d668bb67612c2ef4b04'}}],
            'must': [{'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}}]
        }
    },
    'aggs': {
        'by_index': {'terms': {'field': '_index', 'size': 25}},
        'by_class': {'terms': {'field': 'msg_class.keyword', 'size': 25}}
    }
}
url = f'https://{HOST}/connect/api/data/*e511c3fc54cd4d668bb67612c2ef4b04*/_search'
res = requests.get(url, headers=h, json=payload, verify=False)
print('Indices encontrados en las últimas 24h:')
for b in res.json().get('aggregations', {}).get('by_index', {}).get('buckets', []):
    print(f"  {b['key']}: {b['doc_count']:,}")

print('\nMsg classes encontradas en las últimas 24h:')
for b in res.json().get('aggregations', {}).get('by_class', {}).get('buckets', []):
    print(f"  {b['key']}: {b['doc_count']:,}")
