import sys
import paramiko

sys.stdout.reconfigure(encoding='utf-8')
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('172.17.10.25', username='soc-admin', password='LMs0cZXhgds*', timeout=15)

patch_code = """
cat << 'EOF' > /opt/so/conf/logstash/pipelines/search/9805_output_elastic_agent.conf
output {
  if "elastic-agent" in [tags] and "so-ip-mappings" in [tags] {
    elasticsearch {
      hosts => "soc-onion"
      data_stream => false
      user => "so_elastic"
      password => "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"
      document_id => "%{[metadata][_id]}"
      index => "so-ip-mappings"
      silence_errors_in_log => ["version_conflict_engine_exception"]
      ssl_enabled => true
      ssl_verification_mode => "none"
    }
  }
  else {
    if "elastic-agent" in [tags] {
      if [metadata][pipeline] {
        if [metadata][_id] {
          elasticsearch {
            hosts => "soc-onion"
            ecs_compatibility => v8
            data_stream => true
            user => "so_elastic"
            password => "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"
            document_id => "%{[metadata][_id]}"
            pipeline => "%{[metadata][pipeline]}"
            silence_errors_in_log => ["version_conflict_engine_exception"]
            ssl_enabled => true
            ssl_verification_mode => "none"
          }
        }
        else {
          elasticsearch {
            hosts => "soc-onion"
            ecs_compatibility => v8
            data_stream => true
            user => "so_elastic"
            password => "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"
            pipeline => "%{[metadata][pipeline]}"
            silence_errors_in_log => ["version_conflict_engine_exception"]
            ssl_enabled => true
            ssl_verification_mode => "none"
          }
        }
      }
      else {
        elasticsearch {
          hosts => "soc-onion"
          ecs_compatibility => v8
          data_stream => true
          user => "so_elastic"
          password => "8!2ePao_Vg5.|v]W;WNfG!@yX)#5@OPYP71_Ryr4-l|Q0v|2n-8GIvjNNB|C;|-G6@=lz>Me"
          silence_errors_in_log => ["version_conflict_engine_exception"]
          ssl_enabled => true
          ssl_verification_mode => "none"
        }
      }
    }
  }
}
EOF
docker restart so-logstash
"""

stdin, stdout, stderr = s.exec_command(f'echo "LMs0cZXhgds*" | sudo -S bash -c "{patch_code}"')
print("OUTPUT:\n", stdout.read().decode('utf-8', errors='replace'))
print("STDERR:\n", stderr.read().decode('utf-8', errors='replace'))

s.close()
