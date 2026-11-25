// ---- helpers comunes (inyectados por build.py) ----
// Interpreta la salida de un nodo HTTP configurado con onError=continueRegularOutput.
// Si la petición falló, n8n devuelve { error: <string|objeto> } en lugar de la respuesta.
function estadoHttp(j) {
  if (!j || j.error === undefined) return { ok: true, code: null, msg: '' };
  const e = j.error;
  const txt = typeof e === 'string' ? e : JSON.stringify(e);
  let code = (e && typeof e === 'object') ? (e.httpCode || e.status || e.statusCode || (e.cause && e.cause.status) || null) : null;
  if (!code) { const m = txt.match(/\b([45]\d\d)\b/); if (m) code = m[1]; }
  return { ok: false, code: code ? String(code) : null, msg: txt.slice(0, 300) };
}
function motivoFallo(st) {
  if (st.code === '429') return 'límite de tasa (429) tras reintentos';
  if (st.code === '401' || st.code === '403') return `credencial inválida o sin permiso (${st.code})`;
  return `${st.code ? st.code + ' ' : ''}${st.msg}`.trim() || 'sin respuesta';
}
// Dominio registrable aproximado (sin Public Suffix List completa).
function registrable(h) {
  h = String(h || '').trim().toLowerCase()
    .replace(/^[a-z]+:\/\//, '').split(/[\/?#:]/)[0]
    .replace(/^\*\./, '').replace(/^www\./, '').replace(/\.$/, '');
  if (!/^[a-z0-9.-]+\.[a-z]{2,}$/.test(h)) return null;
  const p = h.split('.');
  if (p.length <= 2) return h;
  const sld = p[p.length - 2], tld = p[p.length - 1];
  const tres = tld.length === 2 && ['com', 'net', 'org', 'gov', 'gob', 'edu', 'co', 'ac', 'mil', 'nom', 'int'].includes(sld);
  return p.slice(tres ? -3 : -2).join('.');
}
// ---- fin helpers ----
