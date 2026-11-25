// Modo: una vez para todos. Lista ÚNICA de dominios candidatos (de todos los nombres) para resolver DNS.
// Emite tanto el dominio raíz como www.<dominio> para no descartar portales que solo configuran www.
const set = new Set();
for (const it of $input.all()) {
  const d = it.json.descubrimiento;
  (d.directo && d.directo.dominios || []).forEach(x => set.add(x));
  (d.wikidata.dominios || []).forEach(x => set.add(x));
  (d.crtsh.dominios || []).forEach(x => set.add(x));
  (d.heuristica.dominios || []).forEach(x => set.add(x));
}
const out = [];
for (const dom of set) {
  out.push({ json: { dominio: dom, host_dns: dom, es_www: false }, pairedItem: { item: 0 } });
  out.push({ json: { dominio: dom, host_dns: `www.${dom}`, es_www: true }, pairedItem: { item: 0 } });
}
return out.length ? out : [{ json: { sin_candidatos: true }, pairedItem: { item: 0 } }];
