import os
import sys

def check_report():
    p = r"c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Reportes\Reporte_Consolidado_Cortex_XDR_Technoma.md"
    if not os.path.exists(p):
        print("No existe reporte")
        return
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    for idx, l in enumerate(lines[:120]):
        print(f"{idx+1}: {l.rstrip()}")

if __name__ == "__main__":
    check_report()
