// Modo: una vez para todos. Deduplica IPs entre dominios (p.ej. hosting compartido):
// cada IP se consulta UNA sola vez en Shodan / AbuseIPDB / IP-API.
const m = new Map();
$input.all().forEach((it, idx) => {
  for (const ip of it.json.ips || []) {
    if (!m.has(ip)) m.set(ip, { dominios: [], idx });
    m.get(ip).dominios.push(it.json.dominio);
  }
});
return [...m].map(([ip, v]) => ({ json: { ip, dominios: v.dominios }, pairedItem: { item: v.idx } }));
