import json
import urllib3
import requests

# Desactivar advertencias de certificados autofirmados (típico en Security Onion)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración de Security Onion
SO_IP = "172.17.10.25"
API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

# Cabeceras de autenticación para Elasticsearch
headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

# Query de Elastic: Buscar cualquier evento (limit 1) relacionado a la IP
payload = {
    "size": 1,
    "sort": [
        {"@timestamp": {"order": "desc"}}
    ],
    "query": {
        "query_string": {
            "query": "\"192.168.169.16\""
        }
    }
}

print(f"Conectando al motor Elasticsearch de Security Onion en {SO_IP}...")

try:
    url_directa = f"https://{SO_IP}:9200/_search"
    response = requests.post(url_directa, headers=headers, json=payload, verify=False, timeout=10)

    # Si devuelve error HTTP, lanzará excepción acá
    response.raise_for_status()
    
    # Tratamos de decodificar el JSON real
    data = response.json()
    
    hits = data.get("hits", {}).get("hits", [])
    print(f"Conexion exitosa! Se extrajeron {len(hits)} eventos de tu SIEM.")
    
    # Guardamos los resultados
    output_file = "so_alertas.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print(f"Eventos guardados crudos en '{output_file}'.")

except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")
    if response.status_code == 401:
        print("Problema de permisos: La API Key fue rechazada.")
    elif response.status_code == 403:
        print("Problema de permisos: La API Key no tiene permisos de lectura.")
except Exception as e:
    print(f"Error de conexion general: {e}")
