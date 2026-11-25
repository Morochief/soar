//@@HELPERS
// Modo: una vez por ítem. 4/5 del embudo (b): abuse.ch ThreatFox (IOCs de malware / botnets).
const ctx = $('Norm URLhaus').item.json;
const st = estadoHttp($json);
let threatfox;
if (!st.ok) {
  threatfox = { estado: 'no_disponible', motivo: motivoFallo(st) };
} else if ($json.query_status === 'no_result') {
  threatfox = { estado: 'ok', listado: false };
} else if ($json.query_status === 'ok') {
  const data = Array.isArray($json.data) ? $json.data : [];
  threatfox = {
    estado: 'ok',
    listado: data.length > 0,
    iocs: data.slice(0, 10).map(x => ({ ioc: x.ioc, tipo: x.threat_type, malware: x.malware_printable, confianza: x.confidence_level, primera_vez: x.first_seen }))
  };
} else {
  threatfox = { estado: 'no_disponible', motivo: `query_status=${$json.query_status}` };
}
return { json: { ...ctx, abusech: { ...ctx.abusech, threatfox } } };
