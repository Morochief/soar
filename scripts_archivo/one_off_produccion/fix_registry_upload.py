import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

# 1. Remove stale incomplete upload chunks in registry
print(sudo_cmd("rm -rf /nsm/docker-registry/docker/registry/v2/repositories/security-onion-solutions/so-elastic-fleet-package-registry/_uploads/*"))

# 2. Restart registry cleanly
print(sudo_cmd("docker restart so-dockerregistry"))

print("\nRegistry status:")
print(sudo_cmd("docker ps --filter 'name=so-dockerregistry' --format 'table {{.Names}}\t{{.Status}}'"))

ssh.close()
