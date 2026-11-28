# -*- coding: utf-8 -*-
"""
Conversor Universal de JSON a Reporte HTML para n8n Threat Intelligence.
Toma el archivo JSON descargado de n8n, extrae su propiedad "html"
(o genera el reporte visual) y lo abre directamente en el navegador sin ningún puerto.
"""
import sys
import json
import webbrowser
from pathlib import Path

# Agregar directorio de la app para importar generador si hace falta
APP_DIR = Path(__file__).resolve().parent / "cti_dominios_app"
if not APP_DIR.exists():
    APP_DIR = Path(__file__).resolve().parent

if APP_DIR.exists():
    sys.path.insert(0, str(APP_DIR))
    try:
        from html_report import generar_html_estatico
    except ImportError:
        generar_html_estatico = None
else:
    generar_html_estatico = None

def convertir_json_a_html(ruta_json):
    p_json = Path(ruta_json).resolve()
    if not p_json.is_file():
        print(f"[-] Error: El archivo no existe o es un directorio: {p_json}")
        return None

    try:
        data = json.loads(p_json.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[-] Error al leer JSON: {e}")
        return None

    # En n8n, la salida suele ser una lista [{json: ...}] o un objeto directo
    item = data[0] if isinstance(data, list) and len(data) > 0 else data

    html_content = None
    if isinstance(item, dict) and "html" in item and item["html"] and "SOC Threat Intelligence Suite" in item["html"]:
        html_content = item["html"]
        print("[+] Propiedad 'html' (Suite Completa) encontrada en el JSON de n8n.")
    elif generar_html_estatico and isinstance(item, dict) and "dominios" in item:
        print("[*] Generando Suite Dossier HTML a partir de los hallazgos del JSON...")
        html_content = generar_html_estatico(item)
    elif isinstance(item, dict) and "html" in item and item["html"]:
        html_content = item["html"]
        print("[+] Propiedad 'html' encontrada en el JSON.")
    else:
        print("[-] El archivo JSON no contiene la propiedad 'html' ni estructura válida.")
        return None

    # Guardar archivo .html con el mismo nombre en la misma carpeta
    p_html = p_json.with_suffix(".html")
    p_html.write_text(html_content, encoding="utf-8")
    print(f"[+] Archivo HTML generado exitosamente:\n    {p_html}")

    # Abrir en el navegador local (file:///)
    webbrowser.open(p_html.as_uri())
    return p_html

def main():
    arg = sys.argv[1].strip() if len(sys.argv) > 1 else ""
    if arg and Path(arg).is_file():
        ruta = Path(arg)
    else:
        # Buscar el JSON más reciente en carpetas típicas de descargas y proyectos
        directorios = [
            Path.cwd(),
            Path(__file__).resolve().parent,
            Path(__file__).resolve().parent / "cti_dominios_app",
            Path(__file__).resolve().parent.parent / "cti_dominios_app",
            Path.home() / "Downloads",
        ]
        candidatos = []
        for d in directorios:
            if d.exists() and d.is_dir():
                candidatos.extend(list(d.glob("ti_dominios_*.json")))
        
        if candidatos:
            # Ordenar por fecha de modificación más reciente
            candidatos.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            ruta = candidatos[0]
            print(f"[*] Tomando el JSON más reciente encontrado ({ruta.name}):\n    {ruta}")
        else:
            print("[-] No se encontró ningún archivo ti_dominios_*.json.")
            print("    Arrastra un archivo sobre convertir_json_a_html.bat")
            input("\nPresiona Enter para salir...")
            return

    convertir_json_a_html(ruta)

if __name__ == "__main__":
    main()
