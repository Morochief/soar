// Modo: una vez para todos. Reagrupa resultados por IP en cada dominio y cruza con Feodo Tracker
// (abuse.ch, botnets C2) descargado UNA sola vez por ejecución.
let feodo = { estado: 'no_disponible', motivo: 'sin respuesta', mapa: new Map() };
try {
  const f = $('Feodo Blocklist').first().json;
  if (f.error === undefined) {
    const arr = JSON.parse(f.data || '[]');
    const m = new Map();
    arr.forEach(e => m.set(e.ip_address, { malware: e.malware, puerto: e.port, estado: e.status, ultimo_online: e.last_online }));
    feodo = { estado: 'ok', mapa: m };
  } else {
    feodo.motivo = (typeof f.error === 'string' ? f.error : JSON.stringify(f.error)).slice(0, 200);
  }
} catch (e) { feodo.motivo = 'blocklist ilegible'; }

const porIp = new Map($('Norm IP-API').all().map(i => [i.json.ip, i.json]));
const sinRes = { estado: 'no_disponible', motivo: 'sin resultado para la IP' };

return $('Dominios únicos').all().map((it, idx) => {
  const d = it.json;
  const ips = (d.ips || []).map(ip => {
    const r = porIp.get(ip) || {};
    return {
      ip,
      shodan: r.shodan || sinRes,
      abuseipdb: r.abuseipdb || sinRes,
      ipapi: r.ipapi || sinRes,
      feodo: feodo.estado === 'ok'
        ? { estado: 'ok', listada: feodo.mapa.has(ip), detalle: feodo.mapa.get(ip) || null }
        : { estado: 'no_disponible', motivo: feodo.motivo }
    };
  });
  return {
    json: { dominio: d.dominio, url: d.url, nombres_origen: d.nombres_origen, confianza_match: d.confianza, fuentes_match: d.fuentes, ips },
    pairedItem: { item: 0 }
  };
});
