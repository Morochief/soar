#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open("auditoria_cuota_stellar/caso_17813_detail.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

data = raw.get("data", {})
details = data.get("details", {})
alerts = data.get("alerts", [])
observables = data.get("observables", {})
activity = data.get("activity", [])
scores = data.get("scores", [])

print("=== DETALLES DEL CASO ===")
print(f"Ticket ID: {details.get('ticket_id')}")
print(f"Case ID: {details.get('case_id', details.get('_id'))}")
print(f"Nombre: {details.get('name')}")
print(f"Estado: {details.get('status')}")
print(f"Severidad: {details.get('severity')}")
print(f"Score: {details.get('score')}")
print(f"Tenant: {details.get('tenant_name')} ({details.get('tenant_group_name')})")
print(f"Asignado a: {details.get('assignee_name')}")
print(f"Creado: {details.get('created_at')} por {details.get('created_by_name')}")
print(f"Modificado: {details.get('modified_at')} por {details.get('modified_by_name')}")
print(f"Rango temporal: {details.get('start_timestamp')} -> {details.get('end_timestamp')}")

print(f"\n=== ALERTAS INVOLUCRADAS ({len(alerts)}) ===")
for i, alt in enumerate(alerts, 1):
    src = alt.get("_source", {})
    xdr = src.get("xdr_event", {})
    print(f"\n--- Alerta #{i} ---")
    print(f"Nombre Alerta: {xdr.get('display_name', src.get('event_name'))}")
    print(f"Fase KillChain: {xdr.get('xdr_killchain_stage')} | Técnica: {xdr.get('technique', {}).get('name')}")
    print(f"Descripción: {xdr.get('description')}")
    print(f"Timestamp UTC: {src.get('timestamp_utc', src.get('fortinet', {}).get('event_time'))}")
    print(f"Origen: IP={src.get('srcip')}, Host={src.get('srcip_host')}, MAC={src.get('srcmac')}, User={src.get('fortinet', {}).get('unauthuser')}, DeviceName={src.get('fortinet', {}).get('srcname')}")
    print(f"Destino: IP={src.get('dstip')}, Host={src.get('dstip_host')}, Port={src.get('dstport')}, App={src.get('appid_name')}")
    print(f"Acción FW: {src.get('action')} | Policy: {src.get('fw_policy_id')} (Rule 0 / Deny)")
    print(f"Métricas Anomaly: Actual={src.get('actual')}, Típico={src.get('typical')}")
    print(f"Fidelity: {src.get('fidelity')}% | Severity: {src.get('severity')} | Event Score: {src.get('event_score')}")

print("\n=== ACTIVIDAD RECIENTE ===")
for act in activity:
    print(f"- Acción: {act.get('action')} | Campo: {act.get('field')} | De: '{act.get('from')}' -> A: '{act.get('to')}' | Usuario: {act.get('user')} | TS: {act.get('timestamp')}")

print("\n=== OBSERVABLES ===")
print(json.dumps(observables, indent=2))
