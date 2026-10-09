import json
import urllib3
import requests
import re
import socket

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SO_IP = "172.17.10.25"
API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

# Buscamos de 17:40 a 17:56 PY
payload = {
    "size": 500,
    "sort": [{"@timestamp": {"order": "desc"}}],
    "query": {
        "bool": {
            "must": [
                {"query_string": {"query": "message:\"172.17.10.124\""}},
                {"range": {"@timestamp": {"gte": "2026-07-07T20:40:00.000Z", "lt": "2026-07-07T20:56:50.000Z"}}}
            ]
        }
    }
}

try:
    r = requests.post(f"https://{SO_IP}:9200/_search", headers=headers, json=payload, verify=False, timeout=60)
    r.raise_for_status()
    data = r.json()
    hits = data.get("hits", {}).get("hits", [])
    
    ips_sospechosas = set()
    
    for h in hits:
        msg = h.get("_source", {}).get("message", "")
        m_dst = re.search(r"dstip=(\S+)", msg)
        m_port = re.search(r"dstport=(\S+)", msg)
        
        if m_dst and m_port:
            dst = m_dst.group(1)
            port = m_port.group(1)
            # Solo web (80 o 443) y que no sean las de openDNS/Cisco
            if (port == "80" or port == "443") and not dst.startswith("146.112"):
                ips_sospechosas.add(dst)
                
    print("[*] Resolviendo los sitios web visitados antes del ataque...")
    for ip in ips_sospechosas:
        try:
            # Resolucion inversa
            host = socket.gethostbyaddr(ip)[0]
            print(f"IP: {ip:<15} -> {host}")
        except:
            print(f"IP: {ip:<15} -> [Sin Reverse DNS]")
            
except Exception as e:
    print(f"[-] Error: {e}")
