import sys
import json
sys.path.append('soar/tools_so3')
from so3_client import SO3Client

es_pass = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"

with SO3Client() as so:
    print("=== 1. DIAGNÓSTICO PROFUNDO DE SWAP ===")
    out_swap, _ = so.sudo("free -h && swapon --show")
    print(out_swap)
    print("\n--- TOP 10 PROCESOS CONSUMIENDO SWAP ---")
    cmd_top_swap = """for file in /proc/[0-9]*/status; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file 2>/dev/null; done | grep kB | sort -k 2 -n -r | head -15"""
    out_proc_swap, _ = so.sudo(cmd_top_swap)
    print(out_proc_swap)
    print("\n--- VM.SWAPPINESS ACTUAL ---")
    out_swp, _ = so.sudo("sysctl vm.swappiness")
    print(out_swp)

    print("\n=== 2. AUDITORÍA DE ERRORES EN ELASTALERT ===")
    out_ea_err, _ = so.sudo(f"curl -k -s -u 'so_elastic:{es_pass}' 'https://127.0.0.1:9200/elastalert_error/_search?size=5&sort=@timestamp:desc'")
    try:
        data_ea = json.loads(out_ea_err)
        total_ea_err = data_ea.get('hits', {}).get('total', {}).get('value')
        print(f"Total errores históricos en elastalert_error: {total_ea_err}")
        print("Últimos errores registrados:")
        for h in data_ea.get('hits', {}).get('hits', []):
            s = h['_source']
            print(f"  [{s.get('@timestamp')}] {s.get('message', '')[:160]}")
    except Exception as e:
        print(e)
    
    print("\n--- ERRORES EN LOGS DE DOCKER SO-ELASTALERT (ÚLTIMAS 2 HORAS) ---")
    out_ea_docker, _ = so.sudo("docker logs --since 2h so-elastalert 2>&1 | grep -iE 'error|exception|traceback' | tail -10")
    print(out_ea_docker if out_ea_docker.strip() else "Cero errores/excepciones en el contenedor.")

    print("\n=== 3. AUDITORÍA DEL CRON DAILY / ROTATE DE SECURITY ONION ===")
    out_crons, _ = so.sudo("cat /etc/cron.d/so* /var/spool/cron/* 2>/dev/null")
    print(out_crons[:800])
