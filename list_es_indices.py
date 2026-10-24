import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

# Check elastic password
es_user = sudo_cmd("salt-call pillar.get elasticsearch:auth:users:so_elastic_user:user --out=txt").split(':')[-1].strip()
es_pass = sudo_cmd("salt-call pillar.get elasticsearch:auth:users:so_elastic_user:pass --out=txt").split(':')[-1].strip()

print(f"ES USER: {es_user}")

# Query indices
cmd = f"curl -s -k -u '{es_user}:{es_pass}' 'https://127.0.0.1:9200/_cat/indices?s=pri.store.size:desc&v'"
res = sudo_cmd(cmd)
print("\nTOP INDICES BY SIZE:")
lines = res.splitlines()
for l in lines[:40]:
    print(l)

ssh.close()
