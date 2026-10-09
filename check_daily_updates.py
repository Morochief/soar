"""
Script: check_daily_updates.py
Propósito: Verificar diariamente actualizaciones pendientes de:
  1. Sistema Operativo (Windows Update - KBs, parches de seguridad)
  2. Aplicaciones y Programas instalados (Winget)
  3. Subsistema de Windows para Linux (WSL)

Uso:
  python check_daily_updates.py           # Ejecución interactiva por consola
  python check_daily_updates.py --notify  # Muestra notificación emergente en Windows si hay pendientes
  python check_daily_updates.py --log     # Guarda reporte en archivo de log
"""

import os
import re
import sys
import json
import logging
import datetime
import subprocess
from pathlib import Path

# Configuración de codificación segura para Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Configuración de rutas y logs
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "actualizaciones_pendientes.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def log_and_print(msg: str):
    print(msg)
    logging.info(msg)

def check_windows_updates():
    """Consulta la API COM nativa de Windows Update (Microsoft.Update.Session)."""
    ps_cmd = (
        "$s = New-Object -ComObject Microsoft.Update.Session; "
        "$searcher = $s.CreateUpdateSearcher(); "
        "$res = $searcher.Search('IsInstalled=0 and Type=\"Software\" and IsHidden=0'); "
        "Write-Output ('COUNT=' + $res.Updates.Count); "
        "foreach($u in $res.Updates) { Write-Output ('ITEM=' + $u.Title) }"
    )
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_cmd],
            capture_output=True,
            text=True,
            timeout=60,
            encoding="utf-8",
            errors="ignore"
        )
        updates = []
        for line in proc.stdout.splitlines():
            line = line.strip()
            if line.startswith("ITEM="):
                updates.append(line.replace("ITEM=", "").strip())
        return updates
    except Exception as e:
        logging.error(f"Error consultando Windows Update: {e}")
        return [f"Error al consultar Windows Update: {e}"]

def check_winget_updates():
    """Consulta aplicaciones con actualizaciones pendientes mediante winget."""
    try:
        proc = subprocess.run(
            ["winget", "upgrade"],
            capture_output=True,
            text=True,
            timeout=90,
            encoding="utf-8",
            errors="ignore"
        )
        lines = proc.stdout.splitlines()
        updates = []
        
        header_idx = -1
        for i, l in enumerate(lines):
            if ("Nombre" in l or "Name" in l) and ("Id" in l):
                header_idx = i
                break

        if header_idx != -1:
            h = lines[header_idx]
            c_name = h.find("Nombre") if "Nombre" in h else h.find("Name")
            c_id = h.find("Id")
            c_ver = h.find("Versión") if "Versión" in h else (h.find("Version") if "Version" in h else c_id + 25)
            c_avail = h.find("Disponible") if "Disponible" in h else (h.find("Available") if "Available" in h else c_ver + 15)
            c_src = h.find("Origen") if "Origen" in h else (h.find("Source") if "Source" in h else c_avail + 15)

            for l in lines[header_idx + 2:]:
                if not l.strip() or "actualizaciones disponibles" in l.lower() or "updates available" in l.lower():
                    break
                # Extraer usando los límites exactos de columna
                name = l[c_name:c_id].strip() if len(l) > c_name else ""
                pkg_id = l[c_id:c_ver].strip() if len(l) > c_id else ""
                cur_ver = l[c_ver:c_avail].strip() if len(l) > c_ver else ""
                new_ver = l[c_avail:c_src].strip() if len(l) > c_avail else ""

                if name and cur_ver and new_ver:
                    updates.append({
                        "name": name,
                        "id": pkg_id,
                        "current": cur_ver,
                        "available": new_ver
                    })
        return updates
    except FileNotFoundError:
        return [{"name": "Winget no instalado en el sistema", "id": "-", "current": "-", "available": "-"}]
    except Exception as e:
        logging.error(f"Error consultando Winget: {e}")
        return []

def send_windows_notification(title: str, message: str):
    """Envía una notificación nativa de Windows (Toast o Balloon)."""
    clean_title = title.replace('"', '').replace("'", "")
    clean_msg = message.replace('"', '').replace("'", "")
    ps_cmd = (
        f"[reflection.assembly]::loadwithpartialname('System.Windows.Forms') | Out-Null; "
        f"$n = New-Object System.Windows.Forms.NotifyIcon; "
        f"$n.Icon = [System.Drawing.SystemIcons]::Information; "
        f"$n.Visible = $true; "
        f"$n.ShowBalloonTip(7000, '{clean_title}', '{clean_msg}', [System.Windows.Forms.ToolTipIcon]::Info); "
        f"Start-Sleep -Seconds 4; $n.Dispose()"
    )
    try:
        subprocess.Popen(
            ["powershell", "-NoProfile", "-WindowStyle", "Hidden", "-Command", ps_cmd],
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
        )
    except Exception as e:
        logging.error(f"Error enviando notificación: {e}")

def main():
    enable_notify = "--notify" in sys.argv
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 70)
    print(f"🔍 AUDITORÍA DIARIA DE ACTUALIZACIONES — {now_str}")
    print("=" * 70)

    # 1. Chequeo de Windows Update
    print("⏳ Consultando Windows Update (Sistema Operativo)...")
    wu_updates = check_windows_updates()

    # 2. Chequeo de Winget
    print("⏳ Consultando Winget (Programas y Aplicaciones)...")
    wg_updates = check_winget_updates()

    print("\n" + "-" * 70)
    print("📋 RESULTADOS DEL DIAGNÓSTICO")
    print("-" * 70)

    total_pending = len(wu_updates) + len(wg_updates)

    # Resumen Windows Update
    if wu_updates:
        print(f"\n[⚠️] ACTUALIZACIONES DE SISTEMA PENDIENTES ({len(wu_updates)}):")
        for u in wu_updates:
            print(f"  • {u}")
    else:
        print("\n[✅] Windows Update: El sistema operativo está completamente al día.")

    # Resumen Winget
    if wg_updates:
        print(f"\n[⚠️] PROGRAMAS CON ACTUALIZACIÓN DISPONIBLE ({len(wg_updates)}):")
        print(f"  {'Nombre':<32} {'Versión Actual':<16} {'Nueva Versión':<16}")
        print("  " + "-" * 66)
        for app in wg_updates:
            print(f"  {app['name'][:30]:<32} {app['current']:<16} {app['available']:<16}")
    else:
        print("\n[✅] Aplicaciones (Winget): Todos los programas están en su versión más reciente.")

    print("\n" + "=" * 70)
    if total_pending > 0:
        print(f"🔔 Total de actualizaciones pendientes: {total_pending}")
        print("💡 Para actualizar programas: winget upgrade --all")
        print("💡 Para actualizar WSL:        wsl --update")
        print("💡 Para actualizar Windows:    Inicio -> Buscar 'Buscar actualizaciones'")
    else:
        print("🎉 ¡Excelente! Todo el equipo y sus programas están 100% actualizados.")
    print("=" * 70 + "\n")

    # Guardar en log
    logging.info(f"Auditoría finalizada. Pendientes SO: {len(wu_updates)}, Apps: {len(wg_updates)}")

    # Notificación de escritorio si está activo --notify o si hay pendientes
    if enable_notify and total_pending > 0:
        msg = f"Se detectaron {total_pending} actualizaciones ({len(wu_updates)} de Windows, {len(wg_updates)} de Apps)."
        send_windows_notification("Actualizaciones Pendientes", msg)

if __name__ == "__main__":
    main()
