import os, json, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path('G:/SOC/soar/.env'))
host = os.environ.get('STELLAR_HOST')
email = os.environ.get('STELLAR_EMAIL')
token = os.environ.get('STELLAR_TOKEN')

import base64
url = f'https://{host}/connect/api/v1/access_token'
pair = f'{email}:{token}'
b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {b64}', 'Content-Type': 'application/json'}
res = requests.post(url, headers=headers, json={}, verify=True, timeout=10)
jwt = res.json().get('access_token')
auth_headers = {'Authorization': f'Bearer {jwt}', 'Content-Type': 'application/json'}

r = requests.get(f'https://{host}/connect/api/v1/log_filters', headers=auth_headers, timeout=15)
filters = r.json().get('data', [])

output = []
for idx, f in enumerate(filters):
    raw = f.get('content', '{}')
    fid = f.get('_id')
    try:
        content = json.loads(raw)
    except:
        content = {}
    output.append({
        "num": idx + 1,
        "id": fid,
        "dev_type": content.get('dev_type', 'all'),
        "dev_type_label": content.get('dev_type_label', ''),
        "rules": content.get('rules', {})
    })

out_path = Path('G:/SOC/soar/Analista SOC/Reportes/inventario_filtros_activos.json')
with open(out_path, 'w', encoding='utf-8') as out_f:
    json.dump(output, out_f, indent=2, ensure_ascii=False)

print(f"Exported {len(output)} filters to {out_path}")
