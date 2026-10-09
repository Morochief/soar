import csv, re
from datetime import datetime

with open('cases - Fri Oct 02 2026.csv', 'r', encoding='utf-8', errors='ignore') as f:
    stellar = list(csv.DictReader(f))

with open('XDR_Issues_2026-10-02T11_29_10.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    issues = list(csv.DictReader(f, delimiter='\t'))

with open('XDR_Cases_2026-10-02T12_19_18.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    cases_new = list(csv.DictReader(f, delimiter='\t'))
with open('XDR_Cases_2026-10-02T10_39_42.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    cases_old = list(csv.DictReader(f, delimiter='\t'))

print(f"Total Stellar: {len(stellar)} | Total Issues: {len(issues)} | Total Cases: {len(cases_new)}")

# Helper to normalize dates for comparison
# Stellar: "2026-10-01 15:45:00" -> "2026-10-01"
# Cortex: "Oct 1st 2026 15:34:51" -> "2026-10-01"
def parse_cortex_date(d_str):
    if not d_str:
        return ""
    # "Oct 1st 2026 15:34:51"
    m = re.search(r'([A-Za-z]+)\s+(\d+)(?:st|nd|rd|th)?\s+(\d{4})', d_str)
    if m:
        month_str, day_str, year_str = m.groups()
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                  'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        mo = months.get(month_str[:3].title(), 1)
        return f"{year_str}-{mo:02d}-{int(day_str):02d}"
    return ""

matched_count = 0
results = []

for s in stellar:
    s_id = s['Case ID']
    s_name = s['Case Name']
    s_who = s['Who'].upper().replace('.TECHNOMA.LOCAL', '').strip()
    s_date = s['Created At'][:10]
    
    # Extract core alert from Stellar Name
    m = re.search(r':\s*(.+?)(?:\s+and\s+\d+\s+other|$)', s_name, re.I)
    core = m.group(1).strip().lower() if m else s_name.lower()
    
    best_match_case = None
    best_match_issues = []
    
    # 1. Search in Cortex Issues
    for idx_i, iss in enumerate(issues, 1):
        i_name = iss['Name'].lower()
        i_date = parse_cortex_date(iss['Observation Time'])
        i_desc = (iss['Description'] + ' ' + iss['Extended Description']).upper()
        
        # Check host
        host_ok = (s_who in i_desc) or (s_who in i_name.upper()) if len(s_who) > 3 else True
        
        # Check date within 1-2 days
        date_ok = (s_date == i_date)
        
        # Check core alert match
        name_ok = (core in i_name) or (i_name in core) or (core[:15] in i_name)
        
        if host_ok and name_ok and date_ok:
            best_match_issues.append((idx_i, iss['Name'], iss['Case IDs']))
    
    # 2. Search in Cortex Cases
    for idx_c, (cn, co) in enumerate(zip(cases_new, cases_old), 1):
        c_name = cn['Case Name'].lower()
        c_date = parse_cortex_date(cn['Last Updated'])
        c_desc = (co['Case Description'] + ' ' + co['Resolution Comment']).upper()
        
        host_ok = (s_who in c_desc) or (s_who in c_name.upper()) if len(s_who) > 3 else True
        date_ok = (s_date == c_date)
        name_ok = (core in c_name) or (c_name in core) or (core[:15] in c_name)
        
        if host_ok and name_ok and date_ok:
            best_match_case = (idx_c, cn['Case Name'])
            break
            
    if best_match_case or best_match_issues:
        matched_count += 1
        results.append({
            'stellar_id': s_id,
            'stellar_name': s_name,
            'stellar_who': s_who,
            'stellar_date': s['Created At'],
            'stellar_res': s['Resolution'],
            'stellar_assignee': s['Assignee'],
            'cortex_case': best_match_case,
            'cortex_issues': best_match_issues[:3]
        })

print(f"Casos de Stellar correlacionados exitosamente: {matched_count}/{len(stellar)} ({matched_count/len(stellar)*100:.1f}%)")

print("\nEjemplos de correlación lograda:")
for r in results[:10]:
    c_info = f"Cortex Case #{r['cortex_case'][0]} ({r['cortex_case'][1][:30]})" if r['cortex_case'] else "Mapeado vía Issues"
    i_info = f"{len(r['cortex_issues'])} Issues coinciden (ej. #{r['cortex_issues'][0][0]}: {r['cortex_issues'][0][1][:25]})" if r['cortex_issues'] else "Sin issue atómico directo"
    print(f"Stellar Case #{r['stellar_id']} [{r['stellar_who']}] ({r['stellar_date'][:10]}):")
    print(f"  -> {c_info}")
    print(f"  -> {i_info}")
