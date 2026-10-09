import csv

with open('cases - Fri Oct 02 2026.csv', 'r', encoding='utf-8', errors='ignore') as f:
    stellar = list(csv.DictReader(f))

print("Stellar cases:")
print("  Total:", len(stellar))
print("  Newest:", stellar[0]['Created At'])
print("  Oldest:", stellar[-1]['Created At'])

for s in stellar[:15]:
    print(f"  #{s['Case ID']} | {s['Created At']} | {s['Who'][:15]} | {s['Score']} | {s['Severity']} | {s['Case Name'][:60]}")
