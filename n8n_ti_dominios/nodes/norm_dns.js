//@@HELPERS
// Modo: una vez para todos. Normaliza registros DNS directos vía Google DoH y enriquece MXToolbox (fallback sin cuotas).
const exp = $('Expandir DNS DoH').all();
const res = $input.all();
const porDom = {};

res.forEach((r, i) => {
  const { dominio, tipo } = exp[i].json;
  const st = estadoHttp(r.json);
  const d = (porDom[dominio] = porDom[dominio] || { mx: [], spf: [], dmarc: [], ns: [], txt_extra: [] });
  if (!st.ok || !Array.isArray(r.json.Answer)) return;

  const ans = r.json.Answer;
  if (tipo === 'MX') {
    d.mx = ans.filter(a => a.type === 15).map(a => String(a.data || '').replace(/\.$/, '').trim()).filter(Boolean);
  } else if (tipo === 'SPF') {
    const txts = ans.filter(a => a.type === 16).map(a => String(a.data || '').replace(/^"|"$/g, '').replace(/"\s+"/g, '').trim()).filter(Boolean);
    d.spf = txts.filter(t => /^v=spf1\b/i.test(t));
    d.txt_extra = txts.filter(t => !/^v=spf1\b/i.test(t)).slice(0, 8);
  } else if (tipo === 'DMARC') {
    const txts = ans.filter(a => a.type === 16).map(a => String(a.data || '').replace(/^"|"$/g, '').replace(/"\s+"/g, '').trim()).filter(Boolean);
    d.dmarc = txts.filter(t => /^v=DMARC1\b/i.test(t));
  } else if (tipo === 'NS') {
    d.ns = ans.filter(a => a.type === 2).map(a => String(a.data || '').replace(/\.$/, '').trim()).filter(Boolean);
  }
});

return $('Norm MXToolbox').all().map((it, idx) => {
  const dom = it.json.dominio;
  const mx = JSON.parse(JSON.stringify(it.json.mxtoolbox || {}));
  const dns = porDom[dom] || { mx: [], spf: [], dmarc: [], ns: [], txt_extra: [] };

  // Enriquecer MX con registros directos DoH
  if (dns.mx.length) {
    if (!mx.mx || mx.mx.estado !== 'ok') {
      mx.mx = { estado: 'ok', fuente: 'Google DoH', failed: [], warnings: [], passed: dns.mx.length, registros: dns.mx.map(v => ({ clave: 'MX', valor: v })) };
    } else if (!mx.mx.registros || !mx.mx.registros.length) {
      mx.mx.registros = dns.mx.map(v => ({ clave: 'MX', valor: v }));
    }
  }

  // Enriquecer SPF con registros directos DoH
  if (dns.spf.length || !mx.spf || mx.spf.estado !== 'ok') {
    const spfVal = dns.spf[0] || null;
    if (!mx.spf || mx.spf.estado !== 'ok') {
      const failed = [];
      if (!spfVal) failed.push('SPF Record Not Found');
      else if (/\+all\b/i.test(spfVal)) failed.push('SPF Syntax/Permissive (+all)');
      mx.spf = { estado: 'ok', fuente: 'Google DoH', failed, warnings: [], passed: spfVal ? 1 : 0, registros: spfVal ? [{ clave: 'SPF', valor: spfVal }] : [] };
    } else if ((!mx.spf.registros || !mx.spf.registros.length) && spfVal) {
      mx.spf.registros = [{ clave: 'SPF', valor: spfVal }];
    }
  }

  // Enriquecer DMARC con registros directos DoH
  if (dns.dmarc.length || !mx.dmarc || mx.dmarc.estado !== 'ok') {
    const dmVal = dns.dmarc[0] || null;
    if (!mx.dmarc || mx.dmarc.estado !== 'ok') {
      const failed = [];
      const warnings = [];
      if (!dmVal) failed.push('DMARC Record Not Found');
      else if (/p=none\b/i.test(dmVal)) warnings.push('DMARC Policy Not Enabled (p=none)');
      mx.dmarc = { estado: 'ok', fuente: 'Google DoH', failed, warnings, passed: dmVal ? 1 : 0, registros: dmVal ? [{ clave: 'DMARC', valor: dmVal }] : [] };
    } else if ((!mx.dmarc.registros || !mx.dmarc.registros.length) && dmVal) {
      mx.dmarc.registros = [{ clave: 'DMARC', valor: dmVal }];
    }
  }

  const cmds = ['mx', 'spf', 'dmarc', 'blacklist'];
  const ok = cmds.filter(c => mx[c] && mx[c].estado === 'ok').length;
  mx.estado = ok === 4 ? 'ok' : ok === 0 ? 'no_disponible' : 'parcial';

  return { json: { ...it.json, mxtoolbox: mx, dns_detalle: dns }, pairedItem: { item: idx } };
});
