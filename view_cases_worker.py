import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def view_cases_worker():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    start_idx = -1
    for i, l in enumerate(lines):
        if "class CasesWorker" in l:
            start_idx = i
            break
            
    if start_idx != -1:
        print(f"[*] CasesWorker starts at line {start_idx+1}:")
        for j in range(start_idx, min(start_idx + 120, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")

if __name__ == "__main__":
    view_cases_worker()
