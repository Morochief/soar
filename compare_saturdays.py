import sys
import json
import base64
import time
import requests
from datetime import datetime, timezone

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
# Hoy sábado 17/10 desde las 00:00 GMT-3 (03:00 UTC)
today_start_ms = int(datetime(2026, 10, 17, 3, 0, 0, tzinfo=timezone.utc).timestamp() * 1000)
# Sábado pasado 10/10 a la misma hora (00:00 a 12:38 GMT-3)
past_sat_start_ms = int(datetime(2026, 10, 10, 3, 0, 0, tzinfo=timezone.utc).timestamp() * 1000)
past_sat_end_ms = past_sat_start_ms + (now_ms - today_start_ms)

def query_stats(start, end, label):
    payload = {
        'size': 0,
        'query': {
            'bool': {
                'filter': [{'term': {'tenantid': 'e511c3fc54cd4d668bb67612c2ef4b04'}}],
                'must': [{'range': {'timestamp': {'gte': start, 'lte': end}}}]
            }
        },
        'aggs': {
            'by_class': {
                'terms': {'field': 'msg_class.keyword', 'size': 10}
            },
            'by_action': {
                'terms': {'field': 'action.keyword', 'size': 10}
            }
        }
    }
    url = f'https://{HOST}/connect/api/data/*adr*e511c3fc54cd4d668bb67612c2ef4b04*/_search'
    res = requests.get(url, headers=h, json=payload, verify=False)
    data = res.json()
    total = data.get('hits', {}).get('total', {}).get('value', 0)
    print(f'=== {label} ===')
    print(f'Total Eventos Firewall/Sensor: {total:,}')
    for b in data.get('aggregations', {}).get('by_class', {}).get('buckets', []):
        print(f"  Class {b['key']}: {b['doc_count']:,}")
    print('  Acciones principales:')
    for a in data.get('aggregations', {}).get('by_action', {}).get('buckets', []):
        print(f"    {a['key']}: {a['doc_count']:,}")
    print()

query_stats(past_sat_start_ms, past_sat_end_ms, 'SÁBADO PASADO (10/10/2026) - Misma Franja Horaria (00:00 a 12:38)')
query_stats(today_start_ms, now_ms, 'HOY SÁBADO (17/10/2026) - Con Filtros Activos (00:00 a 12:38)')
