import requests
import urllib3
import re
urllib3.disable_warnings()

url = 'https://technoma.stellarcyber.cloud/api-docs/'
r = requests.get(url, verify=False, timeout=10)

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', r.text)
print("Scripts in page:", scripts)

for s in scripts:
    if s.startswith('/'):
        s_url = f'https://technoma.stellarcyber.cloud{s}'
    else:
        s_url = f'https://technoma.stellarcyber.cloud/{s}'
    try:
        s_r = requests.get(s_url, verify=False, timeout=10)
        # search for swagger or openapi or connect/api
        apis = set(re.findall(r'/connect/api/v1/[a-zA-Z0-9_\-\/]+', s_r.text))
        swaggers = set(re.findall(r'[a-zA-Z0-9_\-\/\.]*(?:swagger|openapi)[a-zA-Z0-9_\-\/\.]*', s_r.text, re.IGNORECASE))
        print(f"\nIn script {s} (size {len(s_r.text)}):")
        if swaggers:
            print("  Swaggers:", list(swaggers)[:10])
        if apis:
            print(f"  Found {len(apis)} connect/api/v1 endpoints!")
            print("  Sample endpoints:", list(apis)[:15])
    except Exception as e:
        print(f"Error fetching {s}: {e}")
