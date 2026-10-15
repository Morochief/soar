#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
07: Investigar Activo, IP o Hostname en el Data Lake

Permite auditar el comportamiento de un equipo específico que esté generando
volumen anómalo en el Firewall.

Uso:
  python 07_investigar_activo_o_ip.py <ip_o_hostname> [limite_muestras]

Ejemplos:
  python 07_investigar_activo_o_ip.py 192.168.169.102
  python 07_investigar_activo_o_ip.py 10.11.4.2
  python 07_investigar_activo_o_ip.py 192.168.16.6
  python 07_investigar_activo_o_ip.py BB09C2DPAG00002
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
    if len(sys.argv) < 2:
        print("Uso: python 07_investigar_activo_o_ip.py <ip_o_hostname> [limite_muestras]")
        print("Ejemplo: python 07_investigar_activo_o_ip.py 192.168.169.102")
        return
        
    target = sys.argv[1]
    limit_samples = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    
    print("=" * 70)
    print(f"   AUDITORÍA ESPECÍFICA DE ACTIVO / IP: {target}")
    print("=" * 70)
    
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    # Query aggs + sample docs
    q_filter = {
        "bool": {
            "filter": [
                {"term": {"tenantid": CUST_ID}},
                {
                    "bool": {
                        "should": [
                            {"term": {"srcip_host.keyword": target}},
                            {"term": {"srcip.keyword": target}},
                            {"term": {"dstip_host.keyword": target}},
                            {"term": {"dstip.keyword": target}},
                            {"query_string": {"query": f"\"{target}\""}}
                        ],
                        "minimum_should_match": 1
                    }
                }
            ]
        }
    }
    
    body = {
        "size": limit_samples,
        "query": q_filter,
        "aggs": {
            "by_policy": {"terms": {"field": "fw_policy_id.keyword", "size": 10}},
            "by_action": {"terms": {"field": "action.keyword", "size": 10}},
            "by_dstport": {"terms": {"field": "dstport", "size": 10}},
            "by_dstip": {"terms": {"field": "dstip_host.keyword", "size": 10}},
            "by_appid": {"terms": {"field": "appid_name.keyword", "size": 10}}
        }
    }
    
    url = f"https://{HOST}/connect/api/data/*{CUST_ID}*/_search"
    r = requests.get(url, headers=headers, json=body, verify=False, timeout=60)
    
    if r.status_code != 200:
        print(f"[-] Error en consulta ({r.status_code}): {r.text[:300]}")
        return
        
    res = r.json()
    total = res.get("hits", {}).get("total", {}).get("value", 0)
    print(f"[+] Total de logs encontrados para '{target}': {total:,}\n")
    
    aggs = res.get("aggregations", {})
    
    print("--- Políticas Disparadas ---")
    for b in aggs.get("by_policy", {}).get("buckets", []):
        print(f"  - {b['key']:<25}: {b['doc_count']:>8,} logs")
        
    print("\n--- Acciones Aplicadas ---")
    for b in aggs.get("by_action", {}).get("buckets", []):
        print(f"  - {b['key']:<20}: {b['doc_count']:>8,} logs")

    print("\n--- Puertos Destino Más Solicitados ---")
    for b in aggs.get("by_dstport", {}).get("buckets", []):
        print(f"  - Puerto {b['key']:<15}: {b['doc_count']:>8,} logs")
        
    print("\n--- Principales Destinos ---")
    for b in aggs.get("by_dstip", {}).get("buckets", []):
        print(f"  - {b['key']:<30}: {b['doc_count']:>8,} logs")

    hits = res.get("hits", {}).get("hits", [])
    if hits:
        print(f"\n--- Muestras de Logs Raw (Primeros {len(hits)}) ---")
        for i, h in enumerate(hits, 1):
            s = h.get("_source", {})
            print(f"\n[Muestra #{i}]")
            print(f"  Time: {s.get('timestamp_utc') or s.get('write_time')}")
            print(f"  Flujo: {s.get('srcip')}:{s.get('srcport')} -> {s.get('dstip')}:{s.get('dstport')}")
            print(f"  Regla: {s.get('fw_policy_id')} | Acción: {s.get('action')} | App: {s.get('appid_name')}")
            print(f"  Raw Syslog: {s.get('parser_raw_msg', '')[:200]}")

if __name__ == "__main__":
    main()
