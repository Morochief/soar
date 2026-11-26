import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

es_user = sudo_cmd("salt-call pillar.get elasticsearch:auth:users:so_elastic_user:user --out=txt").split(':')[-1].strip()
es_pass = sudo_cmd("salt-call pillar.get elasticsearch:auth:users:so_elastic_user:pass --out=txt").split(':')[-1].strip()

# 1. Delete .ds-logs-zeek-so-2026.10.21-000053 (18 GB of old Zeek connection logs from Oct 16 to Oct 21)
print("DELETING OLD ZEEK INDEX (18 GB)...")
cmd_del = f"curl -s -k -X DELETE -u '{es_user}:{es_pass}' 'https://127.0.0.1:9200/.ds-logs-zeek-so-2026.10.21-000053'"
print(sudo_cmd(cmd_del))

# 2. Check disk space afterwards
print("\nDISCO DESPUES DE LIBERAR ZEEK:")
stdin, stdout, stderr = ssh.exec_command("df -h / /nsm")
print(stdout.read().decode('utf-8', errors='ignore').strip())

ssh.close()
