import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def inspect_hm_worker():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    m = re.search(r"class HealthMailboxAutoRemediatorWorker\(.*?\):.*?(?=class |\Z)", content, re.DOTALL)
    if m:
        lines = m.group(0).splitlines()
        for idx, line in enumerate(lines):
            print(f"{idx+1}: {line}")

if __name__ == "__main__":
    inspect_hm_worker()
