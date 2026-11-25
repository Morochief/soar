//@@HELPERS
// Modo: una vez para todos. Normaliza las 4 consultas MXToolbox y las reagrupa por dominio.
const exp = $('Expandir MX').all();
const res = $input.all();
const porDominio = {};
res.forEach((r, i) => {
  const { dominio, cmd } = exp[i].json;
  const st = estadoHttp(r.json);
  let v;
  if (!st.ok) {
    v = { estado: 'no_disponible', motivo: motivoFallo(st), failed: [], warnings: [], passed: 0, registros: [] };
  } else if (!r.json.Command && !Array.isArray(r.json.Failed)) {
    v = { estado: 'no_disponible', motivo: 'respuesta inesperada (¿cuota agotada?)', failed: [], warnings: [], passed: 0, registros: [] };
  } else {
    const nombres = arr => (arr || []).map(x => `${x.Name || ''}${x.Info ? ': ' + x.Info : ''}`);
    let registros = [];
    if (Array.isArray(r.json.Information)) {
      registros = r.json.Information.map(x => ({
        clave: x.Name || x.Hostname || x.Type || x.Prefix || '',
        valor: x.Value || x.IP_Address || x.Info || '',
        desc: x.Description || ''
      })).filter(x => x.clave || x.valor);
    }
    v = {
      estado: 'ok',
      failed: nombres(r.json.Failed),
      warnings: nombres(r.json.Warnings),
      passed: (r.json.Passed || []).length,
      registros: registros.slice(0, 15),
      info: JSON.stringify(r.json.Information || []).slice(0, 2000)
    };
  }
  (porDominio[dominio] = porDominio[dominio] || {})[cmd] = v;
});

return $('Norm ThreatFox').all().map((it, idx) => {
  const m = porDominio[it.json.dominio] || {};
  const cmds = ['mx', 'spf', 'dmarc', 'blacklist'];
  cmds.forEach(c => { if (!m[c]) m[c] = { estado: 'no_disponible', motivo: 'sin resultado', failed: [], warnings: [], passed: 0, registros: [] }; });
  const ok = cmds.filter(c => m[c].estado === 'ok').length;
  m.estado = ok === 4 ? 'ok' : ok === 0 ? 'no_disponible' : 'parcial';
  return { json: { ...it.json, mxtoolbox: m }, pairedItem: { item: idx } };
});
