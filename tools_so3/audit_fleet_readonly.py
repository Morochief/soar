#!/usr/bin/env python3
# Auditoria SOLO LECTURA de Fleet: agentes y policies (via indices .fleet-*)
import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools_so3.so3_client import SO3Client

ES_USER = os.getenv("SO_ES_USER", "so_elastic")
ES_PASS = os.getenv("SO_ES_PASS", "")

def q(so, path, body=None):
    data = f" -H 'Content-Type: application/json' -d '{json.dumps(body)}'" if body else ""
    out, _ = so.sudo(f"curl -k -s -u '{ES_USER}:{ES_PASS}' 'https://127.0.0.1:9200/{path}'{data}")
    try:
        return json.loads(out)
    except Exception:
        return out[:500]

with SO3Client() as so:
    r = q(so, ".fleet-agents/_search?size=20", {"sort": [{"last_checkin": "desc"}], "_source": ["local_metadata.host.hostname", "policy_id", "policy_revision", "active", "last_checkin", "agent.version", "status"]})
    for h in r.get("hits", {}).get("hits", []) if isinstance(r, dict) else []:
        s = h["_source"]
        print(s.get("local_metadata", {}).get("host", {}).get("hostname"), "|", s.get("policy_id"), "| rev", s.get("policy_revision"), "| active", s.get("active"), "|", s.get("last_checkin"))
    print("---")
    out, _ = so.sudo("free -m | head -3")
    print(out)

