import json
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('G:/SOC/soar/Analista SOC/Reportes/inventario_filtros_activos.json', encoding='utf-8') as f:
    filters = json.load(f)

print(f"Total de filtros analizados: {len(filters)}\n")

blind_spots = []
for f in filters:
    fid = f.get('id')
    num = f.get('num')
    dev = f.get('dev_type')
    rules = f.get('rules', {})
    
    issues = []
    severity = "INFO"
    rule_keys = set(rules.keys())
    
    # 1. Silenciamiento completo de una IP (Ceguera Total sobre el Host)
    if rule_keys == {'srcip'} or rule_keys == {'dstip'}:
        severity = "CRITICA"
        issues.append("CEGUERA TOTAL DEL HOST: Silencia una IP completa sin restringir puerto, aplicacion ni servicio. Cualquier ataque, compromiso o malware desde/hacia esta IP quedara 100% invisible para el SOC.")
    
    # 2. Descarte global de puertos o protocolos sin limitar hosts
    if rule_keys == {'dstport'} or rule_keys == {'proto'}:
        severity = "ALTA"
        issues.append(f"DESCARTE GLOBAL DE PUERTO/PROTOCOLO: Descarta {list(rules.keys())[0]} en TODA la red sin importar el origen o destino. Puede ocultar escaneos o canales C2 en esos puertos.")
        
    # 3. Descarte de protocolos web/cifrados genericos (HTTPS, SSL, QUIC) sin dominio ni destino
    if 'appid_name' in rules:
        apps = rules['appid_name'].get('value', [])
        if any(a.upper() in ['HTTPS', 'SSL', 'QUIC', 'HTTP'] for a in apps):
            if 'dstip' not in rules and 'domain_list' not in rules:
                severity = "CRITICA"
                issues.append(f"DESCARTE CIEGO DE PROTOCOLO WEB ({apps}): Filtra tráfico web/cifrado sin especificar dominio ni destino benigno. Cualquier exfiltración o baliza C2 por estos protocolos queda silenciada.")
    
    # 4. Descarte de denegaciones (Action Deny) sin aplicacion ni destino benigno
    if 'action' in rules and any(a.lower() == 'deny' for a in rules['action'].get('value', [])):
        if 'appid_name' not in rules and 'dstip' not in rules:
            severity = "ALTA"
            issues.append("DESCARTE CIEGO DE DENEGACIONES: Descarta 'deny' sin especificar aplicación ni destino benigno. Oculta escaneos perimetrales, ataques bloqueados y beacons hacia C2.")
        elif 'appid_name' not in rules:
            if severity != "CRITICA": severity = "MEDIA"
            issues.append("DENEGACION SIN APLICACION: Descarta 'deny' limitando IP/puerto pero sin firma L7.")

    # 5. Rangos masivos de red (CIDR /16, /8)
    for k in ['srcip', 'dstip']:
        if k in rules:
            for ip in rules[k].get('value', []):
                if '/16' in ip or '/8' in ip or '/12' in ip:
                    if severity not in ["CRITICA"]: severity = "ALTA"
                    issues.append(f"SUBNET MASIVA ({ip}): Abarca miles de hosts. Riesgo de silenciar tráfico imprevisto.")

    # 6. Descarte por 'computer_name' amplio o regex
    if 'computer_name' in rules:
        val = rules['computer_name'].get('value', [])
        op = rules['computer_name'].get('op', '')
        if op == 'contains' and any(len(v) < 6 for v in val):
            if severity not in ["CRITICA", "ALTA"]: severity = "MEDIA"
            issues.append(f"FILTRADO POR NOMBRE AMPLIO: computer_name {op} {val}")

    if issues:
        blind_spots.append({
            "num": num,
            "id": fid,
            "dev": dev,
            "severity": severity,
            "rules": rules,
            "issues": issues
        })

print(f"Se identificaron {len(blind_spots)} filtros con riesgos de ceguera para el SOC:\n")
# Ordenar por severidad
sev_order = {"CRITICA": 0, "ALTA": 1, "MEDIA": 2, "INFO": 3}
blind_spots.sort(key=lambda x: (sev_order.get(x['severity'], 9), x['num']))

for bs in blind_spots:
    print(f"[{bs['severity']}] Filtro #{bs['num']} (ID: {bs['id']}) - Dev: {bs['dev']}")
    print(f"  Reglas: {json.dumps(bs['rules'], ensure_ascii=False)}")
    for iss in bs['issues']:
        print(f"  -> {iss}")
    print()
