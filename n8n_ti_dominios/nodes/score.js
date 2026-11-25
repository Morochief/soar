// Modo: una vez por ítem. CONSOLIDACIÓN Y SCORE 1-100 por dominio.
// Aplica la regla de ponderación definida en el nodo Config y deja un "libro mayor" (score_detalle)
// con cada consulta que aportó puntos. Fuentes no disponibles aportan 0 y quedan marcadas.
const cfg = $('Config').first().json;
const P = cfg.pesos;
const d = $json;
const reIC = new RegExp(cfg.regex_infra_compartida, 'i');
const detalle = [];
const r1 = x => Math.round(x * 10) / 10;

const okE = e => e === 'ok' || e === 'ok_sin_datos';
const agregado = estados => {
  const ok = estados.filter(okE).length;
  return estados.length && ok === estados.length ? 'ok' : ok === 0 ? 'no_disponible' : 'parcial';
};
// Suma entradas de una fuente aplicando el tope de puntos positivos y las registra en el detalle.
function registrar(fuente, entradas, max) {
  let pos = 0;
  for (const e of entradas) {
    detalle.push({ fuente, ...e, puntos: r1(e.puntos) });
    if (e.puntos > 0) pos += e.puntos;
  }
  if (max !== undefined && pos > max) {
    detalle.push({ fuente, consulta: 'tope_de_fuente', evidencia: `positivos ${r1(pos)} > tope ${max}`, puntos: r1(max - pos) });
  }
}
function noDisponible(fuente, motivo) {
  detalle.push({ fuente, consulta: '-', evidencia: `FUENTE NO DISPONIBLE: ${motivo}. No aporta puntos (no se imputa valor).`, puntos: 0 });
}
// Para fuentes por IP: evalúa cada IP y se queda con la PEOR (mayor suma positiva).
function peorIp(fn) {
  let mejor = null;
  for (const ipr of d.ips) {
    const ent = fn(ipr);
    if (!ent) continue;
    const s = ent.reduce((a, e) => a + e.puntos, 0);
    if (!mejor || s > mejor.s) mejor = { s, ent };
  }
  return mejor ? mejor.ent : [];
}
const infraCompartida = ipr =>
  reIC.test(`${ipr.shodan.org || ''} ${ipr.shodan.isp || ''} ${ipr.abuseipdb.isp || ''} ${ipr.ipapi.org || ''} ${ipr.ipapi.isp || ''}`) || ipr.ipapi.hosting === true;

detalle.push({ fuente: 'base', consulta: '-', evidencia: 'Punto de partida neutral', puntos: P.base });

// ---------- 1. SHODAN ----------
const estShodan = agregado(d.ips.map(i => i.shodan.estado));
if (estShodan === 'no_disponible') noDisponible('shodan', d.ips[0] ? d.ips[0].shodan.motivo : 'sin IPs');
else registrar('shodan', peorIp(ipr => {
  const s = ipr.shodan; if (s.estado !== 'ok') return null;
  const e = [];
  const nv = s.vulns.length;
  if (nv >= 5) e.push({ consulta: `host/${ipr.ip}`, evidencia: `${nv} CVEs asociadas (${s.vulns.slice(0, 5).join(', ')}...)`, puntos: P.shodan.cves_5 });
  else if (nv >= 1) e.push({ consulta: `host/${ipr.ip}`, evidencia: `${nv} CVE(s): ${s.vulns.join(', ')}`, puntos: P.shodan.cves_1 });
  const riesgo = s.puertos.filter(p => cfg.puertos_riesgo.includes(p));
  if (riesgo.length) e.push({ consulta: `host/${ipr.ip}`, evidencia: `Puertos sensibles expuestos: ${riesgo.join(', ')}`, puntos: Math.min(riesgo.length * P.shodan.puerto_riesgo, P.shodan.max_puertos) });
  if (!nv && s.puertos.length && s.puertos.every(p => cfg.puertos_web.includes(p))) e.push({ consulta: `host/${ipr.ip}`, evidencia: `Solo puertos web (${s.puertos.join(', ')}) y sin CVEs`, puntos: P.shodan.solo_web });
  if (!e.length) e.push({ consulta: `host/${ipr.ip}`, evidencia: `Puertos: ${s.puertos.join(', ') || 'ninguno'}; sin hallazgos ponderables`, puntos: 0 });
  return e;
}), P.shodan.max);

// ---------- 2. ABUSEIPDB ----------
const estAbuse = agregado(d.ips.map(i => i.abuseipdb.estado));
if (estAbuse === 'no_disponible') noDisponible('abuseipdb', d.ips[0] ? d.ips[0].abuseipdb.motivo : 'sin IPs');
else registrar('abuseipdb', peorIp(ipr => {
  const a = ipr.abuseipdb; if (a.estado !== 'ok') return null;
  const f = infraCompartida(ipr) ? P.cdn_factor : 1;
  const nota = f < 1 ? ` (infraestructura compartida x${P.cdn_factor})` : '';
  const ev = `confianza_abuso=${a.confianza_abuso}, reportes=${a.total_reportes}`;
  const c = `check/${ipr.ip}`;
  if (a.confianza_abuso >= P.abuseipdb.alto.umbral) return [{ consulta: c, evidencia: ev + nota, puntos: P.abuseipdb.alto.pts * f }];
  if (a.confianza_abuso >= P.abuseipdb.medio.umbral) return [{ consulta: c, evidencia: ev + nota, puntos: P.abuseipdb.medio.pts * f }];
  if (a.confianza_abuso >= P.abuseipdb.bajo.umbral) return [{ consulta: c, evidencia: ev + nota, puntos: P.abuseipdb.bajo.pts * f }];
  if (!a.total_reportes) return [{ consulta: c, evidencia: 'Sin reportes de abuso (90 días)', puntos: P.abuseipdb.limpio }];
  return [{ consulta: c, evidencia: ev + ' (reportes antiguos/baja confianza, informativo)', puntos: 0 }];
}), P.abuseipdb.max);

// ---------- 3. IP-API (PROXY / HOSTING / DATACENTER) ----------
const estIPAPI = agregado(d.ips.map(i => i.ipapi.estado));
if (estIPAPI === 'no_disponible') noDisponible('ipapi', d.ips[0] ? d.ips[0].ipapi.motivo : 'sin IPs');
else registrar('ipapi', peorIp(ipr => {
  const a = ipr.ipapi; if (a.estado !== 'ok') return null;
  const f = infraCompartida(ipr) ? P.cdn_factor : 1;
  const c = `ip-api/json/${ipr.ip}`;
  if (a.proxy) return [{ consulta: c, evidencia: `IP clasificada como PROXY / VPN / Anonimizador (${a.isp || a.org || 'desconocido'})`, puntos: P.ipapi.proxy * f }];
  if (a.hosting) return [{ consulta: c, evidencia: `IP alojada en Datacenter / Cloud / Hosting (${a.isp || a.org || 'desconocido'})`, puntos: P.ipapi.hosting * f }];
  return [{ consulta: c, evidencia: `Infraestructura corporativa/residencial propia (no proxy/no hosting)`, puntos: P.ipapi.limpio }];
}), P.ipapi.max);

// ---------- 4. ABUSE.CH (URLhaus + ThreatFox + Feodo) ----------
const uh = d.abusech.urlhaus, tf = d.abusech.threatfox;
const estFeodo = agregado(d.ips.map(i => i.feodo.estado));
const estAbusech = agregado([uh.estado, tf.estado, estFeodo === 'parcial' ? 'ok' : estFeodo]);
if (estAbusech === 'no_disponible') noDisponible('abuse.ch', `URLhaus: ${uh.motivo}; ThreatFox: ${tf.motivo}; Feodo: ${d.ips[0] ? d.ips[0].feodo.motivo : '-'}`);
else {
  const e = [];
  const feodoHit = d.ips.find(i => i.feodo.estado === 'ok' && i.feodo.listada);
  if (feodoHit) e.push({ consulta: 'feodotracker/ipblocklist', evidencia: `${feodoHit.ip} es C2 de botnet (${feodoHit.feodo.detalle.malware})`, puntos: P.abusech.feodo_c2 });
  if (uh.estado === 'ok' && uh.listado) {
    if (uh.urls_online > 0) e.push({ consulta: 'urlhaus/host', evidencia: `${uh.urls_online} URL(s) de malware ONLINE (${uh.amenazas.join(', ')})`, puntos: P.abusech.urlhaus_online });
    else e.push({ consulta: 'urlhaus/host', evidencia: `${uh.urls_total} URL(s) históricas, ninguna online`, puntos: P.abusech.urlhaus_historico });
  }
  if (tf.estado === 'ok' && tf.listado) e.push({ consulta: 'threatfox/search_ioc', evidencia: `${tf.iocs.length} IOC(s): ${[...new Set(tf.iocs.map(x => x.malware))].join(', ')}`, puntos: P.abusech.threatfox_ioc });
  if (!e.length) {
    if (estAbusech === 'ok') e.push({ consulta: 'urlhaus+threatfox+feodo', evidencia: 'Sin presencia en listas de abuse.ch', puntos: P.abusech.limpio });
    else e.push({ consulta: 'abuse.ch parcial', evidencia: 'Sin hallazgos en las subconsultas disponibles (cobertura parcial, sin bonificación)', puntos: 0 });
  }
  for (const [n, est] of [['urlhaus', uh], ['threatfox', tf]]) if (est.estado !== 'ok') e.push({ consulta: n, evidencia: `subconsulta no disponible: ${est.motivo}`, puntos: 0 });
  registrar('abuse.ch', e, P.abusech.max);
}

// ---------- 5. MXTOOLBOX ----------
const mx = d.mxtoolbox;
if (mx.estado === 'no_disponible') noDisponible('mxtoolbox', mx.mx.motivo);
else {
  const e = [];
  const txt = o => `${(o.failed || []).join(' | ')} ${(o.warnings || []).join(' | ')} ${o.info || ''}`;
  if (mx.blacklist.estado === 'ok' && mx.blacklist.failed.length) e.push({ consulta: 'lookup/blacklist', evidencia: `Listado en: ${mx.blacklist.failed.slice(0, 5).join('; ')}`, puntos: P.mxtoolbox.blacklist });
  let spfOk = false, dmarcFuerte = false;
  if (mx.spf.estado === 'ok') {
    if (/no spf record|spf record published/i.test(mx.spf.failed.join(' '))) e.push({ consulta: 'lookup/spf', evidencia: 'Sin registro SPF', puntos: P.mxtoolbox.sin_spf });
    else if (/\+all/i.test(txt(mx.spf))) e.push({ consulta: 'lookup/spf', evidencia: 'SPF permisivo (+all)', puntos: P.mxtoolbox.spf_permisivo });
    else spfOk = true;
  }
  if (mx.dmarc.estado === 'ok') {
    if (/no dmarc record|dmarc record published/i.test(mx.dmarc.failed.join(' '))) e.push({ consulta: 'lookup/dmarc', evidencia: 'Sin registro DMARC', puntos: P.mxtoolbox.sin_dmarc });
    else if (/p=none/i.test(txt(mx.dmarc))) e.push({ consulta: 'lookup/dmarc', evidencia: 'DMARC en p=none (solo monitoreo)', puntos: P.mxtoolbox.dmarc_none });
    else if (/p=(reject|quarantine)/i.test(txt(mx.dmarc))) dmarcFuerte = true;
  }
  if (mx.mx.estado === 'ok' && mx.mx.info === '[]') e.push({ consulta: 'lookup/mx', evidencia: 'Sin registros MX (dominio no recibe correo) - informativo', puntos: 0 });
  if (!e.some(x => x.puntos > 0) && mx.estado === 'ok' && spfOk && dmarcFuerte && !mx.blacklist.failed.length) {
    e.push({ consulta: 'mx+spf+dmarc+blacklist', evidencia: 'SPF correcto, DMARC reject/quarantine y sin blacklists', puntos: P.mxtoolbox.correo_ok });
  }
  for (const c of ['mx', 'spf', 'dmarc', 'blacklist']) if (mx[c].estado !== 'ok') e.push({ consulta: `lookup/${c}`, evidencia: `subconsulta no disponible: ${mx[c].motivo}`, puntos: 0 });
  if (!e.length) e.push({ consulta: 'mx+spf+dmarc+blacklist', evidencia: 'Sin hallazgos ponderables', puntos: 0 });
  registrar('mxtoolbox', e, P.mxtoolbox.max);
}

// ---------- ISO (informativo, ajuste leve) ----------
const iso = d.certificados_iso;
if (iso.estado === 'ok' && iso.normas.some(n => n.norma === 'ISO 27001')) {
  detalle.push({ fuente: 'iso', consulta: 'web', evidencia: 'ISO 27001 declarada en el sitio (no verificada)', puntos: P.iso.iso27001_declarado });
}

// ---------- RESULTADO ----------
const total = detalle.reduce((a, e) => a + e.puntos, 0);
const score = Math.max(P.min, Math.min(P.max, Math.round(total)));
const estados = { shodan: estShodan, abuseipdb: estAbuse, ipapi: estIPAPI, abusech: estAbusech, mxtoolbox: mx.estado };
const disponibles = Object.values(estados).filter(e => e !== 'no_disponible').length;
const completas = Object.values(estados).filter(e => e === 'ok').length;

return {
  json: {
    dominio: d.dominio,
    url: d.url,
    nombres_origen: d.nombres_origen,
    confianza_match: d.confianza_match,
    fuentes_match: d.fuentes_match,
    score,
    nivel_riesgo: score < 25 ? 'bajo' : score < 50 ? 'medio' : score < 75 ? 'alto' : 'critico',
    confianza_score: completas === 5 ? 'alta' : disponibles >= 3 ? 'media' : 'baja',
    score_parcial: completas < 5,
    fuentes_disponibles: `${disponibles}/5`,
    score_detalle: detalle,
    estado_consultas: {
      shodan: estShodan,
      abuseipdb: estAbuse,
      ipapi: estIPAPI,
      abusech: { global: estAbusech, urlhaus: uh.estado, threatfox: tf.estado, feodo: estFeodo },
      mxtoolbox: { global: mx.estado, mx: mx.mx.estado, spf: mx.spf.estado, dmarc: mx.dmarc.estado, blacklist: mx.blacklist.estado },
      certificados_iso: iso.estado
    },
    hallazgos: {
      por_ip: d.ips,
      abusech: d.abusech,
      mxtoolbox: mx,
      dns_detalle: d.dns_detalle || null,
      rdap: d.rdap || null
    },
    certificados_iso: iso
  }
};
