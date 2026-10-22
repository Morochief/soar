#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SO3 Case Manager & Automated Escalation Tool
Permite listar, crear y escalar casos automáticamente en Security Onion 3,
asociando observables, eventos de red, firewalls o alertas correlacionadas.
"""

import sys
import os
import json
import uuid
from datetime import datetime, timezone

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from so3_client import SO3Client

ES_USER = "so_elastic"
ES_PASS = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"

def create_case(title, description, severity="high", status="open", assignee="", tags=None):
    """Crea un caso oficial en Security Onion 3 (índice so-case)."""
    case_id = str(uuid.uuid4())
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    if tags is None:
        tags = ["automated-case", "soar"]

    case_doc = {
        "@timestamp": now_iso,
        "so_kind": "case",
        "so_case": {
            "title": title,
            "description": description,
            "severity": severity,
            "status": status,
            "priority": 1,
            "category": "Security Incident",
            "createTime": now_iso,
            "startTime": now_iso,
            "completeTime": "0001-01-01T00:00:00Z",
            "userId": "soar-automation",
            "assigneeId": assignee,
            "template": "Standard",
            "tlp": "amber",
            "pap": "amber",
            "tags": tags
        }
    }

    history_doc = {
        "@timestamp": now_iso,
        "so_kind": "casehistory",
        "so_casehistory": {
            "caseId": case_id,
            "action": "create",
            "description": f"Caso inicializado automáticamente. Asignado: {assignee if assignee else 'Bandeja General'}. Severidad: {severity}.",
            "userId": "soar-automation",
            "time": now_iso
        }
    }

    with SO3Client() as so:
        # Insertar Caso
        so.write_file('/tmp/case_payload.json', json.dumps(case_doc))
        so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/so-case/_doc/{case_id}?refresh=true' -d @/tmp/case_payload.json")
        so.sudo("rm -f /tmp/case_payload.json")

        # Insertar Historial
        so.write_file('/tmp/hist_payload.json', json.dumps(history_doc))
        so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/so-casehistory/_doc?refresh=true' -d @/tmp/hist_payload.json")
        so.sudo("rm -f /tmp/hist_payload.json")

    return case_id

def list_recent_cases(size=10):
    """Lista los casos recientes registrados en so-case."""
    with SO3Client() as so:
        query = {
            "query": {"match_all": {}},
            "sort": [{"@timestamp": {"order": "desc"}}],
            "size": size
        }
        so.write_file('/tmp/q_cases.json', json.dumps(query))
        out, _ = so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/so-case/_search' -d @/tmp/q_cases.json")
        so.sudo("rm -f /tmp/q_cases.json")
        data = json.loads(out)
        return data.get("hits", {}).get("hits", [])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Gestor Automatizado de Casos en Security Onion 3")
    parser.add_argument("--list", action="store_true", help="Listar casos recientes")
    parser.add_argument("--create", action="store_true", help="Crear un nuevo caso")
    parser.add_argument("--title", type=str, default="Caso de Prueba Automatizado", help="Título del caso")
    parser.add_argument("--desc", type=str, default="Descripción generada por SOAR.", help="Descripción")
    parser.add_argument("--severity", type=str, default="high", choices=["low", "medium", "high", "critical"])
    
    args = parser.parse_args()

    if args.create:
        cid = create_case(args.title, args.desc, severity=args.severity)
        print(f"[+] Caso creado exitosamente con ID: {cid}")
    elif args.list or len(sys.argv) == 1:
        cases = list_recent_cases()
        print(f"{'ID':<38} | {'Severidad':<10} | {'Estado':<8} | {'Título'}")
        print("-" * 90)
        for c in cases:
            cid = c.get("_id")
            sc = c.get("_source", {}).get("so_case", {})
            print(f"{cid:<38} | {sc.get('severity',''):<10} | {sc.get('status',''):<8} | {sc.get('title','')[:40]}")
