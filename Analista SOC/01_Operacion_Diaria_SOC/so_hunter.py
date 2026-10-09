import argparse
import json
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración
SO_IP = "172.17.10.25"
API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

def hunt(query_str, limit=5):
    headers = {
        "Authorization": f"ApiKey {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "size": limit,
        "sort": [{"@timestamp": {"order": "desc"}}],
        "query": {
            "query_string": {
                "query": query_str
            }
        }
    }

    print(f"[*] Ejecutando cacería en Security Onion -> Query: {query_str}")
    
    try:
        url = f"https://{SO_IP}:9200/_search"
        response = requests.post(url, headers=headers, json=payload, verify=False, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        hits = data.get("hits", {}).get("hits", [])
        
        print(f"[+] ¡Éxito! Se encontraron {len(hits)} resultados.")
        
        output_file = "so_hunt_results.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            
        print(f"[*] Resultados guardados en {output_file}. Dile a Antigravity que los analice.")
        
    except Exception as e:
        print(f"[-] Error en la cacería: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramienta CLI de Threat Hunting para Security Onion")
    parser.add_argument("--ip", help="Buscar por Dirección IP (ej: 192.168.1.10)")
    parser.add_argument("--mac", help="Buscar por Dirección MAC (ej: 00:11:22:33:44:55)")
    parser.add_argument("--user", help="Buscar por Nombre de Usuario (ej: egamarra)")
    parser.add_argument("--host", help="Buscar por Nombre de Equipo (ej: NB-NOC1)")
    parser.add_argument("--hash", help="Buscar por Hash de archivo (MD5/SHA256)")
    parser.add_argument("--query", help="Búsqueda avanzada usando sintaxis raw de Kibana/Lucene")
    parser.add_argument("--limit", type=int, default=5, help="Cantidad máxima de eventos a traer (default: 5)")
    
    args = parser.parse_args()
    
    if args.query:
        query_string = args.query
    else:
        query_parts = []
        if args.ip:
            query_parts.append(f"\"{args.ip}\"")
        if args.mac:
            query_parts.append(f"\"{args.mac}\"")
        if args.user:
            query_parts.append(f"*{args.user}*")
        if args.host:
            query_parts.append(f"\"{args.host}\"")
        if args.hash:
            query_parts.append(f"\"{args.hash}\"")
            
        if not query_parts:
            print("[-] Error: Debes proveer al menos un parámetro (--ip, --mac, --query, etc)")
            exit(1)
            
        query_string = " AND ".join(query_parts)
        
    hunt(query_string, args.limit)
