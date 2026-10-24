#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — GENERADOR AUTOMÁTICO DE CASOS CORTEX XDR (CORTEX-TO-CASE)
=============================================================================
Script autónomo que inspecciona en el Data Lake de Stellar Cyber todas las 
alertas de Cortex XDR que posean 'case_id' O 'incident_id'.

Lógica:
  1. Detecta cada ID único de Cortex (ej: Case 618, 617, 615...).
  2. Verifica contra la API de Stellar Cyber si ya existe un Caso creado con ese ID.
  3. Si NO existe:
     - Crea automáticamente el Caso en Stellar Cyber con su título descriptivo y severidad.
     - Incluye las alertas vinculadas de forma atómica en el POST /cases.
=============================================================================
"""

import os
import sys
import time
import json
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

# Carga de credenciales y configuración central
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import stellar_alerts_checker
    HOST = stellar_alerts_checker.HOST
    DEFAULT_TENANT_ID = stellar_alerts_checker.DEFAULT_TENANT_ID
    get_jwt = stellar_alerts_checker.get_jwt
except Exception:
    HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
    DEFAULT_TENANT_ID = os.environ.get("STELLAR_TENANT_ID", "e511c3fc54cd4d668bb67612c2ef4b04")
    def get_jwt():
        return ""


def get_headers() -> Dict[str, str]:
    jwt = get_jwt()
    return {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }


def fetch_stellar_cases(tenant_id: str) -> List[Dict[str, Any]]:
    """Obtiene todos los casos existentes en Stellar Cyber."""
    url = f"https://{HOST}/connect/api/v1/cases"
    headers = get_headers()
    params = {"cust_id": tenant_id, "limit": 200}
    r = requests.get(url, headers=headers, params=params, verify=False, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"Error consultando casos de Stellar ({r.status_code}): {r.text[:200]}")
    data = r.json().get("data", {})
    return data.get("cases", []) if isinstance(data, dict) else data


def fetch_cortex_alerts(tenant_id: str, month: Optional[str] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Busca todas las alertas de Cortex XDR en el Data Lake (aella-ser-*)
    que tengan 'palo_alto_networks.case_id' O 'palo_alto_networks.incident_id'.
    Retorna un diccionario agrupado: { 'ID': [alert1, alert2, ...] }
    """
    url = f"https://{HOST}/connect/api/data/*ser*{tenant_id}*/_search"
    headers = get_headers()
    payload = {
        "size": 500,
        "query": {
            "bool": {
                "must": [
                    {"term": {"tenantid": tenant_id}},
                    {"query_string": {
                        "query": "_exists_:palo_alto_networks.case_id OR _exists_:palo_alto_networks.incident_id"
                    }}
                ]
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}]
    }
    r = requests.get(url, headers=headers, json=payload, timeout=45, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Error consultando Data Lake de Stellar ({r.status_code}): {r.text[:200]}")
    
    hits = r.json().get("hits", {}).get("hits", [])
    grouped: Dict[str, List[Dict[str, Any]]] = {}

    for h in hits:
        src = h.get("_source", {})
        pan = src.get("palo_alto_networks", {})
        cid = pan.get("incident_id") or pan.get("case_id")
        if not cid:
            continue
        
        cid_str = str(cid)
        # Extraer host limpio
        hosts = pan.get("hosts", [])
        host_name = "N/A"
        if hosts:
            h_raw = str(hosts[0])
            host_name = h_raw.split(":")[0].upper() if ":" in h_raw else h_raw.upper()
        
        desc = pan.get("description") or pan.get("incident_name") or src.get("xdr_event", {}).get("description") or "Alerta Cortex XDR"
        ts = src.get("timestamp_utc") or src.get("orig_timestamp_utc") or src.get("timestamp")

        # Filtrado por mes si se especifica
        if month and month not in str(ts):
            continue

        sev = pan.get("severity") or src.get("event_severity") or "High"
        sev_clean = "High"
        if isinstance(sev, str):
            sev_lower = sev.lower()
            if "crit" in sev_lower:
                sev_clean = "Critical"
            elif "high" in sev_lower:
                sev_clean = "High"
            elif "med" in sev_lower:
                sev_clean = "Medium"
            elif "low" in sev_lower:
                sev_clean = "Low"

        alert_info = {
            "_id": h.get("_id"),
            "_index": h.get("_index"),
            "host": host_name,
            "threat": desc[:100],
            "timestamp": str(ts),
            "full_desc": desc,
            "severity": sev_clean
        }

        if cid_str not in grouped:
            grouped[cid_str] = []
        grouped[cid_str].append(alert_info)

    return grouped


def create_stellar_case(tenant_id: str, case_id: str, alerts: List[Dict[str, Any]]) -> Optional[str]:
    """Crea formalmente un caso en Stellar Cyber y vincula sus alertas."""
    first = alerts[0]
    case_name = f"Palo Alto Networks Cortex XDR: {first['threat']} - CASE {case_id}"
    alert_refs = [{"_id": a["_id"], "_index": a["_index"]} for a in alerts]
    
    url = f"https://{HOST}/connect/api/v1/cases"
    headers = get_headers()
    payload = {
        "name": case_name,
        "cust_id": tenant_id,
        "severity": first.get("severity", "High"),
        "status": "New",
        "tags": ["Cortex-XDR", "Sync-Auto", f"Case-{case_id}"],
        "alerts": alert_refs
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=25, verify=False)
        if r.status_code not in (200, 201):
            print(f"  [✘] Error creando caso #{case_id} ({r.status_code}): {r.text[:150]}")
            return None
        
        res = r.json()
        new_hex_id = res.get("data", {}).get("_id") or res.get("data", {}).get("id") or res.get("_id")
        new_ticket = res.get("data", {}).get("ticket_id") or res.get("ticket_id", "N/A")
        print(f"  [✔] CASO CREADO EXITOSAMENTE: '{case_name}' -> Ticket #{new_ticket} ({len(alert_refs)} alertas)")
        return new_hex_id
    except Exception as e:
        print(f"  [✘] Excepción creando caso #{case_id}: {e}")
        return None


def run_sync(tenant_id: str, month: Optional[str] = None, dry_run: bool = False) -> int:
    """Ejecuta una ronda de verificación y creación."""
    print(f"\n[*] Consultando casos y alertas para Tenant: {tenant_id} (Mes: {month or 'Todos'})...")
    existing_cases = fetch_stellar_cases(tenant_id)
    cortex_alerts_map = fetch_cortex_alerts(tenant_id, month=month)
    
    print(f"[*] Total casos actuales en Stellar: {len(existing_cases)}")
    print(f"[*] Incidentes de Cortex XDR encontrados en Data Lake: {len(cortex_alerts_map)}")

    created_count = 0
    already_synced = 0

    sorted_ids = sorted(cortex_alerts_map.keys(), key=lambda x: int(x) if x.isdigit() else 0, reverse=True)

    for cid in sorted_ids:
        alerts = cortex_alerts_map[cid]
        first = alerts[0]

        # Verificar si ya existe el caso
        pattern_1 = f"CASE {cid}"
        pattern_2 = f"CASE_{cid}"
        pattern_3 = f"Case {cid}"
        matched = next((
            c for c in existing_cases 
            if pattern_1 in c.get("name", "").upper() 
            or pattern_2 in c.get("name", "").upper() 
            or pattern_3 in c.get("name", "")
            or f"#{cid}" in c.get("name", "")
            or str(cid) in c.get("description", "")
        ), None)

        if matched:
            already_synced += 1
            continue

        print(f"\n[!] CORTEX CASE #{cid} SIN CASO EN STELLAR:")
        print(f"    Host: {first['host']} | Alertas: {len(alerts)} | Fecha: {first['timestamp']}")
        print(f"    Amenaza: {first['threat']}")

        if dry_run:
            print(f"    [DRY-RUN] Se crearía el caso: 'Palo Alto Networks Cortex XDR: {first['threat']} - CASE {cid}'")
        else:
            nid = create_stellar_case(tenant_id, cid, alerts)
            if nid:
                created_count += 1
            time.sleep(0.5)

    print("\n" + "="*80)
    print(f"RESUMEN: Ya existían: {already_synced} | Creados: {created_count} | {'Modo Simulación' if dry_run else 'Completado'}")
    print("="*80)
    return created_count


def main():
    parser = argparse.ArgumentParser(description="Auto-generador de Casos Cortex XDR a Stellar Cyber")
    parser.add_argument("--month", type=str, default=None, help="Filtrar por mes (ej: '2026-10')")
    parser.add_argument("--dry-run", action="store_true", help="Simular sin crear casos reales")
    parser.add_argument("--tenant", type=str, default=DEFAULT_TENANT_ID, help="ID de Tenant")
    parser.add_argument("--daemon", type=int, default=None, help="Ejecutar en bucle continuo cada N segundos")
    args = parser.parse_args()

    if args.daemon:
        print(f"[*] Iniciando en modo DAEMON (intervalo: {args.daemon}s)... Presione Ctrl+C para detener.")
        while True:
            try:
                run_sync(args.tenant, month=args.month, dry_run=args.dry_run)
            except Exception as e:
                print(f"[!] Error en ciclo daemon: {e}")
            time.sleep(args.daemon)
    else:
        run_sync(args.tenant, month=args.month, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
