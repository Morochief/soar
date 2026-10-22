import sys
import json
import base64
import time
import requests
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

for idx in ['*interim*', '*ade*', '*ser*', '*adr*']:
    url = f"https://{HOST}/connect/api/data/{idx}e511c3fc54cd4d668bb67612c2ef4b04*/_search"
    for q_try in [
        'tags:*port*',
        'tags:*std*',
        'tags:*non*',
        'appid_stdport:"no"',
        'xdr_event.display_name:*Port*',
        'xdr_event.display_name:*port*',
        'xdr_event.name:*port*'
    ]:
        p = {
            'track_total_hits': True,
            'size': 2,
            'query': {
                'bool': {
                    'filter': [{'term': {'tenantid': TENANT_ID}}],
                    'must': [
                        {'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}},
                        {'query_string': {'query': q_try}}
                    ]
                }
            }
        }
        res = requests.get(url, headers=h, json=p, verify=False).json()
        val = res.get('hits', {}).get('total', {}).get('value', 0)
        if val > 0:
            print(f"[{idx}] {q_try} -> {val} hits")
            if val == 2:
                print(f"🎯 MATCH EXACTO 2 HITS EN {idx}: {q_try}")
                for hit in res.get('hits', {}).get('hits', []):
                    s = hit['_source']
                    print("  Hit:", s.get('timestamp'), s.get('srcip'), '->', s.get('dstip'), 'port:', s.get('dstport'), s.get('appid_name'), s.get('msg_class'))
