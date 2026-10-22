import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

def run_sudo(cmd):
    stdin, stdout, stderr = ssh.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{cmd}\'')
    out = stdout.read().decode('utf-8', errors='replace')
    err = stderr.read().decode('utf-8', errors='replace')
    return out, err

print('[1] Creando archivo 9005_drop_sophos_peripherals.conf...')
run_sudo('mkdir -p /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/')

rule_content = """filter {
  if [data_stream][dataset] == "sophos_central.event" or "sophos_central" in [tags] {
    if "Peripheral allowed" in [message] or "Event::Endpoint::Device::AlertedOnly" in [message] or "Event::Endpoint::SavScanComplete" in [message] or "Event::Endpoint::UpdateSuccess" in [message] {
      drop { }
    }
  }
}"""

cmd_file = f"""cat << 'EOF' > /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/9005_drop_sophos_peripherals.conf
{rule_content}
EOF"""
run_sudo(cmd_file)
print('Archivo creado.')

print('[2] Compilando con salt-call state.apply logstash.config...')
out, err = run_sudo('salt-call state.apply logstash.config')
summary = [l for l in out.splitlines() if any(k in l for k in ['Summary for local', 'Succeeded:', 'Failed:'])]
print('\n'.join(summary))

print('[3] Reiniciando Logstash...')
out, err = run_sudo('so-logstash-restart --force')
print(out.strip())

print('[4] Esperando 12s para verificar contenedor...')
time.sleep(12)
out, err = run_sudo('docker ps --filter name=so-logstash --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"')
print(out.strip())

ssh.close()
