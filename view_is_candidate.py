import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def view_is_candidate():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    for idx in range(5140, 5210):
        if idx < len(lines):
            print(f"{idx+1}: {lines[idx].rstrip()}")

if __name__ == "__main__":
    view_is_candidate()
