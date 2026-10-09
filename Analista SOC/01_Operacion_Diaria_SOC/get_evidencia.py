import json
import urllib3
import requests
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SO_IP = "172.17.10.25"
API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

# Buscamos la ventana exacta del Paciente Cero (17:56:45 a 17:56:55 PY ayer)
payload = {
    "size": 10,
    "sort": [{"@timestamp": {"order": "asc"}}],
    "query": {
        "bool": {
            "must": [
                {"query_string": {"query": "message:\"172.17.10.124\" AND (message:\"208.67.222.222\" OR message:\"146.112.61.104\")"}}
            ],
            "filter": [
                {"range": {"@timestamp": {"gte": "2026-07-07T20:56:45.000Z", "lt": "2026-07-07T20:56:55.000Z"}}}
            ]
        }
    }
}

print("[*] Descargando JSONs de la secuencia de ataque (DNS -> Sinkhole)...")

try:
    r = requests.post(f"https://{SO_IP}:9200/_search", headers=headers, json=payload, verify=False, timeout=60)
    r.raise_for_status()
    data = r.json()
    hits = data.get("hits", {}).get("hits", [])
    
    # Extraer solo lo relevante para simplificar la lectura del jefe
    evidencia = []
    
    for h in hits:
        source = h.get("_source", {})
        msg = source.get("message", "")
        
        # Parseo basico
        m_time = re.search(r"time=(\S+)", msg)
        m_dst = re.search(r"dstip=(\S+)", msg)
        m_port = re.search(r"dstport=(\S+)", msg)
        
        hora = m_time.group(1) if m_time else "N/A"
        dst = m_dst.group(1) if m_dst else "N/A"
        port = m_port.group(1) if m_port else "N/A"
        
        # Etiquetar el tipo de paso para el diagrama
        paso = "DESCONOCIDO"
        if port == "53" and dst == "208.67.222.222":
            paso = "Paso 1: Consulta DNS Evasiva a OpenDNS"
        elif port == "80" and dst == "146.112.61.104":
            paso = "Paso 4: Conexion Ciega al Sinkhole HTTP"
            
        evidencia.append({
            "Paso_del_Diagrama": paso,
            "Hora_Local": hora,
            "Raw_Log": msg
        })

    with open("evidencia_secuencia_ataque.json", "w", encoding="utf-8") as f:
        json.dump(evidencia, f, indent=4)
        
    print(f"[*] Guardados {len(evidencia)} logs clave en 'evidencia_secuencia_ataque.json'")
    
except Exception as e:
    print(f"[-] Error: {e}")
