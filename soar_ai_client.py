#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — UNIFIED AI CLIENT (soar_ai_client.py)
=============================================================================
Motor unificado de Inteligencia Artificial para toda la suite SOAR:
  1. Google Antigravity OAuth (Gemini 3.8 Flash High / Tiered, Gemini 3.1 Pro,
     Gemini 2.5 Pro) con rotación multi-cuenta automática sin costo de API Key.
  2. Google Gemini REST API directa (GEMINI_API_KEY) como primer respaldo.
  3. NVIDIA NIM OpenAI-compatible (NVIDIA_API_KEY) como segundo respaldo.
  4. OpenAI API directa (OPENAI_API_KEY) como tercer respaldo.

Incluye soporte para:
  - Generación síncrona y en streaming (iterador de chunks o interfaz compatible con OpenAI SDK).
  - Seudonimización reversible opcional en RAM (SecurityMaskingEngine).
=============================================================================
"""

from __future__ import annotations

import os
import json
import time
import logging
import requests
import urllib3
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, Iterator, List, Optional

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger("soar_ai_client")

# Cargar .env local automáticamente
try:
    from dotenv import load_dotenv
    _env_path = Path(__file__).resolve().parent / ".env"
    if _env_path.exists():
        load_dotenv(_env_path)
    else:
        load_dotenv()
except Exception:
    pass


DEFAULT_ANTIGRAVITY_MODEL = os.environ.get("SOAR_AI_MODEL", "gemini-3.8-flash-high")


def _select_antigravity_account_token(model: str = DEFAULT_ANTIGRAVITY_MODEL) -> Optional[Dict[str, Any]]:
    """Obtiene un token OAuth válido (con refresh automático si expiró) desde ~/.hermes/antigravity-accounts.json."""
    try:
        from antigravity_auth.config import get_config
        from antigravity_auth.interceptor import _select_request_account
        from antigravity_auth.transform.envelope import resolve_model_for_header_style

        cfg = get_config()
        resolved_model = resolve_model_for_header_style(model, "antigravity")
        selected = _select_request_account(resolved_model, "antigravity", cfg)
        if selected and selected.get("access"):
            account = selected.get("account")
            project_id = ""
            if account and getattr(account, "refresh_parts", None):
                project_id = (
                    account.refresh_parts.project_id
                    or account.refresh_parts.managed_project_id
                    or ""
                )
            from antigravity_auth.constants import ANTIGRAVITY_DEFAULT_PROJECT_ID
            return {
                "access_token": selected["access"],
                "project_id": project_id or ANTIGRAVITY_DEFAULT_PROJECT_ID,
                "resolved_model": resolved_model,
                "email": getattr(account, "email", "antigravity-oauth"),
            }
    except Exception as exc:
        logger.debug("Antigravity account token resolution failed: %s", exc)
    return None


def is_antigravity_available() -> bool:
    """Devuelve True si hay cuentas de Antigravity configuradas y accesibles."""
    try:
        from antigravity_auth.storage import load_accounts
        data = load_accounts()
        accounts = data.get("accounts", [])
        return isinstance(accounts, list) and len(accounts) > 0
    except Exception:
        return False


def call_antigravity(
    prompt: str = "",
    system_instruction: str = "",
    model: str = DEFAULT_ANTIGRAVITY_MODEL,
    temperature: float = 0.2,
    max_tokens: int = 8192,
    user_prompt: Optional[str] = None,
    system_prompt: Optional[str] = None,
) -> str:
    """Invoca Google Antigravity Cloud Code (no-streaming) con rotación de cuentas."""
    effective_prompt = user_prompt if user_prompt is not None else prompt
    effective_system = system_prompt if system_prompt is not None else system_instruction
    token_info = _select_antigravity_account_token(model)
    if not token_info:
        raise RuntimeError("No hay cuenta OAuth activa de Google Antigravity disponible.")

    from antigravity_auth.constants import ANTIGRAVITY_ENDPOINT_PROD, ide_user_agent
    from antigravity_auth.transform.envelope import build_antigravity_envelope, build_antigravity_url

    resolved_model = token_info["resolved_model"]
    effective_max_tokens = max(int(max_tokens or 8192), 2048)
    inner_request: Dict[str, Any] = {
        "contents": [{"role": "user", "parts": [{"text": effective_prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": effective_max_tokens,
        },
    }
    if effective_system:
        inner_request["systemInstruction"] = {
            "role": "user",
            "parts": [{"text": effective_system}],
        }

    envelope = build_antigravity_envelope(
        inner_request,
        model=resolved_model,
        project_id=token_info["project_id"],
    )
    url = build_antigravity_url(
        ANTIGRAVITY_ENDPOINT_PROD,
        resolved_model,
        action="generateContent",
        streaming=False,
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token_info['access_token']}",
        "User-Agent": ide_user_agent(),
    }

    resp = requests.post(url, headers=headers, json=envelope, timeout=(10, 90))
    if resp.status_code != 200:
        raise RuntimeError(f"Antigravity HTTP {resp.status_code}: {resp.text[:250]}")

    data = resp.json()
    inner_resp = data.get("response", data)
    candidates = inner_resp.get("candidates", [])
    if not candidates:
        raise RuntimeError("Respuesta vacía de Antigravity Cloud Code.")

    parts = candidates[0].get("content", {}).get("parts", [])
    texts = [
        p.get("text", "")
        for p in parts
        if isinstance(p, dict) and not p.get("thought") and p.get("text")
    ]
    if not texts and parts:
        texts = [p.get("text", "") for p in parts if isinstance(p, dict) and p.get("text")]
    return "".join(texts)


def stream_antigravity(
    messages: List[Dict[str, Any]],
    model: str = DEFAULT_ANTIGRAVITY_MODEL,
    temperature: float = 0.2,
    max_tokens: int = 8192,
) -> Iterator[str]:
    """Transmite tokens en tiempo real (SSE) desde Google Antigravity Cloud Code."""
    token_info = _select_antigravity_account_token(model)
    if not token_info:
        raise RuntimeError("No hay cuenta OAuth activa de Google Antigravity disponible.")

    from antigravity_auth.constants import ANTIGRAVITY_ENDPOINT_PROD, ide_user_agent
    from antigravity_auth.transform.envelope import build_antigravity_envelope, build_antigravity_url

    resolved_model = token_info["resolved_model"]
    system_parts: List[str] = []
    contents: List[Dict[str, Any]] = []

    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if isinstance(content, list):
            text_val = "\n".join(
                item.get("text", "") for item in content if isinstance(item, dict) and item.get("type") == "text"
            )
        else:
            text_val = str(content or "")

        if role == "system":
            if text_val:
                system_parts.append(text_val)
        elif role == "assistant":
            contents.append({"role": "model", "parts": [{"text": text_val}]})
        else:
            contents.append({"role": "user", "parts": [{"text": text_val}]})

    if not contents:
        contents.append({"role": "user", "parts": [{"text": "Hola"}]})

    effective_max_tokens = max(int(max_tokens or 8192), 2048)
    inner_request: Dict[str, Any] = {
        "contents": contents,
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": effective_max_tokens,
        },
    }
    if system_parts:
        inner_request["systemInstruction"] = {
            "role": "user",
            "parts": [{"text": "\n\n".join(system_parts)}],
        }

    envelope = build_antigravity_envelope(
        inner_request,
        model=resolved_model,
        project_id=token_info["project_id"],
    )
    url = build_antigravity_url(
        ANTIGRAVITY_ENDPOINT_PROD,
        resolved_model,
        action="streamGenerateContent",
        streaming=True,
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
        "Authorization": f"Bearer {token_info['access_token']}",
        "User-Agent": ide_user_agent(),
    }

    with requests.post(url, headers=headers, json=envelope, stream=True, timeout=(10, 120)) as resp:
        if resp.status_code != 200:
            raise RuntimeError(f"Antigravity Stream HTTP {resp.status_code}: {resp.text[:250]}")
        resp.encoding = "utf-8"
        for raw_line in resp.iter_lines(decode_unicode=True):
            if not raw_line or not raw_line.startswith("data:"):
                continue
            data_str = raw_line[5:].strip()
            if not data_str or data_str == "[DONE]":
                continue
            try:
                event = json.loads(data_str)
                inner = event.get("response", event)
                for cand in inner.get("candidates", []):
                    for part in cand.get("content", {}).get("parts", []):
                        if isinstance(part, dict) and not part.get("thought") and part.get("text"):
                            yield part["text"]
            except Exception:
                continue


class SoarUnifiedOpenAIClient:
    """
    Cliente drop-in compatible con `OpenAI().chat.completions.create(...)` que enruta
    automáticamente por Google Antigravity OAuth (Gemini 3.8 Flash) y hace fallback
    transparente a NVIDIA NIM / OpenAI si se solicita o si Antigravity no está disponible.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        prefer_antigravity: bool = True,
        **kwargs: Any,
    ) -> None:
        self.api_key = api_key or os.environ.get("NVIDIA_API_KEY", "")
        self.base_url = base_url or os.environ.get("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
        self.extra_client_kwargs = kwargs
        self.prefer_antigravity = prefer_antigravity and (
            os.environ.get("SOAR_AI_PROVIDER", "antigravity").lower() in ("antigravity", "ag", "auto")
        )
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _resolve_model(self, requested_model: str) -> str:
        if not requested_model or "llama" in requested_model.lower() or "glm" in requested_model.lower():
            return os.environ.get("SOAR_AI_MODEL", DEFAULT_ANTIGRAVITY_MODEL)
        return requested_model

    def _create(
        self,
        *,
        model: str = DEFAULT_ANTIGRAVITY_MODEL,
        messages: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.2,
        max_tokens: int = 4096,
        stream: bool = False,
        **kwargs: Any,
    ) -> Any:
        msgs = messages or []
        if self.prefer_antigravity and is_antigravity_available() and not kwargs.get("tools"):
            ag_model = self._resolve_model(model)
            if stream:
                def _chunk_gen():
                    for text_delta in stream_antigravity(
                        msgs, model=ag_model, temperature=temperature, max_tokens=max_tokens
                    ):
                        yield SimpleNamespace(
                            choices=[
                                SimpleNamespace(
                                    delta=SimpleNamespace(content=text_delta),
                                    finish_reason=None,
                                )
                            ]
                        )
                return _chunk_gen()
            else:
                sys_inst = "\n\n".join(
                    str(m.get("content", "")) for m in msgs if m.get("role") == "system"
                )
                user_prompt = "\n\n".join(
                    str(m.get("content", "")) for m in msgs if m.get("role") != "system"
                )
                full_text = call_antigravity(
                    prompt=user_prompt,
                    system_instruction=sys_inst,
                    model=ag_model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                return SimpleNamespace(
                    choices=[
                        SimpleNamespace(
                            message=SimpleNamespace(
                                role="assistant",
                                content=full_text,
                                tool_calls=None,
                            ),
                            finish_reason="stop",
                        )
                    ]
                )

        # Fallback a cliente OpenAI / NVIDIA NIM estándar
        from openai import OpenAI
        fallback_client = OpenAI(base_url=self.base_url, api_key=self.api_key or "missing-key")
        return fallback_client.chat.completions.create(
            model=model,
            messages=msgs,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream,
            **kwargs,
        )
