#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 STELLAR CYBER - GESTOR UNIVERSAL DE CASOS Y ALERTAS (MCP / API CLIENT)
=============================================================================
Herramienta permanente y reutilizable para consultar casos, listar eventos,
extraer alertas y analizar incidentes sin necesidad de crear scripts temporales.

Uso:
  python stellar_case_manager.py --case 17813
  python stellar_case_manager.py --case 17813 --json
  python stellar_case_manager.py --list --limit 10
  python stellar_case_manager.py --list --status "In Progress"
"""

import os
import sys
import json
import base64
import argparse
from datetime import datetime
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración por variables de entorno o valores por defecto del SOC
HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")
MCP_URL = f"https://{HOST}/mcp"

_CACHED_JWT = None

def get_jwt():
    global _CACHED_JWT
    if _CACHED_JWT:
        return _CACHED_JWT
    
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        print(f"[-] Error autenticando contra Stellar Cyber ({r.status_code}): {r.text}", file=sys.stderr)
        sys.exit(1)
    
    _CACHED_JWT = r.json().get("access_token")
    return _CACHED_JWT

def call_mcp(tool_name: str, arguments: dict):
    jwt = get_jwt()
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    # Asegurar token en arguments si no está presente
    if "access_token" not in arguments:
        arguments["access_token"] = jwt
        
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    r = requests.post(MCP_URL, headers=headers, json=payload, timeout=30, verify=False)
    if r.status_code != 200:
        print(f"[-] Error HTTP {r.status_code} llamando a {tool_name}: {r.text}", file=sys.stderr)
        sys.exit(1)
        
    res = r.json()
    if "error" in res:
        print(f"[-] Error MCP ({res['error'].get('code')}): {res['error'].get('message')}", file=sys.stderr)
        sys.exit(1)
        
    content = res.get("result", {}).get("content", [])
    if not content:
        return {}
    
    text = content[0].get("text", "{}")
    try:
        return json.loads(text)
    except Exception:
        return {"raw_text": text}

def format_ts(ts_ms):
    if not ts_ms:
        return "N/A"
    try:
        # Asumiendo timestamp en milisegundos
        dt = datetime.fromtimestamp(ts_ms / 1000.0)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(ts_ms)

def cmd_get_case(ticket_id: str, as_json: bool = False):
    print(f"[*] Consultando detalle del Caso #{ticket_id} en Stellar Cyber...")
    data = call_mcp("getCaseDetail", {"ticket_id": str(ticket_id)})
    
    # Guardar copia de respaldo en json para análisis forense offline
    out_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(out_dir, f"caso_{ticket_id}_detail.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    inner = data.get("data", {})
    details = inner.get("details", {})
    alerts = inner.get("alerts", [])
    observables = inner.get("observables", {})
    activity = inner.get("activity", [])

    print("\n" + "="*80)
    print(f" DETALLE COMPLETO DEL CASO STELLAR #{details.get('ticket_id', ticket_id)}")
    print("="*80)
    print(f"Nombre:           {details.get('name')}")
    print(f"Case ID:          {details.get('case_id', details.get('_id'))}")
    print(f"Estado:           {details.get('status')}")
    print(f"Severidad/Score:  {details.get('severity')} | Score: {details.get('score')}")
    print(f"Tenant:           {details.get('tenant_name')} ({details.get('tenant_group_name')})")
    print(f"Asignado a:       {details.get('assignee_name') or 'Sin Asignar'}")
    print(f"Creado:           {format_ts(details.get('created_at'))} por {details.get('created_by_name')}")
    print(f"Modificado:       {format_ts(details.get('modified_at'))} por {details.get('modified_by_name')}")
    print(f"Ventana Temporal: {format_ts(details.get('start_timestamp'))} -> {format_ts(details.get('end_timestamp'))}")
    
    metrics = details.get("metrics", {})
    for m_id, m_val in metrics.items():
        if isinstance(m_val, dict):
            elapsed_sec = round(m_val.get("elapsed_ms", 0) / 1000.0, 1)
            print(f"Métrica SLA:      {m_val.get('name')}: {elapsed_sec}s ({round(elapsed_sec/60.0, 1)} min)")

    print("\n" + "-"*80)
    print(f" ALERTAS AGRUPADAS ({len(alerts)})")
    print("-"*80)
    for i, alt in enumerate(alerts, 1):
        src = alt.get("_source", {})
        xdr = src.get("xdr_event", {})
        forti = src.get("fortinet", {})
        
        print(f"\n[Alerta #{i}] {xdr.get('display_name', src.get('event_name'))}")
        print(f"  * Kill Chain / Técnica: {xdr.get('xdr_killchain_stage')} | {xdr.get('technique', {}).get('name')}")
        print(f"  * Descripción:          {xdr.get('description')}")
        print(f"  * Hora Evento (Local):  {forti.get('event_time', src.get('timestamp_utc'))}")
        print(f"  * Origen:               IP={src.get('srcip')} | Host={src.get('srcip_host')} | MAC={src.get('srcmac')}")
        print(f"  * Usuario / Dispositivo:User={forti.get('unauthuser')} | DevName={forti.get('srcname')} | InIntf={forti.get('srcintf')}")
        print(f"  * Destino:              IP={src.get('dstip')} | Host={src.get('dstip_host')} | Port={src.get('dstport')} ({src.get('appid_name')})")
        act = src.get('action')
        act_str = act.upper() if act else 'N/A'
        print(f"  * Acción Firewall:      {act_str} por Política: {src.get('fw_policy_id')} (Regla {forti.get('rule_id')})")
        print(f"  * Detección ML:         Bloqueos Actuales={src.get('actual')} vs Típico={src.get('typical')} (Intervalo: {src.get('run_every')} min)")
        print(f"  * Fidelidad / Severidad:Fidelity={src.get('fidelity')}% | Severity={src.get('severity')} | Event Score={src.get('event_score')}")

    print("\n" + "-"*80)
    print(" OBSERVABLES IDENTIFICADOS")
    print("-"*80)
    hosts = observables.get("observables", {}).get("host", [])
    for h in hosts:
        print(f"  - Host: {h.get('hostname')} | IP: {h.get('ip')}")

    print("\n" + "-"*80)
    print(" ACTIVIDAD RECIENTE (AUDITORÍA DE ESTADOS)")
    print("-"*80)
    for act in activity:
        print(f"  * [{format_ts(act.get('timestamp'))}] Acción: {act.get('action')} | Campo: {act.get('field')} | '{act.get('from')}' -> '{act.get('to')}' (User: {act.get('user')})")
    
    print("\n" + "="*80)
    print(f"[+] Detalle JSON completo respaldado en: {json_path}")
    print("="*80 + "\n")

def cmd_list_cases(limit: int = 10, status: str = None):
    print(f"[*] Consultando lista de casos en Stellar Cyber (Límite: {limit})...")
    args = {"limit": limit}
    data = call_mcp("listCases", args)
    
    cases = data.get("cases", [])
    if not cases and isinstance(data, list):
        cases = data
    elif not cases and "data" in data:
        cases = data["data"].get("cases", [])
        
    print("\n" + "="*80)
    print(f" LISTADO DE CASOS (Total obtenidos: {len(cases)})")
    print("="*80)
    print(f"{'TICKET':<8} {'ESTADO':<13} {'SEV':<8} {'SCORE':<7} {'NOMBRE'}")
    print("-" * 80)
    for c in cases:
        c_status = c.get("status", "N/A")
        if status and status.lower() not in c_status.lower():
            continue
        print(f"#{c.get('ticket_id', 'N/A'):<7} {c_status:<13} {c.get('severity', 'N/A'):<8} {c.get('score', 0):<7} {c.get('name', 'N/A')}")
    print("="*80 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Cliente universal de Casos y Alertas de Stellar Cyber")
    parser.add_argument("--case", type=str, help="ID o Ticket del caso a consultar (ej: 17813)")
    parser.add_argument("--list", action="store_true", help="Listar casos recientes")
    parser.add_argument("--limit", type=int, default=10, help="Límite para listado de casos (def: 10)")
    parser.add_argument("--status", type=str, default=None, help="Filtrar listado por estado (ej: 'In Progress', 'New')")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON crudo")
    
    args = parser.parse_args()
    
    if args.case:
        cmd_get_case(args.case, as_json=args.json)
    elif args.list:
        cmd_list_cases(limit=args.limit, status=args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
