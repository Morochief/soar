#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOAR CLI — Unificador de Operaciones para Hermes Agent & Terminal
=============================================================================
Subcomandos soportados:
  - cti <observable>          : Ejecuta CtiEngine.tri_scan en paralelo (VT, AbuseIPDB, URLScan, OTX, MxToolbox)
  - rag <consulta>            : Busca en la base de conocimientos BM25 de 7 capas
  - memory <alerta_o_archivo> : Devuelve en <20ms el Paquete de Memoria Instantánea de las 7 capas del SOC
  - catalog                   : Genera y muestra el resumen de CATALOGO_COMPLETO_MARKDOWNS_SOC.md
  - sla <score_o_json>        : Evalúa prioridad y tiempos SLA/SLO (MTTD, MTTR, Triaje POE)
  - triage <texto_o_archivo>  : Ejecuta el copiloto forense SOC Agent con Google Antigravity (Gemini 3.8 Flash)
=============================================================================
"""

import os
import sys
import json
import argparse
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def cmd_cti(observable: str, no_cache: bool = False) -> None:
    from cti_engine import CtiEngine
    res = CtiEngine.tri_scan(observable, use_cache=not no_cache)
    print(json.dumps(res, indent=2, ensure_ascii=False))


def cmd_rag(query: str, top_k: int = 4, category: str = None) -> None:
    from rag_engine import get_rag
    rag = get_rag()
    results = rag.query(query, top_k=top_k, category=category)
    print(json.dumps(results, indent=2, ensure_ascii=False))


def cmd_memory(target: str) -> None:
    from rag_engine import get_rag
    rag = get_rag()
    p = Path(target)
    if p.exists() and p.is_file():
        content = p.read_text(encoding="utf-8", errors="ignore")
    else:
        content = target
    print(rag.instant_case_context(content))


def cmd_catalog() -> None:
    from rag_engine import get_rag
    rag = get_rag()
    path = rag.export_master_catalog_markdown()
    print(f"✅ Catálogo maestro actualizado en: {path}")
    print(f"   Total de archivos indexados: {len(rag.file_inventory)} ({len(rag.retriever.corpus)} bloques BM25)")


def cmd_sla(raw_input: str) -> None:
    from sla_governance import SlaGovernanceEngine
    try:
        case = json.loads(raw_input)
        if not isinstance(case, dict):
            case = {"score": float(raw_input)}
    except Exception:
        try:
            case = {"score": float(raw_input)}
        except Exception:
            case = {"severity": raw_input}

    p_code, sev_label = SlaGovernanceEngine.get_priority(case)
    mttd = SlaGovernanceEngine.evaluate_mttd(case)
    mttr = SlaGovernanceEngine.evaluate_mttr(case)
    out = {
        "priority": p_code,
        "severity": sev_label,
        "mttd": mttd,
        "mttr": mttr,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_triage(target: str) -> None:
    from soc_agent import ejecutar_consulta
    p = Path(target)
    if p.exists() and p.is_file():
        content = p.read_text(encoding="utf-8", errors="ignore")
        ejecutar_consulta(f"Analiza la siguiente alerta cruda:\n\n{content}")
    else:
        ejecutar_consulta(target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Technoma SOAR CLI for Hermes Agent & Antigravity")
    sub = parser.add_subparsers(dest="subcommand", required=True)

    p_cti = sub.add_parser("cti", help="Consulta CTI tri_scan en paralelo")
    p_cti.add_argument("observable", help="IP, Dominio, URL o Hash SHA256/MD5")
    p_cti.add_argument("--no-cache", action="store_true", help="Ignorar caché TTL")

    p_rag = sub.add_parser("rag", help="Consulta RAG local BM25 (7 capas)")
    p_rag.add_argument("query", help="Término o regla a buscar")
    p_rag.add_argument("-k", "--top-k", type=int, default=4, help="Cantidad de fragmentos")
    p_rag.add_argument(
        "-c",
        "--category",
        help="Filtrar por capa: MEMORIA_SOC | CASO_HISTORICO | PLAYBOOK | PROCEDIMIENTO_ARQ | SKILL_SOC | DOC_STELLAR | ACADEMIA_SOC",
    )

    p_mem = sub.add_parser("memory", help="Devuelve en <20ms el Paquete de Memoria Instantánea de 7 capas para una alerta/caso")
    p_mem.add_argument("target", help="Texto de la alerta, nombre de evento, IP, usuario o ruta a JSON")

    sub.add_parser("catalog", help="Genera CATALOGO_COMPLETO_MARKDOWNS_SOC.md con todos los Markdowns del proyecto")

    p_sla = sub.add_parser("sla", help="Evalúa prioridad y SLA/SLO de un caso")
    p_sla.add_argument("case_input", help="Score numérico (ej. 92), severidad o JSON de caso")

    p_triage = sub.add_parser("triage", help="Triaje forense completo con IA Antigravity")
    p_triage.add_argument("target", help="Texto de la alerta o ruta a archivo JSON")

    args = parser.parse_args()
    if args.subcommand == "cti":
        cmd_cti(args.observable, no_cache=args.no_cache)
    elif args.subcommand == "rag":
        cmd_rag(args.query, top_k=args.top_k, category=args.category)
    elif args.subcommand == "memory":
        cmd_memory(args.target)
    elif args.subcommand == "catalog":
        cmd_catalog()
    elif args.subcommand == "sla":
        cmd_sla(args.case_input)
    elif args.subcommand == "triage":
        cmd_triage(args.target)


if __name__ == "__main__":
    main()
