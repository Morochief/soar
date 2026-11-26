import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=5)

cmd = "echo LMs0cZXhgds* | sudo -S salt 'secops-vascol_sensor' state.apply"
_, o, _ = client.exec_command(cmd)
print("State apply output:\n", o.read().decode()[-1500:])

client.close()
