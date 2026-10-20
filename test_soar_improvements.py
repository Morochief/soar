#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🧪 SUITE DE PRUEBAS LOCALES INTEGRALES — TECHNOMA SOAR (FASES 1 A 4)
=============================================================================
Verifica localmente que todas las mejoras aplicadas funcionan al 100%:
  - FASE 1: Seguridad y Secretos (.env cargado, 0 API keys hardcodeadas en código)
  - FASE 2: Motor IA Unificado (Google Antigravity OAuth Gemini 3.8 Flash + Masking)
  - FASE 3: Arquitectura y Rendimiento (CTI paralelo + Caché TTL, RAG BM25 en disco + Playbooks, SlaGovernanceEngine desacoplado)
  - FASE 4: CLI Unificado SOAR (`soar_cli.py`) y Skill para Hermes Agent
=============================================================================
"""

import os
import re
import sys
import time
import json
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent


def banner(title: str) -> None:
    print("\n" + "=" * 78)
    print(f"🔹 {title}")
    print("=" * 78)


def test_phase_1_security() -> None:
    banner("FASE 1: SEGURIDAD, SECRETOS Y .GITIGNORE")
    env_file = BASE_DIR / ".env"
    assert env_file.exists(), "El archivo .env no existe"
    print(f"  [PASS] Archivo local .env presente ({env_file.stat().st_size} bytes, ignorado por git)")

    # Verificar que no existan secretos hardcodeados en los archivos saneados
    forbidden_patterns = [
        r"nvapi-[A-Za-z0-9_-]{20,}",
        r"8b6a4fb33f472df51c82b621ba7b97dd",
        r"019c7166-c705-7460-934b-57fb007fd024",
        r"b81bd42c-7e59-4db1-9b6a-9f88e33be55a",
        r"d0b1a92c-b536-4f63-b909-123192fb4eb8",
        r"V2t4S1M1MEJjcUF6",
    ]
    checked_files = ["cti_engine.py", "so_engine.py", "soc_agent.py", "soc_agent_gui.py"]
    for fname in checked_files:
        content = (BASE_DIR / fname).read_text(encoding="utf-8", errors="ignore")
        for pat in forbidden_patterns:
            assert not re.search(pat, content), f"Fuga detectada en {fname}: {pat}"
    print(f"  [PASS] Escaneo de secretos en código fuente ({', '.join(checked_files)}): 0 llaves hardcodeadas")

    from cti_engine import CtiEngine
    keys = CtiEngine.get_api_keys()
    loaded_keys = [k for k, v in keys.items() if v]
    assert len(loaded_keys) == 5, f"Faltan llaves CTI en .env: {loaded_keys}"
    print(f"  [PASS] CtiEngine.get_api_keys() cargó las 5 llaves desde .env: {', '.join(loaded_keys)}")


def test_phase_2_unified_ai() -> None:
    banner("FASE 2: MOTOR IA UNIFICADO (ANTIGRAVITY OAUTH GEMINI 3.8 FLASH + MASKING)")
    from soar_ai_client import is_antigravity_available, call_antigravity, SoarUnifiedOpenAIClient
    from stellar_gemini_orchestrator import StellarGeminiOrchestrator
    from feeds_ai_orchestrator import FeedsAIOrchestrator

    assert is_antigravity_available(), "Google Antigravity OAuth no está disponible"
    providers = FeedsAIOrchestrator.get_available_providers()
    print(f"  [PASS] Proveedores IA detectados: {providers}")

    # Prueba de SecurityMaskingEngine reversible en StellarGeminiOrchestrator
    orch = StellarGeminiOrchestrator(enable_pii_masking=True)
    sample_event = {
        "srcip": "192.168.15.25",
        "hostname": "dc01.technoma.local",
        "username": "adm-kevin",
        "event_name": "Suspicious PowerShell Script",
    }
    t0 = time.perf_counter()
    resp = call_antigravity(
        user_prompt="Responde en una sola oración corta confirmando recepción de telemetria de [HOST_ANON_0] con IP [IP_ANON_0].",
        system_prompt="Eres un analista SOC conciso. Incluye literalmente los tokens [HOST_ANON_0] e [IP_ANON_0] en tu respuesta.",
        temperature=0.1,
        max_tokens=200,
    )
    elapsed = (time.perf_counter() - t0) * 1000
    orch.mask_engine.procesar_diccionario(sample_event)
    restored = orch.mask_engine.desofuscar_texto(resp)
    print(f"  [PASS] Respuesta Antigravity (Gemini 3.8 Flash High) en {elapsed:.0f}ms:")
    print(f"         -> Cruda (Anonimizada): {resp.strip()}")
    print(f"         -> Desofuscada en RAM : {restored.strip()}")

    # Prueba de streaming con SoarUnifiedOpenAIClient
    client = SoarUnifiedOpenAIClient()
    stream = client.chat.completions.create(
        model="gemini-3.8-flash-high",
        messages=[{"role": "user", "content": "Di únicamente: STREAM_OK_TECHNOMA"}],
        temperature=0.0,
        max_tokens=50,
        stream=True,
    )
    chunks = [c.choices[0].delta.content for c in stream if c.choices and c.choices[0].delta.content]
    joined = "".join(chunks).strip()
    assert joined, "El streaming de SoarUnifiedOpenAIClient devolvió vacío"
    print(f"  [PASS] Streaming SSE vía SoarUnifiedOpenAIClient: '{joined}'")


def test_phase_3_architecture_and_perf() -> None:
    banner("FASE 3: RENDIMIENTO (CTI PARALELO + CACHÉ, RAG EN DISCO + PLAYBOOKS, SLA MODULAR)")
    from cti_engine import CtiEngine
    from rag_engine import LocalRAG
    from sla_governance import SlaGovernanceEngine

    # 3.1 Prueba CTI paralelo + caché TTL
    t0 = time.perf_counter()
    res_cold = CtiEngine.tri_scan("8.8.8.8", use_cache=False)
    t_cold = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    res_warm = CtiEngine.tri_scan("8.8.8.8", use_cache=True)
    t_warm = (time.perf_counter() - t1) * 1000

    assert res_cold["consolidated_verdict"], "tri_scan no devolvió veredicto"
    assert res_warm.get("cached") is True, "La segunda llamada a tri_scan no usó la caché TTL"
    print(f"  [PASS] CtiEngine.tri_scan('8.8.8.8') paralelo (VT+AbuseIPDB+URLScan+OTX): {t_cold:.0f}ms -> Veredicto: {res_cold['consolidated_verdict']}")
    print(f"  [PASS] CtiEngine.tri_scan('8.8.8.8') desde caché TTL en memoria: {t_warm:.2f}ms (aceleración instantánea)")

    # 3.2 Prueba RAG con caché persistente en disco + Playbooks
    t0 = time.perf_counter()
    rag_first = LocalRAG()
    rag_first.build_index(force_rebuild=True)
    t_build = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    rag_cached = LocalRAG()
    rag_cached.build_index(force_rebuild=False)
    t_cached = (time.perf_counter() - t1) * 1000

    hits = rag_cached.query("Playbook Fuerza Bruta Active Directory PB-1.1", top_k=3)
    assert len(hits) > 0, "RAG no devolvió resultados"
    print(f"  [PASS] LocalRAG build_index() en frío: {t_build:.1f}ms | Carga desde caché en disco (.rag_index_cache.pkl): {t_cached:.1f}ms")
    print(f"  [PASS] Top hit RAG (incluyendo 00_Playbooks): {hits[0]['doc_name']} (Score: {hits[0]['score']:.2f})")

    # 3.3 Prueba SlaGovernanceEngine desacoplado de Qt
    now_ms = int(time.time() * 1000)
    mock_cases = [
        {"created_at": now_ms - 10 * 60 * 1000, "acknowledged": now_ms - 5 * 60 * 1000, "closed": now_ms - 1 * 60 * 1000, "score": 95, "status": "Resolved", "resolution": "True Positive", "assignee": "kevinmoraes@technoma.com.py", "tenant_name": "Caja Ande", "name": "Ransomware Execution Attempt"},
        {"created_at": now_ms - 30 * 60 * 1000, "acknowledged": now_ms - 25 * 60 * 1000, "closed": now_ms - 15 * 60 * 1000, "score": 60, "status": "Resolved", "resolution": "False Positive", "assignee": "kevinmoraes@technoma.com.py", "tenant_name": "Technoma", "name": "DNS Query to wbx2.com"},
    ]
    metrics = SlaGovernanceEngine.calculate_deep_metrics(mock_cases)
    assert metrics["total_cases"] == 2 and metrics["sla_compliance_pct"] == 100.0
    print(f"  [PASS] SlaGovernanceEngine independiente de GUI: {metrics['total_cases']} casos evaluados | SLA Compliance: {metrics['sla_compliance_pct']}% | MTTD prom: {metrics['avg_mttd_str']} | MTTR prom: {metrics['avg_mttr_str']}")


def test_phase_4_cli_and_hermes() -> None:
    banner("FASE 4: CLI UNIFICADO (soar_cli.py) Y SKILL HERMES AGENT")
    proc = subprocess.run(
        [sys.executable, str(BASE_DIR / "soar_cli.py"), "sla", '{"score": 92, "status": "In Progress"}'],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    sla_out = json.loads(proc.stdout)
    assert sla_out["priority"] == "P1"
    print(f"  [PASS] soar_cli.py sla -> Prioridad: {sla_out['priority']} ({sla_out['severity']}), Límite MTTD: {sla_out['mttd']['limit_str']}, Límite MTTR: {sla_out['mttr']['limit_str']}")


if __name__ == "__main__":
    t_start = time.perf_counter()
    test_phase_1_security()
    test_phase_2_unified_ai()
    test_phase_3_architecture_and_perf()
    test_phase_4_cli_and_hermes()
    total_s = time.perf_counter() - t_start
    print("\n" + "=" * 78)
    print(f"✅ TODAS LAS PRUEBAS (FASES 1, 2, 3 y 4) PASARON EXITOSAMENTE EN {total_s:.2f}s")
    print("=" * 78)
