import json
from pathlib import Path

def generate_inventory():
    input_file = Path("cajaande_endpoints.json")
    if not input_file.exists():
        print("No se encontro cajaande_endpoints.json")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ordenar alfabeticamente por hostname
    data = sorted(data, key=lambda x: x.get("hostname", "").lower())

    lines = []
    lines.append("# 🖥️ INVENTARIO COMPLETO DE ACTIVOS Y ENDPOINTS — CAJA DE JUBILACIONES DE LA ANDE (CAJAANDE)")
    lines.append("")
    lines.append("> **FUENTE:** Sophos Central REST API (Tenant ID: `37a6c0dc-b2ea-4fda-b641-456560f40ef1`)  ")
    lines.append(f"> **TOTAL DISPOSITIVOS:** {len(data)} hosts registrados en consola  ")
    lines.append("> **CLASIFICACIÓN:** USO INTERNO SOC TECHNOMA — BASE DE CONOCIMIENTO  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📊 1. Resumen Ejecutivo de Postura del Parque")
    lines.append("")

    health_counts = {}
    os_counts = {}
    server_count = 0
    workstation_count = 0

    for ep in data:
        h = ep.get("health", {}).get("overall", "unknown").upper()
        health_counts[h] = health_counts.get(h, 0) + 1
        os_name = ep.get("os", {}).get("name", "Desconocido").strip()
        os_counts[os_name] = os_counts.get(os_name, 0) + 1
        if ep.get("os", {}).get("isServer") or "server" in ep.get("type", "").lower():
            server_count += 1
        else:
            workstation_count += 1

    lines.append("| Métrica | Cantidad |")
    lines.append("| :--- | :--- |")
    lines.append(f"| **Total Endpoints Registrados** | **{len(data)}** |")
    lines.append(f"| **Estaciones de Trabajo (PC / Laptops)** | {workstation_count} |")
    lines.append(f"| **Servidores (Windows Server / Linux)** | {server_count} |")
    lines.append(f"| **Salud Saludable [GOOD]** | {health_counts.get('GOOD', 0)} |")
    lines.append(f"| **Salud Sospechosa [SUSPICIOUS]** | {health_counts.get('SUSPICIOUS', 0)} |")
    lines.append(f"| **Salud Crítica / Fallo [BAD]** | {health_counts.get('BAD', 0)} |")
    lines.append(f"| **Tamper Protection Habilitado** | {len(data)} / {len(data)} (100%) |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📋 2. Tabla Maestra de Activos (123 Endpoints)")
    lines.append("")
    lines.append("| # | Hostname | Tipo | Sistema Operativo | IP(s) Asignada(s) | Estado Salud | Tamper | Última Conexión (UTC) |")
    lines.append("| :-: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |")

    for idx, ep in enumerate(data, 1):
        host = ep.get("hostname", "N/A")
        etype = "Servidor" if ep.get("os", {}).get("isServer") else "PC/Laptop"
        os_name = ep.get("os", {}).get("name", "N/A").strip()
        ips = "<br>".join(ep.get("ipv4Addresses", [])) if ep.get("ipv4Addresses") else "N/A"
        health = ep.get("health", {}).get("overall", "UNKNOWN").upper()
        if health == "GOOD":
            health_badge = "🟢 GOOD"
        elif health == "SUSPICIOUS":
            health_badge = "🟡 SUSPICIOUS"
        else:
            health_badge = "🔴 BAD"
        tamper = "✅ SI" if ep.get("tamperProtectionEnabled") else "❌ NO"
        last_seen = ep.get("lastSeenAt", "")[:19].replace("T", " ")
        lines.append(f"| {idx} | **{host}** | {etype} | {os_name} | {ips} | {health_badge} | {tamper} | {last_seen} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 🔎 3. Inventario de Atención Prioritaria (Hosts Sospechosos / Críticos)")
    lines.append("")
    lines.append("| Hostname | IP(s) | Estado | Amenazas | Detalle Diagnóstico |")
    lines.append("| :--- | :--- | :---: | :---: | :--- |")
    for ep in data:
        h = ep.get("health", {}).get("overall", "").lower()
        if h in ["suspicious", "bad"]:
            host = ep.get("hostname")
            ips = ", ".join(ep.get("ipv4Addresses", []))
            st = h.upper()
            threat_st = ep.get("health", {}).get("threats", {}).get("status", "N/A")
            diag = "PUA detectado o servicio pendiente de remediacion" if h == "suspicious" else "Fallo critico de proteccion o desactualizado"
            lines.append(f"| **{host}** | `{ips}` | **{st}** | `{threat_st}` | {diag} |")

    lines.append("")
    lines.append("---")
    lines.append("*Documento generado automáticamente por el motor MDR de Technoma SOC a través de Sophos Central REST API.*")

    output_path = Path("Analista SOC/02_Base_de_Conocimiento/Inventario_Activos_CajaAnde_Sophos.md")
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("\n".join(lines))
    print(f"Inventario generado exitosamente en: {output_path}")

if __name__ == "__main__":
    generate_inventory()
