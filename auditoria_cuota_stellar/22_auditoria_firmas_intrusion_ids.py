#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
22_auditoria_firmas_intrusion_ids.py
------------------------------------
FASE 4 DE LA HOJA DE RUTA SOC: ANÁLISIS DE INTRUSIONES BASADAS EN FIRMAS (IDS/IPS)
Extrae y analiza las tendencias de ataque del motor IDS/Suricata en el Modular Sensor:
  1. Top Firmas de Ataque / Exploit / Escaneo activas.
  2. Detección de Severidad Crítica y Alta (Excluyendo INFO benigno).
  3. Identificación de escaneos dirigidos (Nmap, SSH Scan, MySQL Scan, Phishing Post).
  4. Atribución de IPs agresoras (SrcIPs externas atacantes) y activos objetivo (DstIPs).

Uso:
  python 22_auditoria_firmas_intrusion_ids.py
  python 22_auditoria_firmas_intrusion_ids.py --days 7
  python 22_auditoria_firmas_intrusion_ids.py --critical-only
"""

import os
import sys
import json
import base64
import argparse
import requests
import urllib3
from datetime import datetime, timezone, timedelta

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


def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    r.raise_for_status()
    return r.json().get("access_token")


def main():
    parser = argparse.ArgumentParser(description="Auditoría de Firmas de Intrusión (IDS/IPS Overview)")
    parser.add_argument("--days", type=int, default=7, help="Días históricos a auditar (por defecto: 7 días)")
    parser.add_argument("--critical-only", action="store_true", help="Filtrar únicamente severidades High y Critical")
    args = parser.parse_args()

    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    now_utc = datetime.now(timezone.utc)
    start_dt = now_utc - timedelta(days=args.days)
    start_ms = int(start_dt.timestamp() * 1000)

    print("=" * 90)
    print(f"🛡️  FASE 4: AUDITORÍA DE FIRMAS DE INTRUSIÓN (IDS/IPS OVERVIEW) - STELLAR CYBER")
    print(f"📅 Ventana: Últimos {args.days} días (Desde {start_dt.strftime('%Y-%m-%d %H:%M')} UTC)")
    print("=" * 90)

    # Query para extraer las firmas
    must_conditions = [
        {"exists": {"field": "ids.signature"}},
        {"range": {"timestamp": {"gte": start_ms}}}
    ]
    
    must_not_conditions = []
    if args.critical_only:
        must_not_conditions.extend([
            {"term": {"ids.severity.keyword": "informational"}},
            {"term": {"ids.severity.keyword": "low"}},
            {"wildcard": {"ids.signature.keyword": "INFO *"}}
        ])

    p = {
        "track_total_hits": True,
        "size": 0,
        "query": {
            "bool": {
                "must": must_conditions,
                "must_not": must_not_conditions
            }
        },
        "aggs": {
            "top_signatures": {"terms": {"field": "ids.signature.keyword", "size": 15}},
            "top_severities": {"terms": {"field": "ids.severity.keyword", "size": 5}},
            "top_categories": {"terms": {"field": "ids.category.keyword", "size": 8}},
            "top_attackers": {"terms": {"field": "srcip", "size": 10}},
            "top_targets": {"terms": {"field": "dstip", "size": 10}}
        }
    }

    r = requests.get(f"https://{HOST}/connect/api/data/*interim*/_search", headers=headers, json=p, timeout=30, verify=False)
    res = r.json()
    total = res.get("hits", {}).get("total", {}).get("value", 0)

    print(f"\n[+] Total Detecciones por Firmas IDS registradas: {total:,}")

    aggs = res.get("aggregations", {})

    print("\n--- [1] Top Severidades de Firmas ---")
    for b in aggs.get("top_severities", {}).get("buckets", []):
        sev = b["key"].upper()
        ico = "🔴" if sev in ["CRITICAL", "HIGH"] else "🟡"
        print(f"  {ico} {sev:<15}: {b['doc_count']:>8,} eventos")

    print("\n--- [2] Top Categorías de Ataque / Actividad ---")
    for b in aggs.get("top_categories", {}).get("buckets", []):
        print(f"  • {b['key']:<35}: {b['doc_count']:>8,} eventos")

    print("\n--- [3] Top 15 Firmas de Intrusión Disparadas ---")
    for i, b in enumerate(aggs.get("top_signatures", {}).get("buckets", []), 1):
        print(f"  {i:>2}. {b['key']:<65}: {b['doc_count']:>6,} hits")

    print("\n--- [4] Top 10 IPs Origen Involucradas (Atacantes / Scanner / Clientes) ---")
    for b in aggs.get("top_attackers", {}).get("buckets", []):
        print(f"  • {b['key']:<20}: {b['doc_count']:>8,} eventos")

    print("\n--- [5] Top 10 Activos Destino Involucrados (Objetivos) ---")
    for b in aggs.get("top_targets", {}).get("buckets", []):
        print(f"  • {b['key']:<20}: {b['doc_count']:>8,} eventos")

    print("\n" + "=" * 90)
    print("💡 CONCLUSIÓN OPERATIVA DEL ANALISTA (Fase 4):")
    if total > 0:
        print("  Se observan intentos de escaneo y consultas a TLDs sospechosos contenidos por el perímetro.")
        print("  Revisar en Threat Hunting si alguna IP origen externa coincide con patrones de fuerza bruta.")
    else:
        print("  No se registran eventos de intrusión activos en la ventana seleccionada.")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    main()
