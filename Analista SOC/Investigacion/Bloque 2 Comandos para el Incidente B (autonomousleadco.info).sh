# 1. Consulta WHOIS tradicional del dominio
whois autonomousleadco.info

# 2. Consulta avanzada RDAP directo al registro de Identity Digital
curl -s https://rdap.identitydigital.services/rdap/domain/autonomousleadco.info | json_pp

# 3. Resolución de direcciones IP (Registros A detrás de Cloudflare)
dig autonomousleadco.info A +short

# 4. Auditoría de registros TXT/SPF para verificar proveedor de envío (Google)
dig autonomousleadco.info TXT +short

# 5. Búsqueda de políticas DMARC del dominio
dig _dmarc.autonomousleadco.info TXT +short

# 6. Rastrear la cadena completa de servidores DNS desde la raíz
dig autonomousleadco.info +trace

# 7. Intento de transferencia de zona DNS (Auditoría de subdominios)
dig @joaquin.ns.cloudflare.com autonomousleadco.info axfr

# 8. Detección y lectura de redireccionamientos web activos (HTTP 301)
curl -I -k https://autonomousleadco.info