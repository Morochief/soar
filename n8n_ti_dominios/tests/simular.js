// Simulación local del workflow: ejecuta los nodos Code reales del JSON generado con respuestas HTTP simuladas.
// Uso: node tests/simular.js
const fs = require('fs');
const path = require('path');
const wf = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'workflow_ti_dominios.json'), 'utf8'));
const byName = Object.fromEntries(wf.nodes.map(n => [n.name, n]));

function runCode(name, input, store) {
  const node = byName[name];
  const $ = (n) => {
    if (!store[n]) throw new Error(`Node '${n}' hasn't been executed`);
    return { first: () => store[n][0], all: () => store[n], get item() { return store[n][curIdx]; } };
  };
  let curIdx = 0;
  const $input = { all: () => input, first: () => input[0] };
  const fn = new Function('$', '$input', '$json', node.parameters.jsCode);
  if (node.parameters.mode === 'runOnceForEachItem') {
    return input.map((it, i) => { curIdx = i; const r = fn($, $input, it.json); return { json: r.json }; });
  }
  return fn($, $input, undefined);
}
const err = (code, msg) => ({ json: { error: { message: `${code} - ${msg}`, httpCode: String(code) } } });

// ---------- respuestas simuladas ----------
const MOCK = {
  'Wikidata SPARQL': j => j.nombre.startsWith('Acme')
    ? { json: { results: { bindings: [{ item: { value: 'Q1' }, itemLabel: { value: 'Acme' }, website: { value: 'https://www.acme-corp.com/' } }] } } }
    : { json: { results: { bindings: [] } } },
  'crt.sh Organización': j => err(502, 'Bad Gateway'),
  'Búsqueda web (Brave)': j => j.nombre.startsWith('Acme')
    ? { json: { web: { results: [{ url: 'https://es.wikipedia.org/wiki/Acme' }, { url: 'https://www.acme-corp.com/es' }, { url: 'https://shop.acme.com.ar' }] } } }
    : { json: { web: { results: [{ url: 'https://www.linkedin.com/x' }] } } },
  'DoH Candidatos': j => ({
    'acme-corp.com': { json: { Status: 0, Answer: [{ type: 1, data: '203.0.113.10' }, { type: 1, data: '203.0.113.11' }] } },
    'acme.com.ar': { json: { Status: 0, Answer: [{ type: 1, data: '203.0.113.10' }] } }
  }[j.dominio] || { json: { Status: 3 } }),
  'Shodan Host': j => j.ip === '203.0.113.10'
    ? { json: { org: 'Acme Hosting', isp: 'Acme', ports: [22, 80, 443, 3389], vulns: ['CVE-2024-1', 'CVE-2024-2'], data: [{ port: 3389, transport: 'tcp', product: 'RDP' }] } }
    : err(404, 'No information available for that IP.'),
  'AbuseIPDB Check': j => j.ip === '203.0.113.10'
    ? { json: { data: { abuseConfidenceScore: 80, totalReports: 42, numDistinctUsers: 10, isWhitelisted: false, isp: 'Acme' } } }
    : { json: { data: { abuseConfidenceScore: 0, totalReports: 0 } } },
  'IP-API Proxy & Hosting': j => ({
    json: {
      status: 'success',
      country: 'Paraguay',
      countryCode: 'PY',
      regionName: 'Asuncion',
      city: 'Asuncion',
      isp: 'Acme ISP',
      org: 'Acme Hosting',
      as: 'AS12345 Acme Corp',
      proxy: false,
      hosting: false,
      query: j.ip
    }
  }),
  'Feodo Blocklist': () => ({ json: { data: JSON.stringify([{ ip_address: '198.51.100.7', malware: 'QakBot', port: 443, status: 'online' }]) } }),
  'URLhaus Host': j => j.dominio === 'acme-corp.com'
    ? { json: { query_status: 'ok', url_count: '2', urls: [{ url: 'http://acme-corp.com/x.exe', url_status: 'online', threat: 'malware_download', tags: ['AgentTesla'] }, { url: 'http://acme-corp.com/y', url_status: 'offline', threat: 'malware_download' }] } }
    : { json: { query_status: 'no_results' } },
  'ThreatFox IOC': j => ({ json: { query_status: 'no_result' } }),
  'MXToolbox Lookup': j => {
    if (j.cmd === 'blacklist' && j.dominio === 'acme-corp.com') return err(429, 'Too Many Requests');
    if (j.cmd === 'dmarc') return { json: { Command: 'dmarc', Failed: [], Passed: [{}], Information: [{ Value: 'v=DMARC1; p=reject' }] } };
    if (j.cmd === 'spf') return { json: { Command: 'spf', Failed: [], Passed: [{}], Information: [{ Value: 'v=spf1 include:_spf.google.com -all' }] } };
    return { json: { Command: j.cmd, Failed: [], Passed: [{}], Information: [{ Hostname: 'mx.acme' }] } };
  },
  'DoH DNS Registros': j => {
    if (j.tipo === 'MX') return { json: { Status: 0, Answer: [{ type: 15, data: '10 mail.acme-corp.com.' }] } };
    if (j.tipo === 'SPF') return { json: { Status: 0, Answer: [{ type: 16, data: '"v=spf1 include:_spf.google.com -all"' }] } };
    if (j.tipo === 'DMARC') return { json: { Status: 0, Answer: [{ type: 16, data: '"v=DMARC1; p=reject"' }] } };
    if (j.tipo === 'NS') return { json: { Status: 0, Answer: [{ type: 2, data: 'ns1.acme-corp.com.' }] } };
    return { json: { Status: 3 } };
  },
  'RDAP Whois': j => ({
    json: {
      events: [{ eventAction: 'registration', eventDate: '2010-05-01T00:00:00Z' }, { eventAction: 'expiration', eventDate: '2028-05-01T00:00:00Z' }],
      entities: [{ roles: ['registrar'], vcardArray: ['vcard', [['fn', {}, 'text', 'GoDaddy.com, LLC']]] }],
      status: ['clientTransferProhibited'],
      secureDNS: { delegationSigned: true }
    }
  }),
  'Web ISO': j => j.url === 'https://acme-corp.com/certificaciones'
    ? { json: { html: '<html><p>Contamos con certificación ISO/IEC 27001:2022 e ISO 9001</p></html>' } }
    : (j.url.endsWith('/') ? { json: { html: '<html>home</html>' } } : err(404, 'Not Found'))
};
const HTTP = (name, input) => byName[name].executeOnce ? [MOCK[name](input[0].json)] : input.map(i => MOCK[name](i.json));

function ejecutar(nombres) {
  const s = {};
  s['Config'] = runCode('Config', [{ json: { body: { nombres } } }], s);
  const seq1 = ['Normalizar nombres', 'Wikidata SPARQL', 'Norm Wikidata', 'crt.sh Organización', 'Norm crt.sh', 'Expandir candidatos'];
  let prev = s['Config'];
  for (const n of seq1) { prev = s[n] = MOCK[n] ? HTTP(n, prev) : runCode(n, prev, s); }
  if (!prev[0].json.sin_candidatos) prev = s['DoH Candidatos'] = HTTP('DoH Candidatos', prev);
  prev = s['Validar candidatos'] = runCode('Validar candidatos', prev, s);
  if (prev[0].json.dominios.length > 0) {
    const seq2 = ['Dominios únicos', 'IPs únicas', 'Shodan Host', 'Norm Shodan', 'AbuseIPDB Check', 'Norm AbuseIPDB',
      'IP-API Proxy & Hosting', 'Norm IP-API', 'Feodo Blocklist', 'Agrupar por dominio', 'URLhaus Host', 'Norm URLhaus',
      'ThreatFox IOC', 'Norm ThreatFox', 'Expandir MX', 'MXToolbox Lookup', 'Norm MXToolbox', 'Expandir DNS DoH',
      'DoH DNS Registros', 'Norm DNS DoH', 'RDAP Whois', 'Norm RDAP', 'Expandir URLs ISO', 'Web ISO', 'Norm ISO', 'Score'];
    for (const n of seq2) { prev = s[n] = MOCK[n] ? HTTP(n, prev) : runCode(n, prev, s); }
  }
  return runCode('Reporte final', prev, s)[0].json;
}

const assert = require('assert');
const r = ejecutar(['Acme Corp S.A.', 'Empresa Inexistente XYZ 123', 'acme corp s.a.']);
console.log(JSON.stringify(r.tabla, null, 2));
console.log('sin_dominio:', JSON.stringify(r.sin_dominio.map(x => [x.nombre, x.motivo])));
const acme = r.dominios.find(d => d.dominio === 'acme-corp.com');
console.log('\nDetalle score acme-corp.com:');
acme.score_detalle.forEach(e => console.log(`  ${String(e.puntos).padStart(6)}  ${e.fuente.padEnd(10)} ${e.consulta.padEnd(24)} ${e.evidencia}`));
console.log('estado_consultas:', JSON.stringify(acme.estado_consultas));

assert.strictEqual(r.resumen.nombres_procesados, 2, 'dedupe de nombres');
assert.strictEqual(r.sin_dominio.length, 1);
assert.ok(acme, 'acme-corp.com aceptado');
assert.strictEqual(acme.estado_consultas.mxtoolbox.blacklist, 'no_disponible');
assert.strictEqual(acme.estado_consultas.mxtoolbox.global, 'parcial');
assert.strictEqual(acme.estado_consultas.ipapi, 'ok');
assert.ok(acme.certificados_iso.normas.some(n => n.norma === 'ISO 27001' && n.versiones.includes('2022')));
assert.ok(acme.score >= 1 && acme.score <= 100);
const suma = Math.max(1, Math.min(100, Math.round(acme.score_detalle.reduce((a, e) => a + e.puntos, 0))));
assert.strictEqual(suma, acme.score, 'score = suma del detalle');

const r2 = ejecutar(['Empresa Inexistente XYZ 123']);
assert.strictEqual(r2.dominios.length, 0);
assert.strictEqual(r2.sin_dominio.length, 1);
console.log('\nOK: todas las aserciones pasaron');
