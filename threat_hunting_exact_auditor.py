#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ AUDITOR EXACTO DE THREAT HUNTING LIBRARY — STELLAR CYBER OPENXDR
=============================================================================
Consulta la API oficial utilizando exactamente los índices y campos nativos
de Stellar Cyber para replicar el 100% de los números de tu pantalla:
  - All Login Failures (60.2k)
  - DNS Analysis (717.1k)
  - Firewall (2.1M)
  - Google Workspace (59.7k)
  - Network Applications (3.3M)
  - Non-Standard Port Usage (2)
  - Sophos Endpoint (626)
  - Windows Account Changes (4)
  - Windows Command Line (3.4k)
  - Windows Login Failures (9)
  - Windows Logins (22.4k)
  - Windows New Processes (3.4k)
  - Windows Privilege Escalations (10.4k)
=============================================================================
"""

import os
import sys
import json
import base64
import time
import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")
TENANT_ID = os.environ.get("STELLAR_TENANT_ID", "e511c3fc54cd4d668bb67612c2ef4b04")

def get_jwt() -> str:
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    return r.json().get("access_token")

# Especificación 1:1 con las tarjetas de Stellar Cyber
CARD_SPECS = [
    {
        "name": "Firewall",
        "ui_estimate": "2.1M",
        "index": "*adr*",
        "lucene": "msg_class.keyword:firewall",
        "origin": "Syslog perimetral Fortinet FortiGate (inicios, cierres y denegaciones)."
    },
    {
        "name": "Network Applications",
        "ui_estimate": "3.3M",
        "index": "*adr*",
        "lucene": "msg_class.keyword:interflow_traffic",
        "origin": "Sensor Modular NDR (inspección de paquetes DPI L7 de aplicaciones)."
    },
    {
        "name": "DNS Analysis",
        "ui_estimate": "717.1k",
        "index": "*adr*",
        "lucene": "msg_class.keyword:interflow_traffic AND (dstport:53 OR appid_name:DNS)",
        "origin": "Consultas DNS decodificadas y resueltas por el sensor en la red."
    },
    {
        "name": "Google Workspace",
        "ui_estimate": "59.7k",
        "index": "*audit*",
        "lucene": "msg_class.keyword:gsuite OR engid_name:gsuite_Workspace-THN",
        "origin": "Cloud Connector Google Workspace (actividad Drive, logins y correos)."
    },
    {
        "name": "All Login Failures",
        "ui_estimate": "60.2k",
        "index": "*wineventlog*",
        "lucene": "login_result.keyword:fail OR event_id:4768",
        "origin": "Intentos fallidos de autenticación Kerberos y Active Directory."
    },
    {
        "name": "Windows Logins",
        "ui_estimate": "22.4k",
        "index": "*wineventlog*",
        "lucene": "event_id:4624",
        "origin": "Inicios de sesión exitosos en servidores y endpoints Windows (4624)."
    },
    {
        "name": "Windows Privilege Escalations",
        "ui_estimate": "10.4k",
        "index": "*wineventlog*",
        "lucene": "event_id:4672",
        "origin": "Inicios de sesión con privilegios especiales/administrador (4672)."
    },
    {
        "name": "Windows New Processes",
        "ui_estimate": "3.4k",
        "index": "*wineventlog*",
        "lucene": "event_id:4688",
        "origin": "Creación y ejecución de nuevos procesos en servidores Windows (4688)."
    },
    {
        "name": "Windows Command Line",
        "ui_estimate": "3.4k",
        "index": "*wineventlog*",
        "lucene": "event_id:4688",
        "origin": "Auditoría de comandos ejecutados en consola/PowerShell."
    },
    {
        "name": "Sophos Endpoint",
        "ui_estimate": "626",
        "index": "*ser*,*audit*",
        "lucene": "msg_class.keyword:*sophos* OR engid_name:*sophos*",
        "origin": "Alertas y telemetría de antivirus Sophos Central."
    },
    {
        "name": "Windows Login Failures",
        "ui_estimate": "9",
        "index": "*wineventlog*",
        "lucene": "event_id:4625",
        "origin": "Fallos de inicio de sesión directo/interactivo en Windows (4625)."
    },
    {
        "name": "Windows Account Changes",
        "ui_estimate": "4",
        "index": "*wineventlog*",
        "lucene": "event_id:(4720 OR 4722 OR 4724 OR 4738)",
        "origin": "Cuentas de usuario creadas, modificadas o desbloqueadas en AD."
    },
    {
        "name": "Non-Standard Port Usage",
        "ui_estimate": "2",
        "index": "*adr*",
        "lucene": 'appid_stdport:"no"',
        "origin": "Detección DPI de protocolos conocidos cursados en puertos anómalos (ej: HTTPS sobre TCP 8889)."
    }
]

def main():
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    now_ms = int(time.time() * 1000)
    start_ms = now_ms - (24 * 3600 * 1000)
    
    print("=" * 115)
    print("🎯 RECONCILIACIÓN FORENSE 1:1 DE THREAT HUNTING LIBRARY (STELLAR CYBER)")
    print(f"⏱️ Ventana: Últimas 24 Horas (Hasta {datetime.fromtimestamp(now_ms/1000).strftime('%Y-%m-%d %H:%M:%S')} GMT-3)")
    print("=" * 115)
    print(f"{'TARJETA EN TU PANTALLA':<30} | {'UI APROX':<10} | {'TOTAL REAL API':<15} | {'ORIGEN Y EXPLICACIÓN DE LOS NÚMEROS'}")
    print("-" * 115)
    
    for c in CARD_SPECS:
        indices = c["index"].split(",")
        total_card = 0
        for idx in indices:
            clean_idx = idx.strip().replace("*", "")
            url = f"https://{HOST}/connect/api/data/*{clean_idx}*e511c3fc54cd4d668bb67612c2ef4b04*/_search"
            payload = {
                "track_total_hits": True,
                "size": 0,
                "query": {
                    "bool": {
                        "filter": [{"term": {"tenantid": TENANT_ID}}],
                        "must": [
                            {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                            {"query_string": {"query": c["lucene"]}}
                        ]
                    }
                }
            }
            try:
                r = requests.get(url, headers=headers, json=payload, timeout=20, verify=False)
                if r.status_code == 200:
                    cnt = r.json().get("hits", {}).get("total", {}).get("value", 0)
                    total_card += cnt
            except Exception:
                pass
        
        print(f"{c['name']:<30} | {c['ui_estimate']:<10} | {total_card:>12,}    | {c['origin']}")

    print("=" * 115)

if __name__ == "__main__":
    main()
