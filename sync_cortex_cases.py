#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — SINCRONIZADOR DE CASOS CORTEX XDR A STELLAR CYBER
=============================================================================
Rastrea todas las alertas de Cortex XDR en el Data Lake de Stellar Cyber
que posean un 'palo_alto_networks.case_id' válido.

Para cada 'case_id' de Cortex:
  1. Verifica si ya existe un Caso formal en Stellar Cyber.
  2. Si no existe, lo crea automáticamente vía POST /connect/api/v1/cases.
  3. Vincula todos los hits y alertas forenses correspondientes a dicho Caso
     vía POST /connect/api/v1/cases/{case_id}/alerts.

Uso:
  python sync_cortex_cases.py --dry-run     # Solo audita y muestra qué crearía
  python sync_cortex_cases.py               # Crea y sincroniza los casos faltantes
  python sync_cortex_cases.py --limit 10    # Procesa hasta 10 casos recientes
=============================================================================
"""

import os
import sys
import json
import base64
import argparse
from typing import Any, Dict, List, Optional
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importar configuración y sesión
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import stellar_alerts_checker
from cortex_case_matching import case_matches_cortex_id, find_case_for_cortex_id, alert_in_month  # noqa: F401

HOST = stellar_alerts_checker.HOST
DEFAULT_TENANT_ID = stellar_alerts_checker.DEFAULT_TENANT_ID


def get_headers() -> Dict[str, str]:
    jwt = stellar_alerts_checker.get_jwt()
    return {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }


def fetch_stellar_cases(tenant_id: str, page_size: int = 200, max_cases: int = 20000) -> List[Dict[str, Any]]:
    """Recupera TODOS los casos del tenant en Stellar Cyber, paginando con limit/skip."""
    url = f"https://{HOST}/connect/api/v1/cases"
    headers = get_headers()
    all_cases: List[Dict[str, Any]] = []
    seen = set()
    skip = 0
    while skip < max_cases:
        params = {"cust_id": tenant_id, "limit": page_size, "skip": skip}
        r = requests.get(url, headers=headers, params=params, verify=False, timeout=30)
        if r.status_code != 200:
            raise RuntimeError(f"Error consultando casos de Stellar ({r.status_code}): {r.text[:200]}")
        page = (r.json().get("data", {}) or {}).get("cases", []) or []
        nuevos = 0
        for c in page:
            cid = c.get("_id")
            if cid and cid not in seen:
                seen.add(cid)
                all_cases.append(c)
                nuevos += 1
        # Fin: página incompleta, o la API ignoró 'skip' y repitió la misma página
        if len(page) < page_size or nuevos == 0:
            break
        skip += page_size
    return all_cases


def fetch_cortex_alerts_with_case_id(tenant_id: str, max_hits: int = 10000, page_size: int = 1000) -> Dict[Any, List[Dict[str, Any]]]:
    """
    Busca en el Data Lake (aella-ser-*) todas las alertas de Palo Alto Cortex XDR
    que posean 'palo_alto_networks.case_id' asignado.
    Retorna un diccionario agrupado: { case_id: [alert_hit1, alert_hit2, ...] }
    """
    url = f"https://{HOST}/connect/api/data/*ser*{tenant_id}*/_search"
    headers = get_headers()
    base_query = {
        "bool": {
            "must": [
                {"term": {"msg_class": "palo_alto_networks_cortex_xdr_alerts"}},
                {"exists": {"field": "palo_alto_networks.case_id"}}
            ]
        }
    }
    # Paginación (from/size) hasta max_hits para no perder casos viejos
    hits: List[Dict[str, Any]] = []
    offset = 0
    while offset < max_hits:
        size = min(page_size, max_hits - offset)
        payload = {
            "from": offset,
            "size": size,
            "query": base_query,
            "sort": [{"timestamp": {"order": "desc"}}]
        }
        r = requests.get(url, headers=headers, json=payload, timeout=45, verify=False)
        if r.status_code != 200:
            raise RuntimeError(f"Error consultando alertas de Cortex ({r.status_code}): {r.text[:200]}")
        page = r.json().get("hits", {}).get("hits", [])
        hits.extend(page)
        if len(page) < size:
            break
        offset += size
    cases_map: Dict[Any, List[Dict[str, Any]]] = {}
    
    for h in hits:
        src = h.get("_source", {})
        pan = src.get("palo_alto_networks", {})
        cid = pan.get("case_id")
        if cid is None:
            continue
        if cid not in cases_map:
            cases_map[cid] = []
        cases_map[cid].append({
            "_id": h.get("_id"),
            "_index": h.get("_index"),
            "alert_id": pan.get("alert_id"),
            "host": src.get("host", {}).get("name") or "UNKNOWN",
            "threat": src.get("event", {}).get("threat", {}).get("name") or pan.get("name") or "Cortex XDR Detection",
            "severity": pan.get("severity") or src.get("event", {}).get("severity_str") or "Medium",
            "timestamp": src.get("timestamp_utc") or src.get("timestamp")
        })
    return cases_map


def format_severity(sev_str: str) -> str:
    """Convierte severidades a las opciones exactas permitidas por Stellar: Low, Medium, High, Critical."""
    s = str(sev_str).strip().lower()
    if "crit" in s:
        return "Critical"
    if "high" in s:
        return "High"
    if "low" in s:
        return "Low"
    return "Medium"


def create_stellar_case(tenant_id: str, cortex_case_id: Any, alerts: List[Dict[str, Any]]) -> Optional[str]:
    """Crea un caso formal en Stellar Cyber vinculado al Case ID de Cortex."""
    first = alerts[0]
    threat = first["threat"]
    host = first["host"]
    # Severidad del caso = la más alta de todas sus alertas (no solo la primera)
    _rank = {"Low": 0, "Medium": 1, "High": 2, "Critical": 3}
    severity = max((format_severity(a.get("severity", "Medium")) for a in alerts), key=lambda x: _rank.get(x, 1))
    
    case_name = f"Palo Alto Networks Cortex XDR: {threat} - CASE {cortex_case_id}"
    
    alert_refs = [{"_id": a["_id"], "_index": a["_index"]} for a in alerts]
    
    payload = {
        "name": case_name,
        "cust_id": tenant_id,
        "severity": severity,
        "status": "New",
        "tags": ["Cortex-XDR", "Sync-Auto", f"Case-{cortex_case_id}"],
        "alerts": alert_refs
    }
    
    url = f"https://{HOST}/connect/api/v1/cases"
    headers = get_headers()
    r = requests.post(url, headers=headers, json=payload, verify=False, timeout=30)
    if r.status_code in (200, 201):
        case_obj = r.json().get("data", {})
        stellar_cid = case_obj.get("_id")
        ticket_id = case_obj.get("ticket_id")
        print(f"  [+] CREADO Caso Stellar ID {stellar_cid} (Ticket #{ticket_id}) para Cortex Case #{cortex_case_id}")
        
        # Asegurar vinculación explícita de alertas vía subrecurso
        link_alerts_to_case(stellar_cid, alert_refs)
        return stellar_cid
    else:
        print(f"  [-] ERROR creando caso para Cortex #{cortex_case_id}: {r.status_code} - {r.text[:200]}")
        return None


def link_alerts_to_case(stellar_case_id: str, alert_refs: List[Dict[str, str]]):
    """Vincula alertas forenses al caso en Stellar Cyber."""
    url = f"https://{HOST}/connect/api/v1/cases/{stellar_case_id}/alerts"
    headers = get_headers()
    payload = {"alerts": alert_refs}
    r = requests.post(url, headers=headers, json=payload, verify=False, timeout=30)
    if r.status_code == 200:
        print(f"      -> {len(alert_refs)} alerta(s) forense(s) vinculada(s) con éxito.")
    else:
        print(f"      -> Aviso vinculación: {r.status_code} - {r.text[:150]}")


def sync(tenant_id: str, limit: Optional[int] = None, dry_run: bool = False, month: Optional[str] = None):
    print("=" * 80)
    print(f"🛡️ INICIANDO SINCRONIZACIÓN DE CASOS CORTEX XDR ➔ STELLAR CYBER")
    print(f"Tenant: {tenant_id} | Host: {HOST} | Modo Dry-Run: {dry_run} | Filtro Mes: {month or 'Todos'}")
    print("=" * 80)
    
    # 1. Casos existentes en Stellar
    existing_cases = fetch_stellar_cases(tenant_id)
    print(f"[*] Casos actuales registrados en Stellar Cyber: {len(existing_cases)}")
    
    # 2. Alertas con Case ID en Data Lake
    cortex_cases_map = fetch_cortex_alerts_with_case_id(tenant_id)
    print(f"[*] Casos de Cortex XDR detectados en Data Lake: {len(cortex_cases_map)}")
    
    # Filtrar por mes si se especifica (ej: '2026-10')
    if month:
        filtered_map = {}
        for cid, alerts in cortex_cases_map.items():
            month_alerts = [a for a in alerts if alert_in_month(a, month)]
            if month_alerts:
                filtered_map[cid] = month_alerts
        cortex_cases_map = filtered_map
        print(f"[*] Casos de Cortex XDR correspondientes a {month}: {len(cortex_cases_map)}")
    
    sorted_case_ids = sorted(cortex_cases_map.keys(), key=lambda x: int(x) if str(x).isdigit() else 0, reverse=True)
    if limit:
        sorted_case_ids = sorted_case_ids[:limit]
        print(f"[*] Limitando procesamiento a los {limit} casos.")
    
    created_count = 0
    already_synced = 0
    
    for cid in sorted_case_ids:
        alerts = cortex_cases_map[cid]
        first = alerts[0]
        
        # Verificar si ya existe por patrón CASE <id> o CASE_<id>
        matched_case = find_case_for_cortex_id(existing_cases, cid)
        
        if matched_case:
            already_synced += 1
            st_id = matched_case.get("_id")
            st_ticket = matched_case.get("ticket_id")
            print(f"[OK] Cortex Case #{cid} ya existe en Stellar: '{matched_case.get('name')}' (ID: {st_id})")
            
            # Asegurar que sus alertas estén vinculadas
            if not dry_run:
                alert_refs = [{"_id": a["_id"], "_index": a["_index"]} for a in alerts]
                link_alerts_to_case(st_id, alert_refs)
            continue
        
        print(f"\n[!] CORTEX CASE #{cid} PENDIENTE DE SINCRONIZAR:")
        print(f"    Host: {first['host']} | Amenaza: {first['threat']} | Alertas: {len(alerts)} | Fecha: {first['timestamp']}")
        
        if dry_run:
            print(f"    [DRY-RUN] Se crearía el caso: 'Palo Alto Networks Cortex XDR: {first['threat']} - CASE {cid}'")
        else:
            new_cid = create_stellar_case(tenant_id, cid, alerts)
            if new_cid:
                created_count += 1
    
    print("\n" + "=" * 80)
    print(f"RESUMEN DE SINCRONIZACIÓN:")
    print(f"  - Ya existían: {already_synced}")
    print(f"  - Creados nuevos: {created_count}")
    print(f"  - Pendientes / Modo: {'Simulación (Dry-Run)' if dry_run else 'Completado'}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sincronizador de Casos Cortex XDR a Stellar Cyber")
    parser.add_argument("--limit", type=int, default=None, help="Límite de casos a procesar")
    parser.add_argument("--dry-run", action="store_true", help="Simular sin crear casos reales")
    parser.add_argument("--tenant", type=str, default=DEFAULT_TENANT_ID, help="ID de Tenant de Stellar")
    parser.add_argument("--month", type=str, default=None, help="Filtrar por año-mes (ej. 2026-10)")
    
    args = parser.parse_args()
    sync(tenant_id=args.tenant, limit=args.limit, dry_run=args.dry_run, month=args.month)
