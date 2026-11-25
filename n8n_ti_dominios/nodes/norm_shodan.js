//@@HELPERS
// Modo: una vez por ítem. 1/5 del embudo: Shodan (servicios, puertos, CPEs, vulnerabilidades CVE).
const ctx = $('IPs únicas').item.json;
const st = estadoHttp($json);
let shodan;
if (!st.ok) {
  shodan = st.code === '404'
    ? { estado: 'ok_sin_datos', nota: 'Shodan no tiene información indexada de la IP', puertos: [], vulns: [], cpes: [], tags: [], hostnames: [] }
    : { estado: 'no_disponible', motivo: motivoFallo(st), puertos: [], vulns: [], cpes: [], tags: [], hostnames: [] };
} else {
  const vulns = Array.isArray($json.vulns) ? $json.vulns : Object.keys($json.vulns || {});
  const cpes = Array.isArray($json.cpes) ? $json.cpes : [];
  const hostnames = Array.isArray($json.hostnames) ? $json.hostnames : [];
  const tags = Array.isArray($json.tags) ? $json.tags : [];
  shodan = {
    estado: 'ok',
    org: $json.org || (cpes.length ? cpes.join(', ') : null) || 'Shodan InternetDB',
    isp: $json.isp || hostnames.join(', ') || null,
    asn: $json.asn || null,
    pais: $json.country_code || null,
    puertos: ($json.ports || []).slice().sort((a, b) => a - b),
    vulns,
    cpes,
    tags,
    servicios: ($json.data || []).slice(0, 20).map(s => ({ puerto: s.port, transporte: s.transport, producto: s.product || null, version: s.version || null })),
    hostnames,
    ultima_actualizacion: $json.last_update || null
  };
}
return { json: { ...ctx, shodan } };
