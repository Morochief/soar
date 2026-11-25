"""Genera el workflow n8n importable (workflow_ti_dominios.json) a partir de nodes/*.js.

Uso:  python build.py
Las claves de API NO se incluyen: los nodos HTTP referencian Credentials de n8n por nombre.
"""
import json
import pathlib
import uuid

BASE = pathlib.Path(__file__).parent
NODES_DIR = BASE / "nodes"
HELPERS = (NODES_DIR / "_helpers.js").read_text(encoding="utf-8")

nodes, connections = [], {}


def js(fname):
    code = (NODES_DIR / fname).read_text(encoding="utf-8")
    return code.replace("//@@HELPERS", HELPERS)


def add(node, pos):
    node.setdefault("id", str(uuid.uuid5(uuid.NAMESPACE_URL, "ti-dominios/" + node["name"])))
    node["position"] = list(pos)
    nodes.append(node)
    return node["name"]


def code(name, fname, pos, each=False):
    return add({
        "name": name, "type": "n8n-nodes-base.code", "typeVersion": 2,
        "parameters": {"mode": "runOnceForEachItem" if each else "runOnceForAllItems", "jsCode": js(fname)},
    }, pos)


def params(lst):
    return {"parameters": [{"name": k, "value": v} for k, v in lst]}


def http(name, pos, url, method="GET", cred=None, query=None, headers=None, form=None, json_body=None,
         batch=(1, 1000), retry=(3, 5000), timeout=20000, text_field=None, execute_once=False, notes=None):
    p = {"method": method, "url": url}
    node = {"name": name, "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2, "parameters": p,
            "onError": "continueRegularOutput", "alwaysOutputData": False}
    if cred:
        ctype, cname = cred
        p["authentication"] = "genericCredentialType"
        p["genericAuthType"] = ctype
        node["credentials"] = {ctype: {"id": "CONFIGURAR_" + cname.replace(" ", "_").replace(".", ""), "name": cname}}
    if query:
        p["sendQuery"] = True
        p["queryParameters"] = params(query)
    hdrs = [("Accept", "application/json")] + (headers or [])
    p["sendHeaders"] = True
    p["headerParameters"] = params(hdrs)
    if form:
        p["sendBody"] = True
        p["contentType"] = "form-urlencoded"
        p["bodyParameters"] = params(form)
    if json_body:
        p["sendBody"] = True
        p["specifyBody"] = "json"
        p["jsonBody"] = json_body
    opts = {"timeout": timeout}
    if batch:
        opts["batching"] = {"batch": {"batchSize": batch[0], "batchInterval": batch[1]}}
    if text_field:
        opts["response"] = {"response": {"responseFormat": "text", "outputPropertyName": text_field}}
    p["options"] = opts
    if retry:
        node.update({"retryOnFail": True, "maxTries": retry[0], "waitBetweenTries": retry[1]})
    if execute_once:
        node["executeOnce"] = True
    if notes:
        node["notes"] = notes
        node["notesInFlow"] = True
    return add(node, pos)


def if_node(name, pos, expr):
    return add({
        "name": name, "type": "n8n-nodes-base.if", "typeVersion": 2.2,
        "parameters": {
            "conditions": {
                "options": {"caseSensitive": True, "leftValue": "", "typeValidation": "loose", "version": 2},
                "conditions": [{"id": str(uuid.uuid4()), "leftValue": expr, "rightValue": "",
                                "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
                "combinator": "and"},
            "options": {}},
    }, pos)


def link(a, b, out=0):
    m = connections.setdefault(a, {"main": []})["main"]
    while len(m) <= out:
        m.append([])
    m[out].append({"node": b, "type": "main", "index": 0})


def chain(*names):
    for a, b in zip(names, names[1:]):
        link(a, b)


UA = "={{ $('Config').first().json.user_agent }}"
X, Y = 220, 0  # paso horizontal

# ---------------- ENTRADA ----------------
add({"name": "Inicio manual", "type": "n8n-nodes-base.manualTrigger", "typeVersion": 1, "parameters": {}}, (0, 0))
code("Nombres de ejemplo", "ejemplo.js", (X, 0))
add({"name": "Webhook entrada", "type": "n8n-nodes-base.webhook", "typeVersion": 2,
     "webhookId": str(uuid.uuid5(uuid.NAMESPACE_URL, "ti-dominios-webhook")),
     "parameters": {"httpMethod": "POST", "path": "ti-dominios", "authentication": "headerAuth",
                    "responseMode": "responseNode", "options": {}},
     "credentials": {"httpHeaderAuth": {"id": "CONFIGURAR_Webhook_TI_token", "name": "Webhook TI token"}}},
    (0, 180))
add({"name": "Formulario Web CTI", "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
     "parameters": {
         "path": "ti-dominios",
         "formTitle": "🛡️ CTI · Análisis de Dominios y Reputación",
         "formDescription": "Ingresa nombres de empresas o personas a investigar (uno por línea). El flujo descubrirá sus dominios y consultará Shodan, AbuseIPDB, IP-API (Proxy/VPN/Hosting), Abuse.ch y MXToolbox.",
         "formFields": {
             "values": [
                 {
                     "fieldLabel": "Nombres de Empresas o Personas",
                     "fieldType": "textarea",
                     "placeholder": "Mercado Libre\nBanco de la República\nTechnoma",
                     "requiredField": True
                 }
             ]
         },
         "responseMode": "onReceived",
         "options": {
             "customSubmittedText": "✅ Análisis completado con éxito. Los dominios y scores fueron procesados y archivados en el SOC."
         }
     }},
    (0, 360))
code("Config", "config.js", (2 * X, 100))
code("Normalizar nombres", "normalizar_nombres.js", (3 * X, 100))

# ---------------- DESCUBRIMIENTO DE DOMINIOS ----------------
http("Wikidata SPARQL", (4 * X, 100), "https://query.wikidata.org/sparql",
     query=[("query", "={{ $json.sparql }}"), ("format", "json")],
     headers=[("User-Agent", UA)], batch=(1, 1000))
code("Norm Wikidata", "norm_wikidata.js", (5 * X, 100), each=True)
http("crt.sh Organización", (6 * X, 100), "https://crt.sh/",
     query=[("O", "={{ $json.nombre }}"), ("output", "json"), ("exclude", "expired")],
     headers=[("User-Agent", UA)], batch=(1, 2000), timeout=45000, text_field="data")
code("Norm crt.sh", "norm_crtsh.js", (7 * X, 100), each=True)
code("Expandir candidatos", "expandir_candidatos.js", (8 * X, 100))
if_node("¿Hay candidatos?", (9 * X, 100), "={{ $json.sin_candidatos !== true }}")
http("DoH Candidatos", (10 * X, 0), "https://dns.google/resolve",
     query=[("name", "={{ $json.host_dns || $json.dominio }}"), ("type", "A")], batch=(10, 500), retry=(3, 2000), timeout=10000)
code("Validar candidatos", "validar_candidatos.js", (11 * X, 100))
if_node("¿Hay dominios?", (12 * X, 100), "={{ $json.dominios.length > 0 }}")

# ---------------- EMBUDO POR IP ----------------
R2 = 450
code("Dominios únicos", "dominios_unicos.js", (0, R2))
code("IPs únicas", "ips_unicas.js", (X, R2))
http("Shodan Host", (2 * X, R2), "={{ 'https://internetdb.shodan.io/' + $json.ip }}",
     cred=None, batch=(5, 500), timeout=10000, notes="1/5 Shodan InternetDB · Rápido y sin cuotas")
code("Norm Shodan", "norm_shodan.js", (3 * X, R2), each=True)
http("AbuseIPDB Check", (4 * X, R2), "https://api.abuseipdb.com/api/v2/check",
     cred=("httpHeaderAuth", "AbuseIPDB API"),
     query=[("ipAddress", "={{ $json.ip }}"), ("maxAgeInDays", "90"), ("verbose", "true")], batch=(1, 1000), notes="2/5 AbuseIPDB (con reportes recientes)")
code("Norm AbuseIPDB", "norm_abuseipdb.js", (5 * X, R2), each=True)
http("IP-API Proxy & Hosting", (6 * X, R2), "={{ 'http://ip-api.com/json/' + $json.ip + '?fields=status,message,continent,country,countryCode,regionName,city,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query' }}",
     cred=None, batch=(1, 1400), timeout=10000, notes="3/5 IP-API Red, Geo, PTR, Proxy & Hosting (Sin API Key)")
code("Norm IP-API", "norm_ipapi.js", (7 * X, R2), each=True)
http("Feodo Blocklist", (8 * X, R2), "https://feodotracker.abuse.ch/downloads/ipblocklist.json",
     batch=None, timeout=30000, text_field="data", execute_once=True, notes="4/5 abuse.ch Feodo (1 descarga)")
code("Agrupar por dominio", "agrupar_dominio.js", (9 * X, R2))

# ---------------- EMBUDO POR DOMINIO ----------------
http("URLhaus Host", (10 * X, R2), "https://urlhaus-api.abuse.ch/v1/host/", method="POST",
     cred=("httpHeaderAuth", "abuse.ch Auth-Key"), form=[("host", "={{ $json.dominio }}")],
     batch=(1, 1000), notes="4/5 abuse.ch URLhaus")
code("Norm URLhaus", "norm_urlhaus.js", (11 * X, R2), each=True)
http("ThreatFox IOC", (12 * X, R2), "https://threatfox-api.abuse.ch/api/v1/", method="POST",
     cred=("httpHeaderAuth", "abuse.ch Auth-Key"),
     json_body="={{ JSON.stringify({ query: 'search_ioc', search_term: $json.dominio, exact_match: true }) }}",
     batch=(1, 1000), notes="4/5 abuse.ch ThreatFox")
code("Norm ThreatFox", "norm_threatfox.js", (13 * X, R2), each=True)

R3 = 750
code("Expandir MX", "expandir_mx.js", (0, R3))
http("MXToolbox Lookup", (X, R3), "={{ 'https://mxtoolbox.com/api/v1/Lookup/' + $json.cmd + '/' + $json.dominio }}",
     cred=("httpHeaderAuth", "MXToolbox API"), batch=(1, 1500), timeout=30000, notes="5/5 MXToolbox mx/spf/dmarc/blacklist")
code("Norm MXToolbox", "norm_mxtoolbox.js", (2 * X, R3))
code("Expandir DNS DoH", "expandir_dns.js", (3 * X, R3))
http("DoH DNS Registros", (4 * X, R3), "https://dns.google/resolve",
     query=[("name", "={{ $json.query }}"), ("type", "={{ $json.dnsType }}")], batch=(10, 300), retry=(2, 1000), timeout=8000, notes="DNS MX/SPF/DMARC/NS sin cuotas")
code("Norm DNS DoH", "norm_dns.js", (5 * X, R3))
http("RDAP Whois", (6 * X, R3), "={{ 'https://rdap.org/domain/' + $json.dominio }}",
     batch=(3, 500), retry=None, timeout=8000, notes="Antigüedad y Registrador RDAP (sin clave)")
code("Norm RDAP", "norm_rdap.js", (7 * X, R3), each=True)

R4 = 1050
code("Expandir URLs ISO", "expandir_iso.js", (0, R4))
http("Web ISO", (X, R4), "={{ $json.url }}",
     headers=[("User-Agent", UA)], batch=(5, 1000), retry=None, timeout=10000, text_field="html",
     notes="Certificados ISO declarados")
code("Norm ISO", "norm_iso.js", (2 * X, R4))
code("Score", "score.js", (3 * X, R4), each=True)
code("Reporte final", "reporte_final.js", (4 * X, R4))
add({"name": "Convertir a JSON", "type": "n8n-nodes-base.convertToFile", "typeVersion": 1.1,
     "parameters": {"operation": "toJson",
                    "options": {"fileName": "=ti_dominios_{{ $now.toFormat('yyyyLLdd_HHmmss') }}.json"}}},
    (5 * X, R4))

# Notas
add({"name": "Nota credenciales", "type": "n8n-nodes-base.stickyNote", "typeVersion": 1,
     "parameters": {"width": 420, "height": 220, "content":
                    "## Credenciales (nunca en texto plano)\nCrear en *Credentials* (cifradas con N8N_ENCRYPTION_KEY):\n"
                    "- **AbuseIPDB API** · Header Auth · `Key`\n"
                    "- **abuse.ch Auth-Key** · Header Auth · `Auth-Key`\n"
                    "- **MXToolbox API** · Header Auth · `Authorization`\n"
                    "- **Webhook TI token** · Header Auth (protege el webhook)\n\n"
                    "*(Shodan InternetDB, IP-API, Google DoH y RDAP funcionan sin API key ni cuotas)*"}}, (0, -320))
add({"name": "Nota score", "type": "n8n-nodes-base.stickyNote", "typeVersion": 1,
     "parameters": {"width": 420, "height": 200, "content":
                    "## Score 1-100\n`clamp(base 10 + Σ puntos, 1, 100)`\nTopes positivos: AbuseIPDB 30 · abuse.ch 30 · "
                    "Shodan 20 · IP-API 15 · MXToolbox 15.\nPeor IP del dominio. CDN/Hosting x0.5 en AbuseIPDB/IP-API.\n"
                    "Fuente caída = 0 pts + `no_disponible`.\nPesos editables en el nodo **Config**."}}, (6 * X, 1200))

# ---------------- CONEXIONES ----------------
chain("Inicio manual", "Nombres de ejemplo", "Config")
link("Webhook entrada", "Config")
link("Formulario Web CTI", "Config")
chain("Config", "Normalizar nombres", "Wikidata SPARQL", "Norm Wikidata", "crt.sh Organización", "Norm crt.sh",
      "Expandir candidatos", "¿Hay candidatos?")
link("¿Hay candidatos?", "DoH Candidatos", 0)
link("¿Hay candidatos?", "Validar candidatos", 1)
chain("DoH Candidatos", "Validar candidatos", "¿Hay dominios?")
link("¿Hay dominios?", "Dominios únicos", 0)
link("¿Hay dominios?", "Reporte final", 1)
chain("Dominios únicos", "IPs únicas", "Shodan Host", "Norm Shodan", "AbuseIPDB Check", "Norm AbuseIPDB",
      "IP-API Proxy & Hosting", "Norm IP-API", "Feodo Blocklist", "Agrupar por dominio", "URLhaus Host",
      "Norm URLhaus", "ThreatFox IOC", "Norm ThreatFox", "Expandir MX", "MXToolbox Lookup", "Norm MXToolbox",
      "Expandir DNS DoH", "DoH DNS Registros", "Norm DNS DoH", "RDAP Whois", "Norm RDAP",
      "Expandir URLs ISO", "Web ISO", "Norm ISO", "Score", "Reporte final", "Convertir a JSON")

wf = {
    "name": "TI · Descubrimiento de dominios + embudo de reputación + score",
    "nodes": nodes,
    "connections": connections,
    "settings": {"executionOrder": "v1", "saveManualExecutions": True},
    "pinData": {},
    "active": False,
    "meta": {"templateCredsSetupCompleted": False},
}
out = BASE / "workflow_ti_dominios.json"
out.write_text(json.dumps(wf, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"OK -> {out} ({len(nodes)} nodos)")
