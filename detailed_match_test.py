import csv
import re

with open('cases - Fri Oct 02 2026.csv', 'r', encoding='utf-8', errors='ignore') as f:
    stellar = list(csv.DictReader(f))

with open('XDR_Issues_2026-10-02T11_29_10.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    issues = list(csv.DictReader(f, delimiter='\t'))

with open('XDR_Cases_2026-10-02T12_19_18.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    cortex_cases = list(csv.DictReader(f, delimiter='\t'))

print("Analyzing Stellar cases against Cortex...")

for s in stellar[:20]:
    s_id = s['Case ID']
    s_date = s['Created At'][:10]
    s_who = s['Who']
    s_name = s['Case Name']
    
    # Strip prefix
    clean_name = re.sub(r'^Palo Alto Networks Cortex XDR \([^)]+\):\s*', '', s_name)
    # Strip suffix 'and X others'
    clean_name = re.sub(r'\s+and\s+\d+\s+other.*$', '', clean_name)
    
    # Check matching issues
    matching_issues = []
    for i_idx, iss in enumerate(issues, 1):
        if clean_name.lower() in iss['Name'].lower() or iss['Name'].lower() in clean_name.lower():
            matching_issues.append((i_idx, iss['Name'], iss['Observation Time'][:12], iss['Case IDs']))
            
    matching_cases = []
    for c_idx, c in enumerate(cortex_cases, 1):
        if clean_name.lower() in c['Case Name'].lower() or c['Case Name'].lower() in clean_name.lower():
            matching_cases.append((c_idx, c['Case Name'], c['Last Updated'][:12]))
            
    print(f"Stellar #{s_id} | {s_date} | {s_who} | {clean_name}")
    print(f"   -> Match en Issues: {len(matching_issues)} encontrados")
    if matching_issues:
        print(f"      Ej: Issue #{matching_issues[0][0]}: {matching_issues[0][1]} ({matching_issues[0][2]}) [Case: {matching_issues[0][3]}]")
    print(f"   -> Match en Cases: {len(matching_cases)} encontrados")
    if matching_cases:
        print(f"      Ej: Case #{matching_cases[0][0]}: {matching_cases[0][1]} ({matching_cases[0][2]})")
    print("-" * 60)
