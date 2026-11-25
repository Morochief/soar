# -*- coding: utf-8 -*-
"""
Motor Central de CTI y Descubrimiento de Dominios.
Implementa el mismo embudo, pesos y lógica que el flujo de n8n.
"""
import os
import re
import json
import time
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests

# Cargar API keys de soar/.env
def cargar_env():
    env_path = Path(__file__).resolve().parents[1] / ".env"
    env = {}
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env

ENV = cargar_env()
SHODAN_KEY = ENV.get("SHODAN_API_KEY", "")
ABUSEIPDB_KEY = ENV.get("ABUSEIPDB_API_KEY", "")
ABUSECH_KEY = ENV.get("ABUSECH_API_KEY", "")
MXTOOLBOX_KEY = ENV.get("MXTOOLBOX_API_KEY", "")

# Rate limiters thread-safe para consultas concurrentes por lotes
_RATE_LOCKS = {
    "ipapi": threading.Lock(),
    "shodan": threading.Lock(),
    "mxtoolbox": threading.Lock(),
}
_LAST_CALL = {"ipapi": 0.0, "shodan": 0.0, "mxtoolbox": 0.0}

def _rate_limit(canal, min_interval):
    with _RATE_LOCKS[canal]:
        elapsed = time.time() - _LAST_CALL[canal]
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        _LAST_CALL[canal] = time.time()

PUERTOS_RIESGO = [21, 23, 25, 110, 135, 139, 143, 445, 1433, 1521, 2375, 3306, 3389, 5432, 5900, 5985, 6379, 9200, 11211, 27017]
PUERTOS_WEB = [80, 443, 8080, 8443]
REGEX_CDN = re.compile(r"cloudflare|akamai|fastly|cloudfront|incapsula|imperva|sucuri|amazon|google|microsoft|azure", re.I)
REGEX_ISO = re.compile(r"ISO\s*(?:/\s*IEC\s*)?[-\s]?(9001|14001|27001|27017|27018|27701|45001|22301|20000(?:-1)?|50001|22000|13485|37001|28000)(?:\s*[:\-]\s*((?:19|20)\d\d))?", re.I)

TLDS_DEFAULT = ['gov.py', 'gob.py', 'com.py', 'edu.py', 'org.py', 'py', 'gov', 'gob', 'com', 'com.ar', 'com.uy', 'com.br', 'cl', 'co', 'net', 'org', 'io', 'tech']

ISO_NOMBRES = {
    "9001": "Gestión de calidad", "14001": "Gestión ambiental", "27001": "Seguridad de la información",
    "27017": "Seguridad en cloud", "27018": "Protección PII en cloud", "27701": "Gestión de privacidad",
    "45001": "Seguridad y salud laboral", "22301": "Continuidad de negocio", "20000": "Gestión de servicios TI",
    "20000-1": "Gestión de servicios TI", "50001": "Gestión energética", "22000": "Inocuidad alimentaria",
    "13485": "Dispositivos médicos", "37001": "Antisoborno", "28000": "Seguridad de cadena de suministro"
}

def clean_domain(h):
    if not h: return None
    h = str(h).strip().lower()
    h = re.sub(r"^[a-z]+://", "", h).split("/")[0].split(":")[0].split("?")[0]
    h = re.sub(r"^\*\.", "", h)
    h = re.sub(r"^www\.", "", h).rstrip(".")
    if not re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", h): return None
    parts = h.split(".")
    if len(parts) <= 2: return h
    sld, tld = parts[-2], parts[-1]
    tres = len(tld) == 2 and sld in ["com", "net", "org", "gov", "gob", "edu", "co", "ac", "mil", "nom", "int"]
    return ".".join(parts[-3:] if tres else parts[-2:])

def resolver_dns(dominio):
    # Prueba primero el dominio raíz y si no tiene IP, prueba con www.
    for host in [dominio, f"www.{dominio}"]:
        try:
            r = requests.get(f"https://dns.google/resolve?name={host}&type=A", timeout=8)
            if r.status_code == 200:
                data = r.json()
                ips = [ans["data"] for ans in data.get("Answer", []) if ans.get("type") == 1]
                public_ips = [ip for ip in ips if not re.match(r"^(10\.|127\.|0\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.|100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.)", ip)]
                if public_ips:
                    return public_ips, (host.startswith("www."))
        except Exception:
            pass
    return [], False

def descubrir_candidatos(nombre, log_cb=None):
    candidatos = {}
    STOP = {"srl", "ltda", "inc", "llc", "corp", "sa", "del", "de", "las", "los", "and", "the", "cia", "sociedad", "anonima"}
    nombre_limpio = nombre.strip()
    
    # Detección de dominio directo (ej: "technoma.com.py" o "https://bcp.gov.py")
    es_dominio_explicito = False
    m_dom = re.search(r"(?:https?://)?([a-z0-9.-]+\.[a-z]{2,})", nombre_limpio, re.I)
    if m_dom:
        d_dir = clean_domain(m_dom.group(1))
        if d_dir:
            candidatos[d_dir] = 1.0
            if not re.search(r"\s", nombre_limpio):
                es_dominio_explicito = True

    tokens = [t for t in re.sub(r"[^a-z0-9]+", " ", nombre_limpio.lower()).split() if len(t) >= 2 and t not in STOP]
    slug = "".join(tokens)
    acronimo = "".join(t[0] for t in tokens) if len(tokens) >= 2 and len(tokens) <= 5 else None
    slug_primero_ultimo = (tokens[0] + tokens[-1]) if len(tokens) >= 2 else None

    if es_dominio_explicito:
        if log_cb: log_cb(f"[*] Resolviendo dominio directo '{list(candidatos.keys())[0]}'...")
        d_dir = list(candidatos.keys())[0]
        ips, usa_www = resolver_dns(d_dir)
        if ips:
            url = f"https://www.{d_dir}" if usa_www else f"https://{d_dir}"
            return [{"dominio": d_dir, "url": url, "confianza": 1.0, "ips": ips[:3]}]
        # Si no resolvió directamente, continuamos con búsqueda amplia por si hubo typo o alias

    if log_cb: log_cb(f"[*] Buscando huella digital para '{nombre_limpio}'...")

    # 1. Wikidata SPARQL
    try:
        esc = nombre_limpio.replace('"', '\\"')
        sparql = f'''SELECT ?item ?itemLabel ?website WHERE {{
          SERVICE wikibase:mwapi {{
            bd:serviceParam wikibase:endpoint "www.wikidata.org";
            wikibase:api "EntitySearch";
            mwapi:search "{esc}";
            mwapi:language "es".
            ?item wikibase:apiOutputItem mwapi:item.
          }}
          ?item wdt:P856 ?website.
        }} LIMIT 5'''
        r = requests.get("https://query.wikidata.org/sparql", params={"query": sparql, "format": "json"}, headers={"User-Agent": "Technoma-SOC-Engine/1.0"}, timeout=10)
        if r.status_code == 200:
            for b in r.json().get("results", {}).get("bindings", []):
                web = b.get("website", {}).get("value")
                d = clean_domain(web)
                if d:
                    candidatos[d] = candidatos.get(d, 0.0) + 0.50
    except Exception:
        pass

    # 2. crt.sh
    try:
        r = requests.get(f"https://crt.sh/?O={urllib.parse.quote(nombre_limpio)}&output=json&exclude=expired", timeout=12)
        if r.status_code == 200:
            for cert in r.json()[:15]:
                for name_val in str(cert.get("name_value", "")).split("\n"):
                    d = clean_domain(name_val)
                    if d:
                        candidatos[d] = candidatos.get(d, 0.0) + 0.30
    except Exception:
        pass

    # 3. Heurística regional con Acrónimos, Slugs y combinaciones (ej: caja + ande -> cajaande)
    slugs_probar = [s for s in [slug_primero_ultimo, acronimo, slug if len(slug) <= 24 else None] if s and len(s) >= 2]
    for s in slugs_probar:
        for tld in TLDS_DEFAULT:
            cand_dom = f"{s}.{tld}"
            candidatos[cand_dom] = candidatos.get(cand_dom, 0.0) + 0.35

    # Validación DNS concurrente (rápida, 10 hilos)
    aceptados = []
    def check_dns(item):
        dom, conf = item
        ips, usa_www = resolver_dns(dom)
        if ips:
            label = dom.split(".")[0]
            if (acronimo and label == acronimo) or (slug_primero_ultimo and label == slug_primero_ultimo) or any((len(t) >= 3 and label in t) or (len(label) >= 3 and t in label) for t in tokens):
                conf += 0.15
            conf = min(round(conf, 2), 1.0)
            if conf >= 0.35:
                url = f"https://www.{dom}" if usa_www else f"https://{dom}"
                return {"dominio": dom, "url": url, "confianza": conf, "ips": ips[:3]}
        return None

    with ThreadPoolExecutor(max_workers=10) as executor:
        resultados = executor.map(check_dns, list(candidatos.items()))
        for r in resultados:
            if r:
                aceptados.append(r)

    aceptados.sort(key=lambda x: x["confianza"], reverse=True)
    return aceptados

def consultar_shodan(ip):
    try:
        if SHODAN_KEY:
            _rate_limit("shodan", 1.05)
            r = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_KEY}", timeout=10)
            if r.status_code == 200:
                data = r.json() or {}
                vulns = list((data.get("vulns") or {}).keys()) if isinstance(data.get("vulns"), dict) else (data.get("vulns") or [])
                servicios = [{"puerto": s.get("port"), "transporte": s.get("transport"), "producto": s.get("product"), "version": s.get("version")} for s in (data.get("data") or [])[:15]]
                return {
                    "estado": "ok", "org": data.get("org") or data.get("isp"), "isp": data.get("isp"),
                    "asn": data.get("asn"), "pais": data.get("country_code"),
                    "puertos": sorted(data.get("ports") or []), "vulns": vulns,
                    "hostnames": data.get("hostnames") or [],
                    "cpes": data.get("cpe") or [],
                    "tags": data.get("tags") or [],
                    "servicios": servicios
                }
            elif r.status_code == 404:
                return {"estado": "ok_sin_datos", "puertos": [], "vulns": [], "hostnames": [], "cpes": [], "tags": [], "servicios": []}

        # Fallback de alta disponibilidad: Shodan InternetDB (oficial de Shodan, sin límite de cuota)
        r_idb = requests.get(f"https://internetdb.shodan.io/{ip}", timeout=8)
        if r_idb.status_code == 200:
            idb = r_idb.json() or {}
            ports = sorted(idb.get("ports") or [])
            return {
                "estado": "ok",
                "org": ", ".join(idb.get("cpes") or []) or "InternetDB Shodan",
                "isp": ", ".join(idb.get("hostnames") or []) or "Shodan FastDB",
                "asn": None, "pais": None,
                "puertos": ports,
                "vulns": idb.get("vulns") or [],
                "hostnames": idb.get("hostnames") or [],
                "cpes": idb.get("cpes") or [],
                "tags": idb.get("tags") or [],
                "servicios": [{"puerto": p, "transporte": "tcp", "producto": None, "version": None} for p in ports]
            }
        elif r_idb.status_code == 404:
            return {"estado": "ok_sin_datos", "puertos": [], "vulns": [], "hostnames": [], "cpes": [], "tags": [], "servicios": []}
        return {"estado": "no_disponible", "motivo": f"HTTP {r_idb.status_code}", "puertos": [], "vulns": [], "hostnames": [], "cpes": [], "tags": [], "servicios": []}
    except Exception as e:
        return {"estado": "no_disponible", "motivo": str(e), "puertos": [], "vulns": [], "hostnames": [], "cpes": [], "tags": [], "servicios": []}

ABUSE_CATS = {
    3: "Fraud", 4: "DDoS", 5: "FTP Brute-Force", 6: "Ping of Death", 7: "Phishing",
    9: "Open Proxy", 10: "Web Spam", 11: "Email Spam", 14: "Port Scan", 15: "Hacking",
    16: "SQL Injection", 18: "Brute-Force", 19: "Bad Web Bot", 20: "Exploited Host",
    21: "Web App Attack", 22: "SSH Attack", 23: "IoT Targeted"
}

def consultar_abuseipdb(ip):
    if not ABUSEIPDB_KEY: return {"estado": "no_disponible", "motivo": "Sin API Key"}
    try:
        headers = {"Key": ABUSEIPDB_KEY, "Accept": "application/json"}
        r = requests.get("https://api.abuseipdb.com/api/v2/check", headers=headers, params={"ipAddress": ip, "maxAgeInDays": 90, "verbose": "true"}, timeout=10)
        if r.status_code == 200:
            d = (r.json() or {}).get("data") or {}
            reportes = []
            for rep in (d.get("reports") or [])[:8]:
                cats = [ABUSE_CATS.get(c, f"Cat-{c}") for c in (rep.get("categories") or [])]
                reportes.append({
                    "fecha": rep.get("reportedAt"),
                    "comentario": (rep.get("comment") or "")[:140],
                    "categorias": cats,
                    "pais_reportante": rep.get("reporterCountryCode")
                })
            return {
                "estado": "ok",
                "confianza_abuso": d.get("abuseConfidenceScore", 0) or 0,
                "total_reportes": d.get("totalReports", 0) or 0,
                "usuarios_distintos": d.get("numDistinctUsers", 0) or 0,
                "ultimo_reporte": d.get("lastReportedAt"),
                "whitelisted": bool(d.get("isWhitelisted", False)),
                "tipo_uso": d.get("usageType"),
                "isp": d.get("isp"),
                "dominio": d.get("domain"),
                "pais": d.get("countryName") or d.get("countryCode"),
                "es_tor": bool(d.get("isTor")),
                "hostnames": d.get("hostnames") or [],
                "reportes_recientes": reportes
            }
        return {"estado": "no_disponible", "motivo": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"estado": "no_disponible", "motivo": str(e)}

def consultar_ipapi(ip):
    try:
        _rate_limit("ipapi", 1.38)  # 45 req/min max sin API key
        url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,countryCode,regionName,city,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            d = r.json() or {}
            if d.get("status") == "success":
                return {
                    "estado": "ok",
                    "pais": d.get("country"),
                    "pais_codigo": d.get("countryCode"),
                    "region": d.get("regionName"),
                    "ciudad": d.get("city"),
                    "zona_horaria": d.get("timezone"),
                    "isp": d.get("isp"),
                    "org": d.get("org"),
                    "as": d.get("as"),
                    "asname": d.get("asname"),
                    "reverse": d.get("reverse"),
                    "mobile": bool(d.get("mobile")),
                    "proxy": bool(d.get("proxy")),
                    "hosting": bool(d.get("hosting"))
                }
            return {"estado": "no_disponible", "motivo": d.get("message", "fail")}
        return {"estado": "no_disponible", "motivo": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"estado": "no_disponible", "motivo": str(e)}

def consultar_abusech(dominio, ips, feodo_map):
    res = {
        "estado": "ok",
        "urlhaus": {"estado": "no_disponible", "listado": False, "urls_total": 0, "urls_online": 0, "amenazas": [], "muestras": []},
        "threatfox": {"estado": "no_disponible", "listado": False, "iocs_total": 0, "iocs": []},
        "feodo": {"estado": "ok", "listada": False, "malware": None, "ip": None}
    }
    for ip in ips:
        if ip in feodo_map:
            res["feodo"] = {"estado": "ok", "listada": True, "ip": ip, "malware": feodo_map[ip]}
            break

    if ABUSECH_KEY:
        try:
            r = requests.post("https://urlhaus-api.abuse.ch/v1/host/", headers={"Auth-Key": ABUSECH_KEY}, data={"host": dominio}, timeout=10)
            if r.status_code == 200:
                data = r.json() or {}
                if data.get("query_status") == "ok":
                    urls = data.get("urls") or []
                    res["urlhaus"] = {
                        "estado": "ok",
                        "listado": True,
                        "urls_total": len(urls),
                        "urls_online": sum(1 for u in urls if u.get("url_status") == "online"),
                        "amenazas": list(set(u.get("threat") for u in urls if u.get("threat"))),
                        "muestras": [{"url": u.get("url"), "estado": u.get("url_status"), "amenaza": u.get("threat"), "tags": u.get("tags") or []} for u in urls[:5]]
                    }
                elif data.get("query_status") == "no_results":
                    res["urlhaus"] = {"estado": "ok", "listado": False, "urls_total": 0, "urls_online": 0, "amenazas": [], "muestras": []}
            else:
                res["urlhaus"] = {"estado": "no_disponible", "motivo": f"HTTP {r.status_code}", "listado": False, "urls_total": 0, "urls_online": 0, "amenazas": [], "muestras": []}
        except Exception as e:
            res["urlhaus"] = {"estado": "no_disponible", "motivo": str(e), "listado": False, "urls_total": 0, "urls_online": 0, "amenazas": [], "muestras": []}

        try:
            r = requests.post("https://threatfox-api.abuse.ch/api/v1/", headers={"Auth-Key": ABUSECH_KEY}, json={"query": "search_ioc", "search_term": dominio, "exact_match": True}, timeout=10)
            if r.status_code == 200:
                data = r.json() or {}
                if data.get("query_status") == "ok":
                    data_iocs = data.get("data") or []
                    res["threatfox"] = {
                        "estado": "ok",
                        "listado": bool(data_iocs),
                        "iocs_total": len(data_iocs),
                        "iocs": [{"ioc": x.get("ioc"), "tipo": x.get("threat_type"), "malware": x.get("malware_printable"), "confianza": x.get("confidence_level")} for x in data_iocs[:8]]
                    }
                elif data.get("query_status") == "no_result":
                    res["threatfox"] = {"estado": "ok", "listado": False, "iocs_total": 0, "iocs": []}
            else:
                res["threatfox"] = {"estado": "no_disponible", "motivo": f"HTTP {r.status_code}", "listado": False, "iocs_total": 0, "iocs": []}
        except Exception as e:
            res["threatfox"] = {"estado": "no_disponible", "motivo": str(e), "listado": False, "iocs_total": 0, "iocs": []}

    oks = sum(1 for k in ("feodo", "urlhaus", "threatfox") if res[k].get("estado") == "ok")
    res["estado"] = "ok" if oks == 3 else "parcial" if oks > 0 else "no_disponible"
    return res

def consultar_mxtoolbox(dominio):
    if not MXTOOLBOX_KEY: return {"estado": "no_disponible", "motivo": "Sin API Key"}
    headers = {"Authorization": MXTOOLBOX_KEY, "Accept": "application/json"}
    cmds = ["mx", "spf", "dmarc", "blacklist"]
    res = {}
    for cmd in cmds:
        try:
            _rate_limit("mxtoolbox", 0.5)
            r = requests.get(f"https://mxtoolbox.com/api/v1/Lookup/{cmd}/{dominio}", headers=headers, timeout=12)
            if r.status_code == 200:
                d = r.json() or {}
                registros = []
                for item in (d.get("Information") or []):
                    val = item.get("Value") or item.get("Hostname") or item.get("IP Address") or ""
                    key = item.get("Name") or item.get("Type") or item.get("Prefix") or ""
                    if val or key:
                        registros.append({"clave": key, "valor": val, "desc": item.get("Description", "")})
                res[cmd] = {
                    "estado": "ok",
                    "failed": [f.get("Name", "") for f in (d.get("Failed") or [])],
                    "warnings": [w.get("Name", "") for w in (d.get("Warnings") or [])],
                    "passed": len(d.get("Passed") or []),
                    "registros": registros[:10]
                }
            else:
                res[cmd] = {"estado": "no_disponible", "motivo": f"HTTP {r.status_code}", "failed": [], "warnings": [], "passed": 0, "registros": []}
        except Exception as e:
            res[cmd] = {"estado": "no_disponible", "motivo": str(e), "failed": [], "warnings": [], "passed": 0, "registros": []}
    res["estado"] = "ok" if all(v.get("estado") == "ok" for v in res.values()) else "parcial"
    return res

def consultar_dns_doh(dominio):
    dns = {"mx": [], "spf": [], "dmarc": [], "ns": [], "txt_extra": [], "_ok": {}}
    consultas = [
        ("MX", dominio, "MX"),
        ("SPF", dominio, "TXT"),
        ("DMARC", f"_dmarc.{dominio}", "TXT"),
        ("NS", dominio, "NS")
    ]
    def query_one(item):
        tipo, host, qtype = item
        try:
            r = requests.get("https://dns.google/resolve", params={"name": host, "type": qtype}, timeout=6)
            if r.status_code == 200:
                return tipo, True, (r.json() or {}).get("Answer") or []
        except Exception:
            pass
        return tipo, False, []

    with ThreadPoolExecutor(max_workers=4) as ex:
        for tipo, ok, ans in ex.map(query_one, consultas):
            dns["_ok"][tipo] = ok
            if tipo == "MX":
                dns["mx"] = [str(a.get("data", "")).rstrip(".").strip() for a in ans if a.get("type") == 15]
            elif tipo == "SPF":
                txts = [re.sub(r'^"|"$', '', str(a.get("data", ""))).replace('" "', '').strip() for a in ans if a.get("type") == 16]
                dns["spf"] = [t for t in txts if re.match(r"^v=spf1\b", t, re.I)]
                dns["txt_extra"] = [t for t in txts if not re.match(r"^v=spf1\b", t, re.I)][:8]
            elif tipo == "DMARC":
                txts = [re.sub(r'^"|"$', '', str(a.get("data", ""))).replace('" "', '').strip() for a in ans if a.get("type") == 16]
                dns["dmarc"] = [t for t in txts if re.match(r"^v=DMARC1\b", t, re.I)]
            elif tipo == "NS":
                dns["ns"] = [str(a.get("data", "")).rstrip(".").strip() for a in ans if a.get("type") == 2]
    return dns

def consultar_rdap(dominio):
    try:
        r = requests.get(f"https://rdap.org/domain/{dominio}", timeout=8)
        if r.status_code == 200:
            d = r.json() or {}
            events = d.get("events") or []
            def get_ev(act):
                for e in events:
                    if e.get("eventAction") == act: return e.get("eventDate")
                return None
            registrador = None
            for ent in (d.get("entities") or []):
                if "registrar" in (ent.get("roles") or []):
                    va = ent.get("vcardArray") or []
                    if len(va) > 1 and isinstance(va[1], list):
                        for item in va[1]:
                            if isinstance(item, list) and len(item) >= 4 and item[0] == "fn":
                                registrador = item[3]
            creacion = get_ev("registration")
            antiguedad = None
            if creacion:
                try:
                    import datetime
                    dt = datetime.datetime.fromisoformat(creacion.replace("Z", "+00:00"))
                    now = datetime.datetime.now(datetime.timezone.utc)
                    antiguedad = round((now - dt).days / 365.25, 1)
                except Exception:
                    pass
            return {
                "estado": "ok",
                "registrador": registrador or "No especificado",
                "creacion": creacion,
                "expiracion": get_ev("expiration"),
                "actualizacion": get_ev("last changed"),
                "antiguedad_anios": antiguedad,
                "estados": d.get("status") or [],
                "dnssec": bool((d.get("secureDNS") or {}).get("delegationSigned"))
            }
        elif r.status_code == 404:
            return {"estado": "no_disponible", "motivo": "TLD sin servidor RDAP público (ej. .py)"}
        return {"estado": "no_disponible", "motivo": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"estado": "no_disponible", "motivo": str(e)}

def verificar_iso(dominio):
    rutas = ["/", "/certificaciones", "/calidad", "/iso", "/certifications"]
    normas = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    hosts_a_probar = [dominio] if dominio.startswith("www.") else [dominio, f"www.{dominio}"]

    def fetch_ruta(url_actual):
        try:
            r = requests.get(url_actual, headers=headers, timeout=5, verify=False)
            if r.status_code == 200:
                return url_actual, True, r.text
        except Exception:
            pass
        return url_actual, False, ""

    paginas_ok = 0
    paginas_fallidas = 0
    for h in hosts_a_probar:
        urls = [f"https://{h}{ruta}" for ruta in rutas]
        with ThreadPoolExecutor(max_workers=5) as ex:
            res_list = list(ex.map(fetch_ruta, urls))
        for url_actual, ok, body in res_list:
            if ok:
                paginas_ok += 1
                texto = re.sub(r"<[^>]+>", " ", body)
                for m in REGEX_ISO.finditer(texto):
                    num = m.group(1)
                    anio = m.group(2)
                    clave = f"ISO {num}"
                    if clave not in normas:
                        normas[clave] = {
                            "norma": clave,
                            "descripcion": ISO_NOMBRES.get(num, "Certificación ISO"),
                            "versiones": [],
                            "evidencias": []
                        }
                    if anio and anio not in normas[clave]["versiones"]:
                        normas[clave]["versiones"].append(anio)
                    if len(normas[clave]["evidencias"]) < 2:
                        start = max(0, m.start() - 60)
                        end = min(len(texto), m.end() + 80)
                        frag = re.sub(r"\s+", " ", texto[start:end]).strip()
                        normas[clave]["evidencias"].append({
                            "url": url_actual,
                            "fragmento": frag
                        })
            else:
                paginas_fallidas += 1
        if normas or paginas_ok > 0:
            break

    lista_normas = list(normas.values())
    return {
        "estado": "ok" if paginas_ok > 0 else "no_disponible",
        "normas": lista_normas,
        "paginas_revisadas": paginas_ok,
        "paginas_fallidas": paginas_fallidas,
        "encontrados": len(lista_normas) > 0,
        "verificado": False
    }

def is_cdn(ip, d):
    sh = d.get("shodan") or {}
    ab = d.get("abuseipdb") or {}
    ia = d.get("ipapi") or {}
    txt = f"{sh.get('org') or ''} {sh.get('isp') or ''} {ab.get('isp') or ''} {ia.get('org') or ''} {ia.get('isp') or ''}"
    return bool(REGEX_CDN.search(txt)) or bool(ia.get("hosting"))

def calcular_score(dominio, ips_data, abusech_data, mxtoolbox_data, iso_data):
    puntos = 10
    detalle = [{"fuente": "base", "consulta": "-", "puntos": 10, "evidencia": "Punto de partida neutral"}]

    # Shodan (peor IP, tope +20)
    peor_shodan = None
    for ip, d in ips_data.items():
        s = d.get("shodan") or {}
        if s.get("estado") == "ok":
            pts = 0
            ev = []
            vulns = s.get("vulns") or []
            puertos = s.get("puertos") or []
            if len(vulns) >= 5: pts += 12; ev.append(f"{len(vulns)} CVEs")
            elif len(vulns) >= 1: pts += 8; ev.append(f"CVEs: {', '.join(vulns[:3])}")
            puertos_r = [p for p in puertos if p in PUERTOS_RIESGO]
            if puertos_r: pts += min(len(puertos_r) * 3, 8); ev.append(f"Puertos sensibles: {puertos_r}")
            if pts == 0 and puertos and all(p in PUERTOS_WEB for p in puertos):
                pts = -2; ev.append(f"Solo puertos web seguros ({puertos})")
            pts = min(pts, 20)
            if ev and (peor_shodan is None or pts > peor_shodan[0]):
                peor_shodan = (pts, f"host/{ip}", ", ".join(ev))
    if peor_shodan and peor_shodan[0] != 0:
        detalle.append({"fuente": "shodan", "consulta": peor_shodan[1], "puntos": peor_shodan[0], "evidencia": peor_shodan[2]})
        puntos += peor_shodan[0]

    # AbuseIPDB (peor IP, tope +30)
    peor_abuse = None
    for ip, d in ips_data.items():
        a = d.get("abuseipdb") or {}
        if a.get("estado") == "ok":
            sc = a.get("confianza_abuso") or 0
            cdn = is_cdn(ip, d) or bool(REGEX_CDN.search(a.get("isp") or ""))
            factor = 0.5 if cdn else 1.0
            if sc >= 75: pts = int(30 * factor)
            elif sc >= 25: pts = int(18 * factor)
            elif sc >= 1: pts = int(8 * factor)
            elif (a.get("total_reportes") or 0) == 0: pts = -3
            else: pts = 0
            if pts != 0 and (peor_abuse is None or pts > peor_abuse[0]):
                ev_str = "Sin reportes de abuso (90 días)" if pts < 0 else f"Confianza abuso: {sc}% ({a.get('total_reportes', 0)} reportes{', CDN/Hosting x0.5' if cdn else ''})"
                peor_abuse = (pts, f"check/{ip}", ev_str)
    if peor_abuse and peor_abuse[0] != 0:
        detalle.append({"fuente": "abuseipdb", "consulta": peor_abuse[1], "puntos": peor_abuse[0], "evidencia": peor_abuse[2]})
        puntos += peor_abuse[0]

    # IP-API (Proxy / VPN / Hosting / Datacenter, tope +15)
    ipapi_ev = None
    for ip, d in ips_data.items():
        ia = d.get("ipapi") or {}
        if ia.get("estado") == "ok":
            cdn = is_cdn(ip, d)
            factor = 0.5 if cdn else 1.0
            if ia.get("proxy"):
                pts = int(15 * factor)
                ev = f"IP clasificada como PROXY/VPN/Tor ({ia.get('isp') or ia.get('org') or 'desconocido'})"
            elif ia.get("hosting"):
                pts = int(5 * factor)
                ev = f"IP alojada en Datacenter / Cloud / Hosting ({ia.get('isp') or ia.get('org') or 'desconocido'})"
            else:
                pts = -2
                ev = "Infraestructura corporativa/residencial propia (no proxy/no hosting)"
            if ipapi_ev is None or pts > ipapi_ev[0]:
                ipapi_ev = (pts, f"ip-api/json/{ip}", ev)
    if ipapi_ev is not None:
        detalle.append({"fuente": "ipapi", "consulta": ipapi_ev[1], "puntos": ipapi_ev[0], "evidencia": ipapi_ev[2]})
        puntos += ipapi_ev[0]

    # Abuse.ch (tope +30)
    ach_pos = 0
    if (abusech_data.get("feodo") or {}).get("listada"):
        f = abusech_data["feodo"]
        detalle.append({"fuente": "abuse.ch", "consulta": "feodotracker", "puntos": 30, "evidencia": f"IP C2 de botnet ({f.get('malware')})"})
        ach_pos += 30
    uh = abusech_data.get("urlhaus") or {}
    if uh.get("estado") == "ok" and uh.get("listado"):
        p_uh = 20 if (uh.get("urls_online") or 0) > 0 else 8
        detalle.append({"fuente": "abuse.ch", "consulta": "urlhaus/host", "puntos": p_uh, "evidencia": f"URLhaus: {uh.get('urls_total')} URLs ({uh.get('urls_online')} activas)"})
        ach_pos += p_uh
    tf = abusech_data.get("threatfox") or {}
    if tf.get("estado") == "ok" and tf.get("listado"):
        iocs_n = tf.get("iocs_total") or len(tf.get("iocs") or [])
        mal_names = list(dict.fromkeys([x.get("malware") for x in (tf.get("iocs") or []) if x.get("malware")]))
        detalle.append({"fuente": "abuse.ch", "consulta": "threatfox/search_ioc", "puntos": 15, "evidencia": f"ThreatFox: {iocs_n} IOC(s)" + (f" ({', '.join(mal_names[:3])})" if mal_names else "")})
        ach_pos += 15
    if ach_pos > 30:
        detalle.append({"fuente": "abuse.ch", "consulta": "tope_de_fuente", "puntos": 30 - ach_pos, "evidencia": f"positivos {ach_pos} > tope 30"})
        puntos += 30
    elif ach_pos > 0:
        puntos += ach_pos
    else:
        detalle.append({"fuente": "abuse.ch", "consulta": "urlhaus+threatfox+feodo", "puntos": -3, "evidencia": "Sin presencia en listas de abuse.ch"})
        puntos -= 3

    # MXToolbox + DNS DoH (tope +15)
    if mxtoolbox_data.get("estado") in ["ok", "parcial"]:
        mx_pos = 0
        mx_neg = 0
        bl = mxtoolbox_data.get("blacklist") or {}
        if bl.get("failed"):
            detalle.append({"fuente": "mxtoolbox", "consulta": "lookup/blacklist", "puntos": 8, "evidencia": f"En blacklist: {', '.join(bl['failed'][:2])}"})
            mx_pos += 8
        spf = mxtoolbox_data.get("spf") or {}
        spf_fails_txt = " ".join(spf.get("failed") or [])
        if re.search(r"Permissive|\+all", spf_fails_txt, re.I):
            detalle.append({"fuente": "mxtoolbox", "consulta": "lookup/spf", "puntos": 3, "evidencia": "SPF permisivo (+all)"})
            mx_pos += 3
        elif spf.get("failed"):
            detalle.append({"fuente": "mxtoolbox", "consulta": "lookup/spf", "puntos": 2, "evidencia": "Falla o ausencia de registro SPF"})
            mx_pos += 2
        dmarc = mxtoolbox_data.get("dmarc") or {}
        dm_warns_txt = " ".join(dmarc.get("warnings") or [])
        if dmarc.get("failed"):
            detalle.append({"fuente": "mxtoolbox", "consulta": "lookup/dmarc", "puntos": 3, "evidencia": "Falla o ausencia de registro DMARC"})
            mx_pos += 3
        elif re.search(r"p=none", dm_warns_txt, re.I):
            detalle.append({"fuente": "mxtoolbox", "consulta": "lookup/dmarc", "puntos": 1, "evidencia": "DMARC en p=none (solo monitoreo)"})
            mx_pos += 1
        if mx_pos == 0 and mxtoolbox_data.get("estado") == "ok" and not bl.get("failed") and not spf.get("failed") and not dmarc.get("failed"):
            detalle.append({"fuente": "mxtoolbox", "consulta": "mx+spf+dmarc+blacklist", "puntos": -3, "evidencia": "SPF/DMARC correctos y sin blacklists"})
            mx_neg = -3
        if mx_pos > 15:
            detalle.append({"fuente": "mxtoolbox", "consulta": "tope_de_fuente", "puntos": 15 - mx_pos, "evidencia": f"positivos {mx_pos} > tope 15"})
            puntos += 15
        else:
            puntos += mx_pos + mx_neg

    # ISO
    if iso_data.get("encontrados") and any(n.get("norma") == "ISO 27001" for n in (iso_data.get("normas") or [])):
        detalle.append({"fuente": "iso", "consulta": "web", "puntos": -1, "evidencia": "ISO 27001 declarada en sitio web"})
        puntos -= 1

    score_final = max(1, min(100, puntos))
    return score_final, detalle

def ejecutar_pipeline(lista_nombres, log_cb=None):
    import urllib3
    urllib3.disable_warnings()

    # Aceptar string o lista y deduplicar entradas manteniendo orden
    if isinstance(lista_nombres, str):
        lista_nombres = re.split(r"[\r\n,;]+", lista_nombres)
    nombres_unicos = []
    vistos_nom = set()
    for n in (lista_nombres or []):
        nl = re.sub(r"\s+", " ", str(n or "").strip())
        if nl and nl.lower() not in vistos_nom:
            vistos_nom.add(nl.lower())
            nombres_unicos.append(nl)

    if log_cb: log_cb("[*] Descargando Feodo Tracker (Botnets C2)...")
    feodo_map = {}
    try:
        r = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.json", timeout=12)
        if r.status_code == 200:
            for item in (r.json() or []):
                if item.get("ip_address"):
                    feodo_map[item.get("ip_address")] = item.get("malware")
    except Exception:
        pass

    # Descubrimiento y deduplicación global de dominios entre entidades
    globales = {}
    sin_dominio = []
    for nombre in nombres_unicos:
        cands = descubrir_candidatos(nombre, log_cb)
        if not cands:
            if log_cb: log_cb(f"[-] '{nombre}': No se encontraron dominios verificados.")
            sin_dominio.append({"nombre": nombre, "motivo": "Sin coincidencias verificadas ni resolución DNS"})
            continue
        for c in cands:
            dom = c["dominio"]
            if dom in globales:
                if nombre not in globales[dom]["nombres_origen"]:
                    globales[dom]["nombres_origen"].append(nombre)
            else:
                globales[dom] = {
                    "dominio": dom,
                    "url": c["url"],
                    "ips": c["ips"],
                    "nombres_origen": [nombre]
                }

    ip_cache = {}
    ip_cache_lock = threading.Lock()

    def enriquecer_ip(ip):
        with ip_cache_lock:
            if ip in ip_cache:
                return ip_cache[ip]
        if log_cb: log_cb(f"    [IP] Consultando Shodan + AbuseIPDB + IP-API ({ip}) en paralelo...")
        with ThreadPoolExecutor(max_workers=3) as ex_ip:
            f_sh = ex_ip.submit(consultar_shodan, ip)
            f_ab = ex_ip.submit(consultar_abuseipdb, ip)
            f_ia = ex_ip.submit(consultar_ipapi, ip)
            res_ip = {"shodan": f_sh.result(), "abuseipdb": f_ab.result(), "ipapi": f_ia.result()}
        with ip_cache_lock:
            ip_cache[ip] = res_ip
        return res_ip

    dominios_resultado = []
    for dom, info in globales.items():
        ips = info["ips"]
        origen_str = ", ".join(info["nombres_origen"])
        if log_cb: log_cb(f"[+] '{origen_str}' -> Analizando: {dom} ({', '.join(ips)})")

        ips_data = {}
        for ip in ips:
            ips_data[ip] = enriquecer_ip(ip)

        if log_cb: log_cb(f"    [+] Consultando Abuse.ch, MXToolbox/DoH, RDAP/WHOIS e ISO en paralelo para {dom}...")
        with ThreadPoolExecutor(max_workers=5) as ex_dom:
            f_ach = ex_dom.submit(consultar_abusech, dom, ips, feodo_map)
            f_mx = ex_dom.submit(consultar_mxtoolbox, dom)
            f_dns = ex_dom.submit(consultar_dns_doh, dom)
            f_rdap = ex_dom.submit(consultar_rdap, dom)
            f_iso = ex_dom.submit(verificar_iso, dom)

            ach_res = f_ach.result()
            mx_res = f_mx.result()
            dns_res = f_dns.result()
            rdap_res = f_rdap.result()
            iso_res = f_iso.result()

        dns_ok = dns_res.get("_ok") or {}
        # Enriquecer MX/SPF/DMARC con DNS DoH directo si MXToolbox dio 429 o sin registros
        if dns_res["mx"] and (mx_res.get("mx", {}).get("estado") != "ok" or not mx_res.get("mx", {}).get("registros")):
            mx_res["mx"] = {"estado": "ok", "fuente": "Google DoH", "failed": [], "warnings": [], "passed": len(dns_res["mx"]), "registros": [{"clave": "MX", "valor": v} for v in dns_res["mx"]]}
        if mx_res.get("spf", {}).get("estado") != "ok" and (dns_res["spf"] or dns_ok.get("SPF")):
            spf_val = dns_res["spf"][0] if dns_res["spf"] else None
            fails = [] if spf_val else ["SPF Record Not Found"]
            if spf_val and re.search(r"\+all\b", spf_val, re.I): fails.append("SPF Permissive (+all)")
            mx_res["spf"] = {"estado": "ok", "fuente": "Google DoH", "failed": fails, "warnings": [], "passed": 1 if spf_val else 0, "registros": [{"clave": "SPF", "valor": spf_val}] if spf_val else []}
        elif dns_res["spf"] and not mx_res.get("spf", {}).get("registros"):
            mx_res["spf"]["registros"] = [{"clave": "SPF", "valor": dns_res["spf"][0]}]
        if mx_res.get("dmarc", {}).get("estado") != "ok" and (dns_res["dmarc"] or dns_ok.get("DMARC")):
            dm_val = dns_res["dmarc"][0] if dns_res["dmarc"] else None
            fails = [] if dm_val else ["DMARC Record Not Found"]
            warns = ["DMARC Policy Not Enabled (p=none)"] if (dm_val and re.search(r"p=none\b", dm_val, re.I)) else []
            mx_res["dmarc"] = {"estado": "ok", "fuente": "Google DoH", "failed": fails, "warnings": warns, "passed": 1 if dm_val else 0, "registros": [{"clave": "DMARC", "valor": dm_val}] if dm_val else []}
        elif dns_res["dmarc"] and not mx_res.get("dmarc", {}).get("registros"):
            mx_res["dmarc"]["registros"] = [{"clave": "DMARC", "valor": dns_res["dmarc"][0]}]
        ok_cmds = sum(1 for c in ["mx", "spf", "dmarc", "blacklist"] if mx_res.get(c, {}).get("estado") == "ok")
        mx_res["estado"] = "ok" if ok_cmds == 4 else "parcial" if ok_cmds > 0 else "no_disponible"

        dns_clean = {k: v for k, v in dns_res.items() if k != "_ok"}

        score, detalle = calcular_score(dom, ips_data, ach_res, mx_res, iso_res)
        nivel = "BAJO" if score < 25 else "MEDIO" if score < 50 else "ALTO" if score < 75 else "CRÍTICO"

        dominios_resultado.append({
            "nombre_origen": origen_str,
            "nombres_origen": info["nombres_origen"],
            "dominio": dom,
            "url": info["url"],
            "score": score,
            "nivel": nivel,
            "ips": ips,
            "certificados_iso": [n["norma"] for n in iso_res.get("normas", [])],
            "desglose": detalle,
            "estado_consultas": {
                "shodan": ips_data[ips[0]]["shodan"].get("estado") if ips else "no_disponible",
                "abuseipdb": ips_data[ips[0]]["abuseipdb"].get("estado") if ips else "no_disponible",
                "ipapi": ips_data[ips[0]]["ipapi"].get("estado") if ips else "no_disponible",
                "abusech": ach_res.get("estado"),
                "mxtoolbox": mx_res.get("estado"),
                "rdap": rdap_res.get("estado")
            },
            "hallazgos": {
                "por_ip": [
                    {
                        "ip": ip,
                        "shodan": ips_data[ip].get("shodan", {}),
                        "abuseipdb": ips_data[ip].get("abuseipdb", {}),
                        "ipapi": ips_data[ip].get("ipapi", {}),
                        "feodo": {"listada": ip in feodo_map, "malware": feodo_map.get(ip)}
                    } for ip in ips
                ],
                "abusech": ach_res,
                "mxtoolbox": mx_res,
                "dns_detalle": dns_clean,
                "rdap": rdap_res
            },
            "certificados_iso_detalle": iso_res
        })

    dominios_resultado.sort(key=lambda x: x["score"], reverse=True)

    # Resumen
    conteo_niveles = {"CRÍTICO": 0, "ALTO": 0, "MEDIO": 0, "BAJO": 0}
    for d in dominios_resultado:
        conteo_niveles[d["nivel"]] = conteo_niveles.get(d["nivel"], 0) + 1

    reporte_final = {
        "generado_en": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "resumen": {
            "nombres_procesados": len(nombres_unicos),
            "dominios_analizados": len(dominios_resultado),
            "sin_dominio_conteo": len(sin_dominio),
            "por_nivel": conteo_niveles
        },
        "dominios": dominios_resultado,
        "sin_dominio": sin_dominio
    }
    return reporte_final
