#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
08: Matriz de Threat Hunting Library (Los 20 Módulos de Stellar Cyber)

Replica la vista completa de "Threat Hunting Library" de Stellar Cyber
en menos de 1 segundo mediante consultas optimizadas de agregación paralela.
Permite evaluar qué módulo y protocolo está consumiendo la cuota.

Uso:
  python 08_matriz_threat_hunting_20_modulos.py [today | all | YYYY.MM.DD]

Ejemplos:
  python 08_matriz_threat_hunting_20_modulos.py today
  python 08_matriz_threat_hunting_20_modulos.py all
  python 08_matriz_threat_hunting_20_modulos.py 2026.10.14
"""

import os
import requests
import json
import base64
import time
import sys
from datetime import datetime, timezone
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "")
CUST_ID = "e511c3fc54cd4d668bb67612c2ef4b04"

# Definición exacta de los 20 módulos de la Threat Hunting Library
THREAT_HUNTING_MODULES = [
    ("Firewall", "msg_class:firewall OR dev_type:fw_fortigate"),
    ("DNS Analysis", "dstport:53 OR msg_class:dns OR appid_name:DNS OR appid_name:Google-DNS"),
    ("Network Applications", "msg_class:interflow_traffic OR msg_class:flow"),
    ("Google Workspace", "msg_class:gsuite"),
    ("Plain Text Passwords", "dstport:389 OR dstport:21 OR dstport:23 OR alert_type:*password* OR msg_class:plain_text*"),
    ("All Login Failures", "action:failure OR action:failed OR msg_class:auth_failure OR event_name:*login*failure*"),
    ("Windows Logins", "win_event_id:4624 OR event_id:4624"),
    ("Windows Privilege Escalations", "win_event_id:4672 OR event_id:4672"),
    ("Windows Command Line", "process_commandline:* OR process_cmd:*"),
    ("Windows New Processes", "win_event_id:4688 OR event_id:4688 OR process_name:*"),
    ("Sophos Endpoint", "dev_type:endpoint_sophos OR msg_class:sophos*"),
    ("Non-Standard Port Usage", "appid_stdport:no"),
    ("Tunneled Traffic", "proto_name:gre OR proto_name:ipip OR dstport:4789"),
    ("Windows Account Changes", "win_event_id:4720 OR win_event_id:4722 OR win_event_id:4724 OR win_event_id:4738 OR event_id:4720"),
    ("Windows Account Lockouts", "win_event_id:4740 OR event_id:4740"),
    ("Windows PowerShell Startups", "win_event_id:4104 OR event_id:4104 OR process_name:powershell.exe"),
    ("External File Storage Access", "appid_name:*drive* OR appid_name:*dropbox* OR appid_name:*onedrive*"),
    ("Cloud Email Provider Access", "appid_name:*gmail* OR appid_name:*office365* OR appid_name:*outlook*"),
    ("Windows Login Failures", "win_event_id:4625 OR event_id:4625"),
    ("Windows Software Installed", "win_event_id:11707 OR event_id:11707")
]

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
    mode = sys.argv[1].lower() if len(sys.argv) > 1 else "today"
    
    if mode == "all":
        target_index = f"*{CUST_ID}*"
        label_periodo = "HISTÓRICO COMPLETO (ALL TIME)"
    elif mode == "today":
        today_str = datetime.now(timezone.utc).strftime("%Y.%m.%d")
        target_index = f"*{today_str}*{CUST_ID}*"
        label_periodo = f"HOY ({today_str}) - CONTROL DE CUOTA"
    else:
        target_index = f"*{mode}*{CUST_ID}*"
        label_periodo = f"FECHA ESPECÍFICA ({mode})"

    print("=" * 80)
    print(f"   MATRIZ STELLAR CYBER THREAT HUNTING LIBRARY ({label_periodo})")
    print("=" * 80)
    print(f"[*] Consultando 20 módulos en paralelo contra el Data Lake...")
    
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    # Construcción de la agregación filters en un solo query
    filters_map = {name: {"query_string": {"query": q}} for name, q in THREAT_HUNTING_MODULES}
    
    body = {
        "size": 0,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": CUST_ID}}
                ]
            }
        },
        "aggs": {
            "th_matrix": {
                "filters": {
                    "filters": filters_map
                }
            }
        }
    }
    
    t0 = time.time()
    url = f"https://{HOST}/connect/api/data/{target_index}/_search"
    r = requests.get(url, headers=headers, json=body, timeout=45, verify=False)
    t_elapsed = time.time() - t0
    
    if r.status_code != 200:
        print(f"[-] Error en consulta ({r.status_code}): {r.text[:300]}")
        return
        
    res = r.json()
    buckets = res.get("aggregations", {}).get("th_matrix", {}).get("buckets", {})
    
    # Ordenar por doc_count descendente
    sorted_items = sorted(buckets.items(), key=lambda x: x[1].get("doc_count", 0), reverse=True)
    
    print(f"[+] 20 Módulos calculados en {t_elapsed:.2f}s!\n")
    print(f"{'#':<3} | {'Módulo Threat Hunting':<34} | {'Eventos':<14} | {'Impacto Cuota':<22}")
    print("-" * 78)
    
    for idx, (name, b) in enumerate(sorted_items, 1):
        cnt = b.get("doc_count", 0)
        
        if cnt >= 1_000_000:
            impacto = "[ALTO - DRENAJE CRITICO]"
        elif cnt >= 100_000:
            impacto = "[MEDIO - VIGILANCIA]"
        elif cnt > 0:
            impacto = "[BAJO - CONTROLADO]"
        else:
            impacto = "[0 - SIN ACTIVIDAD]"
            
        print(f"{idx:2d}. | {name:<34} | {cnt:>12,} | {impacto}")

if __name__ == "__main__":
    main()
