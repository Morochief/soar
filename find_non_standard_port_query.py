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

queries_to_test = [
    'appid_stdport:"no"',
    'appid_stdport:no',
    'appid_stdport:false',
    'is_stdport:false',
    'is_stdport:"no"',
    'non_standard_port:true',
    'tags:*port*',
    'tags:*non_standard*',
    'xdr_event.display_name:*Port*',
    'xdr_event.display_name:*Non-Standard*',
    'xdr_event.display_name:*Non-standard*',
    'stellar_alert_type:*port*',
    'msg_class:*port*'
]

print("=== BUSCANDO LA QUERY QUE DA EXACTAMENTE 2 HITS ===")
for idx in ['*adr*', '*ser*']:
    url = f"https://{HOST}/connect/api/data/{idx}e511c3fc54cd4d668bb67612c2ef4b04*/_search"
    for q_try in queries_to_test:
        payload = {
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
        res = requests.get(url, headers=h, json=payload, verify=False).json()
        val = res.get('hits', {}).get('total', {}).get('value', 0)
        if val > 0:
            print(f"[{idx}] {q_try} -> {val} hits")
            if val == 2:
                print(f"🎯 ¡MATCH EXACTO DE 2 HITS ENCONTRADO!: {q_try} en {idx}")
                for hit in res.get('hits', {}).get('hits', []):
                    s = hit['_source']
                    print("  Detalle:", s.get('timestamp'), s.get('srcip'), '->', s.get('dstip'), 'port:', s.get('dstport'), 'app:', s.get('appid_name'), 'event:', s.get('xdr_event', {}).get('display_name'))
