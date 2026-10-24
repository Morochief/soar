import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_exec(cmd):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {cmd}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

print("=== DF ===")
print(sudo_exec("df -h /nsm /"))

print("\n=== TOP /nsm ===")
print(sudo_exec("du -sh /nsm/* 2>/dev/null | sort -hr"))

print("\n=== DOCKER SYSTEM DF ===")
print(sudo_exec("docker system df"))

print("\n=== ELASTIC INDICES STATS ===")
print(sudo_exec("curl -s -k -u 'so-elastic:$(grep -A 10 elastic /opt/so/conf/elasticsearch/secrets.yaml 2>/dev/null | head -n 1)' https://127.0.0.1:9200/_cat/allocation?v 2>/dev/null || true"))

ssh.close()
