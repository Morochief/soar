import sys
import json
import base64
import time
import requests

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

for p in [1280, 8010, 6180]:
    payload = {
        'size': 0,
        'query': {
            'bool': {
                'filter': [{'term': {'tenantid': TENANT_ID}}],
                'must': [
                    {'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}},
                    {'term': {'dstport': p}}
                ]
            }
        },
        'aggs': {
            'by_action': {'terms': {'field': 'action.keyword', 'size': 5}},
            'by_dst': {'terms': {'field': 'dstip.keyword', 'size': 5}},
            'by_src': {'terms': {'field': 'srcip.keyword', 'size': 5}}
        }
    }
    url = f"https://{HOST}/connect/api/data/*adr*{TENANT_ID}*/_search"
    res = requests.get(url, headers=h, json=payload, verify=False).json()
    total = res.get('hits', {}).get('total', {}).get('value', 0)
    print(f"=== PUERTO {p} (Total: {total:,} logs) ===")
    actions = [f"{b['key']}: {b['doc_count']:,}" for b in res.get('aggregations', {}).get('by_action', {}).get('buckets', [])]
    dsts = [f"{b['key']}: {b['doc_count']:,}" for b in res.get('aggregations', {}).get('by_dst', {}).get('buckets', [])]
    srcs = [f"{b['key']}: {b['doc_count']:,}" for b in res.get('aggregations', {}).get('by_src', {}).get('buckets', [])]
    print('  Acciones:', ', '.join(actions))
    print('  Destinos:', ', '.join(dsts))
    print('  Orígenes:', ', '.join(srcs))
