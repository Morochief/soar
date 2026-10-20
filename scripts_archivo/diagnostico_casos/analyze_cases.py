import csv
from collections import Counter

cases = []
with open('XDR_Cases_2026-10-02T10_39_42.tsv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        cases.append(row)

print(f"Total cases: {len(cases)}")
severities = Counter(c.get('Severity') for c in cases)
print("Severities:", dict(severities))

statuses = Counter(c.get('Status') for c in cases)
print("Statuses:", dict(statuses))

names = Counter(c.get('Case Name') for c in cases)
print("\nTop 20 Case Names:")
for name, count in names.most_common(20):
    print(f"  {count:3d}: {name}")

detailed = [c for c in cases if len(c.get('Resolution Comment', '')) > 50 and 'caso ya resuelto' not in c.get('Resolution Comment', '').lower() and 'caso resuelto y escalado' not in c.get('Resolution Comment', '').lower()]
print(f"\nDetailed cases count: {len(detailed)}")
for i, c in enumerate(detailed):
    print(f"\n[{i+1}] ({c.get('Severity')}) {c.get('Case Name')}")
    print(f"    Date: {c.get('Last Updated')}")
    print(f"    Description: {c.get('Case Description')[:150]}")
    print(f"    Resolution: {c.get('Resolution Comment')[:250]}")
