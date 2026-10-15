import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_menu_init():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    m = re.findall(r"check_auto_[a-zA-Z0-9_]+.*", content)
    for l in m:
        print(l.strip())

if __name__ == "__main__":
    check_menu_init()
