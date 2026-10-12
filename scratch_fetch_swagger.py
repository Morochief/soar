import requests
import urllib3
import re
urllib3.disable_warnings()

url = 'https://technoma.stellarcyber.cloud/api-docs/'
try:
    r = requests.get(url, verify=False, timeout=10)
    print(f"Status: {r.status_code}")
    print(f"Length: {len(r.text)}")
    print("Preview:\n", r.text[:1000])
    
    # Try finding json or yaml paths
    found = re.findall(r'[\'"]([^\'"]*(?:swagger|openapi|api-docs|\.json|\.yaml)[^\'"]*)[\'"]', r.text)
    print("\nPotential spec files found:", set(found))
except Exception as e:
    print(f"Error: {e}")
