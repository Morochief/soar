#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de paso de JWT obtenido por Basic Auth directamente al MCP Server
"""

import os
import sys
import json
import base64
import requests
import urllib3

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

def mcp_call_with_jwt(jwt: str, method: str, params: dict = None):
    url = f"https://{HOST}/mcp"
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": method,
            "arguments": params or {}
        }
    }
    r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
    return r.status_code, r.text

def main():
    jwt = get_jwt()
    print("[+] JWT obtenido exitosamente.")
    
    # Probar pasar el JWT en los argumentos de listTenant
    status, text = mcp_call_with_jwt(jwt, "listTenant", {"access_token": jwt})
    print(f"[+] listTenant con access_token argument -> Status {status}:")
    print(text[:400])

    # Probar pasar el JWT en los argumentos de listCases
    status, text = mcp_call_with_jwt(jwt, "listCases", {"access_token": jwt, "limit": 3})
    print(f"\n[+] listCases con access_token argument -> Status {status}:")
    print(text[:600])

if __name__ == "__main__":
    main()
