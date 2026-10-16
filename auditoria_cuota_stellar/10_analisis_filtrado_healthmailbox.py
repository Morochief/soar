#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota y Filtros Stellar Cyber
10: Inspeccionar cómo filtrar el ruido de autenticación de HealthMailbox en Windows Event Log (Event ID 4776)

Analiza las alertas de 'Internal Account Login Failure Anomaly' / 'Internal User Login Failure Anomaly'
generadas por HealthMailbox y evalúa si es posible descartarlas vía Log Filter o Log Forwarder.
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

def get_jwt() -> str:
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando contra Stellar Cyber ({r.status_code}): {r.text}")
        sys.exit(1)
    return r.json().get("access_token")

def main():
    print("=" * 80)
    print("   ANÁLISIS DE FACTIBILIDAD DE FILTRADO PARA RUIDO DE HEALTHMAILBOX")
    print("=" * 80)
    jwt = get_jwt()
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }

    # 1. Consultar log_filters existentes
    url_filters = f"https://{HOST}/connect/api/v1/log_filters"
    r = requests.get(url_filters, headers=headers, timeout=20, verify=False)
    
    if r.status_code == 200:
        filters = r.json().get("data", [])
        print(f"[+] Total de Log Filters configurados en el sistema: {len(filters)}")
        
        # Buscar si hay alguno que aplique a wineventlog o winlogbeat
        winevent_filters = [f for f in filters if "win" in str(f).lower() or "audit" in str(f).lower()]
        print(f"[+] Filtros existentes vinculados a Windows / Winlogbeat: {len(winevent_filters)}")
        for wf in winevent_filters:
            print(f"    - Nombre: {wf.get('name')}")
            print(f"      Reglas: {wf.get('rules')}")
    else:
        print(f"[-] Error consultando log_filters: {r.status_code}")

    print("\n" + "=" * 80)
    print("   CONCLUSIÓN TÉCNICA DEL ORIGEN DEL EVENTO")
    print("=" * 80)
    print("1. Origen del evento:")
    print("   - Host emisor: VMBASE8 (172.16.201.8, Windows Server 2019)")
    print("   - Agente: Winlogbeat 8.5.3 (Elastic)")
    print("   - Canal de log: Security (Microsoft-Windows-Security-Auditing)")
    print("   - Event ID: 4776 (Credential Validation / NTLM)")
    print("   - TargetUserName: HealthMailbox... (Cuenta interna de Microsoft Exchange)")
    print("   - Workstation: VM-MARANDU")
    print("   - Status: 0xc0000072 (STATUS_ACCOUNT_DISABLED)")
    print("\n2. ¿Por qué ocurre esto?")
    print("   - HealthMailbox son buzones de monitoreo automático (Managed Availability)")
    print("     creados por Microsoft Exchange Server.")
    print("   - Exchange intenta autenticar el buzón continuamente para testear la salud del servicio.")
    print("   - Como la cuenta en Active Directory está deshabilitada (0xc0000072), Windows genera")
    print("     un Evento 4776 de fallo cada pocos segundos, sumando miles de fallos.")
    print("   - El Machine Learning de Stellar Cyber ve 84 fallos en 10 min y cree que es Brute Force.")

if __name__ == "__main__":
    main()
