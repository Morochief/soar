#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejecutor CLI por lotes del flujo de Threat Intelligence de Dominios.
Delega en core_engine y html_report (mismo motor y suite HTML de 7 paneles que la GUI).

Uso:
  python ejecutar_analisis.py "Banco Central del Paraguay" "Technoma" "pechugon.com.py"
  python ejecutar_analisis.py --file lista_entidades.txt --open
"""
import argparse
import json
import re
import sys
import time
import webbrowser
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "cti_dominios_app"
sys.path.insert(0, str(APP_DIR))

from core_engine import ejecutar_pipeline
from html_report import generar_html_estatico


def main():
    parser = argparse.ArgumentParser(description="SOC Threat Intelligence Suite · Ejecutor CLI por Lotes")
    parser.add_argument("objetivos", nargs="*", help="Nombres de empresas o dominios directos a analizar")
    parser.add_argument("-f", "--file", help="Ruta a un archivo .txt/.csv con una entidad o dominio por línea")
    parser.add_argument("-o", "--out", help="Prefijo/ruta base de salida (sin extensión) para guardar .json y .html")
    parser.add_argument("--open", action="store_true", help="Abrir el Dossier HTML generado en el navegador")
    args = parser.parse_args()

    objetivos = list(args.objetivos)
    if args.file:
        p_file = Path(args.file)
        if not p_file.is_file():
            print(f"[-] No existe el archivo: {p_file}")
            sys.exit(1)
        contenido = p_file.read_text(encoding="utf-8", errors="ignore")
        objetivos.extend([x.strip() for x in re.split(r"[\r\n,;]+", contenido) if x.strip()])

    if not objetivos:
        objetivos = ["Banco Central del Paraguay", "Technoma"]

    print("=" * 72)
    print("   SOC THREAT INTELLIGENCE SUITE · ANÁLISIS POR LOTES")
    print("=" * 72)
    print(f"Entidades/Dominios ({len(objetivos)}): {objetivos}\n")

    reporte = ejecutar_pipeline(objetivos, log_cb=lambda m: print(m))

    print("\n" + "=" * 72)
    print("                    RESUMEN EJECUTIVO FINAL")
    print("=" * 72)
    for r in reporte["dominios"]:
        print(f"\n• Dominio: {r['dominio']} (de '{r['nombre_origen']}')")
        print(f"  Score de Riesgo : {r['score']}/100 [{r['nivel']}]")
        print(f"  IPs asociadas   : {', '.join(r['ips'])}")
        print(f"  Certificados ISO: {', '.join(r['certificados_iso']) if r['certificados_iso'] else 'Ninguno declarado'}")
        for d in r["desglose"]:
            signo = f"+{d['puntos']}" if d["puntos"] > 0 else str(d["puntos"])
            print(f"    {signo:>4} pts | {d['fuente'].upper():<10} | {d.get('consulta', '-'):<22} | {d['evidencia']}")

    if reporte["sin_dominio"]:
        print("\n• Entidades sin dominio (Registradas sin detener el flujo):")
        for s in reporte["sin_dominio"]:
            print(f"  - {s['nombre']}: {s['motivo']}")

    ts = time.strftime("%Y%m%d_%H%M%S")
    base_out = Path(args.out) if args.out else (Path(__file__).resolve().parent / f"ti_dominios_{ts}")
    json_path = base_out.with_suffix(".json")
    html_path = base_out.with_suffix(".html")

    json_path.write_text(json.dumps(reporte, indent=2, ensure_ascii=False), encoding="utf-8")
    generar_html_estatico(reporte, str(html_path))

    print("\n" + "=" * 72)
    print(f"[+] JSON guardado en: {json_path}")
    print(f"[+] HTML Suite en   : {html_path}")
    print("=" * 72)

    if args.open:
        webbrowser.open(html_path.as_uri())


if __name__ == "__main__":
    main()
