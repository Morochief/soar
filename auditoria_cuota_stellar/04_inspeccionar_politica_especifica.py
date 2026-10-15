#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
04: Inspeccionar Muestras de una Política Específica de FortiGate

Uso:
  python 04_inspeccionar_politica_especifica.py <fw_policy_id> [fecha_YYYY.MM.DD]

Ejemplo:
  python 04_inspeccionar_politica_especifica.py FG-Technoma_91
"""

import os
import requests
import json
import base64
import sys
from datetime import datetime, timezone
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "")
CUST_ID = "e511c3fc54cd4d668bb67612c2ef4b04"

def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando: {r.text}")
        exit(1)
    return r.json().get("access_token")

def main():
    if len(sys.argv) < 2:
        print("Uso: python 04_inspeccionar_politica_especifica.py <fw_policy_id> [fecha_YYYY.MM.DD]")
        print("Ejemplo: python 04_inspeccionar_politica_especifica.py FG-Technoma_91")
        return
        
    policy_id = sys.argv[1]
    target_date = sys.argv[2] if len(sys.argv) > 2 else datetime.now(timezone.utc).strftime("%Y.%m.%d")
    
    print(f"[*] Inspeccionando política: {policy_id} para fecha: {target_date}...")
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    query = {
        "size": 3,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": CUST_ID}},
                    {"term": {"fw_policy_id.keyword": policy_id}}
                ]
            }
        }
    }
    
    target_index = f"*{target_date}*{CUST_ID}*"
    url = f"https://{HOST}/connect/api/data/{target_index}/_search"
    
    r = requests.get(url, headers=headers, json=query, verify=False, timeout=30)
    if r.status_code != 200:
        print(f"[-] Error en consulta ({r.status_code}): {r.text[:300]}")
        return
        
    res = r.json()
    hits = res.get("hits", {}).get("hits", [])
    total = res.get("hits", {}).get("total", {}).get("value", 0)
    
    print(f"\n[+] Total de hits encontrados: {total:,}")
    if not hits:
        print("[-] No se encontraron registros de muestra.")
        return
        
    for i, h in enumerate(hits, 1):
        s = h.get("_source", {})
        fn = s.get("fortinet", {})
        print(f"\n--- Muestra #{i} (Index: {h.get('_index')}) ---")
        print(f"  Fecha/Hora: {s.get('timestamp_utc') or s.get('write_time')}")
        print(f"  Acción: {s.get('action')} | Tipo: {fn.get('type')} | Subtipo: {fn.get('subtype')}")
        print(f"  Origen: {s.get('srcip')}:{s.get('srcport')} (Intf: {fn.get('srcintf')})")
        print(f"  Destino: {s.get('dstip')}:{s.get('dstport')} (Intf: {fn.get('dstintf')})")
        print(f"  App / Servicio: {s.get('appid_name')} / {s.get('service')}")
        print(f"  Mensaje Syslog Raw:\n    {s.get('parser_raw_msg')}")

if __name__ == "__main__":
    main()
