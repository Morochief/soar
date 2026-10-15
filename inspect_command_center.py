import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def inspect_workers(target_file):
    print(f"[*] Analizando {target_file} ...")
    if not os.path.exists(target_file):
        print(f"[!] No existe: {target_file}")
        return

    with open(target_file, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Find all class definitions
    classes = re.findall(r"class\s+([A-Za-z0-9_]+)\s*\(([^)]*)\):", content)
    print(f"[+] Total clases encontradas: {len(classes)}")
    workers = [c for c in classes if "Worker" in c[0] or "Remediat" in c[0] or "Auto" in c[0]]
    for w in workers:
        print(f"  - Clase: {w[0]} ({w[1]})")

    # Search for DPAPIStorageAutoRemediatorWorker specifically
    if "DPAPIStorageAutoRemediatorWorker" in content:
        print("[+] 'DPAPIStorageAutoRemediatorWorker' ESTÁ presente en el código.")
    else:
        print("[-] 'DPAPIStorageAutoRemediatorWorker' NO está en el código.")

    # Search for how cases are queried from Stellar API in the file
    api_calls = re.findall(r"https?://[^\s\"']+|/connect/api/[^\s\"']+", content)
    unique_endpoints = sorted(list(set(api_calls)))
    print(f"\n[+] Endpoints API encontrados ({len(unique_endpoints)}):")
    for ep in unique_endpoints:
        if "connect" in ep or "case" in ep or "alert" in ep:
            print(f"  - {ep}")

    # Check menu items for SOAR
    menu_matches = re.findall(r"SOAR:\s*[^\"'\n]+", content)
    print(f"\n[+] Referencias a menu SOAR:")
    for m in menu_matches[:5]:
        print(f"  - {m}")

def main():
    paths = [
        r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py",
        r"c:\Users\kevinmoraes\Documents\soc-env\command_center.py"
    ]
    for p in paths:
        print("="*60)
        inspect_workers(p)

if __name__ == "__main__":
    main()
