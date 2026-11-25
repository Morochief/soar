//@@HELPERS
// Modo: una vez para todos. Detecta certificaciones ISO DECLARADAS en el sitio web del dominio.
// Nota: declaración pública != certificación verificada. Se marca verificado=false y se recomienda
// contrastar en IAF CertSearch / organismo certificador (ver README, extensión opcional).
const exp = $('Expandir URLs ISO').all();
const res = $input.all();
const RE = /ISO\s*(?:\/\s*IEC\s*)?[-\s]?(9001|14001|27001|27017|27018|27701|45001|22301|20000(?:-1)?|50001|22000|13485|37001|28000)(?:\s*[:\-]\s*((?:19|20)\d\d))?/gi;
const NOMBRES = {
  '9001': 'Gestión de calidad', '14001': 'Gestión ambiental', '27001': 'Seguridad de la información',
  '27017': 'Seguridad en cloud', '27018': 'Protección PII en cloud', '27701': 'Gestión de privacidad',
  '45001': 'Seguridad y salud laboral', '22301': 'Continuidad de negocio', '20000': 'Gestión de servicios TI',
  '20000-1': 'Gestión de servicios TI', '50001': 'Gestión energética', '22000': 'Inocuidad alimentaria',
  '13485': 'Dispositivos médicos', '37001': 'Antisoborno', '28000': 'Seguridad cadena de suministro'
};
const porDom = {};
res.forEach((r, i) => {
  const { dominio, url } = exp[i].json;
  const p = (porDom[dominio] = porDom[dominio] || { paginas_ok: 0, paginas_fallidas: 0, normas: {} });
  const st = estadoHttp(r.json);
  if (!st.ok || typeof r.json.html !== 'string') { p.paginas_fallidas++; return; }
  p.paginas_ok++;
  const texto = r.json.html.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
  let m;
  RE.lastIndex = 0;
  while ((m = RE.exec(texto)) !== null) {
    const clave = `ISO ${m[1]}`;
    const n = p.normas[clave] || (p.normas[clave] = { norma: clave, descripcion: NOMBRES[m[1]] || null, versiones: [], evidencias: [] });
    if (m[2] && !n.versiones.includes(m[2])) n.versiones.push(m[2]);
    if (n.evidencias.length < 2 && !n.evidencias.some(e => e.url === url)) {
      n.evidencias.push({ url, fragmento: texto.slice(Math.max(0, m.index - 60), m.index + 80).trim() });
    }
  }
});

return $('Norm RDAP').all().map((it, idx) => {
  const p = porDom[it.json.dominio] || { paginas_ok: 0, paginas_fallidas: 0, normas: {} };
  const normas = Object.values(p.normas);
  const certificados_iso = {
    estado: p.paginas_ok > 0 ? 'ok' : 'no_disponible',
    metodo: 'declaracion_en_sitio_web',
    verificado: false,
    encontrados: normas.length > 0,
    normas,
    paginas_revisadas: p.paginas_ok,
    paginas_fallidas: p.paginas_fallidas,
    nota: normas.length ? 'Declarado en el sitio; verificar vigencia en IAF CertSearch u organismo certificador.' : (p.paginas_ok ? 'Sin menciones a normas ISO en las páginas revisadas.' : 'Sitio web no accesible.')
  };
  return { json: { ...it.json, certificados_iso }, pairedItem: { item: idx } };
});
