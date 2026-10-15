import os
import sys

def update_bitacora_with_both_filters():
    file_path = r"c:\Users\kevinmoraes\Documents\soc-env\Analista SOC\Bitacora_Personal_Casos_SOC.md"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} no existe.")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    old_sec2 = """#### 2. Implementación de Mitigación Quirúrgica (Sin Puntos Ciegos)
Para erradicar el ruido masivo sin generar cegueras ante posibles amenazas reales (DNS Tunneling o C2 saliente), se implementó un filtro de ingesta condicional estricto:
* **Filtro Creado:** `DROP-FG-Technoma-WIFI_Corp-Known-Public-DNS`
* **Ruta en Consola:** `System` → `Log Forwarders` (Log Filters)
* **Condiciones Aplicadas:**
  - `fw_policy_id` **is** `FG-Technoma_214`
  - `dstport` **is** `53, 853, 443` (DNS clásico, DNS-over-TLS y HTTPS FortiGuard)
  - `dstip` **matches** `96.45.46.46, 96.45.45.45, 173.243.140.18, 173.243.132.25, 173.243.143.6, 141.109.161.95, 8.8.8.8, 8.8.4.4` (Resolvers oficiales benignos)
  - `action` **is** `deny`
  - **Acción:** `DROP`"""

    new_sec2 = """#### 2. Implementación de Mitigación e Ingestión en Stellar Cyber
Para erradicar el ruido masivo y reducir el sobreconsumo de almacenamiento diario de la licencia, se crearon los siguientes filtros de descarte en **System → Log Forwarders (Log Filters)**:

1. **Filtro Inicial de Descarte DNS 53:**
   * **Nombre:** `Drop_FW_Denial_WiFiCorp_DNS_53`
   * **Definición JSON:**
     ```json
     {"fw_policy_id":{"type":"string","op":"==","value":["FG-Technoma_214"]},"dstport":{"type":"number","op":"==","value":[53]},"action":{"type":"string","op":"==","value":["deny"]}}
     ```
   * **Acción:** `DROP` (descarta denegaciones de resolución estándar en puerto 53 de la regla 214).

2. **Filtro Quirúrgico Multipuerto y Destinos Benignos (Sin Puntos Ciegos):**
   * **Nombre:** `DROP-FG-Technoma-WIFI_Corp-Known-Public-DNS`
   * **Condiciones Aplicadas:**
     - `fw_policy_id` **is** `FG-Technoma_214`
     - `dstport` **is** `53, 853, 443` (DNS estándar, DNS-over-TLS y telemetría/firmas FortiGuard)
     - `dstip` **matches** `96.45.46.46, 96.45.45.45, 173.243.140.18, 173.243.132.25, 173.243.143.6, 141.109.161.95, 8.8.8.8, 8.8.4.4`
     - `action` **is** `deny`
   * **Acción:** `DROP` (neutraliza casos masivos como el #16302 y #12661 preservando detección ante C2 o DNS tunneling a IPs no autorizadas)."""

    if old_sec2 in content:
        content = content.replace(old_sec2, new_sec2)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[+] Caso 020 actualizado con ambos filtros.")
        return True
    else:
        print("[!] No se encontró old_sec2 exactamente.")
        return False

if __name__ == "__main__":
    update_bitacora_with_both_filters()
