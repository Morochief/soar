import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

# Clean stale uploads in so-elasticsearch
sudo_cmd("rm -rf /nsm/docker-registry/docker/registry/v2/repositories/security-onion-solutions/so-elasticsearch/_uploads/*")

python_patch = '''
with open('/tmp/sogh/securityonion/salt/common/tools/sbin/so-image-common', 'r') as f:
    c = f.read()

target = 'docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF" >> "$LOG_FILE" 2>&1 || {'
replacement = 'docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF" >> "$LOG_FILE" 2>&1 || docker push $HOSTNAME:5000/$IMAGEREPO/$image >> "$LOG_FILE" 2>&1 || {'

if target in c:
    c = c.replace(target, replacement)
    with open('/tmp/sogh/securityonion/salt/common/tools/sbin/so-image-common', 'w') as f:
        f.write(c)
    print("Patched repo copy in /tmp/sogh")
else:
    print("Target not found in /tmp/sogh")

with open('/usr/sbin/so-image-common', 'r') as f:
    c2 = f.read()
if target in c2:
    c2 = c2.replace(target, replacement)
    with open('/usr/sbin/so-image-common', 'w') as f:
        f.write(c2)
    print("Patched /usr/sbin/so-image-common")
else:
    print("Target not found or already patched in /usr/sbin")
'''

s = ssh.open_sftp()
with s.file('/tmp/patch_both.py', 'w') as f:
    f.write(python_patch)
s.close()

print(sudo_cmd("python3 /tmp/patch_both.py"))

ssh.close()
