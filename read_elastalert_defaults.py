import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

script = """
cat /opt/so/saltstack/default/salt/elastalert/defaults.yaml
"""

stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{script}\'')
print(stdout.read().decode('utf-8', errors='replace'))
s.close()
