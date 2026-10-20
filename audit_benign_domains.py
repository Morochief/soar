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
start_ms = now_ms - (6 * 3600 * 1000)

filt_res = requests.get(f'https://{HOST}/connect/api/v1/log_filters/6ad0f8dfaa734118df02d27e', headers=h, verify=False)
current_filter = json.loads(filt_res.json()['data']['content'])
current_domains = set(current_filter['rules']['url']['value'])
print(f'Actualmente en el filtro hay {len(current_domains)} dominios configurados.')

payload = {
    'size': 0,
    'query': {
        'bool': {
            'filter': [
                {'term': {'tenantid': 'e511c3fc54cd4d668bb67612c2ef4b04'}}
            ],
            'must': [
                {'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}},
                {'term': {'msg_class.keyword': 'traffic'}},
                {'term': {'action.keyword': 'passthrough'}}
            ]
        }
    },
    'aggs': {
        'top_urls': {
            'terms': {
                'field': 'url.keyword',
                'size': 60
            }
        },
        'top_dst_hosts': {
            'terms': {
                'field': 'dst_host.keyword',
                'size': 60
            }
        }
    }
}

url = f"https://{HOST}/connect/api/data/*adr*e511c3fc54cd4d668bb67612c2ef4b04*/_search"
res = requests.get(url, headers=h, json=payload, verify=False)

if res.status_code == 200:
    res_data = res.json()
    urls = res_data.get('aggregations', {}).get('top_urls', {}).get('buckets', [])
    hosts = res_data.get('aggregations', {}).get('top_dst_hosts', {}).get('buckets', [])
    
    print('\n=== DOMINIOS EN PASSTHROUGH (ÚLTIMAS 6 HORAS) ===')
    print('--- No incluidos todavía en el filtro de descarte ---')
    for u in urls:
        dom = u['key']
        already_covered = any(cd in dom for cd in current_domains)
        if not already_covered:
            print(f'  [NUEVO CANDIDATO URL] {dom}: {u["doc_count"]} hits')
            
    print('\n--- TOP HOSTS DESTINO EN PASSTHROUGH ---')
    for h_item in hosts:
        dom = h_item['key']
        already_covered = any(cd in dom for cd in current_domains)
        if not already_covered:
            print(f'  [NUEVO CANDIDATO HOST] {dom}: {h_item["doc_count"]} hits')
else:
    print('Error:', res.status_code, res.text[:300])
