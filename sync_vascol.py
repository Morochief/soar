import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=5)

cmd = "echo LMs0cZXhgds* | sudo -S salt 'secops-vascol_sensor' service.restart salt-minion"
_, o, _ = client.exec_command(cmd)
print("Restart minion:\n", o.read().decode())

client.close()
