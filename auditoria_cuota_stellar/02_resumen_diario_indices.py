#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
02: Resumen Diario de Índices, Clases de Mensajes y Dispositivos

Consulta el Elasticsearch Data Lake (/connect/api/data/*/_search)
agregando los documentos por índice físico, msg_class y dev_type.
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
CUST_ID = "e511c3fc54cd4d668bb67612c2ef4b04" # Technoma

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
    # Permite pasar la fecha como argumento YYYY.MM.DD (por defecto hoy)
    target_date = sys.argv[1] if len(sys.argv) > 1 else datetime.now(timezone.utc).strftime("%Y.%m.%d")
    print(f"[*] Analizando distribución de ingesta para fecha: {target_date}")
    
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    query = {
        "size": 0,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": CUST_ID}}
                ]
            }
        },
        "aggs": {
            "by_index": {
                "terms": {"field": "_index", "size": 25}
            },
            "by_msg_class": {
                "terms": {"field": "msg_class.keyword", "size": 15}
            },
            "by_dev_type": {
                "terms": {"field": "dev_type.keyword", "size": 15}
            }
        }
    }
    
    index_pattern = f"*{target_date}*{CUST_ID}*"
    url = f"https://{HOST}/connect/api/data/{index_pattern}/_search"
    
    r = requests.get(url, headers=headers, json=query, verify=False, timeout=60)
    if r.status_code != 200:
        print(f"[-] Error en consulta ({r.status_code}): {r.text[:300]}")
        return
        
    res = r.json()
    total_docs = res.get("hits", {}).get("total", {}).get("value", 0)
    print(f"\n=======================================================")
    print(f"TOTAL DE EVENTOS INGERIDOS ({target_date}): {total_docs:,}")
    print(f"=======================================================")
    
    aggs = res.get("aggregations", {})
    
    print("\n--- 1. Top Índices de Almacenamiento ---")
    for b in aggs.get("by_index", {}).get("buckets", []):
        print(f"  {b['key']:<65}: {b['doc_count']:,} docs")
        
    print("\n--- 2. Top Clases de Mensaje (msg_class) ---")
    for b in aggs.get("by_msg_class", {}).get("buckets", []):
        print(f"  {b['key']:<35}: {b['doc_count']:,} docs")
        
    print("\n--- 3. Top Tipos de Dispositivo (dev_type) ---")
    for b in aggs.get("by_dev_type", {}).get("buckets", []):
        print(f"  {b['key']:<35}: {b['doc_count']:,} docs")

if __name__ == "__main__":
    main()
