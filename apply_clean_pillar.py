import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

def sudo_cmd(c):
    stdin, stdout, stderr = ssh.exec_command(f"sudo -S {c}")
    stdin.write("LMs0cZXhgds*\n")
    stdin.flush()
    return stdout.read().decode('utf-8', errors='ignore').strip()

# 1. Truncate lines from line 33 onwards in /opt/so/saltstack/local/pillar/logstash/soc_logstash.sls
sudo_cmd("sed -i '33,$d' /opt/so/saltstack/local/pillar/logstash/soc_logstash.sls")

# 2. Copy the actual config files
sudo_cmd("cp /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/9027_drop_dns_vlans_to_dcs.conf /opt/so/conf/logstash/pipelines/search/9027_drop_dns_vlans_to_dcs.conf")
sudo_cmd("cp /opt/so/saltstack/local/salt/logstash/pipelines/config/custom/9028_drop_windows_diag_traps.conf /opt/so/conf/logstash/pipelines/search/9028_drop_windows_diag_traps.conf")
sudo_cmd("chown 931:939 /opt/so/conf/logstash/pipelines/search/9027_drop_dns_vlans_to_dcs.conf /opt/so/conf/logstash/pipelines/search/9028_drop_windows_diag_traps.conf")
sudo_cmd("chmod 660 /opt/so/conf/logstash/pipelines/search/9027_drop_dns_vlans_to_dcs.conf /opt/so/conf/logstash/pipelines/search/9028_drop_windows_diag_traps.conf")

print("Pillar tail:")
print(sudo_cmd("tail -n 10 /opt/so/saltstack/local/pillar/logstash/soc_logstash.sls"))

print("\n9027 in conf:")
print(sudo_cmd("head -n 5 /opt/so/conf/logstash/pipelines/search/9027_drop_dns_vlans_to_dcs.conf"))

ssh.close()
