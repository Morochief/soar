import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=5)

cmd1 = "echo LMs0cZXhgds* | sudo -S salt 'secops-vascol_sensor' state.apply sensoroni"
_, o1, _ = client.exec_command(cmd1)
print("Apply state sensoroni on vascol:\n", o1.read().decode()[-1500:])

client.close()
