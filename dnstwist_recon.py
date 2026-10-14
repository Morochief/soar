#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
STELLAR CYBER SOAR — NATIVE DNS TWIST & TYPOSQUATTING HUNTER (CTI ENGINE)
===============================================================================
Descubrimiento activo y pasivo de dominios similares, suplantaciones de marca,
phishing, combo-squatting, homóglifos y permutaciones DNS para análisis de SOC.
100% Nativo en Python (Standard Library) con resolución multihilo concurrente.
===============================================================================
"""

import sys
import os
import re
import socket
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

# Asegurar salida UTF-8 sin fallos de códec en terminales Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

KEYBOARD_SUBSTITUTIONS = {
    'a': ['q', 'w', 's', 'z', '4'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'x', 'c'],
    'e': ['w', 'r', 's', 'd', '3'],
    'f': ['d', 'r', 't', 'g', 'c', 'v'],
    'g': ['f', 't', 'y', 'h', 'v', 'b'],
    'h': ['g', 'y', 'u', 'j', 'b', 'n'],
    'i': ['u', 'o', 'k', '8', '1', 'l'],
    'j': ['h', 'u', 'i', 'k', 'n', 'm'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p', '1', 'i'],
    'm': ['n', 'j', 'k'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'p', 'k', 'l', '0'],
    'p': ['o', 'l', '0'],
    'q': ['w', 'a', '1'],
    'r': ['e', 't', 'd', 'f', '4'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    't': ['r', 'y', 'f', 'g', '5'],
    'u': ['y', 'i', 'h', 'j', '7'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'e', 's', '2'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'u', 'g', 'h', '6'],
    'z': ['a', 's', 'x']
}

POPULAR_TLDS = [
    'com', 'net', 'org', 'info', 'biz', 'io', 'co', 'app', 'online', 'site',
    'vip', 'cc', 'to', 'me', 'pro', 'live', 'cm', 'is', 'xyz', 'top', 'club', 'bet'
]

PHISHING_KEYWORDS_SUFFIX = [
    '-login', '-signin', '-auth', '-portal', '-secure', '-app', '-mobile',
    '-account', '-verify', '-ag', 'ag', 's', '-soporte', '-online'
]

PHISHING_KEYWORDS_PREFIX = [
    'login-', 'secure-', 'app-', 'portal-', 'auth-', 'my-', 'the-'
]

# Servidores/IPs conocidos de protección de marcas o parking defensivo
DEFENSIVE_INDICATORS = [
    "safenames", "markmonitor", "csc", "corporatedomains", "sedoparking", "bodis",
    "hugedomains", "dan.com", "afternic", "domainmarket", "redirect.idp365.net"
]


def clean_domain_input(raw: str) -> str:
    """Limpia URLs o protocolos para obtener solo el FQDN base."""
    d = raw.strip()
    d = re.sub(r"^https?://", "", d, flags=re.IGNORECASE)
    d = d.rstrip("/").split("/")[0].split(":")[0]
    return d.lower()


def extract_domain_parts(fqdn: str):
    """Separa el nombre base y el TLD, soportando ccTLDs comunes como .com.py o .co.uk."""
    parts = fqdn.split(".")
    if len(parts) <= 1:
        return fqdn, ""
    
    # Manejo de dominios de 2do nivel (.com.py, .co.uk, .gov.ar, etc.)
    cc_second_levels = {"com", "edu", "gov", "gob", "org", "net", "co", "mil", "nom"}
    if len(parts) >= 3 and parts[-2] in cc_second_levels:
        name = ".".join(parts[:-2])
        tld = ".".join(parts[-2:])
    else:
        name = ".".join(parts[:-1])
        tld = parts[-1]
    
    # Si el nombre contiene subdominios (ej. www.betonline), usamos la última parte como marca
    brand = name.split(".")[-1]
    return brand, tld


def generate_permutations(brand: str, tld: str) -> dict:
    """
    Genera permutaciones estructuradas por categoría.
    Retorna un diccionario { fqdn: category }.
    """
    perms = {}
    orig_fqdn = f"{brand}.{tld}"

    def _add(cand_brand, cand_tld, category):
        cand = f"{cand_brand}.{cand_tld}".lower()
        if cand != orig_fqdn and cand not in perms:
            perms[cand] = category

    # 1. Omisión (Omission: falta 1 letra)
    for i in range(len(brand)):
        omitted = brand[:i] + brand[i+1:]
        if len(omitted) >= 3:
            _add(omitted, tld, "Omisión de Carácter")

    # 2. Reemplazo de teclas adyacentes (Typo / Replacement)
    for i, char in enumerate(brand):
        if char in KEYBOARD_SUBSTITUTIONS:
            for rep in KEYBOARD_SUBSTITUTIONS[char]:
                subbed = brand[:i] + rep + brand[i+1:]
                _add(subbed, tld, "Reemplazo de Tecla")

    # 3. Doble letra (Double letter)
    for i in range(len(brand)):
        doubled = brand[:i] + brand[i] + brand[i:]
        _add(doubled, tld, "Repetición de Letra")

    # 4. Transposición (Swap de caracteres contiguos)
    for i in range(len(brand) - 1):
        swapped = brand[:i] + brand[i+1] + brand[i] + brand[i+2:]
        _add(swapped, tld, "Transposición")

    # 5. Homóglifos visuales comunes
    homo_map = {
        'o': ['0'],
        'l': ['1', 'i'],
        'i': ['1', 'l'],
        'm': ['rn', 'nn'],
        'w': ['vv']
    }
    for i, char in enumerate(brand):
        if char in homo_map:
            for h in homo_map[char]:
                homo_brand = brand[:i] + h + brand[i+1:]
                _add(homo_brand, tld, "Homóglifo Visual")

    # 6. Combo-squatting y Cosechadores de Credenciales (Prefijos y Sufijos de Phishing)
    for pfx in PHISHING_KEYWORDS_PREFIX:
        _add(f"{pfx}{brand}", tld, "Phishing (Prefijo Clave)")
        _add(f"{pfx}{brand}", "com", "Phishing Combo (.com)")

    for sfx in PHISHING_KEYWORDS_SUFFIX:
        _add(f"{brand}{sfx}", tld, "Phishing (Sufijo Clave)")
        _add(f"{brand}{sfx}", "com", "Phishing Combo (.com)")

    # Combo específico con el TLD original (ej. betonline-ag.com)
    if tld and tld != "com":
        _add(f"{brand}-{tld}", "com", "Combo-Squatting TLD Oficial")
        _add(f"{brand}{tld}", "com", "Combo-Squatting TLD Oficial")

    # 7. Suplantación de TLD (TLD Swap en dominios populares)
    for alt_tld in POPULAR_TLDS:
        if alt_tld != tld:
            _add(brand, alt_tld, "Suplantación de TLD")

    return perms


def resolve_single_domain(item):
    """Resuelve un único dominio (A, NS) con timeout estricto."""
    fqdn, category = item
    res = {
        "fqdn": fqdn,
        "category": category,
        "ip": None,
        "ns": [],
        "isp": "",
        "ptr": "",
        "classification": "INACTIVO"
    }

    try:
        # Resolución A rápida
        ip = socket.gethostbyname(fqdn)
        res["ip"] = ip
        res["classification"] = "ACTIVO"
    except Exception:
        # Dominio inactivo / no resuelve
        return None

    # Resolución inversa PTR rápida
    try:
        ptr = socket.gethostbyaddr(ip)[0]
        res["ptr"] = ptr
    except Exception:
        res["ptr"] = ""

    return res


def fetch_ip_info_batch(ips: set) -> dict:
    """Consulta rápida de ASN / Organización para las IPs descubiertas."""
    ip_info = {}
    for ip in ips:
        if not ip:
            continue
        try:
            url = f"https://ipinfo.io/{ip}/json"
            req = urllib.request.Request(url, headers={"User-Agent": "SOAR-DNSTwist-Engine/1.0"})
            with urllib.request.urlopen(req, timeout=3.0) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                org = data.get("org", "Desconocido")
                country = data.get("country", "")
                hostname = data.get("hostname", "")
                ip_info[ip] = {
                    "org": org,
                    "country": country,
                    "hostname": hostname
                }
        except Exception:
            ip_info[ip] = {"org": "Consulta Fallida / Timeout", "country": "", "hostname": ""}
    return ip_info


def classify_threat(fqdn: str, ip: str, info: dict, category: str) -> tuple:
    """
    Clasifica el riesgo de la amenaza:
    - 🚨 CRÍTICO (Phishing Cosechador de Credenciales / APK / App)
    - ⚠️ ALERTA (Typosquatting Activo en Hosting Comercial)
    - 🛡️ DEFENSIVO / PARKING (Protección de Marca o Parking de Dominio)
    """
    fqdn_lower = fqdn.lower()
    org_str = (info.get("org", "") + " " + info.get("hostname", "")).lower()

    # Comprobar si es un parking o protección corporativa
    for dind in DEFENSIVE_INDICATORS:
        if dind in org_str:
            return "🛡️ DEFENSIVO / PARKING", "Registro preventivo o parking de marca (Safenames/Sedo/MarkMonitor)"

    # Phishing de alto riesgo
    phish_tokens = ["login", "signin", "auth", "secure", "portal", "verify", "account", "app", "mobile"]
    for pt in phish_tokens:
        if pt in fqdn_lower:
            return "🚨 CRÍTICO - PHISHING", f"Cosechador de credenciales / suplantación activa ({pt})"

    if "Combo-Squatting" in category:
        return "🚨 ALTO - COMBO SQUAT", "Suplantación de TLD oficial en .com (engaño de usuario)"

    if "Reemplazo" in category or "Omisión" in category or "Homóglifo" in category:
        return "⚠️ ALERTA - TYPOSQUAT", "Permutación tipográfica activa apuntando a hosting externo"

    return "⚠️ ALERTA - LOOKALIKE", "Dominio homónimo activo bajo otro TLD"


def run_dnstwist_recon(target: str, max_workers: int = 40):
    """Ejecutor principal del motor de detección de typosquatting."""
    clean_target = clean_domain_input(target)
    brand, tld = extract_domain_parts(clean_target)

    print("=" * 80)
    print("🌀 STELLAR CYBER SOAR — HUNTER DE TYPOSQUATTING & DNS TWIST")
    print(f"[*] Marca / Base analizada : {brand.upper()}")
    print(f"[*] Dominio Legítimo Base  : {clean_target}")
    print(f"[*] Hilos concurrentes    : {max_workers}")
    print("=" * 80)

    print(f"\n[1/4] Generando permutaciones heurísticas avanzadas...")
    perms = generate_permutations(brand, tld)
    print(f"      -> {len(perms)} variaciones generadas (omisión, teclado, homóglifos, combos, TLDs).")

    print(f"\n[2/4] Resolviendo consultas DNS multihilo en tiempo real...")
    active_results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {executor.submit(resolve_single_domain, item): item for item in perms.items()}
        for future in as_completed(future_map):
            res = future.result()
            if res and res.get("ip"):
                active_results.append(res)
                # Notificación en tiempo real
                print(f"  [+] Resuelto: {res['fqdn']:<30} -> {res['ip']:<15} ({res['category']})")

    print(f"\n[3/4] Enriqueciendo Threat Intelligence de infraestructura para {len(active_results)} activos...")
    unique_ips = {r["ip"] for r in active_results if r["ip"]}
    ip_intel = fetch_ip_info_batch(unique_ips)

    # Clasificación final
    for r in active_results:
        info = ip_intel.get(r["ip"], {})
        r["isp"] = info.get("org", "N/A")
        r["country"] = info.get("country", "")
        level, reason = classify_threat(r["fqdn"], r["ip"], info, r["category"])
        r["risk_level"] = level
        r["risk_reason"] = reason

    # Ordenar por severidad de riesgo
    def _sort_key(item):
        if "CRÍTICO" in item["risk_level"]:
            return 1
        elif "ALTO" in item["risk_level"]:
            return 2
        elif "ALERTA" in item["risk_level"]:
            return 3
        return 4

    active_results.sort(key=_sort_key)

    print("\n" + "=" * 80)
    print(f"📊 MATRIZ FORENSE DE AMENAZAS ENCONTRADAS ({len(active_results)} DOMINIOS ACTIVOS)")
    print("=" * 80)

    if not active_results:
        print("  [+] Excelente noticia: No se detectaron permutaciones activas registradas.")
        print("      Tu marca no presenta indicios evidentes de typosquatting o suplantación activa.")
    else:
        for idx, r in enumerate(active_results, start=1):
            print(f"\n[{idx:02d}] {r['risk_level']}")
            print(f"     Dominio Falso : {r['fqdn']}")
            print(f"     Dirección IP  : {r['ip']} ({r['country']})")
            print(f"     ISP / Hosting : {r['isp']}")
            print(f"     Técnica Usada : {r['category']}")
            print(f"     Diagnóstico   : {r['risk_reason']}")
            print(f"     Pivot VirusTotal : https://www.virustotal.com/gui/domain/{r['fqdn']}")
            print(f"     Pivot URLScan    : https://urlscan.io/search/#page.domain%3A{r['fqdn']}")

    print("\n" + "=" * 80)
    print("🔗 RECOMENDACIONES DE RESPUESTA A INCIDENTES (DFIR / CTI):")
    print(" 1. Bloquear en Firewall/Proxy/EDR los dominios catalogados como CRÍTICO o ALTO.")
    print(" 2. Enviar solicitudes de Takedown (abuso) a los registradores (GoDaddy, Cloudflare, Namecheap).")
    print(" 3. Evaluar la compra defensiva de variaciones aún no registradas para blindar la marca.")
    print("=" * 80)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python dnstwist_recon.py <dominio_o_url>")
        print("Ejemplo: python dnstwist_recon.py betonline.ag")
        sys.exit(1)

    target_domain = sys.argv[1]
    run_dnstwist_recon(target_domain)
