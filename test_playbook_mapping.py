import csv, re

def map_playbook(name, cat, desc, tactic, tech):
    text = f"{name} {cat} {desc} {tactic} {tech}".lower()
    
    # Specific high-confidence mappings
    if 'dns' in text and ('tunnel' in text or 'tuneliz' in text):
        return "PB-5.6 (Tunelización DNS)", "5.6 - Sistema Comprometido (Tunelización DNS)"
    if 'large upload' in text or 'exfiltration' in text or 'data leak' in text or 'fuga' in text:
        return "PB-5.6 (Exfiltración de Datos)", "5.6 - Exfiltración de Datos (Genérico)"
    if 'port scan' in text or 'port sweep' in text or 'nmap' in text or 'discovery' in text or 'reconnaissance' in text:
        return "PB-2.4 (Escaneo y Reconocimiento)", "2.4 - Escaneo de Puertos y/o Vulnerabilidades"
    if 'tor' in text or 'c2' in text or 'command and control' in text or 'beacon' in text:
        return "PB-5.6 (Comunicación C2)", "5.6 - Comunicación con Servidor de Comando y Control (C2)"
    if 'privilege' in text or 'uac' in text or 'escalada' in text or 'elevation' in text:
        return "PB-5.6 (Escalada de Privilegios)", "5.6 - Detección de Escalada de Privilegios"
    if 'failed connections' in text or 'lateral' in text or 'remote service' in text or 'smb' in text:
        return "PB-5.6.1 (Movimiento Lateral)", "5.6.1 - Detección y Respuesta a Movimiento Lateral"
    if 'ransomware' in text or 'encrypt' in text or 'cifrado' in text:
        return "PB-1.1 (Ransomware)", "1.1 - Infecciones por Ransomware"
    if 'malware' in text or 'wildfire' in text or 'dropper' in text or 'trojan' in text or 'pup' in text or 'game' in text or 'minecraft' in text or 'counter-strike' in text or 'roblox' in text:
        return "PB-1.2 (Malware General y PUP)", "1.2 - Infecciones por Malware General"
    if 'firewall' in text or 'bypass' in text or 'security measures' in text or 'wdac' in text or 'defense evasion' in text:
        return "PB-5.2 (Evasión / Configuración)", "5.2 - Problemas de Configuración y Servicios Vulnerables"
    if 'ssh' in text or 'unusual' in text or 'network' in text:
        return "PB-2.2 (Comportamiento en Red)", "2.2 - Respuesta a Comportamiento Malicioso en la Red"
    if 'startup' in text or 'persistence' in text or '.lnk' in text:
        return "PB-1.2 (Persistencia / Malware)", "1.2 - Infecciones por Malware General"
    if 'execution' in text or 'powershell' in text or 'lolbin' in text:
        return "PB-1.2 (Ejecución Sospechosa)", "1.2 - Infecciones por Malware General"
    if 'brute force' in text or 'login' in text or '4625' in text or 'credential' in text:
        return "PB-7.1 (Fuerza Bruta / Login)", "7.1 - Intentos Fallidos de Login (SMB_RDP_SO)"
    
    return "PB-2.2 (Monitoreo de Red)", "2.2 - Respuesta a Comportamiento Malicioso en la Red"

# Test on Cases
with open('XDR_Cases_2026-10-02T12_19_18.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    cases = list(csv.DictReader(f, delimiter='\t'))

pb_case_counts = {}
for c in cases:
    code, full = map_playbook(c['Case Name'], '', '', '', '')
    pb_case_counts[code] = pb_case_counts.get(code, 0) + 1

print("Playbook mapping para Cases (205):")
for k, v in sorted(pb_case_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {k}: {v}")
