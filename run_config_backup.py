import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

print("RUNNING SO-CONFIG-BACKUP...")
print(sudo_cmd("/usr/sbin/so-config-backup"))

print("\nLATEST BACKUP:")
print(sudo_cmd("ls -lh /nsm/backup/ | tail -n 5"))

ssh.close()
