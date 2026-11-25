//@@HELPERS
// Modo: una vez por ítem. 2/5 del embudo: AbuseIPDB (reportes de abuso y categorías de ataque, últimos 90 días).
const ctx = $('Norm Shodan').item.json;
const st = estadoHttp($json);
const CAT_MAP = {
  3: 'Fraud', 4: 'DDoS', 5: 'FTP Brute-Force', 6: 'Ping of Death', 7: 'Phishing',
  9: 'Open Proxy', 10: 'Web Spam', 11: 'Email Spam', 14: 'Port Scan', 15: 'Hacking',
  16: 'SQL Injection', 18: 'Brute-Force', 19: 'Bad Web Bot', 20: 'Exploited Host',
  21: 'Web App Attack', 22: 'SSH Attack', 23: 'IoT Targeted'
};

let abuseipdb;
if (!st.ok) {
  abuseipdb = { estado: 'no_disponible', motivo: motivoFallo(st) };
} else if (!$json.data) {
  abuseipdb = { estado: 'no_disponible', motivo: 'respuesta inesperada (sin campo data)' };
} else {
  const d = $json.data;
  const reportes = Array.isArray(d.reports) ? d.reports.slice(0, 8).map(r => ({
    fecha: r.reportedAt,
    comentario: (r.comment || '').slice(0, 140),
    categorias: (r.categories || []).map(c => CAT_MAP[c] || `Cat-${c}`),
    pais_reportante: r.reporterCountryCode || null
  })) : [];
  abuseipdb = {
    estado: 'ok',
    confianza_abuso: d.abuseConfidenceScore,
    total_reportes: d.totalReports,
    usuarios_distintos: d.numDistinctUsers,
    ultimo_reporte: d.lastReportedAt || null,
    whitelisted: d.isWhitelisted,
    tipo_uso: d.usageType || null,
    isp: d.isp || null,
    dominio: d.domain || null,
    pais: d.countryName || d.countryCode || null,
    es_tor: Boolean(d.isTor),
    hostnames: d.hostnames || [],
    reportes_recientes: reportes
  };
}
return { json: { ...ctx, abuseipdb } };
