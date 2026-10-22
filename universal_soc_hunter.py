#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🔍 TECHNOMA SOC — BUSCADOR UNIVERSAL FEDERADO (STELLAR CYBER + SECURITY ONION)
=============================================================================
Herramienta de Threat Hunting unificada para investigar simultáneamente en:
  1. Stellar Cyber (Data Lake Interflow, Syslog, WinEventLog, Firewall)
  2. Security Onion 3 (Elasticsearch: Zeek, Suricata, FortiGate, Sophos, Alerts)

Uso:
  python universal_soc_hunter.py --ip 192.168.169.28
  python universal_soc_hunter.py --domain mjt.lu
  python universal_soc_hunter.py --user kevinmoraes
  python universal_soc_hunter.py --ioc 181.94.247.147
  python universal_soc_hunter.py --ip 172.16.202.21 --hours 48
=============================================================================
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración UTF-8 en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Paths base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOAR_DIR = os.path.dirname(BASE_DIR) if os.path.basename(BASE_DIR) == "tools_so3" else BASE_DIR
sys.path.append(SOAR_DIR)
sys.path.append(os.path.join(SOAR_DIR, 'tools_so3'))
sys.path.append(os.path.join(SOAR_DIR, 'tools_stellar'))

from tools_so3.so3_client import SO3Client

# Carga de credenciales seguras
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(SOAR_DIR, ".env"))
    load_dotenv()
except Exception:
    pass

# Stellar Cyber Config
STELLAR_HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
STELLAR_EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
STELLAR_TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")

# Security Onion Config
SO_ES_USER = "so_elastic"
SO_ES_PASS = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"


# =====================================================================
# 1. MOTOR DE CONSULTA STELLAR CYBER
# =====================================================================
def get_stellar_jwt() -> Optional[str]:
    import base64
    url = f"https://{STELLAR_HOST}/connect/api/v1/access_token"
    auth_str = f"{STELLAR_EMAIL}:{STELLAR_TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    try:
        resp = requests.post(url, headers=headers, json={}, timeout=15, verify=False)
        if resp.status_code in (200, 201):
            return resp.json().get("access_token")
    except Exception as e:
        print(f"[!] Error conectando a Stellar Cyber: {e}", file=sys.stderr)
    return None


def search_stellar(target: str, target_type: str, hours: int = 24, limit: int = 5) -> Dict[str, Any]:
    jwt = get_stellar_jwt()
    if not jwt:
        return {"error": "No se pudo autenticar con Stellar Cyber."}

    # Construir query Lucene para Stellar
    if target_type == "ip":
        query = f"srcip:{target} OR dstip:{target}"
    elif target_type == "domain":
        query = f"dst_host:*{target}* OR src_host:*{target}* OR domain:*{target}* OR query:*{target}* OR dns.query:*{target}*"
    elif target_type == "user":
        query = f"user:*{target}* OR username:*{target}* OR winlog.event_data.TargetUserName:*{target}*"
    else:
        query = f"*{target}*"

    date_str = datetime.now(timezone.utc).strftime("%Y.%m.%d")
    url = f"https://{STELLAR_HOST}/connect/api/data/*{date_str}*/_search"
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }

    body = {
        "size": limit,
        "query": {
            "query_string": {
                "query": query
            }
        },
        "sort": [{"timestamp": {"order": "desc", "unmapped_type": "long"}}]
    }

    try:
        resp = requests.get(url, json=body, headers=headers, timeout=20, verify=False)
        if resp.status_code != 200:
            fallback_url = f"https://{STELLAR_HOST}/connect/api/data/*/_search"
            resp = requests.get(fallback_url, json=body, headers=headers, timeout=20, verify=False)

        if resp.status_code == 200:
            data = resp.json()
            hits = data.get("hits", {})
            total = hits.get("total", {})
            total_val = total.get("value", 0) if isinstance(total, dict) else total
            return {
                "total": total_val,
                "events": hits.get("hits", [])
            }
        else:
            return {"error": f"HTTP {resp.status_code}: {resp.text[:200]}"}
    except Exception as e:
        return {"error": str(e)}


# =====================================================================
# 2. MOTOR DE CONSULTA SECURITY ONION 3
# =====================================================================
def search_security_onion(target: str, target_type: str, hours: int = 24, limit: int = 5) -> Dict[str, Any]:
    # Construir query Elasticsearch para SO3
    if target_type == "ip":
        query = f"source.ip:{target} OR destination.ip:{target} OR client.ip:{target} OR server.ip:{target}"
    elif target_type == "domain":
        query = f"dns.query.name:*{target}* OR destination.domain:*{target}* OR url.domain:*{target}* OR dns.answers.name:*{target}*"
    elif target_type == "user":
        query = f"user.name:*{target}* OR source.user.name:*{target}* OR sophos_central.event.source.original:*{target}*"
    else:
        query = f"*{target}*"

    es_body = {
        "size": limit,
        "query": {
            "bool": {
                "must": [
                    {"query_string": {"query": query}},
                    {"range": {"@timestamp": {"gte": f"now-{hours}h"}}}
                ]
            }
        },
        "sort": [{"@timestamp": {"order": "desc"}}]
    }

    try:
        with SO3Client() as so:
            tmp_query_file = f"/tmp/so_query_{os.getpid()}.json"
            so.write_file(tmp_query_file, json.dumps(es_body))
            cmd = f"curl -k -s -u '{SO_ES_USER}:{SO_ES_PASS}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/*so*,*zeek*,*suricata*,*sophos*,*alert*/_search' -d @{tmp_query_file}"
            out, _ = so.sudo(cmd)
            so.sudo(f"rm -f {tmp_query_file}")

            data = json.loads(out)
            hits = data.get("hits", {})
            total = hits.get("total", {})
            total_val = total.get("value", 0) if isinstance(total, dict) else total
            return {
                "total": total_val,
                "events": hits.get("hits", [])
            }
    except Exception as e:
        return {"error": str(e)}


# =====================================================================
# 3. CONSOLIDADOR Y REPORTE FORENSE UNIFICADO
# =====================================================================
def run_universal_search(target: str, target_type: str, hours: int = 24, limit: int = 5):
    print("=" * 78)
    print(f"🔎 BUSCADOR UNIVERSAL FEDERADO — TECHNOMA SOC")
    print(f"🎯 Objetivo: [{target.upper()}] | Tipo: [{target_type.upper()}] | Ventana: [Últimas {hours} horas]")
    print("=" * 78)

    # 1. Stellar Cyber
    print("\n🌐 [1/2] Consultando Stellar Cyber (Data Lake Multi-Tenant)...")
    st_res = search_stellar(target, target_type, hours=hours, limit=limit)
    if "error" in st_res:
        print(f"   ❌ Error en Stellar: {st_res['error']}")
    else:
        tot = st_res.get("total", 0)
        print(f"   ✅ Stellar Cyber: {tot:,} eventos encontrados.")
        for i, ev in enumerate(st_res.get("events", [])[:limit], 1):
            src = ev.get("_source", {})
            ts = src.get("timestamp") or src.get("@timestamp")
            m_class = src.get("msg_class") or src.get("event_type", "log")
            sip = src.get("srcip", "-")
            dip = src.get("dstip", "-")
            dport = src.get("dstport", "-")
            proto = src.get("proto", "-")
            tenant = src.get("tenant_name", "Global")
            print(f"      [{i}] {ts} | Tenant: {tenant} | Class: {m_class}")
            print(f"          Conexión: {sip} ➔ {dip}:{dport} ({proto})")

    # 2. Security Onion 3
    print("\n🧅 [2/2] Consultando Security Onion 3 (NDR, Zeek, Suricata, Sophos)...")
    so_res = search_security_onion(target, target_type, hours=hours, limit=limit)
    if "error" in so_res:
        print(f"   ❌ Error en Security Onion: {so_res['error']}")
    else:
        tot_so = so_res.get("total", 0)
        print(f"   ✅ Security Onion: {tot_so:,} eventos encontrados.")
        for i, ev in enumerate(so_res.get("events", [])[:limit], 1):
            src = ev.get("_source", {})
            idx = ev.get("_index", "")
            ts = src.get("@timestamp", "-")
            sip = src.get("source", {}).get("ip") or src.get("client", {}).get("ip", "-")
            dip = src.get("destination", {}).get("ip") or src.get("server", {}).get("ip", "-")
            dport = src.get("destination", {}).get("port", "-")
            module = src.get("event", {}).get("module") or src.get("container", {}).get("id") or idx.split("-")[1] if "-" in idx else idx
            rule = src.get("rule", {}).get("name") or src.get("dns", {}).get("query") or src.get("event", {}).get("action", "-")
            print(f"      [{i}] {ts} | Sensor/Módulo: {module} ({idx})")
            print(f"          Conexión: {sip} ➔ {dip}:{dport} | Info/Regla: {rule}")

    print("\n" + "=" * 78)
    print("🏁 Búsqueda federada finalizada.")
    print("=" * 78)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buscador Universal Federado (Stellar Cyber + Security Onion)")
    parser.add_argument("--ip", type=str, help="IP a rastrear (origen o destino)")
    parser.add_argument("--domain", type=str, help="Dominio o FQDN a rastrear")
    parser.add_argument("--user", type=str, help="Usuario a rastrear")
    parser.add_argument("--ioc", type=str, help="Cualquier indicador genérico (hash, string, IP, dominio)")
    parser.add_argument("--hours", type=int, default=24, help="Ventana de tiempo en horas (por defecto: 24)")
    parser.add_argument("--limit", type=int, default=5, help="Cantidad de eventos a mostrar por plataforma (por defecto: 5)")

    args = parser.parse_args()

    if args.ip:
        run_universal_search(args.ip, "ip", hours=args.hours, limit=args.limit)
    elif args.domain:
        run_universal_search(args.domain, "domain", hours=args.hours, limit=args.limit)
    elif args.user:
        run_universal_search(args.user, "user", hours=args.hours, limit=args.limit)
    elif args.ioc:
        run_universal_search(args.ioc, "generic", hours=args.hours, limit=args.limit)
    else:
        print("Uso: python universal_soc_hunter.py --ip <IP> | --domain <DOMINIO> | --user <USUARIO> | --ioc <IOC> [--hours 24]")
        sys.exit(1)
