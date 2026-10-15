import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def view_lines():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    for i in range(5110, 5145):
        print(f"{i+1}: {lines[i].rstrip()}")

if __name__ == "__main__":
    view_lines()
