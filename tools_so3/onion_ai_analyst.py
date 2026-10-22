#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Security Onion Autonomous AI Analyst (con Memoria RAG Institucional)
Analiza incidentes y casos de Security Onion 3 cruzándolos con la Memoria
Institucional del SOC (rag_engine: Playbooks, Bitácoras, Políticas y Falsos Positivos conocidos).

Regla de Negocio Crítica:
- Clientes con stack exclusivo Security Onion (Valores, Vascol):
  * Se analizan bajo su contexto de cliente específico sin mezclar con las políticas de Technoma.
- Technoma / General:
  * Aplica 100% la memoria RAG del SOC (Rosetta Stone, bitácoras de analistas, falsos positivos).
"""

import sys
import os
import json
from datetime import datetime, timezone
from typing import Dict, Any, Optional

# Paths base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'tools_so3'))

from tools_so3.so3_client import SO3Client
from rag_engine import LocalRAG
import requests

try:
    from google import genai
    from google.genai import types
    HAS_NEW_GENAI = True
except ImportError:
    HAS_NEW_GENAI = False

ES_USER = "so_elastic"
ES_PASS = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"

class OnionAIAnalyst:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.rag = LocalRAG()
        self.rag.build_index()

    def identify_tenant(self, case_doc: Dict[str, Any]) -> str:
        """Identifica si el caso pertenece a un cliente específico (Vascol, Valores) o Technoma."""
        desc = case_doc.get("description", "")
        title = case_doc.get("title", "")
        combined = (desc + " " + title).lower()

        if "vascol" in combined or "192.168.110." in combined or "181.94.247.147" in combined:
            return "VASCOL"
        if "valores" in combined or "10.92." in combined or "181.40.116.2" in combined:
            return "VALORES"
        return "TECHNOMA"

    def analyze_case(self, case_id: str, write_to_so: bool = False) -> Dict[str, Any]:
        """Obtiene un caso de Security Onion, busca memoria RAG y lo analiza con IA."""
        with SO3Client() as so:
            # 1. Obtener el caso de so-case
            out_c, _ = so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' 'https://127.0.0.1:9200/so-case/_doc/{case_id}'")
            try:
                c_json = json.loads(out_c)
                if not c_json.get("found"):
                    return {"error": f"Caso {case_id} no encontrado en so-case."}
                case_data = c_json.get("_source", {}).get("so_case", {})
            except Exception as e:
                return {"error": f"Error parseando caso: {str(e)}"}

        tenant = self.identify_tenant(case_data)
        title = case_data.get("title", "")
        description = case_data.get("description", "")
        severity = case_data.get("severity", "medium")

        # 2. Búsqueda en Memoria RAG Institucional
        rag_context = ""
        if tenant in ["VASCOL", "VALORES"]:
            rag_context = (
                f"[CONTEXTO DE CLIENTE EXCLUSIVO SECURITY ONION: {tenant}]\n"
                f"Este cliente opera en modalidad de monitoreo perimetral / NDR dedicado.\n"
                f"No aplicar políticas internas ni exclusiones de Active Directory de Technoma.\n"
                f"Enfocar el análisis en protección perimetral, escaneos externos y disponibilidad de sus servicios."
            )
        else:
            # Buscar en la base de conocimiento institucional de Technoma
            query_rag = f"{title} {description[:200]}"
            rag_results = self.rag.query(query_rag, top_k=3)
            if rag_results:
                rag_context = "[MEMORIA INSTITUCIONAL DEL SOC / RAG TECHNO-MA]\n"
                for r in rag_results:
                    rag_context += f"--- Fuente: {r.get('rel_path')} (Capa: {r.get('category')}) ---\n"
                    rag_context += f"{r.get('content', '')[:600]}\n\n"

        # 3. Prompt de Ingeniería Forense
        system_prompt = (
            "Eres el Analista Autónomo Senior de Ciberseguridad (Nivel 3) para Security Onion 3.\n"
            "Tu misión es evaluar incidentes, correlacionar eventos crudos de red y dictaminar con precisión militar.\n"
            "Debes estructurar tu respuesta en:\n"
            "1. RESUMEN EJECUTIVO (2 líneas para la guardia)\n"
            "2. CLASIFICACIÓN TÁCTICA MITRE ATT&CK (Táctica, Técnica e ID)\n"
            "3. DICTAMEN FORENSE (Verdadero Positivo / Falso Positivo / Escaneo Bloqueado Sin Impacto)\n"
            "4. JUSTIFICACIÓN BASADA EN EVIDENCIA Y MEMORIA INSTITUCIONAL\n"
            "5. PLAN DE CONTENCIÓN Y ACCIONES INMEDIATAS"
        )

        user_content = f"""
INFORMACIÓN DEL CASO EN SECURITY ONION:
ID: {case_id}
Tenant Identificado: {tenant}
Título: {title}
Severidad: {severity}
Descripción y Evidencia Cruda:
{description}

{rag_context}

Genera tu análisis técnico y dictamen final:
"""

        # 4. Invocación a Gemini
        analysis_text = ""
        if self.api_key and HAS_NEW_GENAI:
            try:
                client = genai.Client(api_key=self.api_key)
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_content,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=0.2
                    )
                )
                analysis_text = response.text
            except Exception as e:
                analysis_text = f"Error al invocar API de Gemini: {str(e)}"
        else:
            analysis_text = (
                f"[SIMULACIÓN ANALIZADOR ONION AI - GEMINI KEY NO CONFIGURADA EN CLI]\n"
                f"Tenant: {tenant}\n"
                f"Memoria RAG Inyectada: {'Sí (Technoma)' if tenant == 'TECHNOMA' else 'Aislamiento de Cliente (' + tenant + ')'}\n"
                f"Dictamen: Caso estructurado listo para evaluación con modelo."
            )

        # 5. Opcional: Escribir el dictamen como comentario en so-casehistory
        if write_to_so and "Error" not in analysis_text:
            with SO3Client() as so:
                now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                comment_doc = {
                    "@timestamp": now_iso,
                    "so_kind": "comment",
                    "so_comment": {
                        "caseId": case_id,
                        "description": f"🤖 **Análisis Autónomo Onion AI (RAG SOC)**:\n\n{analysis_text}",
                        "userId": "onion-ai-analyst",
                        "time": now_iso
                    }
                }
                so.write_file('/tmp/ai_comment.json', json.dumps(comment_doc))
                so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/so-casehistory/_doc?refresh=true' -d @/tmp/ai_comment.json")
                so.sudo("rm -f /tmp/ai_comment.json")

        return {
            "case_id": case_id,
            "tenant": tenant,
            "title": title,
            "analysis": analysis_text
        }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Analizador IA Autónomo para Security Onion 3")
    parser.add_argument("--case", type=str, help="ID del caso en so-case a analizar")
    parser.add_argument("--post-comment", action="store_true", help="Publicar el análisis como comentario en el caso")
    args = parser.parse_args()

    analyst = OnionAIAnalyst()
    if args.case:
        res = analyst.analyze_case(args.case, write_to_so=args.post_comment)
        print(f"\n=== DICTAMEN ONION AI (Tenant: {res.get('tenant')}) ===")
        print(res.get("analysis"))
    else:
        print("Uso: python onion_ai_analyst.py --case <CASE_ID> [--post-comment]")
        print("RAG Institucional cargado y listo.")
