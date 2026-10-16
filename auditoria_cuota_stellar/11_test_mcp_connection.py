#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de verificación del endpoint MCP de Stellar Cyber con headers completos
"""

import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
TOKEN = os.environ.get("STELLAR_TOKEN", "")

def test_mcp():
    url = f"https://{HOST}/mcp"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/list",
        "id": 1,
        "params": {}
    }
    try:
        r_post = requests.post(url, headers=headers, json=payload, timeout=10, verify=False)
        print(f"[+] POST /mcp (tools/list) -> Status: {r_post.status_code}")
        print(f"    Respuesta: {r_post.text[:400]}")
    except Exception as e:
        print(f"[-] Error en POST: {e}")

if __name__ == "__main__":
    test_mcp()
