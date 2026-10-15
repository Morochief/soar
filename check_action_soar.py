import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_action_soar():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    for idx, l in enumerate(lines):
        if "action_soar" in l:
            print(f"{idx+1}: {l.rstrip()}")

if __name__ == "__main__":
    check_action_soar()
