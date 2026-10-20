import sys
import json
import base64
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

res = requests.get(f'https://{HOST}/connect/api/v1/queries', headers=h, verify=False)
queries = res.json().get('data', [])
print(f'Total queries: {len(queries)}')
for q in queries:
    name = q.get('name', '')
    print(f"{name} | {q.get('query')}")
