//@@HELPERS
// Modo: una vez por ítem. Contexto = ítem de "Normalizar nombres".
const ctx = $('Normalizar nombres').item.json;
const st = estadoHttp($json);
let wikidata;
if (!st.ok) {
  wikidata = { estado: 'no_disponible', motivo: motivoFallo(st), dominios: [] };
} else {
  const rows = ($json.results && $json.results.bindings) || [];
  const dominios = [...new Set(rows.map(r => registrable(r.website && r.website.value)).filter(Boolean))];
  wikidata = {
    estado: 'ok',
    dominios,
    entidades: rows.map(r => ({ id: r.item && r.item.value, etiqueta: r.itemLabel && r.itemLabel.value, web: r.website && r.website.value }))
  };
}
return { json: { ...ctx, descubrimiento: { wikidata } } };
