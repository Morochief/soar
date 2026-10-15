#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
05: Auditar Filtros de Log (Log Filters) Activos en Stellar Cyber

Revisa la configuración exportada de Log Filters o consulta la API
para listar los filtros que afectan a FortiGate y comprobar si descartan (Drop)
o si tienen errores sintácticos de campos.
"""

import os
import requests
import json
import base64
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "")

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
    print(f"[*] Consultando Log Filters en Stellar Cyber...")
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    # Intento 1: API de log-filters
    url = f"https://{HOST}/connect/api/v1/log-filters"
    r = requests.get(url, headers=headers, verify=False, timeout=20)
    
    filters = []
    if r.status_code == 200:
        data = r.json()
        filters = data.get("data", data) if isinstance(data, dict) else data
    else:
        # Fallback a archivo local si existe
        local_files = [
            "stellar_log_filters_completos.json",
            "Analista SOC/stellar_log_filters_completos.json",
            "../stellar_log_filters_completos.json"
        ]
        for lf in local_files:
            if os.path.exists(lf):
                with open(lf, "r", encoding="utf-8") as f:
                    d = json.load(f)
                    filters = d.get("filters", d) if isinstance(d, dict) else d
                print(f"[!] Usando respaldo local: {lf}")
                break

    if not filters:
        print("[-] No se pudieron obtener los log filters.")
        return
        
    print(f"\n=======================================================")
    print(f"TOTAL LOG FILTERS REGISTRADOS: {len(filters)}")
    print("=======================================================")
    
    fg_filters = []
    for flt in filters:
        name = flt.get("name", "")
        summary = flt.get("rules_summary", "")
        rules_str = str(flt.get("rules", ""))
        action = flt.get("action", "Drop")
        created_by = flt.get("created_by", "N/A")
        
        text = (name + " " + summary + " " + rules_str).lower()
        if any(k in text for k in ["forti", "fg-", "firewall", "fw", "deny", "block", "7680", "53"]):
            fg_filters.append((name, action, created_by, summary, flt.get("in_use", {})))
            
    print(f"[+] Filtros relacionados a Firewall/FortiGate: {len(fg_filters)}\n")
    for idx, (name, action, creator, summary, in_use) in enumerate(fg_filters, 1):
        print(f"[{idx}] {name}")
        print(f"    Acción: {action} | Creador: {creator}")
        print(f"    Regla: {summary}")
        print(f"    Asignado a: {list(in_use.keys()) if isinstance(in_use, dict) else in_use}")
        print("-" * 60)

if __name__ == "__main__":
    main()
