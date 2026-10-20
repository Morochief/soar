#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — MOTOR DE THREAT HUNTING DIRECTO (stellar_threat_hunter.py)
=============================================================================
Herramienta de caza de amenazas y minería profunda de logs en tiempo real
sobre el Data Lake de Stellar Cyber (Interflow, Syslog, WinEventLog, Firewall).

Permite buscar con sintaxis Lucene nativa, agregar por campos, filtrar
por tenant y ventana temporal, y formatear hallazgos forenses al instante.

Uso:
  python stellar_threat_hunter.py --query "srcip:192.168.169.133"
  python stellar_threat_hunter.py --query "dstport:445 AND msg_class:firewall" --limit 15
  python stellar_threat_hunter.py --ip 172.16.202.24                                   # Caza bidireccional (srcip o dstip)
  python stellar_threat_hunter.py --user egonzalez                                     # Caza de actividad de usuario
  python stellar_threat_hunter.py --query "action:deny" --top-srcip                    # Agregación Top IPs bloqueadas
  python stellar_threat_hunter.py --query "msg_class:interflow_traffic" --top-ports   # Top puertos en tráfico
  python stellar_threat_hunter.py --query "process_name:*powershell*" --index winevent # Caza en logs de Windows
=============================================================================
"""

import os
import sys
import json
import base64
import argparse
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración UTF-8 indestructible en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Carga de credenciales seguras
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
DEFAULT_TENANT_ID = os.environ.get("STELLAR_TENANT_ID", "e511c3fc54cd4d668bb67612c2ef4b04")  # Technoma

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
        raise RuntimeError(f"Error autenticando con Stellar Cyber ({r.status_code}): {r.text}")
    _CACHED_JWT = r.json().get("access_token")
    return _CACHED_JWT


def hunt_logs(
    lucene_query: str,
    target_date: Optional[str] = None,
    tenant_id: Optional[str] = None,
    index_filter: str = "*",
    limit: int = 10,
    aggs: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Ejecuta una búsqueda Lucene en el Data Lake de Stellar Cyber."""
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    date_str = target_date or datetime.now(timezone.utc).strftime("%Y.%m.%d")
    cust_str = tenant_id or DEFAULT_TENANT_ID

    # Construir índice objetivo
    # Patrón: stellar-index-v1-{index_filter}-*-{date_str}*{cust_str}*
    index_pattern = f"*{index_filter}*{date_str}*{cust_str}*"
    url = f"https://{HOST}/connect/api/data/{index_pattern}/_search"

    payload: Dict[str, Any] = {
        "size": limit,
        "query": {
            "bool": {
                "filter": [
                    {"term": {"tenantid": cust_str}}
                ],
                "must": [
                    {"query_string": {"query": lucene_query}}
                ]
            }
        },
        "sort": [
            {"timestamp": {"order": "desc", "unmapped_type": "long"}}
        ]
    }

    if aggs:
        payload["aggs"] = aggs

    r = requests.get(url, headers=headers, json=payload, timeout=60, verify=False)
    if r.status_code != 200:
        # Fallback resiliente a búsqueda amplia si el patrón de fecha cambia de día
        fallback_url = f"https://{HOST}/connect/api/data/*{cust_str}*/_search"
        r = requests.get(fallback_url, headers=headers, json=payload, timeout=60, verify=False)
        if r.status_code != 200:
            raise RuntimeError(f"Error en Data Lake ({r.status_code}): {r.text[:300]}")

    return r.json()


def format_log_hit(hit: Dict[str, Any], idx: int) -> str:
    """Extrae y formatea de forma forense y limpia un evento de Interflow/Syslog."""
    src = hit.get("_source", {})
    ts = src.get("timestamp") or src.get("process_time") or hit.get("_id")
    msg_class = src.get("msg_class") or src.get("event_name") or "unknown"
    srcip = src.get("srcip") or src.get("host_ip") or "N/A"
    srcport = src.get("srcport", "")
    dstip = src.get("dstip", "N/A")
    dstport = src.get("dstport", "")
    proto = src.get("proto_name") or src.get("proto", "")
    action = src.get("action") or src.get("status") or ""
    user = src.get("srcip_username") or src.get("username") or src.get("user", {}).get("name") or ""
    host = src.get("srcip_host") or src.get("computer_name") or src.get("host_name") or ""
    desc = src.get("description") or src.get("message") or ""

    endpoint_info = f"{srcip}:{srcport} -> {dstip}:{dstport} ({proto})" if dstip != "N/A" else f"Host: {srcip}"

    lines = [
        f"[{idx}] Timestamp: {ts} | Clase: {msg_class} | Acción: {action or 'N/A'}",
        f"    Flujo:     {endpoint_info}",
    ]
    if host or user:
        lines.append(f"    Contexto:  Host={host or 'N/A'} | User={user or 'N/A'}")
    if desc:
        clean_desc = desc.replace("\n", " ")[:200]
        lines.append(f"    Detalle:   {clean_desc}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Stellar Cyber Threat Hunter Engine")
    parser.add_argument("--query", "-q", type=str, help="Expresión Lucene (ej: 'srcip:10.11.1.1 AND dstport:445')")
    parser.add_argument("--ip", type=str, help="Caza bidireccional por IP (srcip:IP OR dstip:IP)")
    parser.add_argument("--user", type=str, help="Caza por usuario (srcip_username:USER OR username:USER)")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Límite de eventos a mostrar (default: 10)")
    parser.add_argument("--index", type=str, default="*", help="Filtro de índice (adr, winevent, syslog, audit, ade)")
    parser.add_argument("--date", type=str, help="Fecha en formato YYYY.MM.DD (default: hoy)")
    parser.add_argument("--top-srcip", action="store_true", help="Agregar y mostrar Top 10 IPs de origen")
    parser.add_argument("--top-dstip", action="store_true", help="Agregar y mostrar Top 10 IPs de destino")
    parser.add_argument("--top-ports", action="store_true", help="Agregar y mostrar Top 10 puertos de destino")
    parser.add_argument("--raw", action="store_true", help="Imprimir JSON crudo del primer hit")
    args = parser.parse_args()

    # Construir query según argumentos
    query_parts = []
    if args.query:
        query_parts.append(f"({args.query})")
    if args.ip:
        query_parts.append(f"(srcip:{args.ip} OR dstip:{args.ip} OR host_ip:{args.ip})")
    if args.user:
        query_parts.append(f"(srcip_username:{args.user} OR username:{args.user} OR user.name:{args.user})")

    if not query_parts:
        parser.print_help()
        print("\n[!] Debe especificar al menos una query con --query, --ip o --user.")
        return

    full_query = " AND ".join(query_parts)

    aggs = {}
    if args.top_srcip:
        aggs["top_srcip"] = {"terms": {"field": "srcip.keyword", "size": 10}}
    if args.top_dstip:
        aggs["top_dstip"] = {"terms": {"field": "dstip.keyword", "size": 10}}
    if args.top_ports:
        aggs["top_ports"] = {"terms": {"field": "dstport", "size": 10}}

    print(f"\n{'='*80}")
    print(f"🎯 THREAT HUNTING EN DATA LAKE STELLAR CYBER")
    print(f"{'='*80}")
    print(f"Query Lucene:  {full_query}")
    print(f"Índice:        {args.index} | Límite: {args.limit}")
    print(f"{'-'*80}")

    res = hunt_logs(
        lucene_query=full_query,
        target_date=args.date,
        index_filter=args.index,
        limit=args.limit,
        aggs=aggs if aggs else None
    )

    hits_obj = res.get("hits", {})
    total_val = hits_obj.get("total", {}).get("value", 0)
    hits = hits_obj.get("hits", [])

    print(f"[+] Total de Eventos Encontrados en Data Lake: {total_val:,}\n")

    if not hits:
        print("[-] No se encontraron registros con los criterios especificados.")
        print(f"{'='*80}\n")
        return

    for i, h in enumerate(hits, 1):
        print(format_log_hit(h, i))
        print(f"{'-'*80}")

    if "aggregations" in res:
        print(f"\n📊 AGREGACIONES FORENSES DE THREAT HUNTING:")
        for agg_name, agg_data in res["aggregations"].items():
            print(f"\n  Top {agg_name}:")
            for b in agg_data.get("buckets", []):
                print(f"    • {str(b.get('key')):<30} -> {b.get('doc_count'):,} eventos")

    if args.raw and hits:
        print(f"\n{'='*80}\n📄 PAYLOAD CRUDO DEL PRIMER HIT:\n{'='*80}")
        print(json.dumps(hits[0].get("_source", {}), indent=2, ensure_ascii=False))

    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
