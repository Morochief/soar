#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta SOC - Auditoría de Cuota Stellar Cyber
01: Consultar Consumo Diario y Mensual de Licencia por Tenant

Consulta el endpoint oficial /storage-usages/daily_and_monthly
para verificar el consumo en GB/día y el acumulado mensual.
"""

import os
import requests
import json
import base64
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    from dotenv import load_dotenv
    _env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(_env_path):
        load_dotenv(_env_path)
    else:
        load_dotenv()
except Exception:
    pass

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")

def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando contra Stellar Cyber ({r.status_code}): {r.text}")
        exit(1)
    return r.json().get("access_token")

def main():
    print(f"[*] Conectando a Stellar Cyber: https://{HOST}")
    print(f"[*] Usuario: {EMAIL}")
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    
    url = f"https://{HOST}/connect/api/v1/storage-usages/daily_and_monthly"
    r = requests.get(url, headers=headers, timeout=20, verify=False)
    
    if r.status_code != 200:
        print(f"[-] Error al consultar storage-usages ({r.status_code}): {r.text}")
        return
        
    data = r.json()
    print("\n" + "=" * 65)
    print("         REPORTE DE INGESTA Y CONSUMO DE LICENCIA")
    print("=" * 65)
    
    tenants_list = data.get("data", []) if isinstance(data, dict) else data
    for info in tenants_list:
        name = info.get("tenant_name", "Desconocido")
        cust_id = info.get("cust_id", "N/A")
        monthly_gb = info.get("monthly_usage", 0)
        print(f"\n[+] Tenant: {name} (ID: {cust_id})")
        print(f"    Consumo acumulado mensual: {monthly_gb:.2f} GB")
        
        daily = info.get("daily_usage", [])
        if daily:
            print("    Historial de Ingesta Diaria:")
            print(f"    {'Fecha':<14} | {'Consumo (GB)':<14} | {'Estado vs Cuota (8.0 GB)':<25}")
            print("    " + "-" * 56)
            for d in daily[-14:]:
                d_date = d.get("date", "N/A")[:10]
                d_gb = d.get("usage", 0)
                estado = "[OK - NORMAL]" if d_gb <= 8.0 else f"[ALERTA DESBORDE +{d_gb - 8.0:.2f} GB]"
                print(f"    {d_date:<14} | {d_gb:>10.2f} GB | {estado}")

if __name__ == "__main__":
    main()
