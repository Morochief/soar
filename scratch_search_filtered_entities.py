import os
import sys
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv(Path('G:/SOC/soar/.env'))

host = os.environ.get('STELLAR_HOST')
email = os.environ.get('STELLAR_EMAIL')
token = os.environ.get('STELLAR_TOKEN')

import base64
url = f'https://{host}/connect/api/v1/access_token'
pair = f'{email}:{token}'
b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {b64}', 'Content-Type': 'application/json'}
res = requests.post(url, headers=headers, json={}, verify=True, timeout=10)
jwt = res.json().get('access_token')
auth_headers = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

targets_to_hunt = [
    ("192.168.15.27", "NOC Server (Filtros #1, #2)"),
    ("172.17.10.25", "Security Onion 1 (Filtro #57, #59)"),
    ("172.17.10.71", "Security Onion 2 (Filtro #57, #59)"),
    ("192.168.15.31", "Zabbix Server (Filtros #41, #46, #47, #60)"),
    ("10.2.1.4", "Servidor Informix (Filtros #49, #60)"),
    ("10.2.1.3", "Servidor Informix DB (Filtro #49)"),
    ("192.168.16.16", "CCTV Dahua (Filtro #51)"),
    ("10.11.4.2", "Veeam Backup (Filtro #33)"),
    ("192.168.15.23", "Pantalla Grafana (Filtros #36, #62)"),
    ("165.1.125.196", "IP Externa 165.1.125.196 (Filtro #52)"),
    ("dev-grafana", "Host dev-grafana (Filtro #62)"),
    ("Healthmailbox", "Exchange Healthmailbox (Filtro #61)"),
    ("192.168.169.44", "Helpdesk PING (Filtro #55)"),
    ("10.40.2.240", "Odoo PostgreSQL 5432 (Filtro #56)")
]

print("=" * 80)
print("🔍 BÚSQUEDA FORENSE EN STELLAR CYBER PARA ENTIDADES CON FILTROS APLICADOS")
print("=" * 80)

for entity, label in targets_to_hunt:
    u = f"https://{host}/connect/api/v1/cases"
    params = {"search": entity, "limit": 20}
    try:
        r = requests.get(u, headers=auth_headers, params=params, timeout=12)
        if r.status_code == 200:
            d = r.json() or {}
            cases = (d.get("data") or {}).get("cases", []) if isinstance(d.get("data"), dict) else (d.get("cases") or [])
            if cases:
                print(f"\n[+] Coincidencias para {label} ({entity}): {len(cases)} CASOS / ALERTAS ENCONTRADOS")
                for c in cases[:3]:
                    cid = c.get('ticket_id') or c.get('_id')
                    cname = c.get('name')
                    cscore = c.get('score')
                    csev = c.get('severity')
                    cstatus = c.get('status')
                    cwho = c.get('who')
                    cdate = c.get('created_at') or c.get('created_ts')
                    print(f"    • Ticket #{cid} | Score: {cscore} ({csev}) | Estado: {cstatus} | Who: {cwho}")
                    print(f"      Nombre: {cname}")
            else:
                print(f"[-] Sin casos activos para {label} ({entity})")
        else:
            print(f"[!] Error consultando {entity}: HTTP {r.status_code}")
    except Exception as e:
        print(f"[!] Excepción con {entity}: {e}")
