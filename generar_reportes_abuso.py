#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
GENERADOR AUTOMÁTICO DE REPORTES DE ABUSO / ESCANEO (SOC TECHNOMA)
=============================================================================
Analiza volcados JSON de Stellar Cyber / Interflow y genera los correos
de notificación formal por cada IP única detectada, listos para enviar.
=============================================================================
"""

import sys
import json
import re
from pathlib import Path

def extraer_log_limpio(raw_msg: str) -> str:
    """Extrae desde 'srcip=' en adelante del syslog crudo del FortiGate."""
    match = re.search(r'(srcip=.*)$', raw_msg)
    if match:
        return match.group(1).strip()
    return raw_msg.strip()

from abuse_report_dialog import AbuseReportEngine

def procesar_interflow_json(ruta_json: str):
    ruta = Path(ruta_json)
    if not ruta.exists():
        print(f"[!] Error: No se encuentra el archivo {ruta}")
        return []

    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

    return AbuseReportEngine.parse_payload(contenido)

if __name__ == "__main__":
    archivo = sys.argv[1] if len(sys.argv) > 1 else r"Analista SOC\interflow (1).json"
    reportes = procesar_interflow_json(archivo)
    print(f"[*] Total de IPs únicas procesadas: {len(reportes)}\n")
    for idx, rep in enumerate(reportes, 1):
        print(f"==================================================")
        print(f"CORREO #{idx} | IP: {rep['ip']} | Entidad: {rep['org']} | Intentos: {rep['hits']}")
        print(f"Incidente: {rep['tipo_label']} | Servicio Afectado: {rep['servicio']}")
        print(f"Destinatario (To): {rep['abuse_email']}")
        print(f"--------------------------------------------------")
        print(f"Asunto Oficial (Playbook): {rep['asunto_es']}")
        print(f"Asunto Internacional:     {rep['asunto_en']}\n")
        print(f"{rep['cuerpo']}\n")

