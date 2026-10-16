#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test de getCaseDetail para el Caso 17813 usando el MCP Server
"""

import os
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
        exit(1)
    return r.json().get("access_token")

def main():
    jwt = get_jwt()
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
            "name": "getCaseDetail",
            "arguments": {
                "access_token": jwt,
                "ticket_id": "17813"
            }
        }
    }
    r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
    if r.status_code == 200:
        res = r.json()
        content = res.get("result", {}).get("content", [])
        if content:
            raw_text = content[0].get("text")
            data = json.loads(raw_text)
            out_file = "auditoria_cuota_stellar/caso_17813_detail.json"
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"[+] Detalle guardado exitosamente en {out_file}")
            print(f"Case ID: {data.get('case', {}).get('case_id')}")
            print(f"Ticket ID: {data.get('case', {}).get('ticket_id')}")
            print(f"Name: {data.get('case', {}).get('name')}")
            print(f"Status: {data.get('case', {}).get('status')}")
            print(f"Severity: {data.get('case', {}).get('severity')}")
            print(f"Score: {data.get('case', {}).get('score')}")
            print(f"Alerts count in response: {len(data.get('alerts', []))}")
        else:
            print("Sin contenido:", res)
    else:
        print(f"Error {r.status_code}: {r.text}")

if __name__ == "__main__":
    main()
