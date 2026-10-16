#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 STELLAR CYBER - CLI UNIFICADO DEL SOC (MCP & REST API ENGINE)
=============================================================================
Herramienta central y definitiva para todas las operaciones de analistas SOC:
- Casos (detalle, listado, actualización)
- Alertas (detalle de alertas, alertas por caso)
- Tenants (listado de clientes y grupos)
- Cuota y Licencia (consumo diario y mensual en GB)
- Búsqueda en Data Lake / Threat Hunting (queries Lucene en Interflow)
- Log Filters y Alert Customizations

Uso:
  python stellar_cli.py --case 17813
  python stellar_cli.py --list-cases --limit 10 --status "In Progress"
  python stellar_cli.py --case-alerts 17813
  python stellar_cli.py --alert <ALERT_ID>
  python stellar_cli.py --quota
  python stellar_cli.py --tenants
  python stellar_cli.py --search "srcip:192.168.169.11"
  python stellar_cli.py --filters
"""

import os
import sys
import json
import base64
import argparse
from datetime import datetime
from typing import Any, Dict, List, Optional
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración de conexión
HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "796e625a6552636a4e326b54784a553868504f47514a387768636b4d32646f364375494d485050516b763131766a4f65")
MCP_URL = f"https://{HOST}/mcp"

_CACHED_JWT: Optional[str] = None

def get_jwt() -> str:
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

def get_rest_headers() -> Dict[str, str]:
    jwt = get_jwt()
    return {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }

def call_mcp(tool_name: str, arguments: dict) -> Any:
    jwt = get_jwt()
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
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
        print(f"[-] Error HTTP {r.status_code} llamando a herramienta MCP {tool_name}: {r.text}", file=sys.stderr)
        sys.exit(1)
        
    res = r.json()
    if "error" in res:
        req_id = res.get("request_id") or res.get("requestId") or "N/A"
        print(f"[-] Error MCP ({res['error'].get('code')} | Request ID: {req_id}): {res['error'].get('message')}", file=sys.stderr)
        sys.exit(1)
        
    content = res.get("result", {}).get("content", [])
    if not content:
        return {}
    
    text = content[0].get("text", "{}")
    try:
        return json.loads(text)
    except Exception:
        return {"raw_text": text}

def format_ts(ts_ms) -> str:
    if not ts_ms:
        return "N/A"
    try:
        dt = datetime.fromtimestamp(ts_ms / 1000.0)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(ts_ms)

# =============================================================================
# COMANDOS: CASOS
# =============================================================================

def handle_get_case(ticket_id: str, as_json: bool = False):
    print(f"[*] Consultando detalle del Caso #{ticket_id}...")
    data = call_mcp("getCaseDetail", {"ticket_id": str(ticket_id)})
    
    # Guardar respaldo
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
            state = m_val.get("state", "N/A").upper()
            print(f"Métrica SLA (7.0.0s):{m_val.get('name')}: {elapsed_sec}s ({round(elapsed_sec/60.0, 1)} min) [Estado: {state}]")

    print("\n" + "-"*80)
    print(f" ALERTAS AGRUPADAS ({len(alerts)})")
    print("-"*80)
    for i, alt in enumerate(alerts, 1):
        src = alt.get("_source", {})
        xdr = src.get("xdr_event", {})
        forti = src.get("fortinet", {})
        ids_payload = src.get("ids", {}).get("payload_details", {}).get("payload_printable")
        
        print(f"\n[Alerta #{i}] {xdr.get('display_name', src.get('event_name'))}")
        print(f"  * Kill Chain / Técnica: {xdr.get('xdr_killchain_stage')} | {xdr.get('technique', {}).get('name')}")
        print(f"  * Descripción:          {xdr.get('description')}")
        print(f"  * Hora Evento (Local):  {forti.get('event_time', src.get('timestamp_utc'))}")
        print(f"  * Origen:               IP={src.get('srcip')} | Host={src.get('srcip_host')} | MAC={src.get('srcmac')}")
        print(f"  * Usuario / Dispositivo:User={forti.get('unauthuser')} | DevName={forti.get('srcname')} | InIntf={forti.get('srcintf')}")
        print(f"  * Destino:              IP={src.get('dstip')} | Host={src.get('dstip_host')} | Port={src.get('dstport')} ({src.get('appid_name')})")
        print(f"  * Acción Firewall:      {str(src.get('action')).upper()} por Política: {src.get('fw_policy_id')} (Regla {forti.get('rule_id')})")
        print(f"  * Detección ML:         Bloqueos Actuales={src.get('actual')} vs Típico={src.get('typical')} (Intervalo: {src.get('run_every')} min)")
        print(f"  * Fidelidad / Severidad:Fidelity={src.get('fidelity')}% | Severity={src.get('severity')} | Event Score={src.get('event_score')}")
        if ids_payload:
            print(f"  * Payload Imprimible IDS (7.0.0s): {ids_payload[:300]}")

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

def handle_list_cases(limit: int = 15, status: Optional[str] = None):
    print(f"[*] Consultando lista de casos recientes (Límite: {limit})...")
    data = call_mcp("listCases", {"limit": limit})
    cases = data.get("cases", [])
    if not cases and isinstance(data, list):
        cases = data
    elif not cases and "data" in data:
        cases = data["data"].get("cases", [])
        
    print("\n" + "="*80)
    print(f" LISTADO DE CASOS (Total: {len(cases)})")
    print("="*80)
    print(f"{'TICKET':<8} {'ESTADO':<13} {'SEV':<8} {'SCORE':<7} {'NOMBRE'}")
    print("-" * 80)
    for c in cases:
        c_status = c.get("status", "N/A")
        if status and status.lower() not in c_status.lower():
            continue
        print(f"#{str(c.get('ticket_id', 'N/A')):<7} {c_status:<13} {str(c.get('severity', 'N/A')):<8} {str(c.get('score', 0)):<7} {c.get('name', 'N/A')}")
    print("="*80 + "\n")

def handle_update_case(case_id: str, status: Optional[str] = None, assignee: Optional[str] = None, comment: Optional[str] = None):
    print(f"[*] Actualizando caso {case_id}...")
    args: Dict[str, Any] = {"case_id": str(case_id)}
    if status:
        args["status"] = status
    if assignee:
        args["assignee"] = assignee
    if comment:
        args["comment"] = comment
        
    res = call_mcp("updateCase", args)
    print(f"[+] Resultado de actualización: {res}")

# =============================================================================
# COMANDOS: ALERTAS
# =============================================================================

def handle_case_alerts(ticket_id: str):
    print(f"[*] Consultando alertas del Caso #{ticket_id}...")
    data = call_mcp("getCaseAlerts", {"ticket_id": str(ticket_id)})
    print(json.dumps(data, indent=2, ensure_ascii=False))

def handle_alert_detail(alert_id: str, index: Optional[str] = None):
    print(f"[*] Consultando detalle de alerta {alert_id}...")
    args = {"alert_id": alert_id}
    if index:
        args["index"] = index
    data = call_mcp("getAlertDetail", args)
    print(json.dumps(data, indent=2, ensure_ascii=False))

# =============================================================================
# COMANDOS: TENANTS
# =============================================================================

def handle_tenants():
    print("[*] Consultando lista de tenants configurados...")
    data = call_mcp("listTenant", {})
    tenants = data.get("tenants", []) if isinstance(data, dict) else data
    print("\n" + "="*80)
    print(f" LISTADO DE TENANTS ({len(tenants)})")
    print("="*80)
    for t in tenants:
        if isinstance(t, dict):
            print(f"- {t.get('name', 'N/A')} (ID: {t.get('cust_id', t.get('_id', 'N/A'))})")
        else:
            print(f"- {t}")
    print("="*80 + "\n")

# =============================================================================
# COMANDOS: CUOTA Y LICENCIA (REST API)
# =============================================================================

def handle_quota():
    print("[*] Consultando consumo de almacenamiento y cuota de licencia...")
    headers = get_rest_headers()
    url = f"https://{HOST}/connect/api/v1/storage-usages/daily_and_monthly"
    r = requests.get(url, headers=headers, timeout=20, verify=False)
    if r.status_code != 200:
        print(f"[-] Error al consultar cuota ({r.status_code}): {r.text}", file=sys.stderr)
        return
        
    data = r.json()
    print("\n" + "="*80)
    print(" REPORTE DE CONSUMO DE LICENCIA Y ALMACENAMIENTO")
    print("="*80)
    tenants_list = data.get("data", []) if isinstance(data, dict) else data
    for info in tenants_list:
        name = info.get("tenant_name", "Desconocido")
        cust_id = info.get("cust_id", "N/A")
        monthly_gb = info.get("monthly_usage", 0)
        print(f"\n[+] Tenant: {name} (ID: {cust_id})")
        print(f"    Consumo acumulado mensual: {monthly_gb:.2f} GB")
        daily = info.get("daily_usage", [])
        if daily:
            last = daily[-1]
            print(f"    Último registro diario:    {last.get('date', 'N/A')} -> {last.get('usage', 0):.2f} GB")
    print("="*80 + "\n")

# =============================================================================
# COMANDOS: BÚSQUEDA THREAT HUNTING (REST API / QUERIES)
# =============================================================================

def handle_search(query_str: str, cust_id: str = "all-tenants", limit: int = 15):
    print(f"[*] Ejecutando búsqueda en Data Lake: '{query_str}' (Tenant: {cust_id})...")
    headers = get_rest_headers()
    payload = {
        "cust_id": cust_id,
        "name": f"SOC_CLI_Hunt_{int(datetime.now().timestamp())}",
        "conditions": {
            "modifier": "and",
            "conditions": [
                {"type": "query_string", "value": [query_str]}
            ]
        }
    }
    r = requests.post(f"https://{HOST}/connect/api/v1/queries", headers=headers, json=payload, timeout=20, verify=False)
    if r.status_code not in (200, 201):
        print(f"[-] Error ejecutando búsqueda ({r.status_code}): {r.text}", file=sys.stderr)
        return
        
    res = r.json()
    print("\n" + "="*80)
    print(f" RESULTADOS DE THREAT HUNTING: {query_str}")
    print("="*80)
    print(json.dumps(res, indent=2, ensure_ascii=False)[:3000])
    print("="*80 + "\n")

# =============================================================================
# COMANDOS: LOG FILTERS (REST API)
# =============================================================================

def handle_filters():
    print("[*] Consultando Log Filters activos...")
    headers = get_rest_headers()
    url = f"https://{HOST}/connect/api/v1/log_filters"
    r = requests.get(url, headers=headers, timeout=20, verify=False)
    if r.status_code != 200:
        print(f"[-] Error consultando log_filters ({r.status_code}): {r.text}", file=sys.stderr)
        return
        
    data = r.json()
    filters = data.get("data", []) if isinstance(data, dict) else data
    print("\n" + "="*80)
    print(f" FILTROS DE LOGS ACTIVOS ({len(filters)})")
    print("="*80)
    for f in filters:
        status = "ACTIVO" if f.get("enabled", True) else "INACTIVO"
        print(f"- [{status}] {f.get('name', 'Sin Nombre')} | Sensor: {f.get('sensor_name', 'Global')} | Condición: {f.get('filter_condition', 'N/A')}")
    print("="*80 + "\n")

# =============================================================================
# COMANDOS: ACCIONES RESPONDER FORTIGATE (7.0.0s AELDEV-67465)
# =============================================================================

def handle_block_target(target: str, target_type: str = "domain", device_name: str = "FG-Technoma", duration: int = 0):
    print(f"[*] Ejecutando orden de bloqueo de {target_type.upper()}: '{target}' en Firewall {device_name} (Stellar 7.0.0s)...")
    headers = get_rest_headers()
    action_name = f"block_{target_type}"
    payload = {
        "action": action_name,
        "target": target,
        "device_name": device_name,
        "duration": duration,
        "description": f"Bloqueo de {target_type.upper()} ejecutado vía Stellar SOC CLI"
    }
    url = f"https://{HOST}/connect/api/v1/actions/firewall"
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        req_id = r.headers.get("request_id") or r.headers.get("requestId") or "N/A"
        if r.status_code in [200, 201]:
            print(f"[+] [SUCCESS] Bloqueo de {target_type.upper()} '{target}' aplicado exitosamente en {device_name} (ReqID: {req_id})")
        else:
            print(f"[-] [FAILED] Error al ejecutar bloqueo en FortiGate ({r.status_code} | ReqID: {req_id}): {r.text}")
    except Exception as e:
        print(f"[-] Error de conexión al despachar acción: {e}")

# =============================================================================
# MAIN PARSER
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Stellar Cyber Unified SOC CLI (MCP & REST Engine)")
    
    # Casos
    parser.add_argument("--case", type=str, help="Consultar detalle completo de un caso por Ticket ID (ej: --case 17813)")
    parser.add_argument("--list-cases", action="store_true", help="Listar casos recientes de incidentes")
    parser.add_argument("--limit", type=int, default=15, help="Límite de casos a listar (def: 15)")
    parser.add_argument("--status", type=str, help="Filtrar por estado (ej: 'In Progress', 'New', 'Closed')")
    parser.add_argument("--update-case", type=str, help="Case ID para actualizar (ej: --update-case 6ad1... --set-status Closed)")
    parser.add_argument("--set-status", type=str, help="Nuevo estado para --update-case")
    parser.add_argument("--set-assignee", type=str, help="User ID para asignar en --update-case")
    
    # Alertas
    parser.add_argument("--case-alerts", type=str, help="Listar alertas asociadas a un Ticket ID")
    parser.add_argument("--alert", type=str, help="Consultar detalle de una alerta individual por Alert ID")
    parser.add_argument("--alert-index", type=str, help="Índice opcional para --alert")
    
    # Tenants
    parser.add_argument("--tenants", action="store_true", help="Listar todos los tenants")
    
    # Cuota y Licencia
    parser.add_argument("--quota", action="store_true", help="Consultar consumo diario y mensual de cuota de licencia")
    
    # Hunting / Data Lake
    parser.add_argument("--search", type=str, help="Búsqueda Lucene en el Data Lake (ej: --search 'srcip:192.168.169.11')")
    parser.add_argument("--tenant", type=str, default="all-tenants", help="Tenant ID para la búsqueda (def: all-tenants)")
    
    # Filtros
    parser.add_argument("--filters", action="store_true", help="Listar filtros de logs activos")
    
    # Responders FortiGate 7.0.0s (AELDEV-67465)
    parser.add_argument("--block-domain", type=str, help="Bloquear dominio malicioso en FortiGate (ej: --block-domain evil.com)")
    parser.add_argument("--block-url", type=str, help="Bloquear URL de phishing en FortiGate (ej: --block-url http://phish.com/login)")
    parser.add_argument("--device-name", type=str, default="FG-Technoma", help="Nombre del Firewall (def: FG-Technoma)")
    parser.add_argument("--duration", type=int, default=0, help="Duración del bloqueo en segundos (0 = permanente)")
    
    # Formato
    parser.add_argument("--json", action="store_true", help="Imprimir salida en formato JSON crudo")

    args = parser.parse_args()

    if args.case:
        handle_get_case(args.case, as_json=args.json)
    elif args.list_cases:
        handle_list_cases(limit=args.limit, status=args.status)
    elif args.update_case:
        handle_update_case(args.update_case, status=args.set_status, assignee=args.set_assignee)
    elif args.case_alerts:
        handle_case_alerts(args.case_alerts)
    elif args.alert:
        handle_alert_detail(args.alert, index=args.alert_index)
    elif args.tenants:
        handle_tenants()
    elif args.quota:
        handle_quota()
    elif args.search:
        handle_search(args.search, cust_id=args.tenant, limit=args.limit)
    elif args.filters:
        handle_filters()
    elif args.block_domain:
        handle_block_target(args.block_domain, target_type="domain", device_name=args.device_name, duration=args.duration)
    elif args.block_url:
        handle_block_target(args.block_url, target_type="url", device_name=args.device_name, duration=args.duration)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
