//@@HELPERS
// Modo: una vez por ítem. Resultados del buscador + candidatos heurísticos (slug + TLD).
const cfg = $('Config').first().json;
const ctx = $('Norm crt.sh').item.json;
const st = estadoHttp($json);
const excl = new Set(cfg.dominios_excluidos);
let busqueda;
if (!st.ok) {
  busqueda = { estado: 'no_disponible', motivo: motivoFallo(st), dominios: [] };
} else {
  const res = ($json.web && $json.web.results) || [];
  const vistos = new Set();
  const dominios = [];
  for (const r of res) {
    const d = registrable(r.url);
    if (!d || excl.has(d) || vistos.has(d)) continue;
    vistos.add(d);
    dominios.push({ dominio: d, posicion: dominios.length + 1, titulo: r.title || null });
    if (dominios.length >= 5) break;
  }
  busqueda = { estado: 'ok', dominios };
}
const slugs = [];
if (ctx.slug && ctx.slug.length >= 3) slugs.push(ctx.slug);
if (ctx.acronimo && ctx.acronimo.length >= 2 && ctx.acronimo !== ctx.slug) slugs.push(ctx.acronimo);

const heuristicaDominios = [];
for (const s of slugs) {
  for (const t of cfg.tlds_heuristica) {
    heuristicaDominios.push(`${s}.${t}`);
  }
}

const heuristica = {
  estado: 'ok',
  dominios: heuristicaDominios
};
const directo = {
  estado: 'ok',
  dominios: ctx.dominio_directo ? [ctx.dominio_directo] : []
};
return { json: { ...ctx, descubrimiento: { ...ctx.descubrimiento, busqueda, heuristica, directo } } };
