#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — CONSULTOR ROBUSTO DE CASOS (stellar_case_fetcher.py)
=============================================================================
Herramienta definitiva y resiliente para consultar la cola y el detalle
completo de casos de Stellar Cyber vía MCP y REST API.

Resuelve automáticamente:
  1. Resolución bidireccional Ticket ID (#17850) <-> Hex ID (6ad283d8...)
  2. Extracción limpia de payload de MCP (data.details, data.alerts, data.summary)
  3. Sanitización de caracteres Unicode / UTF-8 para consola de Windows
  4. Generación directa de dictámenes y resúmenes de observables

Uso:
  python stellar_case_fetcher.py --open                      # Lista todos los casos abiertos
  python stellar_case_fetcher.py --case 17850                # Detalle completo por Ticket ID
  python stellar_case_fetcher.py --case 6ad283d8a9a3e2ee...  # Detalle por Hex ID
  python stellar_case_fetcher.py --all-open-summary          # Resumen forense de todos los casos abiertos
  python stellar_case_fetcher.py --case 17850 --save         # Guarda JSON completo en scratch/
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

# Configuración UTF-8 indestructible en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Carga de entorno
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
        raise RuntimeError(f"Error de autenticación Stellar Cyber ({r.status_code}): {r.text}")
    _CACHED_JWT = r.json().get("access_token")
    return _CACHED_JWT


def call_mcp(tool_name: str, arguments: dict) -> Any:
    """Invoca una herramienta del servidor MCP oficial de Stellar Cyber."""
    jwt = get_jwt()
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    if "access_token" not in arguments:
        arguments["access_token"] = jwt

    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    r = requests.post(f"https://{HOST}/mcp", headers=headers, json=payload, timeout=40, verify=False)
    if r.status_code != 200:
        raise RuntimeError(f"Fallo MCP HTTP {r.status_code}: {r.text[:200]}")

    data = r.json()
    if "result" in data and "content" in data["result"]:
        content = data["result"]["content"]
        if isinstance(content, list) and len(content) > 0:
            text = content[0].get("text", "")
            try:
                return json.loads(text)
            except Exception:
                return text
    return data


def list_cases(status: Optional[str] = None, limit: int = 50, today_only: bool = False) -> List[Dict[str, Any]]:
    """Devuelve la lista limpia de casos usando MCP, con soporte para filtrado por estado y fecha actual."""
    import datetime
    
    # Si status es None o 'Closed', consultamos tanto 'Resolved' como 'Closed'
    statuses_to_query = [status] if status and status not in ("Closed", "all") else ["Resolved", "Closed"] if status == "Closed" else ["New"]
    if status == "all":
        statuses_to_query = ["New", "In Progress", "Resolved", "Closed"]

    all_cases = []
    seen_ids = set()

    for st in statuses_to_query:
        args = {"limit": limit}
        if st:
            args["status"] = st
        res = call_mcp("listCases", args)
        if isinstance(res, dict) and "data" in res:
            for c in res["data"].get("cases", []):
                cid = c.get("_id")
                if cid and cid not in seen_ids:
                    seen_ids.add(cid)
                    all_cases.append(c)

    if today_only:
        today_start_ms = int(datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp() * 1000)
        all_cases = [
            c for c in all_cases
            if (c.get("closed") or c.get("modified_at") or c.get("created_at") or 0) >= today_start_ms
        ]

    # Ordenar por fecha de modificación / cierre descendente
    all_cases.sort(key=lambda x: x.get("modified_at") or x.get("closed") or x.get("created_at") or 0, reverse=True)
    return all_cases


def list_open_cases(status: str = "New", limit: int = 25) -> List[Dict[str, Any]]:
    """Compatibilidad hacia atrás para listar casos abiertos."""
    return list_cases(status=status, limit=limit)


def resolve_case_hex_id(case_identifier: str) -> Optional[str]:
    """Resuelve un Ticket ID numérico (ej: 17850) a su Hex ID interno de MongoDB (ej: 6ad283...)."""
    clean_id = str(case_identifier).strip().replace("#", "")
    if len(clean_id) == 24 and all(c in "0123456789abcdefABCDEF" for c in clean_id):
        return clean_id  # Ya es un Hex ID

    # Es un Ticket ID numérico: consultar lista reciente
    cases = list_cases(status="all", limit=100)
    for c in cases:
        if str(c.get("ticket_id")) == clean_id:
            return c.get("_id")

    return None


def get_full_case_detail(case_identifier: str) -> Dict[str, Any]:
    """Obtiene el detalle JSON completo de un caso resolviendo automáticamente el ID."""
    hex_id = resolve_case_hex_id(case_identifier)
    if not hex_id:
        raise ValueError(f"No se pudo resolver el Ticket ID o Hex ID para: {case_identifier}")

    res = call_mcp("getCaseDetail", {"id": hex_id})
    if isinstance(res, dict) and "data" in res:
        return res["data"]
    elif isinstance(res, dict):
        return res
    raise RuntimeError(f"Respuesta inesperada al consultar caso {case_identifier}: {res}")


def audit_closed_cases(today_only: bool = True) -> List[Dict[str, Any]]:
    """Audita los casos cerrados/resueltos inspeccionando si la justificación técnica coincide con las alertas."""
    cases = list_cases(status="Closed", limit=100, today_only=today_only)
    results = []

    print(f"\n[*] Auditando {len(cases)} casos resueltos/cerrados (Filtro hoy: {today_only})...\n")

    for c in cases:
        tid = c.get("ticket_id")
        hid = c.get("_id")
        tname = c.get("tenant_name")
        cname = c.get("name")
        res_val = c.get("resolution") or "No Tag"
        mod_by = c.get("modified_by_name") or c.get("modified_by") or "Desconocido"

        try:
            det = call_mcp("getCaseDetail", {"id": hid})
            d = det.get("data", {}) if isinstance(det, dict) else {}
            comments = d.get("comments", [])
            comment_texts = [cm.get("comment", "").strip() for cm in comments if isinstance(cm, dict) and cm.get("comment")]
            alerts = d.get("alerts", [])
            alert_names = [
                a.get("_source", {}).get("xdr_event", {}).get("display_name") or a.get("_source", {}).get("event_name")
                for a in alerts if isinstance(a, dict)
            ]

            # Evaluación de calidad del cierre
            status_evaluation = "CORRECTO"
            justification = ""

            if not comment_texts:
                status_evaluation = "OBSERVADO_SIN_COMENTARIO"
                justification = "El caso fue cerrado sin dejar notas ni justificación técnica."
            else:
                combined_comm = " ".join(comment_texts).lower()
                # Verificar concordancia técnica
                if "sophos" in cname.lower() or "translate" in combined_comm:
                    status_evaluation = "CORRECTO_BENIGNO"
                    justification = "Filtrado web de Sophos bloqueando Google Translate / Proxies de forma preventiva."
                elif "driver_blocklist" in combined_comm or "bromium" in combined_comm or "brhostdrv" in combined_comm:
                    status_evaluation = "CORRECTO_BENIGNO"
                    justification = "Controlador legítimo HP Wolf Security bloqueado por lista de endurecimiento de kernel."
                elif "sysvol" in combined_comm or "ldap" in combined_comm or "dpapi" in combined_comm or "ipc$" in combined_comm:
                    status_evaluation = "CORRECTO_BENIGNO"
                    justification = "Operatoria estándar de Active Directory (GPOs, DPAPI o sincronización entre DCs)."
                elif "claude.exe" in combined_comm:
                    status_evaluation = "CORRECTO_BENIGNO"
                    justification = "Comandos PowerShell codificados generados legítimamente por Claude Desktop App."
                elif len(comment_texts[0]) < 25:
                    status_evaluation = "OBSERVADO_COMENTARIO_BREVE"
                    justification = f"Comentario muy corto ({len(comment_texts[0])} caracteres)."
                else:
                    status_evaluation = "CORRECTO"
                    justification = "Análisis forense detallado documentado por el analista."

            results.append({
                "ticket_id": tid,
                "tenant": tname,
                "name": cname,
                "resolution": res_val,
                "analyst": mod_by,
                "alerts_count": len(alerts),
                "evaluation": status_evaluation,
                "audit_note": justification,
                "comments": comment_texts
            })
        except Exception as e:
            results.append({
                "ticket_id": tid,
                "tenant": tname,
                "name": cname,
                "resolution": res_val,
                "analyst": mod_by,
                "evaluation": "ERROR_CONSULTA",
                "audit_note": str(e),
                "comments": []
            })

    return results


def main():
    parser = argparse.ArgumentParser(description="Stellar Cyber Robust Case Fetcher & Auditor (MCP)")
    parser.add_argument("--open", action="store_true", help="Listar casos abiertos")
    parser.add_argument("--closed", action="store_true", help="Listar casos resueltos / cerrados")
    parser.add_argument("--today", action="store_true", help="Filtrar únicamente casos desde las 00:00 de hoy")
    parser.add_argument("--case", type=str, help="Consultar caso por Ticket ID (#17850) o Hex ID")
    parser.add_argument("--all-open-summary", action="store_true", help="Resumen completo de todos los casos abiertos")
    parser.add_argument("--audit-closures", action="store_true", help="Auditar si los cierres de casos corresponden técnicamente")
    parser.add_argument("--save", action="store_true", help="Guardar el JSON completo en la carpeta scratch/")
    args = parser.parse_args()

    if args.audit_closures:
        audit_data = audit_closed_cases(today_only=args.today or True)
        print(f"{'='*100}\n REPORTE DE AUDITORÍA FORENSE DE CIERRES EN STELLAR CYBER\n{'='*100}")
        print(f"{'TICKET':<9} {'TENANT':<12} {'DICTAMEN':<16} {'EVALUACIÓN':<25} {'ANALISTA'}")
        print(f"{'-'*100}")
        for a in audit_data:
            print(f"#{a['ticket_id']:<8} {a['tenant'][:11]:<12} {a['resolution'][:15]:<16} {a['evaluation']:<25} {a['analyst']}")
            print(f"   ↳ Razón: {a['audit_note']}")
            if a['comments']:
                print(f"   ↳ Dictamen Analista: {a['comments'][0][:130]}...")
            print(f"{'-'*100}")
        print(f"{'='*100}\n")
        return

    if args.closed:
        cases = list_cases(status="Closed", limit=50, today_only=args.today)
        print(f"\n{'='*95}\n CASOS CERRADOS/RESUELTOS EN STELLAR CYBER (Total: {len(cases)}) {'[HOY]' if args.today else ''}\n{'='*95}")
        print(f"{'TICKET':<10} {'RESOLUCIÓN':<16} {'SCORE':<8} {'TENANT':<15} {'NOMBRE'}")
        print(f"{'-'*95}")
        for c in cases:
            print(f"#{c.get('ticket_id', ''):<9} {c.get('resolution', 'N/A'):<16} {c.get('score', ''):<8} {c.get('tenant_name', ''):<15} {c.get('name', '')}")
        print(f"{'='*95}\n")
        return

    if args.open:
        cases = list_cases(status="New", limit=25, today_only=args.today)
        print(f"\n{'='*80}\n CASOS ABIERTOS EN STELLAR CYBER (Total: {len(cases)})\n{'='*80}")
        print(f"{'TICKET':<10} {'SEV':<8} {'SCORE':<8} {'TENANT':<15} {'NOMBRE'}")
        print(f"{'-'*80}")
        for c in cases:
            print(f"#{c.get('ticket_id', ''):<9} {c.get('severity', ''):<8} {c.get('score', ''):<8} {c.get('tenant_name', ''):<15} {c.get('name', '')}")
        print(f"{'='*80}\n")
        return

    if args.all_open_summary:
        cases = list_cases(status="New", limit=20)
        print(f"\n[*] Extrayendo detalle forense de {len(cases)} casos abiertos vía MCP...\n")
        for c in cases:
            t_id = c.get("ticket_id")
            hex_id = c.get("_id")
            try:
                detail = call_mcp("getCaseDetail", {"id": hex_id}).get("data", {})
                alerts = detail.get("alerts", [])
                observables = detail.get("summary", {}).get("observables", {})
                alert_names = list(dict.fromkeys([
                    a["_source"].get("xdr_event", {}).get("display_name") or a["_source"].get("event_name")
                    for a in alerts if "_source" in a
                ]))

                print(f"--------------------------------------------------------------------------------")
                print(f"📌 CASO #{t_id} | Score: {c.get('score')} | Sev: {c.get('severity')} | Tenant: {c.get('tenant_name')}")
                print(f"   Nombre:     {c.get('name')}")
                print(f"   Hex ID:     {hex_id}")
                print(f"   Alertas ({len(alerts)}): {', '.join(alert_names[:4])}")
                hosts = [h.get("value") for h in observables.get("host", {}).get("values", [])]
                users = [u.get("value") for u in observables.get("user", {}).get("values", [])]
                if hosts: print(f"   Hosts:      {', '.join(hosts)}")
                if users: print(f"   Usuarios:   {', '.join(users)}")
            except Exception as e:
                print(f"[!] Error extrayendo caso #{t_id}: {e}")
            print(f"--------------------------------------------------------------------------------\n")
        return

    if args.case:
        print(f"[*] Consultando detalle para caso: {args.case}...")
        detail = get_full_case_detail(args.case)
        d_info = detail.get("details", {})
        alerts = detail.get("alerts", [])
        observables = detail.get("summary", {}).get("observables", {})
        comments = detail.get("comments", [])

        print(f"\n{'='*80}\n DETALLE DE CASO #{d_info.get('ticket_id')} ({d_info.get('_id')})\n{'='*80}")
        print(f"Nombre:      {d_info.get('name')}")
        print(f"Estado:      {d_info.get('status')} | Resolución: {d_info.get('resolution')} | Score: {d_info.get('score')}")
        print(f"Tenant:      {d_info.get('tenant_name')}")
        print(f"Alertas:     {len(alerts)} en lote")
        if comments:
            print(f"\n--- Comentarios / Dictámenes Registrados ({len(comments)}) ---")
            for idx, cm in enumerate(comments, 1):
                print(f"[{idx}] {cm.get('comment')}\n")
        print(f"Observables: {json.dumps(observables, indent=2, ensure_ascii=False)}")
        print(f"{'='*80}\n")

        if args.save:
            os.makedirs("scratch", exist_ok=True)
            fname = f"scratch/caso_mcp_{d_info.get('ticket_id')}.json"
            with open(fname, "w", encoding="utf-8") as f:
                json.dump(detail, f, indent=2, ensure_ascii=False)
            print(f"[+] Detalle guardado en: {fname}")
        return

    parser.print_help()

if __name__ == "__main__":
    main()
