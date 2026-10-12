import requests
import urllib3
import re
urllib3.disable_warnings()

t = requests.get('https://technoma.stellarcyber.cloud/main-TXXJEEET.js', verify=False).text
matches = re.findall(r'\{[^{}]*api-docs[^{}]*\}', t)
print("Matches:", matches)

# Find all chunk imports
lazy_chunks = re.findall(r'chunk-[a-zA-Z0-9]+\.js', t)
print(f"Total chunk references in main: {len(set(lazy_chunks))}")

# Check which chunk has api-docs
for ch in set(lazy_chunks):
    u = f'https://technoma.stellarcyber.cloud/{ch}'
    try:
        c_text = requests.get(u, verify=False, timeout=5).text
        if 'api-docs' in c_text or 'swagger' in c_text.lower():
            print(f"Found match in {ch}!")
            # inspect where swagger or yaml or json is loaded
            found = set(re.findall(r'[\'"][^\'"]*(?:\.yaml|\.json|swagger|connect/api)[^\'"]*[\'"]', c_text))
            print("  Details:", list(found)[:15])
    except Exception:
        pass
