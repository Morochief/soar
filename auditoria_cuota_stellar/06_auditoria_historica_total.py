#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
06: Auditoría Histórica Total de Firewall (Data Lake & Threat Hunting Library)

Genera la radiografía consolidada de todo el pozo de firewall (106.3M de eventos):
- Top 15 Políticas de Firewall
- Top 15 Equipos de Origen (Top Sources)
- Top 15 Destinos / Servidores (Top Destinations)
- Distribución de Acciones (Permitido vs Denegado)
- Correlación exacta con la vista "Threat Hunting Library -> Firewall"
"""

import os
import requests
import json
import base64
import sys
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
    print("=" * 75)
    print("  AUDITORÍA HISTÓRICA COMPLETA DE FORTIGATE (THREAT HUNTING DATA LAKE)")
    print("=" * 75)
    print(f"[*] Consultando Data Lake de Stellar Cyber para Technoma...")
    
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    agg_query = {
        "size": 0,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": CUST_ID}},
                    {"term": {"dev_type.keyword": "fw_fortigate"}}
                ]
            }
        },
        "aggs": {
            "top_policies": {"terms": {"field": "fw_policy_id.keyword", "size": 15}},
            "top_sources": {"terms": {"field": "srcip_host.keyword", "size": 15}},
            "top_destinations": {"terms": {"field": "dstip_host.keyword", "size": 15}},
            "top_actions": {"terms": {"field": "action.keyword", "size": 10}},
            "top_subtypes": {"terms": {"field": "fortinet.subtype.keyword", "size": 10}}
        }
    }
    
    url = f"https://{HOST}/connect/api/data/*{CUST_ID}*/_search"
    r = requests.get(url, headers=headers, json=agg_query, verify=False, timeout=60)
    
    if r.status_code != 200:
        print(f"[-] Error en consulta ({r.status_code}): {r.text[:300]}")
        return
        
    res = r.json()
    aggs = res.get("aggregations", {})
    
    print("\n--- 1. TOP 15 POLÍTICAS DEL FIREWALL (Mayor Impacto en Cuota) ---")
    for idx, b in enumerate(aggs.get("top_policies", {}).get("buckets", []), 1):
        print(f"  {idx:2d}. {b['key']:<28}: {b['doc_count']:>12,} logs")
        
    print("\n--- 2. TOP 15 EQUIPOS / IPs DE ORIGEN (Top Talkers) ---")
    for idx, b in enumerate(aggs.get("top_sources", {}).get("buckets", []), 1):
        print(f"  {idx:2d}. {b['key']:<32}: {b['doc_count']:>12,} logs")

    print("\n--- 3. TOP 15 DESTINOS Y SERVIDORES ---")
    for idx, b in enumerate(aggs.get("top_destinations", {}).get("buckets", []), 1):
        print(f"  {idx:2d}. {b['key']:<45}: {b['doc_count']:>12,} logs")
        
    print("\n--- 4. ACCIONES REGISTRADAS (Permitido vs Denegado) ---")
    for idx, b in enumerate(aggs.get("top_actions", {}).get("buckets", []), 1):
        print(f"  {idx:2d}. {b['key']:<20}: {b['doc_count']:>12,} logs")

    print("\n--- 5. SUBTIPOS DE TELEMETRÍA FORTIOS ---")
    for idx, b in enumerate(aggs.get("top_subtypes", {}).get("buckets", []), 1):
        print(f"  {idx:2d}. {b['key']:<20}: {b['doc_count']:>12,} logs")

if __name__ == "__main__":
    main()
