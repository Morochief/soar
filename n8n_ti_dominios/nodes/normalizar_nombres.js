//@@HELPERS
// Normaliza y deduplica nombres; prepara tokens, slug, detección de dominio directo y consulta SPARQL de Wikidata.
const cfg = $('Config').first().json;
const STOP = new Set(['srl', 'ltda', 'inc', 'llc', 'corp', 'group', 'grupo', 'del', 'las', 'los', 'and', 'the', 'cia',
  'company', 'sociedad', 'anonima', 'limitada', 'holding', 'internacional']);
const vistos = new Set();
const out = [];
for (const raw of cfg.nombres) {
  const nombre = String(raw || '').trim().replace(/\s+/g, ' ');
  if (!nombre) continue;
  const clave = nombre.toLowerCase();
  if (vistos.has(clave)) continue;           // evita procesar dos veces el mismo nombre
  vistos.add(clave);

  // Detectar si el usuario ingresó directamente un dominio o URL (ej: technoma.com.py)
  let dominioDirecto = null;
  const mDom = nombre.toLowerCase().match(/(?:https?:\/\/)?([a-z0-9.-]+\.[a-z]{2,})/i);
  if (mDom) {
    dominioDirecto = registrable(mDom[1]);
  }

  const base = nombre.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const tokens = base.split(/[^a-z0-9]+/).filter(t => t.length >= 2 && !STOP.has(t));
  const slug = tokens.join('');
  const acronimo = tokens.length >= 2 && tokens.length <= 5 ? tokens.map(t => t[0]).join('') : null;
  const slugPrimeroUltimo = tokens.length >= 2 ? (tokens[0] + tokens[tokens.length - 1]) : null;
  const esc = nombre.replace(/\\/g, '\\\\').replace(/"/g, '\\"');
  const sparql = `SELECT ?item ?itemLabel ?website WHERE { SERVICE wikibase:mwapi { bd:serviceParam wikibase:endpoint "www.wikidata.org"; wikibase:api "EntitySearch"; mwapi:search "${esc}"; mwapi:language "es". ?item wikibase:apiOutputItem mwapi:item. } ?item wdt:P856 ?website. SERVICE wikibase:label { bd:serviceParam wikibase:language "es,en". } } LIMIT 5`;
  out.push({ json: { nombre, tokens, slug, acronimo, slug_primero_ultimo: slugPrimeroUltimo, sparql, dominio_directo: dominioDirecto } });
}
return out;
