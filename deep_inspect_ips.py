import os
import sys
import json
import base64
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")

def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    return r.json().get("access_token")

jwt = get_jwt()
headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

for ip in ["192.168.15.70", "192.168.9.5"]:
    print(f"\n================ DNS & HTTP Queries for {ip} ================")
    # Buscamos en tráfico DNS de ADR
    url = f"https://{HOST}/connect/api/data/*adr*/_search"
    p = {
        "size": 15,
        "query": {
            "query_string": {
                "query": f'srcip:"{ip}" AND (dstport:53 OR appid_name:dns OR app_path:*dns*)'
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}]
    }
    r = requests.get(url, headers=headers, json=p, timeout=20, verify=False)
    if r.status_code == 200:
        for hit in r.json().get("hits", {}).get("hits", []):
            s = hit.get("_source", {})
            dns_q = s.get("dns", {}).get("query_name") or s.get("dns_query") or s.get("domain") or s.get("dstip_host")
            dns_res = s.get("dns", {}).get("response") or s.get("dns_response")
            print(f"  DNS Req: {dns_q} -> Res: {dns_res}")
    
    # Buscamos nombres de host o certificados TLS en conexiones HTTPS
    p_tls = {
        "size": 10,
        "query": {
            "query_string": {
                "query": f'srcip:"{ip}" AND (appid_name:https OR dstport:443 OR dstport:8889)'
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}]
    }
    r_tls = requests.get(url, headers=headers, json=p_tls, timeout=20, verify=False)
    if r_tls.status_code == 200:
        print(f"--- TLS / HTTP SNI para {ip} ---")
        for hit in r_tls.json().get("hits", {}).get("hits", []):
            s = hit.get("_source", {})
            sni = s.get("tls", {}).get("sni") or s.get("server_name") or s.get("dstip_host") or s.get("domain")
            subj = s.get("tls", {}).get("subject") or s.get("cert_subject")
            dstip = s.get("dstip")
            dstport = s.get("dstport")
            print(f"  Destino: {dstip}:{dstport} | Host/SNI: {sni} | Cert: {subj}")
