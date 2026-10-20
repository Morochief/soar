import os
import sys
import json
import base64
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HOST = 'technoma.stellarcyber.cloud'
EMAIL = 'kevinmoraes@technoma.com.py'
TOKEN = 'rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ'
auth_str = f'{EMAIL}:{TOKEN}'
auth_b64 = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {auth_b64}', 'Content-Type': 'application/x-www-form-urlencoded'}
jwt = requests.post(f'https://{HOST}/connect/api/v1/access_token', headers=headers, json={}, timeout=15, verify=False).json().get('access_token')
auth_hdr = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

queries = [
    'appid_stdport:"no"',
    'appid_stdport:"no" AND tenantid:"392cf7319d694d53889280340fff51e9"',
    'appid_stdport:"no" AND dstport:8889',
    'appid_stdport:"no" AND flow_score:98',
    'appid_stdport:"no" AND state:"Aborted"',
    'appid_stdport:"no" AND appid_family:"Web"',
    'xdr_event.display_name:*Non-Standard*',
    'tags:*non_standard*'
]
for q in queries:
    url = f'https://{HOST}/connect/api/data/*adr*/_search'
    p = {'track_total_hits': True, 'size': 0, 'query': {'query_string': {'query': q}}}
    res = requests.get(url, headers=auth_hdr, json=p, timeout=15, verify=False).json()
    val = res.get('hits', {}).get('total', {}).get('value')
    print(f'{q} --> {val}')
