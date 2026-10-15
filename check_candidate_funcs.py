import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_candidates_definitions():
    path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\command_center.py"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    funcs = ["_is_healthmailbox_candidate", "_is_sophos_translate_candidate", "_is_sati_vpn_candidate", "_is_dpapi_storage_candidate"]
    for fn in funcs:
        m = re.search(rf"def {fn}\(self, case.*?\):.*?(?=\n    def |\nclass |\Z)", content, re.DOTALL)
        if m:
            print(f"=== {fn} ===")
            print(m.group(0))
            print("\n")
        else:
            print(f"[!] {fn} NO encontrada!")

if __name__ == "__main__":
    check_candidates_definitions()
