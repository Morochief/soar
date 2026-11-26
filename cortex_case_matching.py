#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helpers compartidos (sin dependencias) para relacionar casos de Stellar Cyber
con Case IDs de Palo Alto Cortex XDR. Los usan sync_cortex_cases.py,
close_cases_bulk.py y auto_create_cortex_cases.py.

Antes cada script comparaba con `"CASE 61" in name`, que también coincide con
"CASE 610", "CASE 611", etc. y podía cerrar/vincular el caso equivocado.
"""

import re
from typing import Any, Dict, List, Optional


def case_matches_cortex_id(case: Dict[str, Any], cortex_case_id: Any) -> bool:
    """
    True solo si el caso de Stellar corresponde EXACTAMENTE al Case ID de Cortex.
    Usa borde de palabra para que 'CASE 61' no coincida con 'CASE 610', y acepta
    también el tag 'Case-<id>' que pone este script al crear el caso.
    """
    cid = re.escape(str(cortex_case_id).strip())
    if not cid:
        return False
    tags = [str(t).strip().lower() for t in (case.get("tags") or [])]
    if f"case-{str(cortex_case_id).strip().lower()}" in tags:
        return True
    name = str(case.get("name") or "")
    if re.search(rf"\bCASE[ _#]?{cid}(?!\d)", name, re.IGNORECASE):
        return True
    # Formato alternativo usado en algunos nombres: "... #61"
    return re.search(rf"(?<![\w#])#{cid}(?!\d)", name) is not None


def alert_in_month(alert: Dict[str, Any], month: str) -> bool:
    """True si el timestamp de la alerta (ISO o epoch en s/ms) cae en el mes 'YYYY-MM'."""
    ts = alert.get("timestamp")
    if ts is None or ts == "":
        return False
    if isinstance(ts, (int, float)) or (isinstance(ts, str) and ts.strip().isdigit()):
        from datetime import datetime, timezone
        val = float(ts)
        if val > 1e11:  # milisegundos
            val /= 1000.0
        try:
            return datetime.fromtimestamp(val, tz=timezone.utc).strftime("%Y-%m") == month
        except (OverflowError, OSError, ValueError):
            return False
    return str(ts).startswith(month)


def find_case_for_cortex_id(cases: List[Dict[str, Any]], cortex_case_id: Any) -> Optional[Dict[str, Any]]:
    """Devuelve el caso que coincide exactamente con el Case ID de Cortex, o None."""
    return next((c for c in cases if case_matches_cortex_id(c, cortex_case_id)), None)
