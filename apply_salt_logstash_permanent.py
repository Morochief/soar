import sys
import paramiko
import time

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

print("Esperando que termine el highstate de Salt si está en ejecución...")
for i in range(12):
    stdin, stdout, stderr = s.exec_command('echo "LMs0cZXhgds*" | sudo -S salt-run jobs.active')
    active = stdout.read().decode('utf-8', errors='replace').strip()
    if not active or "2026" not in active:
        print("Salt libre!")
        break
    print(f"Esperando a Salt... ({i})")
    time.sleep(5)

stdin, stdout, stderr = s.exec_command('echo "LMs0cZXhgds*" | sudo -S salt-call state.apply logstash.config')
print("APPLY LOGSTASH:\n", stdout.read().decode('utf-8', errors='replace'))

s.close()
