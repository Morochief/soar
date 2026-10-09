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

# Buscamos desde las 00:00 AM (PY) hasta las 03:37 AM (PY) para ver qué hacía en la madrugada
# 00:00 PY = 03:00 UTC
# 03:37 PY = 06:37 UTC
payload = {
    "size": 100,
    "sort": [{"@timestamp": {"order": "desc"}}],
    "query": {
        "bool": {
            "must": [
                {"query_string": {"query": "message:\"172.17.10.124\""}},
                {"range": {"@timestamp": {"gte": "2026-07-08T03:00:00.000Z", "lt": "2026-07-08T06:37:00.000Z"}}}
            ]
        }
    }
}

print("[*] Buscando eventos desde la Medianoche (00:00) hasta las 03:37 AM (PY)...")

try:
    r = requests.post(f"https://{SO_IP}:9200/_search", headers=headers, json=payload, verify=False, timeout=60)
    r.raise_for_status()
    data = r.json()
    hits = data.get("hits", {}).get("hits", [])
    total = data.get("hits", {}).get("total", {}).get("value", 0)
    
    print(f"[*] Se encontraron {total} eventos totales en esa madrugada. Mostrando los ultimos {len(hits)} previos a las 3:37:")
    print("-" * 70)
    
    for h in reversed(hits):
        msg = h.get("_source", {}).get("message", "")
        ts = h.get("_source", {}).get("@timestamp", "")
        
        m_time = re.search(r"time=(\S+)", msg)
        m_dst = re.search(r"dstip=(\S+)", msg)
        m_port = re.search(r"dstport=(\S+)", msg)
        m_sent = re.search(r"sentbyte=(\S+)", msg)
        
        hora = m_time.group(1) if m_time else ts
        dst = m_dst.group(1) if m_dst else "?"
        port = m_port.group(1) if m_port else "?"
        sent = m_sent.group(1) if m_sent else "0"
        
        print(f"{hora} (PY) | Destino: {dst}:{port:<5} | Sent: {sent}")
        
    print("-" * 70)
    
except Exception as e:
    print(f"[-] Error: {e}")
