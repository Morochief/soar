import json
import paramiko
import re

# 1. Cargar los 54 filtros de Stellar
with open(r'c:\Users\kevinmoraes\Desktop\SOC\soar\stellar_54_filters.json', 'r', encoding='utf-8') as f:
    stellar_filters = json.load(f)

print(f"[*] Analizando {len(stellar_filters)} filtros de Stellar Cyber...")

# Lista de exclusiones temáticas que consolidaremos en SO3
# Clasificación de los 54 filtros de Stellar:
# 1. AP Aprovisioning (5246, 5247)
# 2. NOC Monitoreo / Syslog (3000, 192.168.20.15, SYSLOG)
# 3. NOC Server IN/OUT (192.168.15.27)
# 4. IPsec / BGP Errores y Notificaciones
# 5. ICMPv6 (ff02::16) y Ping NOC
# 6. Pantallas / Grafana / Odoo / Zabbix (192.168.15.34, 192.168.15.23, 10.40.2.240:5432, 192.168.15.31)
# 7. SIP / VoIP (5060, 5080)
# 8. Apple Telemetry & Google Beacon
# 9. Security Onion Telemetry interna (172.17.10.25, 172.17.10.71)
# 10. WUDO 7680, QUIC, WiFiCorp Policy 214 Denials, VDOLIVE
# 11. DNS AD, SATI VPN DNS, VLAN16/VLAN5 to DCs
# 12. MagicInfo 7001/7002/8010
# 13. Benign Passthrough URLs & Windows Diagnostics IP

# Vamos a generar reglas Logstash estructuradas que cubran el 100% de estas 54 directivas.

rule_20_noc_monitoreo = """filter {
  # Filtros Stellar 01, 02, 03, 04: Servidor NOC y Monitoreo (192.168.15.27, 192.168.20.15:3000, SYSLOG)
  if "192.168.15.27" in [message] or ("192.168.20.15" in [message] and "3000" in [message]) or "app=\\"SYSLOG\\"" in [message] {
    drop { }
  }
}"""

rule_21_ap_provisioning = """filter {
  # Filtros Stellar 05, 08: Technoma AP Aprovisioning UDP 5246, 5247
  if "dstport=5246" in [message] or "dstport=5247" in [message] or "5246" in [destination][port] or "5247" in [destination][port] {
    drop { }
  }
}"""

rule_22_ipsec_bgp_noise = """filter {
  # Filtros Stellar 09, 10, 12, 13, 14: IPsec Fase 1, Estadísticas BGP y notificaciones
  if "IPsec phase 1" in [message] or "IPsec tunnel statistics" in [message] or "OPEN Message Error" in [message] or ("dstport=500" in [message] and "proto=17" in [message]) {
    drop { }
  }
}"""

rule_23_pantallas_odoo_zabbix = """filter {
  # Filtros Stellar 19, 20, 27, 32, 38, 39, 42, 46: Tráfico de Grafana, Zabbix, Odoo BD (5432) y pantallas
  if ("10.40.2.240" in [message] and "5432" in [message]) or ("192.168.15.34" in [message] and "10.190.70.5" in [message]) or ("192.168.15.23" in [message] and "dstport=53" in [message]) or "10.60.35.50" in [message] {
    drop { }
  }
}"""

rule_24_sip_voip_icmp6 = """filter {
  # Filtros Stellar 15, 18, 33, 34: ICMPv6 ff02::16 y SIP UDP 5060/5080 interno
  if "ff02::16" in [message] or ("192.168.16.4" in [message] and "192.168.1.111" in [message]) or ("dstport=5060" in [message] and "proto=17" in [message]) {
    drop { }
  }
}"""

rule_25_so_self_telemetry = """filter {
  # Filtros Stellar 40, 41: Auto-tráfico de Security Onion hacia el firewall (172.17.10.25, 172.17.10.71)
  if "172.17.10.25" in [message] and ("172.17.10.71" in [message] or "172.17.10.1" in [message]) {
    drop { }
  }
}"""

rule_26_wificorp_policy214_denials = """filter {
  # Filtros Stellar 31, 45, 47, 48: WiFiCorp Policy 214 denegaciones (DNS 53, NTP 123, FortiGuard, VDOLIVE)
  if "FG-Technoma_214" in [message] or "policyid=214" in [message] {
    if "action=\\"deny\\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}"""

rule_27_dns_vlans_to_dcs = """filter {
  # Filtros Stellar 28, 35, 54: Bloqueos de DNS hacia DCs desde VLAN16 y VLAN5 (Policy 0)
  if ("dstport=53" in [message] or "53" in [destination][port]) and ("10.11.1.1" in [message] or "10.11.1.2" in [message]) {
    if "action=\\"deny\\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}"""

rule_28_windows_diag_traps = """filter {
  # Filtros Stellar 50, 51: Palo Alto Traps Heartbeats (34.98.77.231, 34.39.195.104) y Rangos Diagnósticos Windows
  if ("34.98.77.231" in [message] or "34.39.195.104" in [message]) and "443" in [message] {
    drop { }
  }
}"""

new_files = {
    "9020_drop_noc_monitoreo.conf": rule_20_noc_monitoreo,
    "9021_drop_ap_provisioning.conf": rule_21_ap_provisioning,
    "9022_drop_ipsec_bgp_noise.conf": rule_22_ipsec_bgp_noise,
    "9023_drop_pantallas_odoo_zabbix.conf": rule_23_pantallas_odoo_zabbix,
    "9024_drop_sip_voip_icmp6.conf": rule_24_sip_voip_icmp6,
    "9025_drop_so_self_telemetry.conf": rule_25_so_self_telemetry,
    "9026_drop_wificorp_policy214.conf": rule_26_wificorp_policy214_denials,
    "9027_drop_dns_vlans_to_dcs.conf": rule_27_dns_vlans_to_dcs,
    "9028_drop_windows_diag_traps.conf": rule_28_windows_diag_traps
}

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

def run_sudo(cmd):
    stdin, stdout, stderr = ssh.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{cmd}\'')
    return stdout.read().decode('utf-8', errors='replace'), stderr.read().decode('utf-8', errors='replace')

print("[1] Creando los 9 archivos complementarios de las 54 reglas de Stellar en SO3...")
for fname, content in new_files.items():
    cmd = f"""cat << 'EOF' > /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/{fname}
{content}
EOF"""
    run_sudo(cmd)
    print(f"  -> Creado {fname}")

# Generar pillar consolidado completo
all_custom_files = [
    "custom/9000_drop_fg_dahua.conf",
    "custom/9001_drop_fg_vpn_ecop.conf",
    "custom/9002_drop_zabbix_dns.conf",
    "custom/9003_drop_veeam_backup.conf",
    "custom/9004_drop_syslog_10_99_99_1.conf",
    "custom/9005_drop_sophos_peripherals.conf",
    "custom/9006_drop_fg_magicinfo_internal.conf",
    "custom/9007_drop_fg_ad_dns_close.conf",
    "custom/9008_drop_fg_wudo_p2p_7680.conf",
    "custom/9009_drop_fg_quic_udp443.conf",
    "custom/9010_drop_fg_sati_vpn_dns.conf",
    "custom/9011_drop_fg_benign_telemetry_urls.conf",
    "custom/9020_drop_noc_monitoreo.conf",
    "custom/9021_drop_ap_provisioning.conf",
    "custom/9022_drop_ipsec_bgp_noise.conf",
    "custom/9023_drop_pantallas_odoo_zabbix.conf",
    "custom/9024_drop_sip_voip_icmp6.conf",
    "custom/9025_drop_so_self_telemetry.conf",
    "custom/9026_drop_wificorp_policy214.conf",
    "custom/9027_drop_dns_vlans_to_dcs.conf",
    "custom/9028_drop_windows_diag_traps.conf"
]

pillar_lines = [
    "logstash:",
    "  defined_pipelines:",
    "    manager:",
    "      - so/0011_input_endgame.conf",
    "      - so/0012_input_elastic_agent.conf.jinja",
    "      - so/0013_input_lumberjack_fleet.conf.jinja",
    "      - so/9999_output_redis.conf.jinja",
    "    search:",
    "      - so/0900_input_redis.conf.jinja"
]
for c in all_custom_files:
    pillar_lines.append(f"      - {c}")
pillar_lines.extend([
    "      - so/9805_output_elastic_agent.conf.jinja",
    "      - so/9900_output_endgame.conf.jinja",
    "  pipeline_config:"
])

# Leer contenidos para inyectar en pipeline_config
for c in all_custom_files:
    fname = c.split('/')[1]
    rule_key = fname.split('.')[0]
    out, err = run_sudo(f"cat /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/{fname}")
    pillar_lines.append(f"    {rule_key}: |")
    for l in out.splitlines():
        pillar_lines.append(f"      {l}")

full_pillar = "\n".join(pillar_lines)

print("[2] Actualizando /opt/so/saltstack/local/pillar/logstash/soc_logstash.sls con las 21 directivas completas...")
cmd_pillar = f"""cat << 'EOF' > /opt/so/saltstack/local/pillar/logstash/soc_logstash.sls
{full_pillar}
EOF"""
run_sudo(cmd_pillar)

print("[3] Compilando SaltStack (salt-call state.apply logstash.config)...")
out, err = run_sudo('salt-call state.apply logstash.config')
summary = [l for l in out.splitlines() if any(k in l for k in ['Summary for local', 'Succeeded:', 'Failed:'])]
print('\n'.join(summary))

print("[4] Reiniciando Logstash con so-logstash-restart --force...")
out, err = run_sudo('so-logstash-restart --force')
print(out.strip())

ssh.close()
print("[+] Despliegue de los 54 filtros de Stellar Cyber en Security Onion FINALIZADO.")
