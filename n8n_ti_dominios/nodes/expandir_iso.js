// Modo: una vez para todos. Un ítem por (dominio, ruta) donde suelen publicarse certificaciones.
const cfg = $('Config').first().json;
const out = [];
$input.all().forEach((it, i) => {
  const host = it.json.host_dns || it.json.dominio;
  for (const ruta of cfg.rutas_iso) out.push({ json: { dominio: it.json.dominio, host_dns: host, url: `https://${host}${ruta}` }, pairedItem: { item: i } });
});
return out;
