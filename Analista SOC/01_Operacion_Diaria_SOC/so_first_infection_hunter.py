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

# Ordenamos ASCENDENTE (del más viejo al más nuevo) y pedimos solo 1 resultado
payload = {
    "size": 1,
    "sort": [{"@timestamp": {"order": "asc"}}],
    "query": {
        "query_string": {
            "query": "message:\"172.17.10.124\" AND message:\"146.112.61.104\""
        }
    }
}

print("[*] Buscando la PRIMERA conexión histórica registrada al C2 (Sinkhole)...")

try:
    r = requests.post(f"https://{SO_IP}:9200/_search", headers=headers, json=payload, verify=False, timeout=60)
    r.raise_for_status()
    data = r.json()
    hits = data.get("hits", {}).get("hits", [])
    total = data.get("hits", {}).get("total", {}).get("value", 0)
    
    if hits:
        first_hit = hits[0]
        msg = first_hit.get("_source", {}).get("message", "")
        ts = first_hit.get("_source", {}).get("@timestamp", "")
        
        m_date = re.search(r"date=(\S+)", msg)
        m_time = re.search(r"time=(\S+)", msg)
        m_dst = re.search(r"dstip=(\S+)", msg)
        m_port = re.search(r"dstport=(\S+)", msg)
        
        fecha = m_date.group(1) if m_date else ""
        hora = m_time.group(1) if m_time else ""
        dst = m_dst.group(1) if m_dst else "?"
        port = m_port.group(1) if m_port else "?"
        
        print(f"[*] Total histórico de conexiones bloqueadas: {total}")
        print(f"[*] ¡PACIENTE CERO ENCONTRADO!")
        print(f"    Fecha exacta (PY): {fecha}")
        print(f"    Hora exacta (PY) : {hora}")
        print(f"    Destino          : {dst}:{port}")
        print(f"    Timestamp UTC    : {ts}")
    else:
        print("[-] No se encontraron registros.")
        
except Exception as e:
    print(f"[-] Error: {e}")
