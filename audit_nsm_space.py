import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=10)

commands = [
    ("Filesystem Usage", "df -h /nsm /"),
    ("Top directories in /nsm", "sudo du -sh /nsm/* 2>/dev/null | sort -hr"),
    ("Docker images on host", "sudo docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}' | head -n 30"),
    ("Docker dangling images / system df", "sudo docker system df"),
    ("Docker registry content size", "sudo du -sh /nsm/docker-registry/* 2>/dev/null | sort -hr | head -n 15"),
    ("Curator / Elasticsearch indices size", "sudo du -sh /nsm/elasticsearch/* 2>/dev/null | sort -hr | head -n 10"),
    ("Influxdb / Repo / Backups", "sudo du -sh /nsm/repo /nsm/backup 2>/dev/null")
]

for title, cmd in commands:
    print(f"=== {title} ===")
    stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
    if 'sudo' in cmd:
        stdin.write('LMs0cZXhgds*\n')
        stdin.flush()
    out = stdout.read().decode('utf-8', errors='ignore').strip()
    print(out)
    print()

ssh.close()
