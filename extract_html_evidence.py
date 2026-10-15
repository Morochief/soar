import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_html_proton_evidence():
    path = r"c:\Users\kevinmoraes\Documents\soc-env\Dashboard_Timeline_ProtonDrive_FMORA.html"
    if not os.path.exists(path):
        print("No existe html")
        return
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Search for xql queries or evidence sections
    print("=== SECCIONES EN HTML ===")
    matches = re.findall(r"<h[1-4][^>]*>(.*?)</h[1-4]>", content)
    for m in matches:
        print(f"  Header: {m}")

    print("\n=== CONSULTAS XQL O PROTON EN HTML ===")
    xqls = re.findall(r"dataset\s*=.*?(?=</pre>|</div>|\n\n)", content, re.DOTALL)
    for x in xqls:
        print("--- XQL ---")
        print(x.strip())

if __name__ == "__main__":
    check_html_proton_evidence()
