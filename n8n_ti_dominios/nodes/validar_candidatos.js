//@@HELPERS
// Modo: una vez para todos. Cruza candidatos + DNS, calcula confianza de coincidencia por nombre,
// separa aceptados / posibles / descartados y REGISTRA los nombres sin dominio (el flujo continúa).
const cfg = $('Config').first().json;
const W = cfg.pesos_descubrimiento;
const esPrivada = ip => /^(10\.|127\.|0\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.|100\.(6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.)/.test(ip);

// 1) Resultado DNS por dominio (agrega respuestas del dominio raíz y de www.)
const dns = {};
let resol = [];
try { resol = $('DoH Candidatos').all(); } catch (e) { resol = []; }
const cands = $('Expandir candidatos').all();
resol.forEach((r, i) => {
  const itemCand = cands[i] && cands[i].json;
  if (!itemCand || !itemCand.dominio) return;
  const dom = itemCand.dominio;
  dns[dom] = dns[dom] || { estado: 'no_disponible', ips: [], usa_www: false };
  const st = estadoHttp(r.json);
  if (!st.ok) return;
  const ips = [...new Set((r.json.Answer || []).filter(a => a.type === 1).map(a => a.data))];
  const publicas = ips.filter(ip => !esPrivada(ip));
  if (publicas.length > 0) {
    dns[dom].estado = 'ok';
    publicas.forEach(ip => {
      if (!dns[dom].ips.includes(ip)) dns[dom].ips.push(ip);
    });
    if (itemCand.es_www && dns[dom].ips.length === publicas.length) {
      dns[dom].usa_www = true;
    }
  } else if (dns[dom].estado !== 'ok') {
    dns[dom].estado = r.json.Status === 0 ? (ips.length ? 'solo_ip_privada' : 'sin_registro_a') : 'nxdomain';
  }
});

// 2) Evaluación por nombre
const nombres = $('Norm crt.sh').all().map(i => i.json);
const resumenNombres = [], sinDominio = [], globales = new Map();
for (const n of nombres) {
  const d = n.descubrimiento;
  const cand = new Map();
  const sumar = (dom, fuente, pts) => {
    if (!dom) return;
    const c = cand.get(dom) || { dominio: dom, fuentes: [], confianza: 0 };
    if (!c.fuentes.includes(fuente)) { c.fuentes.push(fuente); c.confianza += pts; }
    cand.set(dom, c);
  };
  (d.directo && d.directo.dominios || []).forEach(x => sumar(x, 'directo', 1.0));
  (d.wikidata.dominios || []).forEach(x => sumar(x, 'wikidata', W.wikidata));
  (d.crtsh.dominios || []).forEach(x => sumar(x, 'crt.sh', W.crtsh));
  if (d.busqueda && d.busqueda.dominios) {
    d.busqueda.dominios.forEach(x => sumar(x.dominio, `busqueda#${x.posicion}`, x.posicion === 1 ? W.busqueda_top1 : W.busqueda_top5));
  }
  (d.heuristica.dominios || []).forEach(x => sumar(x, 'heuristica', W.heuristica));

  const aceptados = [], posibles = [], descartados = [];
  for (const c of cand.values()) {
    const label = c.dominio.split('.')[0];
    const matchToken = (n.acronimo && label === n.acronimo) || (n.slug_primero_ultimo && label === n.slug_primero_ultimo) || n.tokens.some(t => (t.length >= 3 && label.includes(t)) || (label.length >= 3 && t.includes(label)));
    if (matchToken) { c.confianza += W.bonus_token; c.fuentes.push('token_en_dominio'); }
    c.confianza = Math.min(1, Math.round(c.confianza * 100) / 100);
    const r = dns[c.dominio] || { estado: 'no_resuelto', ips: [], usa_www: false };
    c.dns = r.estado;
    c.ips = r.ips.slice(0, cfg.max_ips_por_dominio);
    c.url = r.usa_www ? `https://www.${c.dominio}` : `https://${c.dominio}`;
    const soloHeur = c.fuentes.every(f => f === 'heuristica' || f === 'token_en_dominio');
    if (!r.ips.length) {
      if (!soloHeur) descartados.push({ ...c, motivo: r.estado === 'no_disponible' ? 'DNS no disponible' : `no resuelve a IP pública (${r.estado})` });
    } else if (c.confianza >= cfg.umbral_confianza_dominio) {
      aceptados.push(c);
    } else {
      posibles.push({ ...c, motivo: 'confianza de coincidencia insuficiente (revisión manual)' });
    }
  }
  aceptados.sort((a, b) => b.confianza - a.confianza);

  const estadoFuentes = { wikidata: d.wikidata.estado, crtsh: d.crtsh.estado };
  const motivosFuentes = {};
  for (const k of ['wikidata', 'crtsh']) if (d[k] && d[k].motivo) motivosFuentes[k] = d[k].motivo;

  const reg = { nombre: n.nombre, estado: aceptados.length ? 'con_dominio' : 'sin_dominio', dominios_aceptados: aceptados, posibles, descartados, estado_fuentes: estadoFuentes, motivos_fuentes: motivosFuentes };
  resumenNombres.push(reg);

  if (!aceptados.length) {
    const todasCaidas = Object.values(estadoFuentes).every(e => e === 'no_disponible');
    sinDominio.push({
      nombre: n.nombre,
      motivo: todasCaidas ? 'todas las fuentes de descubrimiento no disponibles (reintentar)' : 'sin coincidencias verificadas',
      posibles_para_revision: posibles.map(p => ({ dominio: p.dominio, confianza: p.confianza, fuentes: p.fuentes })),
      estado_fuentes: estadoFuentes,
      registrado_en: new Date().toISOString()
    });
  }

  // 3) Deduplicación global: un dominio compartido por varios nombres se consulta UNA vez
  for (const a of aceptados) {
    const g = globales.get(a.dominio);
    if (g) {
      if (!g.nombres_origen.includes(n.nombre)) g.nombres_origen.push(n.nombre);
      g.confianza = Math.max(g.confianza, a.confianza);
      g.fuentes = [...new Set([...g.fuentes, ...a.fuentes])];
    } else {
      globales.set(a.dominio, { dominio: a.dominio, url: a.url, nombres_origen: [n.nombre], confianza: a.confianza, fuentes: [...a.fuentes], ips: a.ips });
    }
  }
}

const dominios = [...globales.values()];
return [{
  json: {
    nombres: resumenNombres,
    dominios,
    sin_dominio: sinDominio,
    lista_urls: dominios.map(x => x.url)
  },
  pairedItem: { item: 0 }
}];
