import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

python_patch = """
with open('/usr/sbin/so-image-common', 'r') as f:
    content = f.read()

target = 'docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF" >> "$LOG_FILE" 2>&1 || {'
replacement = 'docker buildx imagetools create --tag $HOSTNAME:5000/$IMAGEREPO/$image "$VERIFIED_REF" >> "$LOG_FILE" 2>&1 || docker push $HOSTNAME:5000/$IMAGEREPO/$image >> "$LOG_FILE" 2>&1 || {'

if target in content:
    content = content.replace(target, replacement)
    with open('/usr/sbin/so-image-common', 'w') as f:
        f.write(content)
    print("Successfully patched /usr/sbin/so-image-common")
else:
    print("Target string not found in /usr/sbin/so-image-common")
"""

s = ssh.open_sftp()
with s.file('/tmp/patch_script.py', 'w') as f:
    f.write(python_patch)
s.close()

print(sudo_cmd("python3 /tmp/patch_script.py"))
print(sudo_cmd("sed -n '205,215p' /usr/sbin/so-image-common"))

ssh.close()
