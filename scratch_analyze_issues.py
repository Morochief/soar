import csv
import re

with open('XDR_Issues_2026-10-02T11_29_10.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))

print(f"Total issues: {len(rows)}")

for idx, r in enumerate(rows[:20], 1):
    desc = r.get('Description', '')
    ext = r.get('Extended Description', '')
    evi = r.get('Initial Evidence', '')
    name = r.get('Name', '')
    res_c = r.get('Resolution Comment', '')
    res_r = r.get('Resolution Reason', '')
    case_ids = r.get('Case IDs', '')
    tactic = r.get('Mitre ATT&CK Tactic', '')
    tech = r.get('Mitre ATT&CK Technique', '')
    
    text = desc + ' ' + ext + ' ' + evi
    m_host = re.search(r'\b(NB-[A-Za-z0-9_-]+|nb-[a-z0-9_-]+|[a-zA-Z0-9_-]+\.vascol\.local|192\.168\.[0-9.]+|10\.[0-9.]+)\b', text)
    host = m_host.group(1).upper() if m_host else 'Varios / Red'
    
    m_user = re.search(r'(technoma\\[a-zA-Z0-9_-]+|nt authority\\system|[a-zA-Z0-9_.-]+@technoma\.com\.py)', text, re.I)
    user = m_user.group(1) if m_user else ('SYSTEM' if 'system' in text.lower() else 'No especificado')
    
    print(f"{idx} | {r['Severity']} | {name[:35]} | {host} | {user} | {r['Status']} | Case: {case_ids}")
