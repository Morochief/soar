#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
03: Auditoría Deep Dive de Syslogs de FortiGate

Analiza a fondo la ingesta de FortiGate:
- Subtipos (forward, webfilter, ssl, local)
- Acciones (accept, deny, passthrough, close, rst)
- Top de Políticas / Reglas de Firewall generadoras
- Interfaces de origen y destino
- Puertos y Aplicaciones
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
    target_date = sys.argv[1] if len(sys.argv) > 1 else datetime.now(timezone.utc).strftime("%Y.%m.%d")
    print(f"[*] Ejecutando Deep Dive de FortiGate para fecha: {target_date}...")
    
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
            "by_subtype": {"terms": {"field": "fortinet.subtype.keyword", "size": 10}},
            "by_action": {"terms": {"field": "action.keyword", "size": 15}},
            "by_policy": {"terms": {"field": "fw_policy_id.keyword", "size": 20}},
            "by_srcintf": {"terms": {"field": "fortinet.srcintf.keyword", "size": 15}},
            "by_dstintf": {"terms": {"field": "fortinet.dstintf.keyword", "size": 15}},
            "by_port": {"terms": {"field": "dstport", "size": 15}},
            "by_app": {"terms": {"field": "appid_name.keyword", "size": 15}}
        }
    }
    
    target_index = f"*{target_date}*{CUST_ID}*"
    url = f"https://{HOST}/connect/api/data/{target_index}/_search"
    
    r = requests.get(url, headers=headers, json=agg_query, verify=False, timeout=60)
    if r.status_code != 200:
        print(f"[-] Error en consulta ({r.status_code}): {r.text[:300]}")
        return
        
    res = r.json()
    total_fg = res.get("hits", {}).get("total", {}).get("value", 0)
    
    print("\n" + "=" * 70)
    print(f"   AUDITORIA FORENSE DE SYSLOGS FORTIGATE - {target_date}")
    print(f"   Total de Logs Ingeridos: {total_fg:,}")
    print("=" * 70)
    
    if total_fg == 0:
        print("[-] No se encontraron registros de FortiGate para la fecha especificada.")
        return
        
    aggs = res.get("aggregations", {})
    
    print("\n[1] SUBTIPOS DE FORTIGATE:")
    for b in aggs.get("by_subtype", {}).get("buckets", []):
        pct = (b['doc_count'] / total_fg) * 100
        print(f"  - {b['key']:<20}: {b['doc_count']:>10,} logs ({pct:>5.1f}%)")
        
    print("\n[2] ACCIONES DE FIREWALL:")
    for b in aggs.get("by_action", {}).get("buckets", []):
        pct = (b['doc_count'] / total_fg) * 100
        print(f"  - {b['key']:<20}: {b['doc_count']:>10,} logs ({pct:>5.1f}%)")
        
    print("\n[3] TOP POLÍTICAS / REGLAS GENERADORAS:")
    for b in aggs.get("by_policy", {}).get("buckets", []):
        pct = (b['doc_count'] / total_fg) * 100
        print(f"  - {b['key']:<25}: {b['doc_count']:>10,} logs ({pct:>5.1f}%)")
        
    print("\n[4] TOP INTERFACES DE ORIGEN:")
    for b in aggs.get("by_srcintf", {}).get("buckets", []):
        pct = (b['doc_count'] / total_fg) * 100
        print(f"  - {b['key']:<20}: {b['doc_count']:>10,} logs ({pct:>5.1f}%)")
        
    print("\n[5] TOP PUERTOS DESTINO:")
    for b in aggs.get("by_port", {}).get("buckets", []):
        pct = (b['doc_count'] / total_fg) * 100
        print(f"  - Puerto {b['key']:<15}: {b['doc_count']:>10,} logs ({pct:>5.1f}%)")

if __name__ == "__main__":
    main()
