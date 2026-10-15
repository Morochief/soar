import os
import sys

def read_bitacora_end():
    path = r"c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Bitacora_Personal_Casos_SOC.md"
    if not os.path.exists(path):
        print("No existe bitacora")
        return
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    print(f"Total lineas: {len(lines)}")
    print("Ultimas 60 lineas:")
    for l in lines[-60:]:
        print(l.rstrip())

if __name__ == "__main__":
    read_bitacora_end()
