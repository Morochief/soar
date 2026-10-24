import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=5)

cmd1 = "echo LMs0cZXhgds* | sudo -S so-elasticsearch-query '.kibana*/_settings?expand_wildcards=all' -XPUT -d '{\"index.blocks.read_only_allow_delete\": null}'"
_, o1, _ = client.exec_command(cmd1)
print("Unblock hidden indices:", o1.read().decode())

cmd2 = "echo LMs0cZXhgds* | sudo -S so-elasticsearch-query '_all/_settings?expand_wildcards=all' -XPUT -d '{\"index.blocks.read_only_allow_delete\": null}'"
_, o2, _ = client.exec_command(cmd2)
print("Unblock all hidden:", o2.read().decode())

client.close()
