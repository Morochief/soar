//@@HELPERS
// Modo: una vez por ítem. crt.sh devuelve un array JSON (se pidió como texto para que n8n no lo divida).
// Agrega también los candidatos heurísticos (slugs + acrónimos + TLDs) y dominios directos.
const cfg = $('Config').first().json;
const ctx = $('Norm Wikidata').item.json;
const st = estadoHttp($json);
let crtsh;
if (!st.ok) {
  crtsh = { estado: 'no_disponible', motivo: motivoFallo(st), dominios: [] };
} else {
  let arr;
  try { arr = JSON.parse($json.data || '[]'); } catch (e) { arr = null; }
  if (!Array.isArray(arr)) {
    crtsh = { estado: 'no_disponible', motivo: 'respuesta no JSON (crt.sh saturado)', dominios: [] };
  } else {
    const cuenta = {};
    for (const c of arr) {
      for (const n of String(c.name_value || '').split('\n')) {
        const d = registrable(n);
        if (d) cuenta[d] = (cuenta[d] || 0) + 1;
      }
    }
    const dominios = Object.entries(cuenta).sort((a, b) => b[1] - a[1]).slice(0, 10).map(x => x[0]);
    crtsh = { estado: 'ok', certificados: arr.length, dominios };
  }
}

// Generación heurística (slugs + acrónimos) y dominios directos
// Si el usuario ya ingresó explícitamente un dominio/URL (ej: pechugon.com.py), evitar 50+ permutaciones heurísticas
const esDominioExplicito = Boolean(ctx.dominio_directo) && !/\s/.test(ctx.nombre || '');
const heuristicaDominios = [];
if (!esDominioExplicito) {
  const slugs = [];
  if (ctx.slug && ctx.slug.length >= 3) slugs.push(ctx.slug);
  if (ctx.acronimo && ctx.acronimo.length >= 2 && ctx.acronimo !== ctx.slug) slugs.push(ctx.acronimo);
  if (ctx.slug_primero_ultimo && ctx.slug_primero_ultimo.length >= 3 && !slugs.includes(ctx.slug_primero_ultimo)) {
    slugs.push(ctx.slug_primero_ultimo);
  }
  for (const s of slugs) {
    for (const t of cfg.tlds_heuristica) {
      heuristicaDominios.push(`${s}.${t}`);
    }
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

return { json: { ...ctx, descubrimiento: { ...ctx.descubrimiento, crtsh, heuristica, directo } } };
