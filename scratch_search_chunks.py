import requests
import urllib3
import re
urllib3.disable_warnings()

chunks = [
    'chunk-Z7SSNN44.js', 'chunk-G2MDN42H.js', 'chunk-EUJBPQCM.js',
    'chunk-IS5CAHZ6.js', 'chunk-B44VVTTL.js', 'chunk-N4ZE7RHP.js',
    'chunk-2LCHZBP6.js', 'chunk-G2VI73RJ.js', 'chunk-HDXGEX7J.js',
    'chunk-TCH65MND.js', 'main-TXXJEEET.js', 'scripts-FXAY3PTA.js'
]

for ch in chunks:
    u = f'https://technoma.stellarcyber.cloud/{ch}'
    try:
        r = requests.get(u, verify=False, timeout=10)
        # Check if swagger or json or api-docs is mentioned
        matches = set(re.findall(r'(/connect/api/v1/[\w/]+|assets/[\w/\.\-]+\.json|assets/[\w/\.\-]+\.yaml)', r.text))
        swag = set(re.findall(r'[\'"][^\'"]*(?:swagger|openapi|api-docs)[^\'"]*[\'"]', r.text, re.IGNORECASE))
        if matches or swag:
            print(f"=== {ch} (size {len(r.text)}) ===")
            if swag:
                print("  Swag matches:", list(swag)[:10])
            if matches:
                print(f"  API matches ({len(matches)}):", list(matches)[:10])
    except Exception as e:
        print(f"Error {ch}: {e}")
