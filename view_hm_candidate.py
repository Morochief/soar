import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def view_hm_candidate():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    m = re.search(r"def _is_healthmailbox_candidate\(.*?\):.*?(?=\n    def |\Z)", content, re.DOTALL)
    if m:
        print(m.group(0))

if __name__ == "__main__":
    view_hm_candidate()
