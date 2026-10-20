#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
  TECHNOMA SOC - FEEDS AI COGNITIVE ORCHESTRATOR
=============================================================================
Motor de Inteligencia Artificial para el análisis y formateo de alertas CTI.
Genera reportes de vulnerabilidad estructurados y profesionales listos para
comunicación con clientes y tickets de escalación del SOC (THN-SOC).

Soporta:
  1. Google Gemini 2.5 Flash (usando GEMINI_API_KEY del SOAR).
  2. OpenAI GPT-4o-mini (usando OPENAI_API_KEY).
"""

import os
import re
import json
import time
import requests
import urllib3
from typing import Dict, Any, Optional, Tuple

try:
    from PySide6.QtCore import QThread, Signal
except ImportError:
    class QThread:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass
    def Signal(*args, **kwargs):  # type: ignore
        class _DummySignal:
            def emit(self, *a, **kw):
                pass
        return _DummySignal()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =============================================================================
# SYSTEM PROMPT ESTRICTO PARA REPORTES DE CLIENTES (ZERO-HALLUCINATION)
# =============================================================================
SYSTEM_PROMPT_VULN_REPORT = """Eres un analista senior de Ciberseguridad del SOC Technoma y un orquestador SOAR especializado en Threat Intelligence.
Tu tarea es analizar el artículo técnico o boletín de vulnerabilidad recibido y estructurarlo obligatoriamente en un Reporte Profesional de Detección de Vulnerabilidades para Clientes en idioma español.

Reglas estrictas de calidad y gobernanza:
1. Responde ÚNICAMENTE con el reporte en formato Markdown estándar. No agregues saludos iniciales, despedidas ni introducciones conversacionales.
2. Si el feed no contiene datos para algún campo específico (como PoC o CVE), escribe explícitamente "No disponible en el feed". NUNCA inventes identificadores, CVEs ni exploits.
3. El "Resumen Ejecutivo" debe ser claro, conciso y comprensible para directivos y gerencia (sin jerga compleja).
4. El "Detalle Técnico" y el "Plan de Mitigación" deben ser precisos, con pasos accionables para administradores de sistemas y equipos de TI.
5. Al final del reporte, añade una sección oculta de metadatos delimitada por '<!-- METADATA_JSON ... -->' con los campos:
   {"severity": "Crítica 🟣 | Alta 🔴 | Media 🟡 | Baja 🟢 | Informativo ℹ️", "cve": "CVE-XXXX o N/A", "affected_technology": "Nombre software/hardware", "mitigation_immediate": "Paso 1"}

--- FORMATO EXACTO OBLIGATORIO ---
## Asunto: [NOTIFICACIÓN DE SEGURIDAD] Alerta de Vulnerabilidad Detectada - {TECNOLOGÍA O TÍTULO}

### 1. Resumen Ejecutivo
* **Fecha de detección:** {FECHA O HOY}
* **Sistema / Tecnología afectada:** {SOFTWARE, HARDWARE O SERVICIO AFECTADO}
* **Severidad estimada:** {Crítica 🟣 / Alta 🔴 / Media 🟡 / Baja 🟢}
* **Impacto potencial para el negocio:** {EXPLICACIÓN CLARA DEL RIESGO OPERATIVO O DE DATOS}

**Descripción breve:** {DESCRIPCIÓN EN LENGUAJE CLARO PARA LA ALTA DIRECCIÓN}

---
### 2. Detalle Técnico de la Vulnerabilidad
* **Nombre de la vulnerabilidad:** {NOMBRE ESTÁNDAR, EJ. EJECUCIÓN REMOTA DE CÓDIGO (RCE), DESBORDAMIENTO, ETC.}
* **Identificador:** {CVE-XXXX-XXXX O ID CORRESPONDIENTE}
* **Descripción técnica:** {EXPLICACIÓN TÉCNICA DEL VECTOR DE ATAQUE Y CONDICIONES DE EXPLOTACIÓN}
* **Prueba de Concepto (PoC) / Evidencia:**
  {DETALLE DE SI EXISTE EXPLOIT PÚBLICO O EVIDENCIA ACTIVA SEGÚN EL FEED}

---
### 3. Plan de Mitigación y Recomendaciones
* **Acción inmediata recomendada:** {PARCHE, REGLA DE FIREWALL O DESHABILITACIÓN RECOMENDADA}
* **Solución a mediano / largo plazo:** {CONFIGURACIÓN ROBUSTA, SEGMENTACIÓN O POLÍTICA}
* **Referencias y enlaces oficiales:**
  {ENLACES Y FUENTES OFICIALES DEL FEED}

---
### 4. Canales de Contacto y Próximos Pasos
Quedamos a su total disposición para colaborar con su equipo técnico en la remediación de este hallazgo. Si requieren soporte adicional para coordinar una sesión de revisión técnica o validar la aplicación de contramedidas, por favor contáctennos directamente.
Una vez aplicado el parche o la mitigación sugerida, infórmennos para registrar la conformidad del activo.

**Technoma SOC - Centro de Operaciones de Ciberseguridad**
*Canal de Guardia:* soc@technoma.com.py | SLA NOC 24/7
---
<!-- METADATA_JSON
{"severity": "Alta 🔴", "cve": "No disponible en el feed", "affected_technology": "General", "mitigation_immediate": "Aplicar parches oficiales"}
-->
"""


class FeedsAIOrchestrator:
    """Motor unificado para invocar modelos LLM (Google Gemini o OpenAI)."""

    @classmethod
    def get_available_providers(cls) -> Dict[str, bool]:
        """Verifica qué credenciales están disponibles en el entorno."""
        antigravity_ok = False
        try:
            from soar_ai_client import is_antigravity_available
            antigravity_ok = is_antigravity_available()
        except Exception:
            pass
        return {
            "antigravity": antigravity_ok,
            "nvidia": bool(os.environ.get("NVIDIA_API_KEY", "").strip()),
            "gemini": antigravity_ok or bool(os.environ.get("GEMINI_API_KEY", "").strip()),
            "openai": bool(os.environ.get("OPENAI_API_KEY", "").strip())
        }

    @classmethod
    def call_nvidia_nim(cls, content: str, api_key: Optional[str] = None, 
                        model: str = "meta/llama-3.2-11b-vision-instruct",
                        image_base64: Optional[str] = None) -> str:
        """
        Invoca a NVIDIA NIM (DeepSeek v4.1-flash / compatible) mediante la API
        OpenAI-compatible en https://integrate.api.nvidia.com/v1.
        Soporta análisis de texto e imágenes/PoC forenses en base64.
        """
        key = api_key.strip() if api_key is not None else os.environ.get("NVIDIA_API_KEY", "").strip()
        if not key:
            raise ValueError("NVIDIA_API_KEY no encontrada en las variables de entorno.")

        url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        # Construir contenido del mensaje de usuario (texto + imagen opcional)
        if image_base64:
            user_content = [
                {"type": "text", "text": f"Analiza y estructura el siguiente boletín/alerta CTI junto con la evidencia gráfica adjunta:\n\n{content}"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
            ]
        else:
            user_content = f"Analiza y estructura el siguiente boletín/noticia CTI:\n\n{content}"

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT_VULN_REPORT},
                {"role": "user", "content": user_content}
            ],
            "temperature": 0.1,
            "max_tokens": 4096
        }

        response = requests.post(url, headers=headers, json=payload, timeout=(10, 60), verify=False)
        if response.status_code == 200:
            res_json = response.json()
            return res_json["choices"][0]["message"]["content"]
        else:
            raise RuntimeError(f"Error NVIDIA NIM API ({response.status_code}): {response.text[:200]}")

    @classmethod
    def call_gemini(cls, content: str, api_key: Optional[str] = None) -> str:
        """Invoca prioritariamente Google Antigravity OAuth (Gemini 3.8 Flash High) con fallback a REST API."""
        user_prompt = f"Analiza y estructura el siguiente boletín/noticia CTI:\n\n{content}"
        if not api_key:
            try:
                from soar_ai_client import is_antigravity_available, call_antigravity
                if is_antigravity_available():
                    return call_antigravity(
                        user_prompt=user_prompt,
                        system_prompt=SYSTEM_PROMPT_VULN_REPORT,
                        temperature=0.1,
                        max_tokens=4096,
                    )
            except Exception as e_ag:
                print(f"[FeedsAI] Antigravity OAuth fallback: {e_ag}")

        key = api_key.strip() if api_key is not None else os.environ.get("GEMINI_API_KEY", "").strip()
        if not key:
            raise ValueError("Ni Antigravity OAuth ni GEMINI_API_KEY están disponibles en el entorno.")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "systemInstruction": {
                "parts": [{"text": SYSTEM_PROMPT_VULN_REPORT}]
            },
            "contents": [
                {
                    "parts": [{"text": user_prompt}]
                }
            ],
            "generationConfig": {
                "temperature": 0.1,
                "topP": 0.95,
                "maxOutputTokens": 4096
            }
        }

        response = requests.post(url, headers=headers, json=payload, timeout=(10, 45), verify=False)
        if response.status_code == 200:
            res_json = response.json()
            candidates = res_json.get("candidates", [])
            if candidates and "content" in candidates[0]:
                return candidates[0]["content"]["parts"][0]["text"]
            raise RuntimeError("Respuesta de Gemini vacía o sin candidatos válidos.")
        else:
            raise RuntimeError(f"Error Gemini API ({response.status_code}): {response.text[:200]}")

    @classmethod
    def call_openai(cls, content: str, api_key: Optional[str] = None, model: str = "gpt-4o-mini") -> str:
        """Invoca a OpenAI API mediante REST API directa resiliente."""
        key = api_key.strip() if api_key is not None else os.environ.get("OPENAI_API_KEY", "").strip()
        if not key:
            raise ValueError("OPENAI_API_KEY no encontrada en las variables de entorno.")

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT_VULN_REPORT},
                {"role": "user", "content": f"Analiza y estructura el siguiente boletín/noticia CTI:\n\n{content}"}
            ],
            "temperature": 0.1
        }

        response = requests.post(url, headers=headers, json=payload, timeout=(10, 45), verify=False)
        if response.status_code == 200:
            res_json = response.json()
            return res_json["choices"][0]["message"]["content"]
        else:
            raise RuntimeError(f"Error OpenAI API ({response.status_code}): {response.text[:200]}")

    @classmethod
    def parse_metadata_from_report(cls, report_text: str) -> Dict[str, Any]:
        """Extrae los metadatos JSON integrados en el reporte generado."""
        default_meta = {
            "severity": "Media 🟡",
            "cve": "N/A",
            "affected_technology": "Varios",
            "mitigation_immediate": "Monitoreo y actualización"
        }
        match = re.search(r'<!--\s*METADATA_JSON\s*(\{.*?\})\s*-->', report_text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group(1))
                if isinstance(parsed, dict):
                    default_meta.update(parsed)
            except Exception:
                pass

        # Heurística de respaldo si no vino el bloque de metadatos
        if default_meta["severity"] == "Media 🟡":
            lower = report_text.lower()
            if "crítica" in lower or "critical" in lower:
                default_meta["severity"] = "Crítica 🟣"
            elif "alta" in lower or "high" in lower:
                default_meta["severity"] = "Alta 🔴"
            elif "baja" in lower or "low" in lower:
                default_meta["severity"] = "Baja 🟢"

        cve_match = re.search(r'(CVE-\d{4}-\d{4,})', report_text, re.IGNORECASE)
        if cve_match:
            default_meta["cve"] = cve_match.group(1).upper()

        return default_meta


# =============================================================================
# HILO ASÍNCRONO DE PROCESAMIENTO CON IA PARA PYSIDE6 (QThread)
# =============================================================================
class FeedsAIWorker(QThread):
    """
    Ejecuta el análisis y formateo del artículo en segundo plano sin congelar
    la ventana principal del SOAR.
    """
    report_ready = Signal(int, str, dict) # item_id, report_markdown, metadata
    progress_status = Signal(str)          # mensaje de estado
    error_occurred = Signal(int, str)      # item_id, error_message

    def __init__(self, item_id: int, feed_title: str, feed_source: str, 
                 feed_url: str, feed_summary: str, provider: str = "gemini"):
        super().__init__()
        self.item_id = item_id
        self.feed_title = feed_title
        self.feed_source = feed_source
        self.feed_url = feed_url
        self.feed_summary = feed_summary
        self.provider = provider.lower()

    def run(self) -> None:
        self.progress_status.emit(f"Analizando '{self.feed_title[:40]}...' con {self.provider.upper()}...")
        try:
            content_payload = (
                f"Fuente de Inteligencia: {self.feed_source}\n"
                f"Título: {self.feed_title}\n"
                f"Enlace Oficial: {self.feed_url}\n"
                f"Contenido / Resumen Crudo:\n{self.feed_summary}"
            )

            report_markdown = None
            if "nvidia" in self.provider or "deepseek" in self.provider:
                report_markdown = FeedsAIOrchestrator.call_nvidia_nim(content_payload)
            elif self.provider == "openai":
                report_markdown = FeedsAIOrchestrator.call_openai(content_payload)
            else:
                # Intento con Gemini, con fallback automático a NVIDIA NIM si la clave de Gemini expiró
                try:
                    report_markdown = FeedsAIOrchestrator.call_gemini(content_payload)
                except Exception as e_gem:
                    if "401" in str(e_gem) or "invalid authentication" in str(e_gem).lower() or "not found" in str(e_gem).lower():
                        # Failover transparente hacia NVIDIA NIM
                        self.progress_status.emit("Gemini no autenticado. Reenrutando a NVIDIA NIM (Llama 3.2)...")
                        report_markdown = FeedsAIOrchestrator.call_nvidia_nim(content_payload)
                    else:
                        raise e_gem

            metadata = FeedsAIOrchestrator.parse_metadata_from_report(report_markdown)
            self.report_ready.emit(self.item_id, report_markdown, metadata)

        except Exception as e:
            self.error_occurred.emit(self.item_id, str(e))
