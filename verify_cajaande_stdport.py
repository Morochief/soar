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
TENANT_ID = '392cf7319d694d53889280340fff51e9' # CAJA ANDE

auth_str = f"{EMAIL}:{TOKEN}"
auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
jwt = r.json().get("access_token")
h = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

now_ms = int(time.time() * 1000)
start_ms = now_ms - (24 * 3600 * 1000)

query_str = 'appid_stdport:"no"'
payload = {
    'track_total_hits': True,
    'size': 5,
    'query': {
        'bool': {
            'filter': [{'term': {'tenantid': TENANT_ID}}],
            'must': [
                {'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}},
                {'query_string': {'query': query_str}}
            ]
        }
    }
}
url = f"https://{HOST}/connect/api/data/*adr*{TENANT_ID}*/_search"
res = requests.get(url, headers=h, json=payload, verify=False).json()
total = res.get('hits', {}).get('total', {}).get('value', 0)
print(f"🎯 Total hits para '{query_str}' en CAJA ANDE: {total}")
for hit in res.get('hits', {}).get('hits', []):
    s = hit['_source']
    print(f"  {s.get('srcip')} -> {s.get('dstip')} | Port: {s.get('dstport')} | App: {s.get('appid_name')} | Score: {s.get('flow_score')}")
