"""
17_auditoria_dominios_y_syslog_diario.py
----------------------------------------
Audita de forma integral el tráfico de las últimas 24 horas (o de una fecha dada YYYY-MM-DD):
1. Firewall / Syslog (msg_class: firewall):
   - Total de logs, Top Acciones (accept, close, deny, passthrough, etc.)
   - Top 35 URLs / Dominios UTM (url.keyword)
   - Top 15 Políticas de Firewall (fw_policy_id.keyword)
   - Top 15 Puertos Destino (dstport) y Aplicaciones L7 (appid_name.keyword)
   - Inspección de muestras reales (SrcIP, DstIP, Policy, Action, Reason) de los puertos más pesados.
2. NDR / Interflow (msg_class: interflow_traffic):
   - Top 30 Dominios DNS consultados (dns.query.keyword)
3. Syslog General No-Firewall (Linux, Switches, Auth, Cron, etc.):
   - Top clases de mensaje (msg_class) y orígenes (dev_type)

Uso:
  python auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py
  python auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py --date 2026-10-17
  python auditoria_cuota_stellar/17_auditoria_dominios_y_syslog_diario.py --ports 1280,8010,7001,7680
"""

import os
import sys
import json
import base64
import argparse
from datetime import datetime, timezone, timedelta
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


def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    r.raise_for_status()
    return r.json().get("access_token")


def main():
    parser = argparse.ArgumentParser(description="Auditoría diaria de Dominios, Firewall, Puertos Pesados y Syslog")
    parser.add_argument("--date", help="Fecha en formato YYYY-MM-DD (UTC). Por defecto: ayer completo.", default=None)
    parser.add_argument("--ports", help="Puertos TCP separados por coma para inspeccionar muestras", default="1280,8010,6180,7001,7680")
    args = parser.parse_args()

    if args.date:
        dt = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        start_ms = int(dt.timestamp() * 1000)
        end_ms = int((dt + timedelta(days=1)).timestamp() * 1000)
        label_date = args.date
    else:
        today_utc = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        yesterday_utc = today_utc - timedelta(days=1)
        start_ms = int(yesterday_utc.timestamp() * 1000)
        end_ms = int(today_utc.timestamp() * 1000)
        label_date = yesterday_utc.strftime("%Y-%m-%d")

    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    print("=" * 85)
    print(f"🔍 AUDITORÍA FORENSE DE FIREWALL, DOMINIOS Y SYSLOG ({label_date} UTC)")
    print("=" * 85)

    # 1. Firewall / Syslog
    p1 = {
        "track_total_hits": True,
        "size": 0,
        "query": {
            "bool": {
                "must": [
                    {"range": {"timestamp": {"gte": start_ms, "lt": end_ms}}},
                    {"term": {"msg_class.keyword": "firewall"}}
                ]
            }
        },
        "aggs": {
            "top_actions": {"terms": {"field": "action.keyword", "size": 10}},
            "top_urls": {"terms": {"field": "url.keyword", "size": 35}},
            "top_policies": {"terms": {"field": "fw_policy_id.keyword", "size": 15}},
            "top_dstports": {"terms": {"field": "dstport", "size": 15}},
            "top_apps": {"terms": {"field": "appid_name.keyword", "size": 15}}
        }
    }
    r1 = requests.get(f"https://{HOST}/connect/api/data/*adr*/_search", headers=headers, json=p1, timeout=30, verify=False)
    res1 = r1.json()
    print(f"Total Firewall logs recibidos ({label_date}): {res1.get('hits', {}).get('total', {}).get('value', 0):,}")

    aggs1 = res1.get("aggregations", {})
    print("\n--- [1] Top Acciones en Firewall ---")
    for b in aggs1.get("top_actions", {}).get("buckets", []):
        print(f"  {b['key']:<20}: {b['doc_count']:>10,} logs")

    print("\n--- [2] Top URLs / Dominios en Firewall (Syslog UTM) ---")
    for b in aggs1.get("top_urls", {}).get("buckets", []):
        print(f"  {b['key']:<45}: {b['doc_count']:>10,} logs")

    print("\n--- [3] Top Políticas de Firewall ---")
    for b in aggs1.get("top_policies", {}).get("buckets", []):
        print(f"  {b['key']:<25}: {b['doc_count']:>10,} logs")

    print("\n--- [4] Top Puertos Destino en Firewall ---")
    for b in aggs1.get("top_dstports", {}).get("buckets", []):
        print(f"  Puerto {b['key']:<15}: {b['doc_count']:>10,} logs")

    print("\n--- [5] Top Aplicaciones L7 en Firewall ---")
    for b in aggs1.get("top_apps", {}).get("buckets", []):
        print(f"  {b['key']:<25}: {b['doc_count']:>10,} logs")

    # 2. DNS Queries en Interflow / NDR
    print("\n" + "=" * 85)
    print(f"🌐 TOP DOMINIOS DNS RESUELTOS EN RED INTERNA (INTERFLOW / NDR) ({label_date})")
    print("=" * 85)
    p2 = {
        "track_total_hits": True,
        "size": 0,
        "query": {
            "bool": {
                "must": [
                    {"range": {"timestamp": {"gte": start_ms, "lt": end_ms}}},
                    {"exists": {"field": "dns.query"}}
                ]
            }
        },
        "aggs": {
            "top_dns": {"terms": {"field": "dns.query.keyword", "size": 30}}
        }
    }
    r2 = requests.get(f"https://{HOST}/connect/api/data/*adr*/_search", headers=headers, json=p2, timeout=30, verify=False)
    res2 = r2.json()
    print(f"Total Eventos con DNS Query ({label_date}): {res2.get('hits', {}).get('total', {}).get('value', 0):,}")
    for b in res2.get("aggregations", {}).get("top_dns", {}).get("buckets", []):
        print(f"  {b['key']:<50}: {b['doc_count']:>10,} queries")

    # 3. Syslog no-Firewall
    print("\n" + "=" * 85)
    print(f"📜 SYSLOG GENERAL (NO-FIREWALL: LINUX, SWITCHES, AUTH, ETC.) ({label_date})")
    print("=" * 85)
    p3 = {
        "track_total_hits": True,
        "size": 0,
        "query": {
            "bool": {
                "must": [
                    {"range": {"timestamp": {"gte": start_ms, "lt": end_ms}}}
                ],
                "must_not": [
                    {"term": {"msg_class.keyword": "firewall"}},
                    {"term": {"msg_class.keyword": "interflow_traffic"}},
                    {"term": {"msg_class.keyword": "Microsoft-Windows-Security-Auditing"}}
                ]
            }
        },
        "aggs": {
            "by_msg_class": {"terms": {"field": "msg_class.keyword", "size": 20}},
            "by_dev_type": {"terms": {"field": "msg_origin.source.keyword", "size": 20}}
        }
    }
    r3 = requests.get(f"https://{HOST}/connect/api/data/*adr*/_search", headers=headers, json=p3, timeout=30, verify=False)
    res3 = r3.json()
    print(f"Total Eventos No-Firewall / No-Interflow / No-WinAudit: {res3.get('hits', {}).get('total', {}).get('value', 0):,}")
    for b in res3.get("aggregations", {}).get("by_msg_class", {}).get("buckets", []):
        print(f"  msg_class: {b['key']:<40}: {b['doc_count']:>10,} eventos")

    # 4. Inspección de Puertos Pesados
    ports_list = [int(x.strip()) for x in args.ports.split(",") if x.strip().isdigit()]
    if ports_list:
        print("\n" + "=" * 85)
        print(f"🔬 MUESTRAS DE TRÁFICO EN PUERTOS PESADOS: {ports_list}")
        print("=" * 85)
        for port in ports_list:
            p_port = {
                "size": 3,
                "query": {
                    "bool": {
                        "must": [
                            {"range": {"timestamp": {"gte": start_ms, "lt": end_ms}}},
                            {"term": {"msg_class.keyword": "firewall"}},
                            {"term": {"dstport": port}}
                        ]
                    }
                }
            }
            r_port = requests.get(f"https://{HOST}/connect/api/data/*adr*/_search", headers=headers, json=p_port, timeout=15, verify=False)
            hits = r_port.json().get("hits", {}).get("hits", [])
            print(f"\n--- Puerto TCP/UDP {port} ---")
            for h in hits:
                s = h.get("_source", {})
                pol = s.get("fw_policy_id")
                act = s.get("action")
                src = f"{s.get('srcip')}:{s.get('srcport')} ({s.get('srcip_host')})"
                dst = f"{s.get('dstip')}:{s.get('dstport')} ({s.get('dstip_host')})"
                app = s.get("appid_name")
                srv = s.get("service")
                reason = s.get("reason")
                print(f"  Policy: {pol} | Action: {act} | Reason: {reason}")
                print(f"    Src: {src} -> Dst: {dst} | App: {app} / Srv: {srv}")


if __name__ == "__main__":
    main()
