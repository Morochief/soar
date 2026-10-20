#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — INSPECTOR DE QUERIES, LOG FILTERS Y REGLAS (stellar_query_inspector.py)
=============================================================================
Herramienta unificada y directa para auditar, inspeccionar y limpiar:
  1. Saved Queries (/connect/api/v1/queries) -> Detección de uso en ATH, Correlación y Charts
  2. Log Filters (/connect/api/v1/log_filters) -> Reglas JSON de descarte en colector/sensor
  3. Alert Watchers / ATH (/connect/api/v1/alert_watchers) -> Playbooks automatizados activos
  4. Action Center Rules (/connect/api/v1/rules) -> Notificaciones Slack / Odoo

Uso rápido:
  python stellar_query_inspector.py --queries                 # Lista todas las Saved Queries y su uso
  python stellar_query_inspector.py --queries --in-use        # Solo queries activas en ATH/Charts/Correlación
  python stellar_query_inspector.py --query-detail "Nombre"   # Muestra el JSON y DSL exacto de una query
  python stellar_query_inspector.py --filters                 # Lista todos los Log Filters con su JSON de reglas
  python stellar_query_inspector.py --filter-detail "Nombre"  # Detalle completo de un Log Filter específico
  python stellar_query_inspector.py --ath                     # Lista los Automated Threat Hunting / Watchers
  python stellar_query_inspector.py --cleanup-orphans         # Lista (o elimina con --confirm) queries temporales de prueba
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

# Configuración UTF-8 en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Carga de credenciales desde .env
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

_CACHED_JWT: Optional[str] = None


def get_jwt() -> str:
    """Obtiene y cachea el JWT de Stellar Cyber."""
    global _CACHED_JWT
    if _CACHED_JWT:
        return _CACHED_JWT

    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Error autenticando contra Stellar Cyber ({r.status_code}): {r.text}")
    _CACHED_JWT = r.json().get("access_token")
    return _CACHED_JWT


def get_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {get_jwt()}",
        "Content-Type": "application/json"
    }


def fetch_saved_queries() -> List[Dict[str, Any]]:
    """Obtiene todas las Saved Queries de /connect/api/v1/queries."""
    r = requests.get(f"https://{HOST}/connect/api/v1/queries", headers=get_headers(), timeout=20, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Error consultando /queries ({r.status_code}): {r.text}")
    return r.json().get("data", [])


def fetch_log_filters() -> List[Dict[str, Any]]:
    """Obtiene todos los Log Filters de /connect/api/v1/log_filters."""
    r = requests.get(f"https://{HOST}/connect/api/v1/log_filters", headers=get_headers(), timeout=20, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Error consultando /log_filters ({r.status_code}): {r.text}")
    return r.json().get("data", [])


def fetch_ath_watchers() -> List[Dict[str, Any]]:
    """Obtiene las reglas de Automated Threat Hunting / Alert Watchers."""
    r = requests.get(f"https://{HOST}/connect/api/v1/alert_watchers", headers=get_headers(), timeout=20, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Error consultando /alert_watchers ({r.status_code}): {r.text}")
    return r.json().get("data", [])


def is_orphan_test_query(q: Dict[str, Any]) -> bool:
    """Identifica si una query es temporal/huérfana creada por pruebas automatizadas y sin uso activo."""
    in_use_total = (
        len(q.get("in_use_ath", [])) +
        len(q.get("in_use_correlation", [])) +
        len(q.get("in_use_report", [])) +
        len(q.get("in_use_chart", []))
    )
    if in_use_total > 0:
        return False

    name = q.get("name", "")
    test_prefixes = (
        "AdHoc_Hunt_", "Gui_Hunt_", "SOC_CLI_Hunt_", "Test_Broad_",
        "Top_Apps_", "Hunt_Test", "Probe_WUDO_7680", "Hunt_FortiGate_",
        "Hunt_Patient_Zero", "Hunt_Hostname", "test_search_"
    )
    return any(name.startswith(pref) for pref in test_prefixes)


def cmd_list_queries(in_use_only: bool = False):
    queries = fetch_saved_queries()
    print(f"\n{'='*100}")
    print(f" SAVED QUERIES EN STELLAR CYBER (Total: {len(queries)}) {'[SOLO EN USO]' if in_use_only else ''}")
    print(f"{'='*100}")
    print(f"{'#':<4} {'NOMBRE':<38} {'TENANT':<13} {'CREADOR':<28} {'USO (ATH/CORR/CHART/REP)'}")
    print(f"{'-'*100}")

    shown = 0
    for idx, q in enumerate(queries, 1):
        ath = len(q.get("in_use_ath", []))
        corr = len(q.get("in_use_correlation", []))
        ch = len(q.get("in_use_chart", []))
        rep = len(q.get("in_use_report", []))
        total_use = ath + corr + ch + rep

        if in_use_only and total_use == 0:
            continue

        shown += 1
        name = q.get("name", "Sin nombre")[:36]
        tenant = str(q.get("tenant_name") or q.get("cust_id") or "N/A")[:12]
        creator = str(q.get("created_by") or "N/A")[:26]
        use_str = f"ATH:{ath} | Corr:{corr} | Chart:{ch} | Rep:{rep}"
        if total_use > 0:
            use_str += " ⭐"
        elif is_orphan_test_query(q):
            use_str += " [TEMP]"

        print(f"{idx:<4} {name:<38} {tenant:<13} {creator:<28} {use_str}")

    print(f"{'='*100}")
    print(f"[*] Mostradas: {shown} de {len(queries)} queries.\n")


def cmd_query_detail(search_term: str):
    queries = fetch_saved_queries()
    term = search_term.lower().strip()
    matches = [
        q for q in queries
        if term in q.get("name", "").lower() or term == q.get("_id", "").lower()
    ]
    if not matches:
        print(f"[-] No se encontró ninguna query que coincida con: '{search_term}'")
        return

    for q in matches:
        print(f"\n{'='*90}")
        print(f" DETALLE DE SAVED QUERY: {q.get('name')} (ID: {q.get('_id')})")
        print(f"{'='*90}")
        print(f"Tenant:       {q.get('tenant_name')} ({q.get('cust_id')})")
        print(f"Creado por:   {q.get('created_by')}")
        print(f"Descripción:  {q.get('data', {}).get('description', 'Sin descripción')}")
        print(f"Índices:      {', '.join(q.get('metadata', {}).get('data_source', [])) or 'Todos'}")
        print(f"En uso ATH:   {q.get('in_use_ath', [])}")
        print(f"En uso Corr:  {q.get('in_use_correlation', [])}")
        print(f"En uso Chart: {q.get('in_use_chart', [])}")
        print(f"\n--- Condiciones Estructuradas ---")
        print(json.dumps(q.get("conditions", {}), indent=2, ensure_ascii=False))
        print(f"\n--- Query DSL (Metadata) ---")
        print(q.get("metadata", {}).get("query", "N/A"))
        print(f"{'='*90}\n")


def cmd_list_filters(search_term: Optional[str] = None):
    filters = fetch_log_filters()
    if search_term:
        t = search_term.lower().strip()
        filters = [f for f in filters if t in f.get("name", "").lower() or t in f.get("content", "").lower()]

    print(f"\n{'='*100}")
    print(f" LOG FILTERS ACTIVOS EN COLECTOR / SENSOR (Total: {len(filters)})")
    print(f"{'='*100}")

    for idx, f in enumerate(filters, 1):
        name = f.get("name", "Sin Nombre")
        fid = f.get("_id", "N/A")
        creator = f.get("created_by", "N/A")
        profiles = ", ".join(f.get("in_use", {}).get("sensor_profile", [])) or "Global"
        try:
            content_obj = json.loads(f.get("content", "{}"))
        except Exception:
            content_obj = {}

        dev_type = content_obj.get("dev_type") or "Cualquiera"
        rules = content_obj.get("rules", {})
        rule_summary = []
        for k, v in rules.items():
            op = v.get("op", "==")
            vals = v.get("value", [])
            val_preview = ", ".join(str(x) for x in vals[:4])
            if len(vals) > 4:
                val_preview += f" ... (+{len(vals)-4} más)"
            rule_summary.append(f"{k} {op} [{val_preview}]")

        print(f"{idx:02d}. {name} (ID: {fid})")
        print(f"    Creador: {creator} | Perfil Sensor: {profiles} | DevType: {dev_type}")
        print(f"    Reglas:  {' AND '.join(rule_summary)}")
        print(f"{'-'*100}")
    print()


def cmd_ath_watchers():
    watchers = fetch_ath_watchers()
    print(f"\n{'='*95}")
    print(f" REGLAS DE AUTOMATED THREAT HUNTING / ALERT WATCHERS (Total: {len(watchers)})")
    print(f"{'='*95}")
    for idx, w in enumerate(watchers, 1):
        wid = w.get("_id")
        active = "ACTIVO" if w.get("active") else "INACTIVO"
        try:
            conf = json.loads(w.get("conf", "{}"))
        except Exception:
            conf = {}
        meta = conf.get("metadata", {})
        print(f"{idx:02d}. [{active}] {meta.get('name', 'Sin nombre')} (ID: {wid})")
        print(f"    Trigger: {json.dumps(conf.get('trigger', {}), ensure_ascii=False)}")
        print(f"    Actions: {json.dumps(conf.get('actions', {}), ensure_ascii=False)[:220]}")
        print(f"{'-'*95}")
    print()


def cmd_cleanup_orphans(confirm: bool = False):
    queries = fetch_saved_queries()
    orphans = [q for q in queries if is_orphan_test_query(q)]
    print(f"\n[*] Detectadas {len(orphans)} queries temporales/huérfanas (sin uso en ATH, Charts ni Correlación):")
    for q in orphans:
        print(f"  - {q.get('name'):<35} (ID: {q.get('_id')}) | Creador: {q.get('created_by')}")

    if not confirm:
        print("\n[i] Modo simulación. Para eliminarlas realmente de Stellar Cyber, agregá el flag --confirm.\n")
        return

    deleted = 0
    for q in orphans:
        qid = q.get("_id")
        r = requests.delete(f"https://{HOST}/connect/api/v1/queries/{qid}", headers=get_headers(), timeout=15, verify=False)
        if r.status_code in (200, 204):
            deleted += 1
            print(f"  [+] Eliminada: {q.get('name')} ({qid})")
        else:
            print(f"  [-] Error eliminando {q.get('name')}: HTTP {r.status_code}")
    print(f"\n[✓] Total eliminadas: {deleted}/{len(orphans)}\n")


def cmd_top_domains(action_filter: str = "passthrough", target_date: Optional[str] = None, top_n: int = 40):
    """Extrae del Data Lake el ranking de dominios (fortinet.hostname), categorías FortiGuard y ASNs."""
    from datetime import datetime, timezone
    cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
    if not target_date:
        target_date = datetime.now(timezone.utc).strftime("%Y.%m.%d")

    filters_es = [
        {"term": {"tenantid": cust_id}},
        {"term": {"dev_type.keyword": "fw_fortigate"}}
    ]
    if action_filter and action_filter.lower() != "all":
        filters_es.append({"term": {"action.keyword": action_filter}})

    query = {
        "size": 0,
        "track_total_hits": True,
        "query": {"bool": {"filter": filters_es}},
        "aggs": {
            "top_hosts": {"terms": {"field": "fortinet.hostname.keyword", "size": top_n}},
            "top_cats": {"terms": {"field": "fortinet.catdesc.keyword", "size": 20}},
            "top_asns": {"terms": {"field": "dstip_asn_org.keyword", "size": 15}}
        }
    }

    target_index = f"*{target_date}*{cust_id}*"
    url = f"https://{HOST}/connect/api/data/{target_index}/_search"
    print(f"[*] Consultando Data Lake ({target_index}) para action='{action_filter}'...")
    r = requests.get(url, headers=get_headers(), json=query, verify=False, timeout=60)
    if r.status_code != 200:
        print(f"[-] Error consultando Data Lake ({r.status_code}): {r.text[:300]}")
        return

    res = r.json()
    total_hits = res.get("hits", {}).get("total", {}).get("value", 0)
    aggs = res.get("aggregations", {})

    print(f"\n{'='*90}")
    print(f" AUDITORÍA DE DOMINIOS Y VOLUMEN FORTIGATE ({target_date} | Action: {action_filter})")
    print(f" Total de Eventos Encontrados: {total_hits:,}")
    print(f"{'='*90}")

    print("\n[1] TOP CATEGORÍAS FORTIGUARD (fortinet.catdesc):")
    for b in aggs.get("top_cats", {}).get("buckets", []):
        pct = (b["doc_count"] / total_hits * 100) if total_hits else 0
        print(f"  - {b['key']:<38} : {b['doc_count']:>10,} logs ({pct:>5.1f}%)")

    print("\n[2] TOP ORGANIZACIONES ASN (dstip_asn_org):")
    for b in aggs.get("top_asns", {}).get("buckets", []):
        pct = (b["doc_count"] / total_hits * 100) if total_hits else 0
        print(f"  - {b['key']:<38} : {b['doc_count']:>10,} logs ({pct:>5.1f}%)")

    print(f"\n[3] TOP {top_n} DOMINIOS / HOSTNAMES (fortinet.hostname):")
    for idx, b in enumerate(aggs.get("top_hosts", {}).get("buckets", []), 1):
        pct = (b["doc_count"] / total_hits * 100) if total_hits else 0
        print(f"  {idx:02d}. {b['key']:<42} : {b['doc_count']:>10,} logs ({pct:>5.1f}%)")
    print(f"{'='*90}\n")


def cmd_audit_filter_coverage(filter_search: str, target_date: Optional[str] = None):
    """Evalúa un Log Filter contra los logs reales del Data Lake para medir % de cobertura y qué se escapa."""
    from datetime import datetime, timezone
    cust_id = "e511c3fc54cd4d668bb67612c2ef4b04"
    if not target_date:
        target_date = datetime.now(timezone.utc).strftime("%Y.%m.%d")

    filters = fetch_log_filters()
    term = filter_search.lower().strip()
    matches = [f for f in filters if term in f.get("name", "").lower() or term == f.get("_id", "").lower()]
    if not matches:
        print(f"[-] No se encontró ningún Log Filter que coincida con: '{filter_search}'")
        return

    target_f = matches[0]
    fname = target_f.get("name")
    content = json.loads(target_f.get("content", "{}"))
    rules = content.get("rules", {})

    print(f"\n[*] Auditando cobertura del filtro: {fname} ({target_f.get('_id')}) en fecha {target_date}...")
    print(f"    Reglas configuradas: {json.dumps(rules, ensure_ascii=False)}")

    # Construir filtro base por dev_type y action si existen
    es_filters = [{"term": {"tenantid": cust_id}}]
    if content.get("dev_type"):
        es_filters.append({"term": {"dev_type.keyword": content["dev_type"]}})
    if "action" in rules:
        act_vals = rules["action"].get("value", [])
        if len(act_vals) == 1:
            es_filters.append({"term": {"action.keyword": act_vals[0]}})

    url_patterns = [p.lower() for p in rules.get("url", {}).get("value", [])]

    query = {
        "size": 0,
        "track_total_hits": True,
        "query": {"bool": {"filter": es_filters}},
        "aggs": {
            "top_hosts": {"terms": {"field": "fortinet.hostname.keyword", "size": 250}},
            "by_hour": {"date_histogram": {"field": "write_time", "fixed_interval": "2h"}}
        }
    }

    target_index = f"*{target_date}*{cust_id}*"
    url = f"https://{HOST}/connect/api/data/{target_index}/_search"
    r = requests.get(url, headers=get_headers(), json=query, verify=False, timeout=60)
    if r.status_code != 200:
        print(f"[-] Error consultando Data Lake ({r.status_code}): {r.text[:300]}")
        return

    res = r.json()
    buckets = res.get("aggregations", {}).get("top_hosts", {}).get("buckets", [])

    covered_docs = 0
    uncovered_docs = 0
    uncovered_list = []
    covered_list = []

    for b in buckets:
        host = b["key"].lower()
        count = b["doc_count"]
        if url_patterns and any(pat in host for pat in url_patterns):
            covered_docs += count
            covered_list.append((b["key"], count))
        else:
            uncovered_docs += count
            uncovered_list.append((b["key"], count))

    total_sample = covered_docs + uncovered_docs
    cov_pct = (covered_docs / total_sample * 100) if total_sample else 0

    print(f"\n{'='*95}")
    print(f" REPORTE DE IMPACTO Y COBERTURA: {fname}")
    print(f"{'='*95}")
    print(f"  Total analizado (Top 250 hosts): {total_sample:,} eventos")
    print(f"  Cubiertos / Descartados por URL: {covered_docs:,} eventos ({cov_pct:.1f}%)")
    print(f"  Visibles en SIEM (No filtrados): {uncovered_docs:,} eventos ({100 - cov_pct:.1f}%)")

    if covered_list:
        print(f"\n  [✓] TOP 10 DOMINIOS ATRAPADOS POR EL FILTRO (Si aún entran es porque se generaron antes de aplicar el filtro):")
        for h, c in covered_list[:10]:
            print(f"      - {h:<42} : {c:>9,} logs")

    if uncovered_list:
        print(f"\n  [👀] TOP 15 DOMINIOS NO FILTRADOS (Siguen entrando al SIEM para visibilidad del SOC):")
        for h, c in uncovered_list[:15]:
            print(f"      - {h:<42} : {c:>9,} logs")
    print(f"{'='*95}\n")


def cmd_add_to_filter(filter_search: str, field_name: str, new_values: List[str]):
    """Agrega nuevos dominios o IPs a un Log Filter existente sin borrar los actuales."""
    filters = fetch_log_filters()
    term = filter_search.lower().strip()
    matches = [f for f in filters if term in f.get("name", "").lower() or term == f.get("_id", "").lower()]
    if not matches:
        print(f"[-] No se encontró ningún Log Filter que coincida con: '{filter_search}'")
        return

    target_f = matches[0]
    fid = target_f["_id"]
    content = json.loads(target_f.get("content", "{}"))
    rules = content.setdefault("rules", {})

    default_op = "contains" if field_name == "url" else "matches" if field_name in ("dstip", "srcip") else "=="
    default_type = "ip" if field_name in ("dstip", "srcip") else "string"

    rule_entry = rules.setdefault(field_name, {"type": default_type, "op": default_op, "value": []})
    current_vals = rule_entry.get("value", [])
    updated_vals = list(dict.fromkeys(current_vals + new_values))
    rule_entry["value"] = updated_vals

    payload_put = {
        "name": target_f["name"],
        "cust_id": target_f["cust_id"],
        "content": json.dumps(content)
    }
    r = requests.put(f"https://{HOST}/connect/api/v1/log_filters/{fid}", headers=get_headers(), json=payload_put, timeout=15, verify=False)
    if r.status_code == 200:
        print(f"\n[✓] Filtro '{target_f['name']}' ({fid}) actualizado exitosamente.")
        print(f"    Campo '{field_name}' ({rule_entry['op']}) ahora tiene {len(updated_vals)} valores:")
        print(f"    Nuevos agregados: {new_values}\n")
    else:
        print(f"[-] Error actualizando filtro ({r.status_code}): {r.text}")


def main():
    parser = argparse.ArgumentParser(description="Stellar Cyber Saved Queries, Log Filters & Domain Volume Inspector")
    parser.add_argument("--queries", action="store_true", help="Listar todas las Saved Queries")
    parser.add_argument("--in-use", action="store_true", help="Filtrar solo queries que están en uso activo")
    parser.add_argument("--query-detail", type=str, help="Ver JSON y DSL completo de una query por nombre o ID")
    parser.add_argument("--filters", action="store_true", help="Listar todos los Log Filters con sus reglas desglosadas")
    parser.add_argument("--filter-detail", type=str, help="Buscar y detallar Log Filters por nombre o contenido (ej: passthrough)")
    parser.add_argument("--ath", action="store_true", help="Listar reglas de Automated Threat Hunting (Alert Watchers)")
    parser.add_argument("--top-domains", action="store_true", help="Ranking de dominios, categorías FortiGuard y ASNs en el Data Lake")
    parser.add_argument("--action", type=str, default="passthrough", help="Acción de firewall para --top-domains (default: passthrough, o accept, deny, all)")
    parser.add_argument("--date", type=str, help="Fecha de índice YYYY.MM.DD (ej: 2026.10.16). Por defecto usa hoy.")
    parser.add_argument("--audit-filter", type=str, help="Simular y auditar qué porcentaje de tráfico cubre un Log Filter y qué deja pasar")
    parser.add_argument("--add-domain", nargs=2, metavar=("FILTER_NAME", "DOMAIN"), help="Agregar un dominio (o lista separada por comas) al campo 'url' de un filtro")
    parser.add_argument("--cleanup-orphans", action="store_true", help="Detectar o limpiar queries temporales de prueba")
    parser.add_argument("--confirm", action="store_true", help="Confirmar eliminación de queries huérfanas")
    args = parser.parse_args()

    if args.queries:
        cmd_list_queries(in_use_only=args.in_use)
        return
    if args.query_detail:
        cmd_query_detail(args.query_detail)
        return
    if args.filters:
        cmd_list_filters()
        return
    if args.filter_detail:
        cmd_list_filters(search_term=args.filter_detail)
        return
    if args.ath:
        cmd_ath_watchers()
        return
    if args.top_domains:
        cmd_top_domains(action_filter=args.action, target_date=args.date)
        return
    if args.audit_filter:
        cmd_audit_filter_coverage(filter_search=args.audit_filter, target_date=args.date)
        return
    if args.add_domain:
        f_name, dom_str = args.add_domain
        doms = [d.strip() for d in dom_str.split(",") if d.strip()]
        cmd_add_to_filter(filter_search=f_name, field_name="url", new_values=doms)
        return
    if args.cleanup_orphans:
        cmd_cleanup_orphans(confirm=args.confirm)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
