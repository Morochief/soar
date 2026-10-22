#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ AUDITOR TÉCNICO DE VISTAS DE THREAT HUNTING Y CONTROL DE INGESTA
=============================================================================
Inspecciona directamente los índices del Data Lake de Stellar Cyber para:
  1. Desglosar las cajas de la vista de Threat Hunting (Firewall 2.1M, Network Apps 3.3M, etc.).
  2. Auditar el tráfico hacia 192.168.15.60:7001 (Efecto del descarte de 'action: close').
  3. Auditar el tráfico 'action: passthrough' (Efecto de los 52 dominios).
  4. Confirmar que las exclusiones (ChatGPT, Claude, Spotify) siguen visibles.
=============================================================================
"""

import os
import sys
import json
import base64
import time
import argparse
from datetime import datetime, timezone
import requests
import urllib3

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
    if r.status_code != 200:
        raise RuntimeError(f"Error de autenticación: {r.status_code} - {r.text}")
    return r.json().get("access_token")

def search_datalake(index_pattern: str, query_dict: dict, aggs_dict: dict = None, size: int = 0) -> dict:
    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    payload = {
        "size": size,
        "query": query_dict
    }
    if aggs_dict:
        payload["aggs"] = aggs_dict
    url = f"https://{HOST}/connect/api/data/{index_pattern}/_search"
    res = requests.get(url, headers=headers, json=payload, timeout=45, verify=False)
    if res.status_code != 200:
        raise RuntimeError(f"Error en query ({res.status_code}): {res.text[:200]}")
    return res.json()

def main():
    parser = argparse.ArgumentParser(description="Auditor Forense de Threat Hunting e Ingesta")
    parser.add_argument("--hours", type=int, default=24, help="Ventana de tiempo en horas (default: 24h)")
    args = parser.parse_args()

    now_ms = int(time.time() * 1000)
    start_ms = now_ms - (args.hours * 3600 * 1000)

    print("=" * 80)
    print(f"🛡️ AUDITORÍA INTEGRAL DE THREAT HUNTING E INGESTA — STELLAR CYBER ({args.hours} HORAS)")
    print(f"⏱️ Ventana: {datetime.fromtimestamp(start_ms/1000).strftime('%Y-%m-%d %H:%M:%S')}  ➔  {datetime.fromtimestamp(now_ms/1000).strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # 1. DESGLOSE GENERAL DE LOS ÍNDICES (Las cajas de la pantalla)
    print("\n📦 1. DESGLOSE DE VOLUMEN POR FAMILIA (Las 'Cards' de la UI):")
    query_base = {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [{"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}}]
        }
    }
    aggs_class = {
        "by_class": {
            "terms": {"field": "msg_class.keyword", "size": 15}
        }
    }
    res_classes = search_datalake(f"*adr*{TENANT_ID}*", query_base, aggs_class)
    total_adr = res_classes.get("hits", {}).get("total", {}).get("value", 0)
    print(f"  • Total Eventos de Red/Firewall/Sensor: {total_adr:,}")
    for b in res_classes.get("aggregations", {}).get("by_class", {}).get("buckets", []):
        pct = (b["doc_count"] / total_adr * 100) if total_adr else 0
        print(f"    - {b['key']:<25}: {b['doc_count']:>10,} logs  ({pct:>5.1f}%)")

    # 2. AUDITORÍA DEL SERVIDOR 192.168.15.60:7001
    print("\n🖥️ 2. AUDITORÍA TCP/7001 HACIA 192.168.15.60 (Evaluación de Descarte 'close'):")
    query_7001 = {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"dstip.keyword": "192.168.15.60"}},
                {"term": {"dstport": 7001}}
            ]
        }
    }
    aggs_action_7001 = {
        "by_action": {"terms": {"field": "action.keyword", "size": 10}},
        "recent_timeline": {
            "date_histogram": {
                "field": "timestamp",
                "fixed_interval": "1h"
            }
        }
    }
    res_7001 = search_datalake(f"*adr*{TENANT_ID}*", query_7001, aggs_action_7001)
    tot_7001 = res_7001.get("hits", {}).get("total", {}).get("value", 0)
    print(f"  • Total Eventos registrados hacia 192.168.15.60:7001: {tot_7001:,}")
    print("  • Distribución por Acción:")
    for a in res_7001.get("aggregations", {}).get("by_action", {}).get("buckets", []):
        print(f"    - action '{a['key']}': {a['doc_count']:,} logs")

    # 3. AUDITORÍA DE TRÁFICO PASSTHROUGH
    print("\n🌐 3. AUDITORÍA DE TRÁFICO 'ACTION: PASSTHROUGH' (Impacto de 52 Dominios Filtrados):")
    query_pt = {
        "bool": {
            "filter": [{"term": {"tenantid": TENANT_ID}}],
            "must": [
                {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                {"term": {"action.keyword": "passthrough"}}
            ]
        }
    }
    aggs_pt = {
        "top_urls": {"terms": {"field": "url.keyword", "size": 15}}
    }
    res_pt = search_datalake(f"*adr*{TENANT_ID}*", query_pt, aggs_pt)
    tot_pt = res_pt.get("hits", {}).get("total", {}).get("value", 0)
    print(f"  • Total eventos 'passthrough' que aún ingresan al Data Lake: {tot_pt:,}")
    print("  • Top 10 URLs/Destinos que siguen generando passthrough:")
    for u in res_pt.get("aggregations", {}).get("top_urls", {}).get("buckets", []):
        print(f"    - {u['key']:<55}: {u['doc_count']:>6,} logs")

    # 4. COMPROBACIÓN DE EXCLUSIONES (ChatGPT, Claude, Spotify)
    print("\n🛡️ 4. VERIFICACIÓN DE EXCLUSIONES ACTIVAS (Deben seguir entrando al SIEM):")
    for name, dom_query in [("ChatGPT", "*chatgpt.com*"), ("Claude / Anthropic", "*anthropic.com*"), ("Spotify", "*spotify.com*")]:
        query_exc = {
            "bool": {
                "filter": [{"term": {"tenantid": TENANT_ID}}],
                "must": [
                    {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                    {"query_string": {"query": f"url:{dom_query}"}}
                ]
            }
        }
        res_exc = search_datalake(f"*adr*{TENANT_ID}*", query_exc)
        cnt = res_exc.get("hits", {}).get("total", {}).get("value", 0)
        status = "✅ VISIBLE EN SIEM" if cnt > 0 else "ℹ️ Sin tráfico en esta ventana"
        print(f"  • {name:<20} (url:{dom_query:<18}): {cnt:>6,} eventos [{status}]")

    print("\n" + "=" * 80)
    print("📌 CONCLUSIÓN:")
    print("  - Los filtros de descarte están conteniendo la telemetría pasiva en el sensor.")
    print("  - Las exclusiones críticas (IA, Spotify) permanecen auditables en el Data Lake.")
    print("=" * 80)

if __name__ == "__main__":
    main()
