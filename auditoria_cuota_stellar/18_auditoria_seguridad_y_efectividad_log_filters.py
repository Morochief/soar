"""
18_auditoria_seguridad_y_efectividad_log_filters.py
---------------------------------------------------
Herramienta oficial del SOC para auditar los Log Filters de Stellar Cyber:
1. Lista los 54+ Log Filters en `/connect/api/v1/log_filters` mostrando:
   - ID, Nombre, Creador, Última Modificación, Tenant, Perfiles de Sensor asociados (`in_use.sensor_profile`)
   - Reglas internas serializadas en `content` (`dev_type`, `rules`, operadores y valores)
   - Clasificación automática de Riesgo de Ceguera (Seguros vs Sin restricción de `action` vs Huérfanos sin perfil)
2. Con `--verify-effectiveness`:
   - Compara empíricamente (en las últimas 48h o `--hours N`) los hits sobrevivientes en `msg_class: firewall`
     contra los flujos reales capturados por la sonda NDR (`msg_class: interflow_traffic`).
   - Esto permite comprobar si un filtro está realmente descartando logs y si existe visibilidad redundante en NDR
     antes de modificarlo (evitando inundar la cuota por error).

Uso:
  python auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py
  python auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py --verify-effectiveness
  python auditoria_cuota_stellar/18_auditoria_seguridad_y_efectividad_log_filters.py --verify-effectiveness --hours 48
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


def audit_inventory(headers):
    r = requests.get(f"https://{HOST}/connect/api/v1/log_filters", headers=headers, timeout=20, verify=False)
    r.raise_for_status()
    filters = r.json().get("data", [])

    print("=" * 90)
    print(f"🛡️ INVENTARIO Y AUDITORÍA DE SEGURIDAD DE LOG FILTERS (Total: {len(filters)})")
    print("=" * 90)

    orphans = []
    no_action_filters = []

    for idx, f in enumerate(filters, 1):
        fid = f.get("_id")
        name = f.get("name")
        creator = f.get("created_by")
        modifier = f.get("modified_by", "")
        cust = f.get("cust_id")
        in_use = f.get("in_use", {}).get("sensor_profile", [])
        content_raw = f.get("content", "{}")
        try:
            content = json.loads(content_raw)
        except Exception:
            content = {}
        dev_type = content.get("dev_type")
        rules = content.get("rules", {})

        has_action = "action" in rules
        if not in_use:
            orphans.append((idx, fid, name))
        if not has_action and in_use:
            no_action_filters.append((idx, fid, name, list(rules.keys())))

        status_tag = "✅ ACTIVO" if in_use else "⚪ INACTIVO (Sin perfil asociado)"
        action_tag = "🔒 Filtra por Action" if has_action else "⚠️ Sin campo Action (Drop total del match)"

        print(f"[{idx:02d}] ID: {fid} | Nombre: {name}")
        print(f"     Estado: {status_tag} ({in_use}) | {action_tag}")
        print(f"     Creador: {creator} | Modificado por: {modifier} | Tenant: {cust} | DevType: '{dev_type}'")
        for rk, rv in rules.items():
            val = rv.get("value", [])
            val_str = f"{val[:5]} ... (+{len(val)-5} más, total {len(val)})" if len(val) > 8 else str(val)
            print(f"       - {rk} ({rv.get('op')}): {val_str}")
        print("-" * 90)

    print(f"\n📌 Resumen Ejecutivo:")
    print(f"  - Total Filtros: {len(filters)}")
    print(f"  - Filtros Activos en Sensor Profiles: {len(filters) - len(orphans)}")
    print(f"  - Filtros Huérfanos (Inactivos en GUI): {len(orphans)}")
    print(f"  - Filtros Activos sin condición 'action': {len(no_action_filters)}")


def check_fw_vs_ndr(headers, start_ms, now_ms, title, lucene_fw, lucene_ndr):
    print(f"\n=========================================================================")
    print(f"🔍 VERIFICANDO EFECTIVIDAD: {title}")
    print(f"=========================================================================")

    p_fw = {
        "track_total_hits": True,
        "size": 2,
        "query": {
            "bool": {
                "must": [
                    {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                    {"term": {"msg_class.keyword": "firewall"}},
                    {"query_string": {"query": lucene_fw}}
                ]
            }
        },
        "aggs": {
            "by_action": {"terms": {"field": "action.keyword", "size": 5}}
        }
    }
    r_fw = requests.get(f"https://{HOST}/connect/api/data/*adr*/_search", headers=headers, json=p_fw, timeout=20, verify=False).json()
    tot_fw = r_fw.get("hits", {}).get("total", {}).get("value", 0)
    actions_fw = [(b["key"], b["doc_count"]) for b in r_fw.get("aggregations", {}).get("by_action", {}).get("buckets", [])]
    print(f"  [1] Logs en FIREWALL (`msg_class: firewall`): {tot_fw:,} hits | Acciones: {actions_fw}")
    for h in r_fw.get("hits", {}).get("hits", []):
        s = h.get("_source", {})
        print(f"      Ej FW: {s.get('srcip')} -> {s.get('dstip')}:{s.get('dstport')} | app={s.get('appid_name')} | action={s.get('action')}")

    p_ndr = {
        "track_total_hits": True,
        "size": 2,
        "query": {
            "bool": {
                "must": [
                    {"range": {"timestamp": {"gte": start_ms, "lte": now_ms}}},
                    {"term": {"msg_class.keyword": "interflow_traffic"}},
                    {"query_string": {"query": lucene_ndr}}
                ]
            }
        }
    }
    r_ndr = requests.get(f"https://{HOST}/connect/api/data/*adr*/_search", headers=headers, json=p_ndr, timeout=20, verify=False).json()
    tot_ndr = r_ndr.get("hits", {}).get("total", {}).get("value", 0)
    print(f"  [2] Tráfico real en NDR / INTERFLOW (`msg_class: interflow_traffic`): {tot_ndr:,} flujos")
    for h in r_ndr.get("hits", {}).get("hits", []):
        s = h.get("_source", {})
        print(f"      Ej NDR: {s.get('srcip')} -> {s.get('dstip')}:{s.get('dstport')} | app={s.get('appid_name')} | state={s.get('state')}")


def main():
    parser = argparse.ArgumentParser(description="Auditoría de Seguridad y Efectividad de Log Filters en Stellar Cyber")
    parser.add_argument("--verify-effectiveness", action="store_true", help="Ejecuta el cruce empírico Firewall vs NDR para comprobar efectividad y volumen retenido")
    parser.add_argument("--hours", type=int, default=48, help="Ventana de horas para la verificación empírica (por defecto: 48)")
    args = parser.parse_args()

    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    audit_inventory(headers)

    if args.verify_effectiveness:
        now_ms = int(time.time() * 1000)
        start_ms = now_ms - (args.hours * 3600 * 1000)

        check_fw_vs_ndr(
            headers, start_ms, now_ms,
            f"Filtro [06] - Puertos TCP 7002, 8000, 38881 (últimas {args.hours}h)",
            "dstport:(7002 OR 8000 OR 38881)",
            "dstport:(7002 OR 8000 OR 38881)"
        )
        check_fw_vs_ndr(
            headers, start_ms, now_ms,
            f"Filtro [13] - Protocolo BGP (últimas {args.hours}h)",
            "appid_name:BGP OR dstport:179",
            "appid_name:bgp OR dstport:179"
        )
        check_fw_vs_ndr(
            headers, start_ms, now_ms,
            f"Filtro [28] - AD DNS Out 10.11.1.1 / 10.11.1.2 (últimas {args.hours}h)",
            "srcip:(10.11.1.1 OR 10.11.1.2) AND (appid_name:DNS OR dstport:53)",
            "srcip:(10.11.1.1 OR 10.11.1.2) AND (appid_name:dns OR dstport:53)"
        )
        check_fw_vs_ndr(
            headers, start_ms, now_ms,
            f"Filtro WUDO 7680 - Drop_FW_Denial_Internal_WUDO_7680 (últimas {args.hours}h)",
            "dstport:7680 AND action:deny",
            "dstport:7680"
        )


if __name__ == "__main__":
    main()
