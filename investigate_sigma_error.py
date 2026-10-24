import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=20)

stdin, stdout, stderr = s.exec_command('echo "LMs0cZXhgds*" | sudo -S grep -A 2 -B 2 "sigmaConvertOutput" /opt/so/log/logstash/logstash.log')
out = stdout.read().decode('utf-8', errors='replace')
print("LONGITUD:", len(out))
if out:
    print("MUESTRA:\n", out[:2000])
else:
    print("STDERR:\n", stderr.read().decode('utf-8', errors='replace'))

s.close()
