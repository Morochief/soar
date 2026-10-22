#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — AUDITOR Y CHEQUEADOR DE HITS DE ALERTAS (stellar_alerts_checker.py)
=============================================================================
Herramienta oficial para inspeccionar la vista de Alertas (Hits) de Stellar Cyber
en ventanas de tiempo arbitrarias (1h, 6h, 12h, 24h, hoy).

Permite:
  1. Replicar exactamente la vista web: https://technoma.stellarcyber.cloud/alerts?view=hits
  2. Listar la tabla agregada por Tipo de Alerta con contadores de hits, severidad y fidelidad.
  3. Ver el detalle de los hits raros o sospechosos (Uncommon Process, arp.exe, PowerShell, etc.)
  4. Extraer el equipo, usuario, línea de comando, IP y payload imprimible IDS.
  5. Evaluar si un hit merece escalar a Caso formal o si es un falso positivo.

Uso:
  python stellar_alerts_checker.py --hours 12               # Agrupación de hits en las últimas 12 horas
  python stellar_alerts_checker.py --today                  # Todos los hits desde las 00:00 de hoy
  python stellar_alerts_checker.py --type "arp.exe"         # Detalle forense de hits de arp.exe
  python stellar_alerts_checker.py --type "powershell"      # Detalle de comandos PowerShell sospechosos
  python stellar_alerts_checker.py --critical               # Filtrar solo hits Críticos / High Fidelity
  python stellar_alerts_checker.py --hours 12 --inspect     # Muestra forense de hits de endpoint no comunes
=============================================================================
"""

import os
import sys
import json
import base64
import argparse
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# UTF-8 para consola de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Carga de credenciales
try:
    from dotenv import load_dotenv
    _env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(_env_path):
        load_dotenv(_env_path)
    else:
        load_dotenv()
except Exception:
    pass

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")
DEFAULT_TENANT_ID = os.environ.get("STELLAR_TENANT_ID", "e511c3fc54cd4d668bb67612c2ef4b04")

_CACHED_JWT: Optional[str] = None

def get_jwt() -> str:
    global _CACHED_JWT
    if _CACHED_JWT:
        return _CACHED_JWT
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Error de autenticación con Stellar Cyber ({r.status_code}): {r.text}")
    _CACHED_JWT = r.json().get("access_token")
    return _CACHED_JWT


def query_alerts_hits(
    start_ms: int,
    end_ms: int,
    tenant_id: Optional[str] = None,
    lucene_filter: Optional[str] = None,
    limit: int = 100,
    aggs: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Consulta directa a los índices de eventos de seguridad (aella-ser-*) en el Data Lake."""
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    cust = tenant_id or DEFAULT_TENANT_ID

    must_clauses = [
        {"range": {"timestamp": {"gte": start_ms, "lte": end_ms}}}
    ]
    if lucene_filter:
        must_clauses.append({"query_string": {"query": lucene_filter}})

    payload: Dict[str, Any] = {
        "size": limit,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": cust}}
                ],
                "must": must_clauses
            }
        },
        "sort": [
            {"timestamp": {"order": "desc", "unmapped_type": "long"}}
        ]
    }
    if aggs:
        payload["aggs"] = aggs

    url = f"https://{HOST}/connect/api/data/*ser*{cust}*/_search"
    r = requests.get(url, headers=headers, json=payload, timeout=45, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Fallo al consultar hits de alertas ({r.status_code}): {r.text[:200]}")
    return r.json()


def format_ts(ts_val) -> str:
    if not ts_val:
        return "N/A"
    try:
        if isinstance(ts_val, (int, float)):
            # Detectar ms vs seg
            if ts_val > 1e11:
                ts_val = ts_val / 1000.0
            return datetime.fromtimestamp(ts_val).strftime("%Y-%m-%d %H:%M:%S")
        return str(ts_val)
    except Exception:
        return str(ts_val)


def main():
    parser = argparse.ArgumentParser(description="Stellar Cyber Alerts (Hits) Checker & Triage Auditor")
    parser.add_argument("--hours", type=int, default=12, help="Ventana de tiempo hacia atrás en horas (default: 12)")
    parser.add_argument("--today", action="store_true", help="Filtrar desde las 00:00 de hoy")
    parser.add_argument("--type", type=str, help="Filtrar y mostrar detalles forenses de un tipo específico de alerta o proceso")
    parser.add_argument("--critical", action="store_true", help="Filtrar solo alertas con severidad Critical o High")
    parser.add_argument("--inspect", action="store_true", help="Inspección forense de hits aislados y comportamientos de endpoint")
    parser.add_argument("--tenant", type=str, default=DEFAULT_TENANT_ID, help="ID del Tenant (default: Technoma)")
    args = parser.parse_args()

    now = datetime.now()
    now_ms = int(now.timestamp() * 1000)

    if args.today:
        start_dt = now.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        start_dt = now - timedelta(hours=args.hours)
    start_ms = int(start_dt.timestamp() * 1000)

    print(f"\n{'='*95}")
    print(f" 🛡️ REPORTE DE HITS DE ALERTAS STELLAR CYBER ({start_dt.strftime('%Y-%m-%d %H:%M')} -> {now.strftime('%H:%M')})")
    print(f"{'='*95}\n")

    # 1. Agregación general (Replica la tabla de la web)
    aggs = {
        "alert_types": {
            "terms": {
                "field": "xdr_event.display_name.keyword",
                "size": 50
            },
            "aggs": {
                "max_score": {"max": {"field": "event_score"}},
                "severities": {"terms": {"field": "severity.keyword", "size": 5}}
            }
        }
    }

    base_filter = None
    if args.critical:
        base_filter = "severity:(critical OR high) OR event_score:[70 TO 100]"
    if args.type:
        base_filter = f"*{args.type}*"

    res = query_alerts_hits(
        start_ms=start_ms,
        end_ms=now_ms,
        tenant_id=args.tenant,
        lucene_filter=base_filter,
        limit=20 if args.inspect or args.type else 0,
        aggs=aggs
    )

    total_hits = res.get("hits", {}).get("total", {})
    total_val = total_hits.get("value", 0) if isinstance(total_hits, dict) else total_hits
    buckets = res.get("aggregations", {}).get("alert_types", {}).get("buckets", [])

    print(f"[*] Total de Hits registrados en la ventana: {total_val}")
    print(f"[*] Tipos de Alertas diferentes observadas: {len(buckets)}\n")

    print(f"{'TIPO DE ALERTA':<55} {'TOTAL HITS':<12} {'MAX SCORE':<12} {'SEVERIDADES'}")
    print(f"{'-'*95}")
    for b in buckets:
        name = b.get("key") or "Desconocido"
        count = b.get("doc_count", 0)
        max_s = b.get("max_score", {}).get("value")
        s_str = f"{max_s:.1f}" if max_s is not None else "N/A"
        sevs = [f"{sb.get('key')}:{sb.get('doc_count')}" for sb in b.get("severities", {}).get("buckets", [])]
        sev_str = ", ".join(sevs) if sevs else "N/A"
        print(f"{name[:53]:<55} {count:<12} {s_str:<12} {sev_str}")
    print(f"{'='*95}\n")

    # 2. Si se solicitó inspección de detalles o filtrado por tipo
    hits = res.get("hits", {}).get("hits", [])
    if (args.inspect or args.type) and hits:
        print(f"[*] DETALLE FORENSE DE LOS EVENTOS / HITS ({len(hits)} muestras recientes):")
        print(f"{'='*95}")
        for i, h in enumerate(hits, 1):
            src = h.get("_source", {})
            xdr = src.get("xdr_event", {})
            ev_name = xdr.get("display_name") or src.get("event_name")
            timestamp = format_ts(src.get("timestamp"))
            src_ip = src.get("srcip", "N/A")
            src_host = src.get("srcip_host", "N/A")
            user = src.get("username") or src.get("user") or "N/A"
            dst_ip = src.get("dstip", "N/A")
            dst_port = src.get("dstport", "N/A")
            app = src.get("appid_name", "N/A")
            score = src.get("event_score") or src.get("score") or "N/A"
            sev = src.get("severity", "N/A")

            # Datos de proceso o comando (Cortex / WinEvent)
            proc = src.get("process", {})
            cmd = proc.get("command_line") or src.get("cmdline") or src.get("command_line") or "N/A"
            parent = proc.get("parent_name") or src.get("parent_process_name") or "N/A"
            
            # Payload IDS 7.0.0s
            ids_payload = src.get("ids", {}).get("payload_details", {}).get("payload_printable")

            print(f"\n[{i}] {ev_name} | {timestamp}")
            print(f"    Severidad: {sev} | Score: {score}")
            print(f"    Origen:    Host={src_host} | IP={src_ip} | Usuario={user}")
            if dst_ip != "N/A":
                print(f"    Destino:   IP={dst_ip} | Puerto={dst_port} ({app})")
            if cmd != "N/A":
                print(f"    Comando:   {cmd[:180]}")
            if parent != "N/A":
                print(f"    Padre:     {parent}")
            if ids_payload:
                print(f"    Payload:   {ids_payload[:200]}...")
            print(f"{'-'*95}")

if __name__ == "__main__":
    main()
