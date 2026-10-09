import datetime
import json
import requests

# Tu API Key personal de AlienVault OTX
API_KEY = "b6ec3460ec6ed672422e0e8f22367db162a03428b33e0b67f57276d385f9819c"
# Endpoint para traer los últimos 15 pulsos (campañas) a los que estás suscrito
URL = "https://otx.alienvault.com/api/v1/pulses/subscribed?limit=15"
OUTPUT_FILE = "otx_amenazas_recientes.md"

headers = {
    "X-OTX-API-KEY": API_KEY
}

print("Conectando con la base de datos global de AlienVault OTX...")

try:
    response = requests.get(URL, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con OTX: {e}")
    exit(1)

pulses = data.get("results", [])
print(f"Éxito: Se descargaron {len(pulses)} campañas de amenazas activas.")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# 👽 Inteligencia de Amenazas Activas (AlienVault OTX)\n\n")
    f.write(f"**Generado el:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
    f.write("> **Nota del Analista:** Este reporte muestra las campañas maliciosas en curso. Los 'IoCs' (Indicadores de Compromiso) son las armas que usan los atacantes (IPs, Dominios, Hashes de virus). Debes bloquearlos en el Firewall.\n\n")
    f.write("---\n\n")

    for pulse in pulses:
        name = pulse.get("name", "Desconocido")
        description = pulse.get("description", "Sin descripción")
        tags = ", ".join(pulse.get("tags", []))
        if not tags:
            tags = "Ninguno"
        indicators = pulse.get("indicators", [])
        
        f.write(f"## 🛑 Campaña: {name}\n")
        f.write(f"* **Descripción:** {description}\n")
        f.write(f"* **Tags / Palabras clave:** `{tags}`\n")
        f.write(f"* **Total de Armas detectadas (IoCs):** {len(indicators)}\n\n")
        
        if indicators:
            f.write("### Muestra de Indicadores Críticos a bloquear (Top 5):\n")
            # Mostramos los primeros 5 para no saturar el reporte si la campaña tiene miles
            for ioc in indicators[:5]:
                ioc_type = ioc.get("type", "Desconocido")
                ioc_val = ioc.get("indicator", "Desconocido")
                f.write(f"- **{ioc_type.upper()}**: `{ioc_val}`\n")
        f.write("\n---\n\n")

print(f"¡Hecho! El archivo ha sido guardado exitosamente como `{OUTPUT_FILE}`.")
