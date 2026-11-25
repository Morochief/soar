//@@HELPERS
// Modo: una vez por ítem. Extrae datos de registro WHOIS/RDAP (antigüedad, registrador, expiración, bloqueos).
const ctx = $('Norm DNS DoH').item.json;
const st = estadoHttp($json);
let rdap;

if (!st.ok) {
  rdap = { estado: 'no_disponible', motivo: st.code === '404' ? 'TLD sin servidor RDAP público (ej. .py)' : motivoFallo(st) };
} else {
  const events = Array.isArray($json.events) ? $json.events : [];
  const getEvent = act => (events.find(e => e.eventAction === act) || {}).eventDate || null;
  let registrador = null;
  const ents = Array.isArray($json.entities) ? $json.entities : [];
  const regEnt = ents.find(e => Array.isArray(e.roles) && e.roles.includes('registrar'));
  if (regEnt && Array.isArray(regEnt.vcardArray) && Array.isArray(regEnt.vcardArray[1])) {
    const fn = regEnt.vcardArray[1].find(v => v[0] === 'fn');
    if (fn && fn[3]) registrador = fn[3];
  }
  const creacion = getEvent('registration');
  let antiguedad_anios = null;
  if (creacion) {
    const diff = Date.now() - new Date(creacion).getTime();
    if (!isNaN(diff) && diff > 0) antiguedad_anios = Math.round((diff / (1000 * 60 * 60 * 24 * 365.25)) * 10) / 10;
  }
  rdap = {
    estado: 'ok',
    registrador: registrador || 'No especificado',
    creacion,
    expiracion: getEvent('expiration'),
    actualizacion: getEvent('last changed'),
    antiguedad_anios,
    estados: Array.isArray($json.status) ? $json.status : [],
    dnssec: Boolean($json.secureDNS && $json.secureDNS.delegationSigned)
  };
}
return { json: { ...ctx, rdap } };
