import json

with open(r'Analista SOC\stellar_log_filters_completos.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

filters = d['filters']
print(f"=== AUDITORÍA TÉCNICA DE LOG FILTERS (Total: {len(filters)}) ===\n")

# Hallazgos clasificados
hallazgos = []

for i, f in enumerate(filters, 1):
    rules = f.get('rules', {})
    issues = []
    
    # 1. Reglas con CIDR y operadores de igualdad
    for field, rule in rules.items():
        if isinstance(rule, dict):
            op = rule.get('op')
            val = rule.get('value', [])
            for v in val:
                if isinstance(v, str) and '/' in v and op in ['==', 'is', 'equals']:
                    issues.append(f"CIDR '{v}' usado con operador estricto '{op}' en vez de 'matches'")

    # 2. appid_name vs ICMP / PING
    if 'appid_name' in rules:
        val = rules['appid_name'].get('value', [])
        for v in val:
            if v == 'PING':
                issues.append("appid_name == 'PING' (En FortiGate/Stellar suele normalizarse como 'icmp/8/0' o 'icmp', mientras que 'PING' viaja en 'service')")

    # 3. Campos anidados fortinet.*
    fortinet_fields = [k for k in rules.keys() if k.startswith('fortinet.')]
    if fortinet_fields:
        issues.append(f"Usa campos anidados directos ({', '.join(fortinet_fields)}). Si el parser de syslog descarta o aplana estos campos antes del filtro, la regla no matchea.")

    # 4. Exceso de especificidad AND (3 o más condiciones que difícilmente coinciden al mismo tiempo)
    if len(rules) >= 3:
        issues.append(f"Alta especificidad: {len(rules)} condiciones unidas por AND. Si un solo campo difiere o llega nulo, el log NO se descarta.")

    # 5. Sin perfil de sensor asignado
    if not f.get('in_use', {}).get('sensor_profile'):
        issues.append("REGLA HUÉRFANA: No está vinculada a ningún sensor_profile, por lo que nunca se evalúa.")

    # 6. Tenant restrictivo vs all-tenants
    tenant = f.get('tenant')
    if tenant and tenant != 'all-tenants':
        issues.append(f"Tenant restringido a '{tenant}'. Si los logs ingresan con 'all-tenants' o sin org_id mapeado, el filtro se ignora.")

    if issues or 'helpdesk' in f.get('name', '').lower():
        hallazgos.append({
            'num': i,
            'name': f.get('name'),
            'created_by': f.get('created_by'),
            'summary': f.get('rules_summary'),
            'issues': issues
        })

print(f"Total de reglas con advertencias/fallas potenciales: {len(hallazgos)}\n")
for h in hallazgos:
    print(f"[{h['num']:02d}] {h['name']} (Autor: {h['created_by']})")
    print(f"     Reglas: {h['summary']}")
    for iss in h['issues']:
        print(f"     [!] {iss}")
    print()
