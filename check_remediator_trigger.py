import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_remediator_trigger():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Search for all invocations of HealthMailboxAutoRemediatorWorker
    matches = [m.start() for m in re.finditer(r"HealthMailboxAutoRemediatorWorker\(", content)]
    print(f"[*] Total invocaciones de HealthMailboxAutoRemediatorWorker: {len(matches)}")
    lines = content.splitlines()
    for m in matches:
        # find line number
        char_count = 0
        line_no = 0
        for idx, line in enumerate(lines):
            char_count += len(line) + 1
            if char_count >= m:
                line_no = idx
                break
        print(f"\n--- Invocacion en linea {line_no+1} ---")
        for k in range(max(0, line_no - 15), min(len(lines), line_no + 30)):
            print(f"{k+1}: {lines[k]}")

if __name__ == "__main__":
    check_remediator_trigger()
