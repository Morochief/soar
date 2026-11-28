import os
import sys
import json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from so3_client import SO3Client

es_pass = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"

with SO3Client() as so:
    print("=== PROBANDO LIMPIEZA DE SWAP (swapoff && swapon) ===")
    out_free_before, _ = so.sudo("free -h")
    print("Antes:\n", out_free_before)
    # Ejecutamos swapoff y swapon para vaciar la swap a la RAM física disponible (hay 5GB de RAM libre)
    # ';' (no '&&'): swapon -a se ejecuta SIEMPRE, aunque swapoff falle a mitad de camino
    out_swap_clean, err_sc = so.sudo("swapoff -a; swapon -a")
    print("Swapoff/swapon resultado:", out_swap_clean, err_sc)
    out_swap_show, _ = so.sudo("swapon --show")
    if not out_swap_show.strip():
        print("⚠️ ATENCIÓN: el nodo quedó SIN swap activa. Ejecutar 'sudo swapon -a' manualmente.")
    out_free_after, _ = so.sudo("free -h")
    print("Después:\n", out_free_after)

    print("\n=== INVESTIGANDO SO-SOC CPU AL 100% ===")
    out_top_soc, _ = so.sudo("docker exec so-soc ps aux 2>/dev/null || ps aux | grep -i soc | head -5")
    print(out_top_soc)
