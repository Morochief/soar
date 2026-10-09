# 1. Consulta WHOIS del dominio
whois evalartemail.com

# 2. Resolución de dirección IP (Registro A)
dig evalartemail.com A +short

# 3. Auditoría de políticas de correo (Registro SPF/TXT)
dig evalartemail.com TXT +short

# 4. Búsqueda de políticas de alineación y reportes de seguridad (DMARC)
dig _dmarc.evalartemail.com TXT +short

# 5. Extracción de la clave pública criptográfica (DKIM con el selector hallado)
dig selector1._domainkey.evalartemail.com TXT +short

# 6. Resolución inversa de la dirección IPv6 atacante identificada
dig -x 2a01:111:f403:c408::3 +short

# 7. Inspección segura de encabezados HTTP del servidor web
curl -I -k https://evalartemail.com