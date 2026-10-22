import sys
import json
import base64
import requests
from datetime import datetime, timezone
from urllib.parse import urlparse

HOST = 'technoma.stellarcyber.cloud'
EMAIL = 'kevinmoraes@technoma.com.py'
TOKEN = 'rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ'
auth_str = f'{EMAIL}:{TOKEN}'
auth_b64 = base64.b64encode(auth_str.encode()).decode()
headers = {'Authorization': f'Basic {auth_b64}', 'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.post(f'https://{HOST}/connect/api/v1/access_token', headers=headers, json={}, verify=False)
jwt = r.json()['access_token']
h = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

# Obtener lista actual de los 43 dominios en el filtro
filt_res = requests.get(f'https://{HOST}/connect/api/v1/log_filters/6ad0f8dfaa734118df02d27e', headers=h, verify=False)
current_filter = json.loads(filt_res.json()['data']['content'])
current_domains = set(current_filter['rules']['url']['value'])
print(f'Dominios actualmente en filtro: {len(current_domains)}')

# Rango de ayer viernes 16/10 completo (00:00:00 a 23:59:59 GMT-3 -> 03:00 UTC 16/10 a 03:00 UTC 17/10)
start_ms = int(datetime(2026, 10, 16, 3, 0, 0, tzinfo=timezone.utc).timestamp() * 1000)
end_ms = int(datetime(2026, 10, 17, 3, 0, 0, tzinfo=timezone.utc).timestamp() * 1000)

payload = {
    'size': 0,
    'query': {
        'bool': {
            'filter': [{'term': {'tenantid': 'e511c3fc54cd4d668bb67612c2ef4b04'}}],
            'must': [
                {'range': {'timestamp': {'gte': start_ms, 'lte': end_ms}}},
                {'term': {'action.keyword': 'passthrough'}}
            ]
        }
    },
    'aggs': {
        'top_urls': {
            'terms': {
                'field': 'url.keyword',
                'size': 150
            }
        },
        'top_dst_hosts': {
            'terms': {
                'field': 'dst_host.keyword',
                'size': 150
            }
        }
    }
}

url = f'https://{HOST}/connect/api/data/*adr*e511c3fc54cd4d668bb67612c2ef4b04*/_search'
res = requests.get(url, headers=h, json=payload, verify=False)

if res.status_code == 200:
    res_data = res.json()
    urls = res_data.get('aggregations', {}).get('top_urls', {}).get('buckets', [])
    hosts = res_data.get('aggregations', {}).get('top_dst_hosts', {}).get('buckets', [])
    total_passthrough = res_data.get('hits', {}).get('total', {}).get('value', 0)
    print(f'Total de eventos passthrough el día de ayer (16/10): {total_passthrough:,}')
    
    # Agrupar por dominio base para no repetir subdominios
    unfiltered_domains = {}
    for u in urls:
        raw_url = u['key']
        count = u['doc_count']
        # extraer host / netloc
        try:
            if not raw_url.startswith('http'):
                dom = raw_url.split('/')[0]
            else:
                dom = urlparse(raw_url).netloc
        except:
            dom = raw_url
        
        # verificar si ya esta cubierto por la lista de 43
        is_covered = any(cd in dom for cd in current_domains)
        if not is_covered:
            unfiltered_domains[dom] = unfiltered_domains.get(dom, 0) + count

    print('\n=== DOMINIOS NO FILTRADOS EN PASSTHROUGH (VIERNES 16/10) ===')
    sorted_doms = sorted(unfiltered_domains.items(), key=lambda x: x[1], reverse=True)
    for d, c in sorted_doms[:35]:
        print(f'{d}: {c:,} eventos')
else:
    print('Error:', res.status_code, res.text[:300])
