import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=5)

cmd = "echo LMs0cZXhgds* | sudo -S docker exec so-postgres psql -U postgres -d securityonion -c 'SELECT * FROM settings;'"
_, o, _ = client.exec_command(cmd)
print("Settings table:\n", o.read().decode())

client.close()
