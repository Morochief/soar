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

try:
    r_auth = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, verify=False, timeout=30)
    r_auth.raise_for_status()
    jwt_token = r_auth.json().get("access_token")
except Exception as e:
    print(f"[-] Error en autenticacion: {e}")
    exit(1)

headers_jwt = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}

# 2. Obtener tenant_id (cust_id)
print("[*] Obteniendo Tenant ID...")
try:
    r_tenants = requests.get(f"https://{HOST}/connect/api/v1/tenants", headers=headers_jwt, verify=False, timeout=30)
    r_tenants.raise_for_status()
    
    # Podría devolver una lista directamente o un dict con "data"
    data = r_tenants.json()
    if isinstance(data, list):
        tenants = data
    else:
        tenants = data.get("data", [])
        
    if not tenants:
        print("[-] No hay tenants configurados.")
        exit(1)
        
    cust_id = tenants[0].get("cust_id") or tenants[0].get("id") or tenants[0].get("uuid")
    print(f"[+] Tenant encontrado: {tenants[0].get('name', 'Desconocido')} (ID: {cust_id})")
except Exception as e:
    print(f"[-] Error obteniendo tenants: {e}")
    exit(1)

# 3. Hacer la busqueda
query_payload = {
    "name": "Hunt_Patient_Zero",
    "cust_id": cust_id,
    "conditions": {
        "modifier": "and",
        "conditions": [
            {"type": "query_string", "value": ["srcip:\"172.17.10.124\" AND (dstport:80 OR dstport:443) AND timestamp:[\"2026-07-07T20:40:00.000Z\" TO \"2026-07-07T20:57:00.000Z\"]"]}
        ]
    }
}

print("[*] Ejecutando busqueda en Stellar Cyber con L7 Interflow...")
try:
    r_query = requests.post(f"https://{HOST}/connect/api/v1/queries", headers=headers_jwt, json=query_payload, verify=False, timeout=60)
    r_query.raise_for_status()
    data = r_query.json()
    hits = data.get("hits", {}).get("hits", [])
    
    print(f"[*] Se encontraron {data.get('hits', {}).get('total', {}).get('value', 0)} registros.")
    print("-" * 60)
    
    urls_encontradas = set()
    
    for h in hits:
        src = h.get("_source", {})
        dstip = src.get("dstip", "?")
        # Campos de Stellar Cyber Interflow
        host_header = src.get("http", {}).get("host") or src.get("http_host")
        url = src.get("http", {}).get("url") or src.get("http_url")
        tls_sni = src.get("tls", {}).get("sni") or src.get("sni") or src.get("dns_name")
        
        info = tls_sni or host_header or url
        if info:
            urls_encontradas.add(f"{dstip:<15} -> {info}")
            
    if urls_encontradas:
        print("[*] Dominios extraidos (SNI/HTTP Host):")
        for u in urls_encontradas:
            print(f"    {u}")
    else:
        print("[-] No se encontro informacion L7 util en estos registros.")
        
except Exception as e:
    print(f"[-] Error en la query: {e}")
