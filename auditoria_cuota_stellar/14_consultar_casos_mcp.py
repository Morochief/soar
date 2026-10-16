#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consulta y Muestra los Casos Activos de Stellar Cyber usando el servidor MCP
"""

import os
import sys
import json
import base64
import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "")

def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando: {r.text}")
        sys.exit(1)
    return r.json().get("access_token")

def mcp_call(method: str, params: dict):
    url = f"https://{HOST}/mcp"
    jwt = get_jwt()
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    # Inyectar access_token requerido por los schemas de Stellar MCP
    params["access_token"] = jwt
    
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": method,
            "arguments": params
        }
    }
    r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}: {r.text}"}
    
    res = r.json()
    content = res.get("result", {}).get("content", [])
    if content and content[0].get("type") == "text":
        return json.loads(content[0].get("text"))
    return res

def main():
    print("=" * 80)
    print("      CONSULTA DE CASOS VIA STELLAR CYBER MCP SERVER")
    print("=" * 80)
    
    data = mcp_call("listCases", {"limit": 5, "order": "desc", "sort": "created_at"})
    
    cases_data = data.get("data", {})
    total = cases_data.get("total", 0)
    cases = cases_data.get("cases", [])
    
    print(f"\n[+] Total de casos encontrados: {total}")
    print(f"[+] Mostrando los últimos {len(cases)} casos ordenados por fecha de creación:\n")
    
    for c in cases:
        ticket_id = c.get("ticket_id")
        name = c.get("name")
        status = c.get("status")
        severity = c.get("severity")
        score = c.get("score")
        created_ms = c.get("created_at", 0)
        created_str = datetime.fromtimestamp(created_ms / 1000).strftime('%Y-%m-%d %H:%M:%S') if created_ms else "N/A"
        
        print(f"  • Ticket #{ticket_id} | {name}")
        print(f"    - Estado: {status} | Severidad: {severity} | Score: {score}")
        print(f"    - Creado: {created_str}")
        print("    " + "-" * 70)

if __name__ == "__main__":
    main()
