// Modo: una vez para todos. 5/5 del embudo: un ítem por (dominio, comando MXToolbox).
const CMDS = ['mx', 'spf', 'dmarc', 'blacklist'];
const out = [];
$input.all().forEach((it, i) => {
  for (const cmd of CMDS) out.push({ json: { dominio: it.json.dominio, cmd }, pairedItem: { item: i } });
});
return out;
