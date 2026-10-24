#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — CIERRE MASIVO DE CASOS STELLAR CYBER (close_cases_bulk.py)
=============================================================================
Herramienta oficial para resolver y cerrar casos de manera masiva o individual
en Stellar Cyber utilizando la API REST v1.

Capacidades:
  1. Cerrar casos por lista de IDs de Cortex XDR (ej. --cortex-cases 610,604,601).
  2. Cerrar casos por lista de IDs nativos de Stellar Cyber (ej. --stellar-cases 6ad37e...,6ad37f...).
  3. Cerrar casos por filtro de mes (ej. --month 2026-10).
  4. Asignar resolución formal estandarizada ('Benign', 'False Positive', 'True Positive').
  5. Soporta modo de simulación (--dry-run).

Uso:
  python close_cases_bulk.py --cortex-cases 610,604 --resolution "False Positive" --reason "Actividad benigna verificada"
  python close_cases_bulk.py --month 2026-10 --resolution "Benign" --dry-run
  python close_cases_bulk.py --stellar-cases 6ad2370de4fb8b7307d83193 --resolution "Benign"
=============================================================================
"""

import os
import sys
import json
import argparse
from typing import Any, Dict, List, Optional
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sync_cortex_cases

HOST = sync_cortex_cases.HOST
DEFAULT_TENANT_ID = sync_cortex_cases.DEFAULT_TENANT_ID

VALID_RESOLUTIONS = ["False Positive", "Benign", "True Positive"]


def close_case_by_stellar_id(stellar_case_id: str, resolution: str, reason: Optional[str] = None, dry_run: bool = False) -> bool:
    """Cierra un caso en Stellar Cyber actualizando su estado a 'Resolved' y su resolución."""
    if dry_run:
        print(f"  [DRY-RUN] Se marcaría 'Resolved' con resolución '{resolution}' el Caso Stellar {stellar_case_id}")
        return True
    
    url = f"https://{HOST}/connect/api/v1/cases/{stellar_case_id}"
    headers = sync_cortex_cases.get_headers()
    payload = {
        "status": "Resolved",
        "resolution": resolution
    }
    r = requests.put(url, headers=headers, json=payload, verify=False, timeout=30)
    if r.status_code == 200:
        print(f"  [+] ÉXITO: Caso Stellar {stellar_case_id} cerrado como '{resolution}'.")
        if reason:
            c_url = f"https://{HOST}/connect/api/v1/cases/{stellar_case_id}/comments"
            try:
                requests.post(c_url, headers=headers, json={"comment": reason}, verify=False, timeout=15)
                print(f"  [+] Comentario registrado en caso {stellar_case_id}.")
            except Exception as e:
                print(f"  [-] Error insertando comentario: {e}")
        return True
    else:
        print(f"  [-] ERROR cerrando Caso Stellar {stellar_case_id}: {r.status_code} - {r.text[:200]}")
        return False


def run_bulk_close(
    tenant_id: str,
    resolution: str,
    reason: Optional[str] = None,
    cortex_cases: Optional[List[str]] = None,
    stellar_cases_ids: Optional[List[str]] = None,
    month: Optional[str] = None,
    dry_run: bool = False
):
    if resolution not in VALID_RESOLUTIONS:
        print(f"[-] Resolución '{resolution}' no válida. Opciones permitidas: {VALID_RESOLUTIONS}")
        return

    print("=" * 80)
    print("🛡️ TECHNOMA SOC — EJECUTANDO CIERRE MASIVO DE CASOS")
    print(f"Host: {HOST} | Tenant: {tenant_id} | Resolución: {resolution}")
    print(f"Motivo / Dictamen: {reason or 'No especificado'} | Modo Dry-Run: {dry_run}")
    print("=" * 80)

    stellar_all_cases = sync_cortex_cases.fetch_stellar_cases(tenant_id)
    print(f"[*] Total de casos registrados en Stellar Cyber: {len(stellar_all_cases)}")

    targets_to_close: List[Dict[str, Any]] = []

    # 1. Filtro directo por Stellar Case IDs
    if stellar_cases_ids:
        for scid in stellar_cases_ids:
            clean_id = scid.strip()
            matched = next((c for c in stellar_all_cases if c.get("_id") == clean_id), None)
            if matched:
                targets_to_close.append(matched)
            else:
                # Agregar aunque no esté en los primeros 200 listados
                targets_to_close.append({"_id": clean_id, "name": f"Stellar Case {clean_id}", "ticket_id": "N/A"})

    # 2. Filtro por Cortex Case IDs (ej. 610, 604)
    if cortex_cases:
        for ccid in cortex_cases:
            clean_cid = str(ccid).strip()
            p1 = f"CASE {clean_cid}"
            p2 = f"CASE_{clean_cid}"
            matched = next((c for c in stellar_all_cases if p1 in c.get("name", "").upper() or p2 in c.get("name", "").upper()), None)
            if matched:
                if matched not in targets_to_close:
                    targets_to_close.append(matched)
            else:
                print(f"  [!] Aviso: No se encontró caso en Stellar asociado a Cortex #{clean_cid}")

    # 3. Filtro por mes (ej. 2026-10)
    if month:
        cortex_map = sync_cortex_cases.fetch_cortex_alerts_with_case_id(tenant_id)
        month_cids = []
        for cid, alerts in cortex_map.items():
            if any(month in str(a.get("timestamp", "")) for a in alerts):
                month_cids.append(str(cid))
        print(f"[*] Casos de Cortex identificados en el mes {month}: {month_cids}")
        for clean_cid in month_cids:
            p1 = f"CASE {clean_cid}"
            p2 = f"CASE_{clean_cid}"
            matched = next((c for c in stellar_all_cases if p1 in c.get("name", "").upper() or p2 in c.get("name", "").upper()), None)
            if matched and matched not in targets_to_close:
                targets_to_close.append(matched)

    if not targets_to_close:
        print("[-] No se encontraron casos objetivo que coincidan con los criterios especificados.")
        return

    print(f"\n[+] Total de casos a cerrar: {len(targets_to_close)}")
    success_count = 0

    for c in targets_to_close:
        st_id = c.get("_id")
        t_id = c.get("ticket_id")
        name = c.get("name")
        print(f"\n-> Procesando: {name} (Ticket #{t_id} | ID: {st_id})")
        if close_case_by_stellar_id(st_id, resolution, dry_run=dry_run):
            success_count += 1

    print("\n" + "=" * 80)
    print(f"RESUMEN DE CIERRE MASIVO:")
    print(f"  - Total objetivos: {len(targets_to_close)}")
    print(f"  - Procesados exitosamente: {success_count}")
    print(f"  - Resolución aplicada: {resolution}")
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cierre masivo de casos en Stellar Cyber")
    parser.add_argument("--resolution", type=str, required=True, choices=VALID_RESOLUTIONS, help="Resolución ('False Positive', 'Benign', 'True Positive')")
    parser.add_argument("--reason", type=str, default="", help="Motivo o dictamen del cierre")
    parser.add_argument("--cortex-cases", type=str, default=None, help="Lista separada por comas de Case IDs de Cortex (ej. 610,604,601)")
    parser.add_argument("--stellar-cases", type=str, default=None, help="Lista separada por comas de Object IDs de Stellar Cyber")
    parser.add_argument("--month", type=str, default=None, help="Filtrar casos de Cortex por mes (ej. 2026-10)")
    parser.add_argument("--tenant", type=str, default=DEFAULT_TENANT_ID, help="Tenant ID de Stellar")
    parser.add_argument("--dry-run", action="store_true", help="Simulación sin modificar datos reales")

    args = parser.parse_args()

    c_cases = args.cortex_cases.split(",") if args.cortex_cases else None
    s_cases = args.stellar_cases.split(",") if args.stellar_cases else None

    run_bulk_close(
        tenant_id=args.tenant,
        resolution=args.resolution,
        reason=args.reason,
        cortex_cases=c_cases,
        stellar_cases_ids=s_cases,
        month=args.month,
        dry_run=args.dry_run
    )
