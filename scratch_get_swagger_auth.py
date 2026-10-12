import os
import requests
import base64
import urllib3
import json
urllib3.disable_warnings()

host = 'technoma.stellarcyber.cloud'
email = 'kevinmoraes@technoma.com.py'
token = 'rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ'
b64 = base64.b64encode(f'{email}:{token}'.encode()).decode()
jwt = requests.post(f'https://{host}/connect/api/v1/access_token', headers={'Authorization': f'Basic {b64}', 'Content-Type': 'application/json'}, json={}, verify=False).json().get('access_token')
auth = {'Authorization': f'Bearer {jwt}'}

for ep in ['api-docs', 'doc']:
    r = requests.get(f'https://{host}/connect/api/v1/{ep}', headers=auth, verify=False)
    print(f"{ep} -> {r.status_code} ({r.headers.get('content-type', '')})")
    try:
        data = r.json()
        print(f"  JSON keys: {list(data.keys())}")
        if 'paths' in data:
            print(f"  TOTAL PATHS IN SWAGGER: {len(data['paths'])}")
            with open('G:/SOC/soar/stellar_api_swagger.json', 'w', encoding='utf-8') as f_out:
                json.dump(data, f_out, indent=2)
            print("  SAVED FULL SWAGGER TO G:/SOC/soar/stellar_api_swagger.json !")
    except Exception:
        print(r.text[:300])
