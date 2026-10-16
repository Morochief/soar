#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de operaciones completas contra el MCP Server de Stellar Cyber
Ejecuta:
1. get_access_token
2. listTenant
3. listCases (casos de las últimas 24h / activos)
4. getCaseDetail (del caso más reciente)
"""

import os
import sys
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
TOKEN = os.environ.get("STELLAR_TOKEN", "")

def mcp_call(method: str, params: dict = None, req_id: int = 1):
    url = f"https://{HOST}/mcp"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": req_id,
        "params": {
            "name": method,
            "arguments": params or {}
        }
    }
    r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
    if r.status_code != 200:
        return {"error": f"HTTP {r.status_code}: {r.text}"}
    return r.json()

def main():
    print("=" * 80)
    print("   PROBANDO OPERACIONES DEL STELLAR CYBER MCP SERVER")
    print("=" * 80)

    # 1. Obtener Token de Acceso
    print("\n[*] 1. Invocando herramienta 'get_access_token'...")
    res_token = mcp_call("get_access_token")
    print("    Resultado:", json.dumps(res_token, indent=2)[:300])

    # 2. Listar Tenants
    print("\n[*] 2. Invocando herramienta 'listTenant'...")
    res_tenant = mcp_call("listTenant")
    print("    Resultado:", json.dumps(res_tenant, indent=2)[:400])

    # 3. Listar Casos
    print("\n[*] 3. Invocando herramienta 'listCases' (últimos casos)...")
    res_cases = mcp_call("listCases", {"limit": 5})
    print("    Resultado:", json.dumps(res_cases, indent=2)[:600])

if __name__ == "__main__":
    main()
