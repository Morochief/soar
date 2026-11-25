//@@HELPERS
// Modo: una vez por ítem. 3/5 del embudo: IP-API (Detección de Proxy, VPN, Tor, Mobile, Reverse DNS y Hosting).
// Sin API key ni cuota mensual.
const ctx = $('Norm AbuseIPDB').item.json;
const st = estadoHttp($json);
let ipapi;
if (!st.ok || $json.status === 'fail') {
  ipapi = { estado: 'no_disponible', motivo: $json.message || motivoFallo(st) };
} else {
  ipapi = {
    estado: 'ok',
    pais: $json.country || null,
    pais_codigo: $json.countryCode || null,
    region: $json.regionName || null,
    ciudad: $json.city || null,
    zona_horaria: $json.timezone || null,
    isp: $json.isp || null,
    org: $json.org || null,
    as: $json.as || null,
    asname: $json.asname || null,
    reverse: $json.reverse || null,
    mobile: Boolean($json.mobile),
    proxy: Boolean($json.proxy),
    hosting: Boolean($json.hosting)
  };
}
return { json: { ...ctx, ipapi } };
