import os
import sys

def read_caso_17():
    p = r"c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Bitacora_Personal_Casos_SOC.md"
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    cases = content.split("### Caso ")
    for c in cases[-3:]:
        print("=== CASO ===")
        print(c[:400])

if __name__ == "__main__":
    read_caso_17()
