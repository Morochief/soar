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

# Buscamos eventos de los 15 minutos previos al primer beaconing (03:43:21 PY = 06:43:21 UTC)
payload = {
    "size": 100,
    "sort": [{"@timestamp": {"order": "desc"}}],
    "query": {
        "bool": {
            "must": [
                {"query_string": {"query": "message:\"172.17.10.124\""}},
                {"range": {"@timestamp": {"gte": "2026-07-08T06:25:00.000Z", "lt": "2026-07-08T06:43:20.000Z"}}}
            ]
        }
    }
}

print("[*] Buscando eventos previos a la infeccion (03:25 AM a 03:43 AM PY)...")

try:
    r = requests.post(f"https://{SO_IP}:9200/_search", headers=headers, json=payload, verify=False, timeout=60)
    r.raise_for_status()
    data = r.json()
    hits = data.get("hits", {}).get("hits", [])
    
    print(f"[*] Se encontraron {len(hits)} eventos en esa ventana de tiempo.")
    print("-" * 70)
    
    # Imprimir en orden cronológico (de más antiguo a más nuevo)
    for h in reversed(hits):
        msg = h.get("_source", {}).get("message", "")
        ts = h.get("_source", {}).get("@timestamp", "")
        
        m_time = re.search(r"time=(\S+)", msg)
        m_dst = re.search(r"dstip=(\S+)", msg)
        m_port = re.search(r"dstport=(\S+)", msg)
        m_sent = re.search(r"sentbyte=(\S+)", msg)
        m_rcvd = re.search(r"rcvdbyte=(\S+)", msg)
        
        hora = m_time.group(1) if m_time else ts
        dst = m_dst.group(1) if m_dst else "?"
        port = m_port.group(1) if m_port else "?"
        sent = m_sent.group(1) if m_sent else "0"
        rcvd = m_rcvd.group(1) if m_rcvd else "0"
        
        print(f"{hora} (PY) | Destino: {dst}:{port:<5} | Bytes (Sent/Rcvd): {sent}/{rcvd}")
        
    print("-" * 70)
    
except Exception as e:
    print(f"[-] Error: {e}")
