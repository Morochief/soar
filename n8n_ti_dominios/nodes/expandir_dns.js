// Modo: una vez para todos. Expande consultas DNS gratuitas vía Google DoH (MX, SPF/TXT, DMARC, NS) por cada dominio.
const out = [];
$input.all().forEach((it, i) => {
  const dom = it.json.dominio;
  out.push({ json: { dominio: dom, tipo: 'MX', query: dom, dnsType: 'MX' }, pairedItem: { item: i } });
  out.push({ json: { dominio: dom, tipo: 'SPF', query: dom, dnsType: 'TXT' }, pairedItem: { item: i } });
  out.push({ json: { dominio: dom, tipo: 'DMARC', query: '_dmarc.' + dom, dnsType: 'TXT' }, pairedItem: { item: i } });
  out.push({ json: { dominio: dom, tipo: 'NS', query: dom, dnsType: 'NS' }, pairedItem: { item: i } });
});
return out;
