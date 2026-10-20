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

for card_name, lucene in [
    ('Windows Logins', 'event.code:4624 OR event_data.LogonType:*'),
    ('Windows Privilege Escalations', 'event.code:4672'),
    ('Windows New Processes', 'event.code:4688'),
    ('Windows Command Line', 'event.code:4688 AND _exists_:event_data.CommandLine'),
    ('Windows Login Failures', 'event.code:4625 OR login_result:fail'),
    ('Windows Account Changes', 'event.code:(4720 OR 4722 OR 4724 OR 4738)')
]:
    payload = {
        'track_total_hits': True,
        'size': 0,
        'query': {
            'bool': {
                'filter': [{'term': {'tenantid': 'e511c3fc54cd4d668bb67612c2ef4b04'}}],
                'must': [
                    {'range': {'timestamp': {'gte': start_ms, 'lte': now_ms}}},
                    {'query_string': {'query': lucene}}
                ]
            }
        }
    }
    url = f'https://{HOST}/connect/api/data/*wineventlog*e511c3fc54cd4d668bb67612c2ef4b04*/_search'
    res = requests.get(url, headers=h, json=payload, verify=False)
    val = res.json().get('hits', {}).get('total', {}).get('value', 0)
    print(f'{card_name}: {val:,}')
