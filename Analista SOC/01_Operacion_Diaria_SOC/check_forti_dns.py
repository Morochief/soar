import json
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SO_IP = "172.17.10.25"
API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

# Buscamos logs UTM de DNS de Fortigate para el host infectado
payload = {
    "size": 10,
    "sort": [{"@timestamp": {"order": "desc"}}],
    "query": {
        "bool": {
            "must": [
                {"query_string": {"query": "message:\"172.17.10.124\" AND (message:\"qname=\" OR message:\"qname\" OR message:\"dns\")"}}
            ],
            "filter": [
                {"range": {"@timestamp": {"gte": "2026-07-07T20:45:00.000Z", "lt": "2026-07-07T20:57:00.000Z"}}}
            ]
        }
    }
}

try:
    r = requests.post(f"https://{SO_IP}:9200/_search", headers=headers, json=payload, verify=False, timeout=60)
    data = r.json()
    hits = data.get("hits", {}).get("hits", [])
    
    print(f"Total eventos que mencionan DNS/qname: {len(hits)}")
    for h in hits:
        print(h.get("_source", {}).get("message", ""))
        print("---")
except Exception as e:
    print(f"Error: {e}")
