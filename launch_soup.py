import paramiko, time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

print("Iniciando 'sudo soup -y' en segundo plano con nohup...")
# Launch soup -y in background redirecting output to /root/soup_run.log
cmd = "sudo nohup /usr/sbin/soup -y > /root/soup_run.log 2>&1 &"
stdin, stdout, stderr = ssh.exec_command(f"sudo -S bash -c 'nohup /usr/sbin/soup -y > /root/soup_run.log 2>&1 &'")
stdin.write("LMs0cZXhgds*\n")
stdin.flush()
time.sleep(2)

stdin, stdout, stderr = ssh.exec_command("ps aux | grep soup")
print(stdout.read().decode('utf-8', errors='ignore').strip())

ssh.close()
