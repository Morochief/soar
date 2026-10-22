import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

script = """
curl -s -k -u "so_elastic:8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me" "https://127.0.0.1:9200/elastalert_error/_search?size=1&sort=@timestamp:desc"
"""

stdin, stdout, stderr = s.exec_command(script)
print(stdout.read().decode('utf-8', errors='replace'))
s.close()
