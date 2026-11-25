//@@HELPERS
// Modo: una vez por ítem. 4/5 del embudo (a): abuse.ch URLhaus (URLs de malware alojadas en el host).
const ctx = $('Agrupar por dominio').item.json;
const st = estadoHttp($json);
let urlhaus;
if (!st.ok) {
  urlhaus = { estado: 'no_disponible', motivo: motivoFallo(st) };
} else if ($json.query_status === 'no_results') {
  urlhaus = { estado: 'ok', listado: false };
} else if ($json.query_status === 'ok') {
  const urls = $json.urls || [];
  urlhaus = {
    estado: 'ok',
    listado: true,
    urls_total: Number($json.url_count || urls.length),
    urls_online: urls.filter(u => u.url_status === 'online').length,
    amenazas: [...new Set(urls.map(u => u.threat).filter(Boolean))],
    blacklists: $json.blacklists || null,
    muestras: urls.slice(0, 5).map(u => ({ url: u.url, estado: u.url_status, amenaza: u.threat, tags: u.tags, alta: u.date_added })),
    referencia: $json.urlhaus_reference || null
  };
} else {
  urlhaus = { estado: 'no_disponible', motivo: `query_status=${$json.query_status}` };
}
return { json: { ...ctx, abusech: { urlhaus } } };
