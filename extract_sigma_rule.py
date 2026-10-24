import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=20)

cmd = 'grep -B 1 "a579e6f662ddda6dc5280" /opt/so/log/logstash/logstash.log | head -n 5'
stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{cmd}\'')
print("CABECERA ANTERIOR:\n", stdout.read().decode('utf-8', errors='replace'))

cmd_tail = 'grep -o \'.\{0,100\}sigmaConvertOutput.\{0,150\}\' /opt/so/log/logstash/logstash.log | head -n 3'
stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c "{cmd_tail}"')
print("CAMPOS CERCA DE SIGMACONVERTOUTPUT:\n", stdout.read().decode('utf-8', errors='replace'))

s.close()
