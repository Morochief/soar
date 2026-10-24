import sys
import paramiko
import time

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

print("Monitoreando el Highstate PID 4138746 hasta que termine...")
while True:
    stdin, stdout, stderr = s.exec_command('echo "LMs0cZXhgds*" | sudo -S ps aux | grep 4138746 | grep -v grep')
    running = stdout.read().decode('utf-8', errors='replace').strip()
    if not running:
        print("Highstate finalizado!")
        break
    time.sleep(4)

stdin, stdout, stderr = s.exec_command('echo "LMs0cZXhgds*" | sudo -S salt-call state.apply logstash.config')
print("RESULTADO DE APPLY LOGSTASH:\n", stdout.read().decode('utf-8', errors='replace'))

s.close()
