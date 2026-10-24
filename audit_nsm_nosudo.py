import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def run(c):
    _, out, _ = ssh.exec_command(c)
    return out.read().decode('utf-8', errors='ignore').strip()

print("DF:")
print(run("df -h / /nsm"))
print("\nREGISTRY DIRECTORIES:")
print(run("ls -lh /nsm/docker-registry/docker/registry/v2/repositories/ 2>/dev/null || echo 'no direct repos'"))

ssh.close()
