import sys
import json
sys.path.append('soar/tools_so3')
from so3_client import SO3Client

es_pass = "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"

with SO3Client() as so:
    print("=== TOP REGLAS QUE GENERAN ERROR EN ELASTALERT EN LOS ÚLTIMOS 15 MINUTOS ===")
    query = {
        "query": {
            "range": {
                "@timestamp": {"gte": "now-15m"}
            }
        },
        "aggs": {
            "top_failing_rules": {
                "terms": {
                    "field": "data.rule_name.keyword",
                    "size": 15
                }
            }
        },
        "size": 2
    }
    so.write_file('/tmp/q_ea_rules.json', json.dumps(query))
    out, _ = so.sudo(f"curl -k -s -u 'so_elastic:{es_pass}' -H 'Content-Type: application/json' -X POST 'https://127.0.0.1:9200/elastalert_error/_search' -d @/tmp/q_ea_rules.json")
    so.sudo("rm -f /tmp/q_ea_rules.json")
    try:
        data = json.loads(out)
        hits = data.get('hits', {}).get('total', {}).get('value')
        print(f"Total errores en últimos 15 min: {hits}")
        for b in data.get('aggregations', {}).get('top_failing_rules', {}).get('buckets', []):
            print(f"  [{b['doc_count']} fallos] {b['key']}")
        print("\nEjemplo de error completo:")
        for h in data.get('hits', {}).get('hits', []):
            print(h['_source'].get('message'))
    except Exception as e:
        print(e)

    print("\n=== TOP CONTENEDORES CONSUMIENDO RAM Y SWAP (docker stats snapshot) ===")
    out_docker, _ = so.sudo("docker stats --no-stream --format 'table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.CPUPerc}}'")
    print(out_docker)
