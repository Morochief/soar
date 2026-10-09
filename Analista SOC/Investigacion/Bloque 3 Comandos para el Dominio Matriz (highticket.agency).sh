# 1. Resolución rápida y humana de registros web y de correo en un solo comando
host highticket.agency

# 2. Resolución específica del registro A (Webflow IP)
dig highticket.agency A +short

# 3. Resolución específica del registro MX (Microsoft Office 365)
dig highticket.agency MX +short

# 4. Extraer el rango de red completo (CIDR) del hosting web mediante filtrado de tubería
whois 198.202.211.1 | grep -i "CIDR"

# 5. Extracción e inspección segura del título web para verificar el contenido del sitio
curl -sL -k https://www.highticket.agency/ | grep -i "<title>"