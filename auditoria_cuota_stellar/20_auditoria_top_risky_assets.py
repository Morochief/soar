"""
20_auditoria_top_risky_assets.py
---------------------------------
Herramienta de diagnóstico forense para auditar el panel 'Top Risky Assets' de Stellar Cyber.
Permite descifrar por qué un activo o IP tiene un Risk Score elevado:
1. Extrae los snapshots de los activos en el índice de Assets (`stellar-index-v1-assets-*`)
   identificando su mapeo real de IPs, MACs, Hostnames y rotación DHCP.
2. Cruza los Asset IDs e IPs contra el índice de eventos de seguridad (`aella-ser-*` / Security Events)
   en una ventana de tiempo configurable (--hours N, por defecto 48h).
3. Inspecciona en profundidad los eventos analíticos (Machine Learning, BIOC, IDS, Exploited C&C,
   Anomalías SMB/LDAP/Firewall) para determinar si se trata de un incidente real o de falsos positivos
   por tráfico administrativo interno (ej. replicación DNS, consultas LDAP 389, FSSO 8002, o bloqueos por policy 0).

Uso:
  python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py
  python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --hours 24
  python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --asset "forestdnszones.technoma.local"
  python auditoria_cuota_stellar/20_auditoria_top_risky_assets.py --ip "192.168.15.23"
"""

import os
import sys
import json
import time
import base64
import argparse
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
    parser = argparse.ArgumentParser(description="Auditoría Forense de Top Risky Assets en Stellar Cyber")
    parser.add_argument("--hours", type=int, default=48, help="Ventana de tiempo en horas para auditar alertas (por defecto: 48)")
    parser.add_argument("--asset", type=str, default=None, help="Filtrar por nombre o hostname específico de activo")
    parser.add_argument("--ip", type=str, default=None, help="Filtrar por IP específica de activo")
    args = parser.parse_args()

    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    now_ms = int(time.time() * 1000)
    start_ms = now_ms - (args.hours * 3600 * 1000)

    print("=" * 90)
    print(f"🛡️ AUDITORÍA FORENSE DE TOP RISKY ASSETS & ALERTAS (ÚLTIMAS {args.hours}H)")
    print("=" * 90)

    # 1. Descubrir el índice de assets más reciente
    p_idx = {
        "size": 0,
        "aggs": {"indices": {"terms": {"field": "_index", "size": 10}}}
    }
    r_idx = requests.get(f"https://{HOST}/connect/api/data/*assets*2026.10*/_search", headers=headers, json=p_idx, timeout=20, verify=False).json()
    indices = [b["key"] for b in r_idx.get("aggregations", {}).get("indices", {}).get("buckets", [])]
    latest_idx = sorted(indices)[-1] if indices else "*assets*"
    print(f"📌 Consultando índice de Assets: {latest_idx}")

    # 2. Obtener Top Risky Assets
    if args.asset:
        must_clauses = [{"query_string": {"query": f"*{args.asset}*"}}]
    elif args.ip:
        must_clauses = [{"term": {"ip.keyword": args.ip}}]
    else:
        must_clauses = [
            {"range": {"risk_score": {"gt": 5.0}}},
            {"term": {"tenant_name.keyword": "technoma"}}
        ]

    p_assets = {
        "size": 15,
        "query": {
            "bool": {
                "must": must_clauses
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}, {"risk_score": {"order": "desc"}}]
    }

    r_ast = requests.get(f"https://{HOST}/connect/api/data/{latest_idx}/_search", headers=headers, json=p_assets, timeout=20, verify=False).json()
    asset_hits = r_ast.get("hits", {}).get("hits", [])
    print(f"Total activos analizados: {len(asset_hits)}\n")

    seen_ids = set()
    for h in asset_hits:
        s = h.get("_source", {})
        aid = s.get("id")
        if aid in seen_ids:
            continue
        seen_ids.add(aid)

        name = s.get("name")
        r_score = s.get("risk_score")
        alt_r_score = s.get("alt_risk_score")
        ips = s.get("ip", [])
        macs = s.get("mac", [])
        hostnames = s.get("hostname", [])
        ts_s = time.strftime('%Y-%m-%d %H:%M', time.gmtime(s.get("timestamp", 0) / 1000))

        print("-" * 90)
        print(f"🎯 Activo: {name} | Risk Score: {r_score} (AltRisk: {alt_r_score}) | Snapshot: {ts_s}")
        print(f"   Asset ID: {aid}")
        print(f"   IPs: {ips[:6]}")
        print(f"   MACs: {macs}")
        print(f"   Hostnames: {hostnames[:6]}")

        # 3. Buscar alertas en *ser* vinculadas al Asset ID o sus IPs principales
        ip_queries = [f"srcip:\"{ip}\"" for ip in ips[:3]] + [f"dstip:\"{ip}\"" for ip in ips[:3]]
        q_or = f"\"{aid}\" OR " + " OR ".join(ip_queries) if ip_queries else f"\"{aid}\""

        p_alerts = {
            "size": 10,
            "sort": [{"timestamp": {"order": "desc"}}],
            "query": {
                "bool": {
                    "must": [
                        {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                        {"query_string": {"query": q_or}}
                    ]
                }
            }
        }
        r_al = requests.get(f"https://{HOST}/connect/api/data/*ser*/_search", headers=headers, json=p_alerts, timeout=20, verify=False).json()
        al_hits = r_al.get("hits", {}).get("hits", [])
        print(f"   Alertas en las últimas {args.hours}h ({len(al_hits)} eventos):")

        for ah in al_hits:
            asrc = ah.get("_source", {})
            ev = asrc.get("xdr_event", {}).get("display_name") or asrc.get("event_name")
            sc = asrc.get("event_score") or asrc.get("score") or asrc.get("fidelity")
            ts_a = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(asrc.get("timestamp", 0) / 1000))
            src_str = f"{asrc.get('srcip')}:{asrc.get('srcport')} ({asrc.get('srcip_host')})"
            dst_str = f"{asrc.get('dstip')}:{asrc.get('dstport')} ({asrc.get('dstip_host')})"
            app = asrc.get("appid_name") or asrc.get("service")
            pol = asrc.get("fw_policy_id")
            act = asrc.get("action")
            user = asrc.get("srcip_username") or asrc.get("unauthuser") or asrc.get("username") or ""

            print(f"     * [{ts_a} UTC] {ev} (Score={sc})")
            print(f"       Src: {src_str} -> Dst: {dst_str} | App: {app} | Action: {act} | Policy: {pol}")
            if user:
                print(f"       Usuario: {user}")
        print()


if __name__ == "__main__":
    main()
