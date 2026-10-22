import paramiko

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

def run(cmd):
    stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c \'{cmd}\'')
    return stdout.read().decode('utf-8', errors='replace')

# 1. Copiar 9805 jinja al arbol local
run('mkdir -p /opt/so/saltstack/local/salt/logstash/pipelines/config/so/')
run('cp /opt/so/saltstack/default/salt/logstash/pipelines/config/so/9805_output_elastic_agent.conf.jinja /opt/so/saltstack/local/salt/logstash/pipelines/config/so/9805_output_elastic_agent.conf.jinja')

# 2. Agregar silence_errors_in_log en las dos ramas que faltaban
script_sed = """
python3 -c "
with open('/opt/so/saltstack/local/salt/logstash/pipelines/config/so/9805_output_elastic_agent.conf.jinja', 'r') as f:
    text = f.read()

# Reemplazar la rama sin id pero con pipeline
old_block1 = '''            pipeline => \"%{[metadata][pipeline]}\"\\n            ssl_enabled => true'''
new_block1 = '''            pipeline => \"%{[metadata][pipeline]}\"\\n            silence_errors_in_log => [\\\"version_conflict_engine_exception\\\"]\\n            ssl_enabled => true'''

# Reemplazar la rama else final (sin pipeline ni id)
old_block2 = '''          password => \"{{ ES_PASS }}\"\\n          ssl_enabled => true'''
new_block2 = '''          password => \"{{ ES_PASS }}\"\\n          silence_errors_in_log => [\\\"version_conflict_engine_exception\\\"]\\n          ssl_enabled => true'''

text = text.replace(old_block1, new_block1).replace(old_block2, new_block2)

with open('/opt/so/saltstack/local/salt/logstash/pipelines/config/so/9805_output_elastic_agent.conf.jinja', 'w') as f:
    f.write(text)
print('Modificado exitosamente')
"
"""
print(run(script_sed))

# 3. Compilar con SaltStack y reiniciar Logstash
print("Compilando con salt-call state.apply logstash.config...")
out = run('salt-call state.apply logstash.config')
for l in out.splitlines():
    if any(k in l for k in ['Summary for local', 'Succeeded:', 'Failed:']):
        print(l)

print("Reiniciando Logstash...")
run('so-logstash-restart --force')

s.close()
