import os
import json
import base64
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "technoma.stellarcyber.cloud"
EMAIL = "kevinmoraes@technoma.com.py"
TOKEN = "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ"

auth_str = f"{EMAIL}:{TOKEN}"
b64_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Authorization": f"Basic {b64_auth}",
    "Content-Type": "application/json"
}

r_auth = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, verify=False, timeout=30)
jwt_token = r_auth.json().get("access_token")

headers_jwt = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}

r_tenants = requests.get(f"https://{HOST}/connect/api/v1/tenants", headers=headers_jwt, verify=False, timeout=30)
data = r_tenants.json()
tenants = data if isinstance(data, list) else data.get("data", [])
cust_id = tenants[0].get("cust_id") or tenants[0].get("id") or tenants[0].get("uuid")

query_payload = {
    "name": "Hunt_Hostname",
    "cust_id": cust_id,
    "conditions": {
        "modifier": "and",
        "conditions": [
            {"type": "query_string", "value": ["172.17.10.124"]}
        ]
    }
}

r_query = requests.post(f"https://{HOST}/connect/api/v1/queries", headers=headers_jwt, json=query_payload, verify=False, timeout=60)
data = r_query.json()
hits = data.get("hits", {}).get("hits", [])

import json
print(json.dumps(hits[0].get("_source", {}), indent=2))

