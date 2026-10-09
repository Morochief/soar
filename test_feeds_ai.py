#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el motor de IA de feeds (feeds_ai_orchestrator.py).
Valida:
1. Parseo de metadatos desde el bloque estructurado.
2. Heurística de fallback para severidad y CVE.
3. Manejo de excepciones en llamadas sin credenciales.
"""

import unittest
from feeds_ai_orchestrator import FeedsAIOrchestrator, SYSTEM_PROMPT_VULN_REPORT


class TestFeedsAIOrchestrator(unittest.TestCase):

    def test_parse_metadata_explicit(self):
        sample_report = """## Asunto: Alerta de Vulnerabilidad
### 1. Resumen Ejecutivo
...
<!-- METADATA_JSON
{"severity": "Crítica 🟣", "cve": "CVE-2026-1122", "affected_technology": "Fortinet FortiOS", "mitigation_immediate": "Actualizar a v7.4.2"}
-->
"""
        meta = FeedsAIOrchestrator.parse_metadata_from_report(sample_report)
        self.assertEqual(meta["severity"], "Crítica 🟣")
        self.assertEqual(meta["cve"], "CVE-2026-1122")
        self.assertEqual(meta["affected_technology"], "Fortinet FortiOS")
        self.assertEqual(meta["mitigation_immediate"], "Actualizar a v7.4.2")

    def test_parse_metadata_fallback_heuristic(self):
        sample_report = """## Alerta
Detectada vulnerabilidad de severidad Alta en servidores Linux bajo CVE-2026-5544.
"""
        meta = FeedsAIOrchestrator.parse_metadata_from_report(sample_report)
        self.assertEqual(meta["severity"], "Alta 🔴")
        self.assertEqual(meta["cve"], "CVE-2026-5544")

    def test_missing_gemini_key_raises(self):
        with self.assertRaises(ValueError):
            FeedsAIOrchestrator.call_gemini("Contenido de prueba", api_key="")

    def test_missing_openai_key_raises(self):
        with self.assertRaises(ValueError):
            FeedsAIOrchestrator.call_openai("Contenido de prueba", api_key="")

    def test_missing_nvidia_key_raises(self):
        with self.assertRaises(ValueError):
            FeedsAIOrchestrator.call_nvidia_nim("Contenido de prueba", api_key="")

    def test_available_providers_keys(self):
        providers = FeedsAIOrchestrator.get_available_providers()
        self.assertIn("nvidia", providers)
        self.assertIn("gemini", providers)
        self.assertIn("openai", providers)

    def test_system_prompt_contains_mandatory_sections(self):
        self.assertIn("1. Resumen Ejecutivo", SYSTEM_PROMPT_VULN_REPORT)
        self.assertIn("2. Detalle Técnico de la Vulnerabilidad", SYSTEM_PROMPT_VULN_REPORT)
        self.assertIn("3. Plan de Mitigación y Recomendaciones", SYSTEM_PROMPT_VULN_REPORT)
        self.assertIn("4. Canales de Contacto y Próximos Pasos", SYSTEM_PROMPT_VULN_REPORT)


if __name__ == "__main__":
    unittest.main()
