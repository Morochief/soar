import sys
import json
import base64
import time
import requests
from datetime import datetime
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

url = f"https://{HOST}/connect/api/data/*adr*{TENANT_ID}*/_search"
payload = {
    'size': 0,
    'query': {
        'bool': {
            'filter': [{'term': {'tenantid': TENANT_ID}}],
            'must': [
                {'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}},
                {'term': {'msg_class.keyword': 'firewall'}}
            ]
        }
    },
    'aggs': {
        'top_policies': {'terms': {'field': 'fw_policy_id', 'size': 10}},
        'dns_actions': {
            'filter': {'term': {'dstport': 53}},
            'aggs': {
                'acts': {'terms': {'field': 'action.keyword', 'size': 5}},
                'top_src': {'terms': {'field': 'srcip.keyword', 'size': 5}},
                'top_dst': {'terms': {'field': 'dstip.keyword', 'size': 5}}
            }
        },
        'https_actions': {
            'filter': {'term': {'dstport': 443}},
            'aggs': {
                'acts': {'terms': {'field': 'action.keyword', 'size': 5}},
                'top_src': {'terms': {'field': 'srcip.keyword', 'size': 5}}
            }
        },
        'port_1280': {
            'filter': {'term': {'dstport': 1280}},
            'aggs': {
                'acts': {'terms': {'field': 'action.keyword', 'size': 5}},
                'top_src': {'terms': {'field': 'srcip.keyword', 'size': 5}},
                'top_dst': {'terms': {'field': 'dstip.keyword', 'size': 5}}
            }
        }
    }
}
res = requests.get(url, headers=h, json=payload, verify=False).json()
print("Top Políticas de Firewall (por fw_policy_id):")
for b in res.get('aggregations', {}).get('top_policies', {}).get('buckets', []):
    print(f"  Policy ID {b['key']}: {b['doc_count']:,} logs")

print("\nAcciones en Puerto 53 (DNS - 607k logs):")
for b in res.get('aggregations', {}).get('dns_actions', {}).get('acts', {}).get('buckets', []):
    print(f"  - Action {b['key']}: {b['doc_count']:,} logs")
print("  Top IPs Origen consultando DNS:")
for b in res.get('aggregations', {}).get('dns_actions', {}).get('top_src', {}).get('buckets', []):
    print(f"    * {b['key']}: {b['doc_count']:,} logs")
print("  Top Servidores DNS Destino:")
for b in res.get('aggregations', {}).get('dns_actions', {}).get('top_dst', {}).get('buckets', []):
    print(f"    * {b['key']}: {b['doc_count']:,} logs")

print("\nAcciones en Puerto 443 (HTTPS - 612k logs):")
for b in res.get('aggregations', {}).get('https_actions', {}).get('acts', {}).get('buckets', []):
    print(f"  - Action {b['key']}: {b['doc_count']:,} logs")
print("  Top IPs Origen generando HTTPS:")
for b in res.get('aggregations', {}).get('https_actions', {}).get('top_src', {}).get('buckets', []):
    print(f"    * {b['key']}: {b['doc_count']:,} logs")

print("\nAcciones en Puerto 1280 (161k logs):")
for b in res.get('aggregations', {}).get('port_1280', {}).get('acts', {}).get('buckets', []):
    print(f"  - Action {b['key']}: {b['doc_count']:,} logs")
print("  Top Destinos en Puerto 1280:")
for b in res.get('aggregations', {}).get('port_1280', {}).get('top_dst', {}).get('buckets', []):
    print(f"    * {b['key']}: {b['doc_count']:,} logs")
