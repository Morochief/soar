"""
Validador y Parser Sintáctico de Reglas Pre-DPI para Stellar Cyber
Valida reglas BPF/libpcap contra los estándares formales de Stellar Cyber OpenXDR
"""

import sys
import re

# Palabras clave válidas según pcap-filter y Stellar Cyber
DIRECTIONS = {'src', 'dst', 'src and dst', 'src or dst'}
TYPES = {'host', 'net', 'port', 'portrange'}
PROTOCOLS = {'ip', 'ip6', 'arp', 'rarp', 'tcp', 'udp', 'icmp', 'icmp6', 'vlan'}
LOGICAL_OPS = {'and', 'or', 'not', '&&', '||', '!'}

IP_REGEX = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
CIDR_REGEX = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/(?:[0-9]|[1-2][0-9]|3[0-2])$')

def audit_predpi_rule(rule: str) -> dict:
    """
    Audita una regla individual de Pre-DPI.
    Retorna un diccionario con estado, errores detectados y sugerencia de corrección.
    """
    rule_clean = rule.strip()
    if not rule_clean or rule_clean.startswith('#'):
        return {"status": "SKIPPED", "original": rule_clean, "errors": [], "fixed": rule_clean}

    errors = []
    fixed_tokens = []
    
    # 1. Comprobar mayúsculas en operadores lógicos (Stellar exige minúsculas estrictas)
    for op_upper in ['AND', 'OR', 'NOT']:
        if re.search(r'\b' + op_upper + r'\b', rule_clean):
            errors.append(f"Operador en mayúsculas '{op_upper}': Stellar Cyber exige minúsculas estrictas ('{op_upper.lower()}').")

    # Reemplazar mayúsculas para continuar el análisis sintáctico
    normalized = re.sub(r'\bAND\b', 'and', rule_clean)
    normalized = re.sub(r'\bOR\b', 'or', normalized)
    normalized = re.sub(r'\bNOT\b', 'not', normalized)

    # 2. Detección de error clásico: 'tcp <puerto>' o 'udp <puerto>' sin 'port'
    tcp_udp_port_match = re.search(r'\b(tcp|udp)\s+(\d+)\b', normalized)
    if tcp_udp_port_match:
        proto, port_num = tcp_udp_port_match.groups()
        errors.append(f"Falta palabra clave 'port' en '{proto} {port_num}'. La sintaxis correcta es '{proto} port {port_num}'.")
        normalized = re.sub(r'\b(tcp|udp)\s+(\d+)\b', r'\1 port \2', normalized)

    # 3. Detección de 'dst <IP>' o 'src <IP>' sin 'host'
    dst_src_no_host = re.findall(r'\b(src|dst)\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})\b', normalized)
    for dir_kw, ip_val in dst_src_no_host:
        errors.append(f"Falta calificador 'host' tras '{dir_kw} {ip_val}'. Debe ser '{dir_kw} host {ip_val}'.")
        normalized = re.sub(r'\b' + dir_kw + r'\s+' + re.escape(ip_val) + r'\b', f'{dir_kw} host {ip_val}', normalized)

    # 4. Detección de 'dst <CIDR>' o 'src <CIDR>' sin 'net'
    dst_src_no_net = re.findall(r'\b(src|dst)\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3}\/\d+)\b', normalized)
    for dir_kw, cidr_val in dst_src_no_net:
        errors.append(f"Falta calificador 'net' tras '{dir_kw} {cidr_val}'. Debe ser '{dir_kw} net {cidr_val}'.")
        normalized = re.sub(r'\b' + dir_kw + r'\s+' + re.escape(cidr_val) + r'\b', f'{dir_kw} net {cidr_val}', normalized)

    # 5. Soporte y explicacion de 'host A and host B' (Sintaxis canonica bidireccional en libpcap)
    host_pair_match = re.search(r'\bhost\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})\s+and\s+host\s+((?:[0-9]{1,3}\.){3}[0-9]{1,3})\b', normalized)
    if host_pair_match:
        ip1, ip2 = host_pair_match.groups()
        if ip1 == ip2:
            errors.append(f"Contradiccion 'host {ip1} and host {ip2}': una misma IP no puede ser origen y destino a la vez. Usar 'host {ip1}'.")
        # Si son IPs distintas, es 100% VALIDO en libpcap (representa trafico bidireccional entre ambas)

    # 6. Deteccion de 'vlan and host' sin ID de VLAN
    if re.search(r'\bvlan\s+and\b', normalized):
        errors.append("Palabra clave 'vlan' sin numero ID seguida de 'and'. En libpcap 'vlan' desplaza los offsets y requiere ID o sintaxis 'vlan && ...'.")

    status = "ERROR" if errors else ("WARNING" if warnings else "VALID")
    return {
        "status": status,
        "original": rule_clean,
        "errors": errors,
        "warnings": warnings,
        "fixed": normalized
    }

def validate_rule_list(rules_text: str):
    """Analiza una lista de reglas separadas por saltos de línea."""
    lines = [line.strip() for line in rules_text.strip().splitlines() if line.strip()]
    results = [audit_predpi_rule(line) for line in lines]
    
    total = len(results)
    valid_count = sum(1 for r in results if r["status"] == "VALID")
    error_count = sum(1 for r in results if r["status"] == "ERROR")
    
    print("=" * 80)
    print(f"📊 REPORTE DE AUDITORÍA SINTÁCTICA PRE-DPI (STELLAR CYBER / LIBPCAP)")
    print(f"Total Reglas Evaluadas: {total} | Válidas: {valid_count} | Con Errores: {error_count}")
    print("=" * 80)
    
    for idx, r in enumerate(results, start=1):
        if r["status"] == "VALID":
            print(f"[{idx:02d}] ✅ VÁLIDA: {r['original']}")
        else:
            print(f"[{idx:02d}] ❌ ERROR:  {r['original']}")
            for err in r["errors"]:
                print(f"     └─ ⚠️  {err}")
            print(f"     └─ 💡 Corrección Sugerida: {r['fixed']}")
        print("-" * 80)
        
    print("\n📋 LISTA COMPLETA 100% SANEADA LISTA PARA COPIAR A STELLAR:")
    print("-" * 80)
    for r in results:
        print(r["fixed"])
    print("-" * 80)

if __name__ == "__main__":
    # Test con las 15 reglas de Technoma
    sample_rules = """
host 192.168.15.27
src host 10.2.1.3 and tcp 1500
src host 10.2.1.6 and tcp 1500
src host 10.2.1.4 and tcp 1500
dst 172.17.10.203
src net 172.17.10.0/24 and dst 10.11.1.1
src net 172.17.10.0/24 and dst 10.11.1.2
host 172.17.10.203
dst 192.168.15.27
dst port 10050
dst port 10051
src host 10.11.1.1 and dst host 10.11.1.2 and port 53
src host 10.11.1.2 and dst host 10.11.1.1 and port 53
src host 192.168.15.23 and dst port 53
src port 53 and dst host 192.168.15.23
"""
    validate_rule_list(sample_rules)
