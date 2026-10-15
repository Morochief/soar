import os
import sys
import re
import datetime
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_process_details():
    cmd = 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -eq 30144 -or $_.CommandLine -like \'*command_center.py*\' } | Select-Object ProcessId, CreationDate, CommandLine | Format-List"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors='replace')
    print("=== PROCESO EN EJECUCIÓN ===")
    print(res.stdout)

def inspect_worker_source(file_path):
    print(f"=== INSPECCIONANDO WORKERS EN {file_path} ===")
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Find CasesWorker run method or query
    cw_match = re.search(r"class CasesWorker\(.*?\):.*?(?=class |\Z)", content, re.DOTALL)
    if cw_match:
        cw_code = cw_match.group(0)
        # extract urls and params
        urls = re.findall(r"url\s*=.*|requests\.[a-z]+\(.*?\)", cw_code)
        print("[*] CasesWorker URL/Requests:")
        for u in urls[:5]:
            print(f"  {u.strip()}")
            
    # Find DPAPIStorageAutoRemediatorWorker
    dp_match = re.search(r"class DPAPIStorageAutoRemediatorWorker\(.*?\):.*?(?=class |\Z)", content, re.DOTALL)
    if dp_match:
        print("\n[*] DPAPIStorageAutoRemediatorWorker encontrado (primeras 40 lineas):")
        dp_lines = dp_match.group(0).splitlines()[:45]
        for l in dp_lines:
            print("  " + l)
            
    # Find how auto-remediators are triggered or started in MainWindow
    starts = re.findall(r"self\.[a-zA-Z0-9_]*auto[a-zA-Z0-9_]*\.start\(.*?\)|self\.[a-zA-Z0-9_]*dpapi[a-zA-Z0-9_]*", content, re.IGNORECASE)
    print("\n[*] Referencias a auto-remediators en MainWindow:")
    for s in set(starts):
        print(f"  {s}")

if __name__ == "__main__":
    check_process_details()
    inspect_worker_source(r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py")
