import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

def run_sudo(cmd):
    stdin, stdout, stderr = ssh.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{cmd}\'')
    return stdout.read().decode('utf-8', errors='replace'), stderr.read().decode('utf-8', errors='replace')

# 1. Definir los nuevos filtros custom
filters = {
    "9006_drop_fg_magicinfo_internal.conf": """filter {
  if [rule][ruleset] == "FG-Technoma_320" or "FG-Technoma_320" in [message] or "policyid=320" in [message] or "192.168.15.50" in [message] {
    if "7002" in [message] or "7001" in [message] {
      drop { }
    }
  }
}""",
    "9007_drop_fg_ad_dns_close.conf": """filter {
  if [rule][ruleset] == "FG-Technoma_74" or "FG-Technoma_74" in [message] or "policyid=74" in [message] {
    if "dstport=53" in [message] and ("10.11.1.1" in [message] or "10.11.1.2" in [message]) {
      drop { }
    }
  }
}""",
    "9008_drop_fg_wudo_p2p_7680.conf": """filter {
  if "dstport=7680" in [message] or "7680" in [destination][port] {
    if "action=\\"deny\\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}""",
    "9009_drop_fg_quic_udp443.conf": """filter {
  if "appid=\\"QUIC\\"" in [message] or "proto=17" in [message] {
    if "dstport=443" in [message] and ("action=\\"deny\\"" in [message] or [rule][action] == "deny") {
      drop { }
    }
  }
}""",
    "9010_drop_fg_sati_vpn_dns.conf": """filter {
  if "10.212.134." in [message] and "dstport=53" in [message] {
    if "action=\\"deny\\"" in [message] or [rule][action] == "deny" {
      drop { }
    }
  }
}""",
    "9011_drop_fg_benign_telemetry_urls.conf": """filter {
  if "action=\\"passthrough\\"" in [message] {
    if "stellarcyber.cloud" in [message] or "paloaltonetworks.com" in [message] or "microsoft.com" in [message] or "windowsupdate.com" in [message] or "google.com" in [message] or "cloudflareclient.com" in [message] {
      drop { }
    }
  }
}"""
}

print("[1] Creando los 6 nuevos archivos de filtros en /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/...")
for fname, content in filters.items():
    cmd = f"""cat << 'EOF' > /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/{fname}
{content}
EOF"""
    run_sudo(cmd)
    print(f"  -> Creado {fname}")

# 2. Actualizar soc_logstash.sls con las 12 reglas
pillar_content = """logstash:
  defined_pipelines:
    manager:
      - so/0011_input_endgame.conf
      - so/0012_input_elastic_agent.conf.jinja
      - so/0013_input_lumberjack_fleet.conf.jinja
      - so/9999_output_redis.conf.jinja
    search:
      - so/0900_input_redis.conf.jinja
      - custom/9000_drop_fg_dahua.conf
      - custom/9001_drop_fg_vpn_ecop.conf
      - custom/9002_drop_zabbix_dns.conf
      - custom/9003_drop_veeam_backup.conf
      - custom/9004_drop_syslog_10_99_99_1.conf
      - custom/9005_drop_sophos_peripherals.conf
      - custom/9006_drop_fg_magicinfo_internal.conf
      - custom/9007_drop_fg_ad_dns_close.conf
      - custom/9008_drop_fg_wudo_p2p_7680.conf
      - custom/9009_drop_fg_quic_udp443.conf
      - custom/9010_drop_fg_sati_vpn_dns.conf
      - custom/9011_drop_fg_benign_telemetry_urls.conf
      - so/9805_output_elastic_agent.conf.jinja
      - so/9900_output_endgame.conf.jinja
  pipeline_config:
    9000_drop_fg_dahua: |
      filter {
        if [source][ip] == "192.168.16.6" or "192.168.16.6" in [message] or "192.168.16.6" in [event][original] {
          drop { }
        }
      }
    9001_drop_fg_vpn_ecop: |
      filter {
        if "ECOP-MATRIZ-SEC" in [message] or "ECOP-MATRIZ-SEC" in [event][original] {
          drop { }
        }
      }
    9002_drop_zabbix_dns: |
      filter {
        if "zbx.technoma.com.py" in [message] or "zbx.technoma.com.py" in [event][original] {
          drop { }
        }
      }
    9003_drop_veeam_backup: |
      filter {
        if ("10.11.4.2" in [message] and "8010" in [message]) or "veeam-server-bd.local" in [message] or "veeam-server-bd.local" in [event][original] {
          drop { }
        }
      }
    9004_drop_syslog_10_99_99_1: |
      filter {
        if ([source][ip] == "10.99.99.1" or [client][ip] == "10.99.99.1") and ([destination][ip] == "192.168.15.70" or [server][ip] == "192.168.15.70" or [destination][port] == 514) {
          drop { }
        }
      }
    9005_drop_sophos_peripherals: |
      filter {
        if [data_stream][dataset] == "sophos_central.event" or "sophos_central" in [tags] {
          if "Peripheral allowed" in [message] or "Event::Endpoint::Device::AlertedOnly" in [message] or "Event::Endpoint::SavScanComplete" in [message] or "Event::Endpoint::UpdateSuccess" in [message] {
            drop { }
          }
        }
      }
    9006_drop_fg_magicinfo_internal: |
      filter {
        if [rule][ruleset] == "FG-Technoma_320" or "FG-Technoma_320" in [message] or "policyid=320" in [message] or "192.168.15.50" in [message] {
          if "7002" in [message] or "7001" in [message] {
            drop { }
          }
        }
      }
    9007_drop_fg_ad_dns_close: |
      filter {
        if [rule][ruleset] == "FG-Technoma_74" or "FG-Technoma_74" in [message] or "policyid=74" in [message] {
          if "dstport=53" in [message] and ("10.11.1.1" in [message] or "10.11.1.2" in [message]) {
            drop { }
          }
        }
      }
    9008_drop_fg_wudo_p2p_7680: |
      filter {
        if "dstport=7680" in [message] or "7680" in [destination][port] {
          if "action=\\"deny\\"" in [message] or [rule][action] == "deny" {
            drop { }
          }
        }
      }
    9009_drop_fg_quic_udp443: |
      filter {
        if "appid=\\"QUIC\\"" in [message] or "proto=17" in [message] {
          if "dstport=443" in [message] and ("action=\\"deny\\"" in [message] or [rule][action] == "deny") {
            drop { }
          }
        }
      }
    9010_drop_fg_sati_vpn_dns: |
      filter {
        if "10.212.134." in [message] and "dstport=53" in [message] {
          if "action=\\"deny\\"" in [message] or [rule][action] == "deny" {
            drop { }
          }
        }
      }
    9011_drop_fg_benign_telemetry_urls: |
      filter {
        if "action=\\"passthrough\\"" in [message] {
          if "stellarcyber.cloud" in [message] or "paloaltonetworks.com" in [message] or "microsoft.com" in [message] or "windowsupdate.com" in [message] or "google.com" in [message] or "cloudflareclient.com" in [message] {
            drop { }
          }
        }
      }
"""

print("[2] Actualizando soc_logstash.sls con las 12 reglas...")
cmd_pillar = f"""cat << 'EOF' > /opt/so/saltstack/local/pillar/logstash/soc_logstash.sls
{pillar_content}
EOF"""
run_sudo(cmd_pillar)

print("[3] Compilando con salt-call state.apply logstash.config...")
out, err = run_sudo('salt-call state.apply logstash.config')
summary = [l for l in out.splitlines() if any(k in l for k in ['Summary for local', 'Succeeded:', 'Failed:'])]
print('\n'.join(summary))

print("[4] Reiniciando Logstash con so-logstash-restart --force...")
out, err = run_sudo('so-logstash-restart --force')
print(out.strip())

print("[5] Esperando 12s para verificar contenedor...")
time.sleep(12)
out, err = run_sudo('docker ps --filter name=so-logstash --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"')
print(out.strip())

ssh.close()
