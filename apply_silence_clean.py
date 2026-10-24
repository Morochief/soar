import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

# Usamos sed para agregar silence_errors_in_log a los bloques de elasticsearch que faltan
cmds = [
    r'sed -i "/hosts => \"soc-onion\"/a \          silence_errors_in_log => [\"version_conflict_engine_exception\"]" /opt/so/conf/logstash/pipelines/search/9805_output_elastic_agent.conf',
    'docker restart so-logstash'
]

for cmd in cmds:
    stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{cmd}\'')
    print("CMD:", cmd)
    print("STDOUT:", stdout.read().decode('utf-8', errors='replace'))
    print("STDERR:", stderr.read().decode('utf-8', errors='replace'))

s.close()
