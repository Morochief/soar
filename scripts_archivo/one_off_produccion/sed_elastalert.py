import paramiko

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

script = """
sed -i 's/disable_rules_on_error: false/disable_rules_on_error: true/' /opt/so/conf/elastalert/elastalert_config.yaml
docker restart so-elastalert
grep disable_rules_on_error /opt/so/conf/elastalert/elastalert_config.yaml
"""

stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c "{script}"')
print("OUT:", stdout.read().decode('utf-8', errors='replace'))
s.close()
