// Modo: una vez para todos. Arma la SALIDA FINAL: Suite de Inteligencia CTI con Dashboard HTML exhaustivo.
const cfg = $('Config').first().json;
const resumen = $('Validar candidatos').first().json;
const dominios = $input.all().map(i => i.json).filter(j => typeof j.score === 'number').sort((a, b) => b.score - a.score);

const conteoNiveles = dominios.reduce((a, x) => { a[x.nivel_riesgo] = (a[x.nivel_riesgo] || 0) + 1; return a; }, { critico: 0, alto: 0, medio: 0, bajo: 0 });

function esc(v) {
  return String(v ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function safeUrl(u) {
  const s = String(u || '').trim();
  return /^https?:\/\//i.test(s) ? esc(s) : '#';
}

function colorScore(s) {
  if (s >= 75) return { bg: '#dc2626', text: '#fef2f2', border: '#b91c1c', label: 'CRÍTICO' };
  if (s >= 50) return { bg: '#ea580c', text: '#fff7ed', border: '#c2410c', label: 'ALTO' };
  if (s >= 25) return { bg: '#ca8a04', text: '#fefce8', border: '#a16207', label: 'MEDIO' };
  return { bg: '#16a34a', text: '#f0fdf4', border: '#15803d', label: 'BAJO' };
}

const PUERTOS_CRITICOS = [21, 22, 23, 25, 110, 135, 139, 143, 445, 1433, 1521, 2375, 3306, 3389, 5432, 5900, 5985, 6379, 9200, 11211, 27017];
const PUERTOS_WEB = [80, 443, 8080, 8443];

function badgePuerto(p) {
  const n = Number(p);
  const isCrit = PUERTOS_CRITICOS.includes(n);
  const isWeb = PUERTOS_WEB.includes(n);
  const bg = isCrit ? '#7f1d1d' : isWeb ? '#1e3a8a' : '#374151';
  const color = isCrit ? '#fca5a5' : isWeb ? '#93c5fd' : '#e5e7eb';
  const border = isCrit ? '#b91c1c' : isWeb ? '#2563eb' : '#4b5563';
  return `<span style="background:${bg};color:${color};border:1px solid ${border};padding:2px 8px;border-radius:6px;font-size:11px;font-weight:600;font-family:monospace;display:inline-block;margin:2px;">${esc(p)}</span>`;
}

function extractMxInfo(sub) {
  if (!sub) return [];
  if (Array.isArray(sub.registros) && sub.registros.length) return sub.registros;
  if (sub.info && typeof sub.info === 'string') {
    try {
      const arr = JSON.parse(sub.info);
      if (Array.isArray(arr)) {
        return arr.map(x => ({
          clave: x.Name || x.Hostname || x.Type || x.Prefix || '',
          valor: x.Value || x['IP Address'] || x.IP_Address || x.Info || '',
          desc: x.Description || ''
        })).filter(x => x.clave || x.valor);
      }
    } catch (e) {}
  }
  return [];
}

const matrizRows = [];
const cardsDominiosHtml = dominios.map((d, idx) => {
  const col = colorScore(d.score);
  const h = d.hallazgos || {};
  const ips = h.por_ip || [];
  const primaryIp = ips[0] || {};
  const ia = primaryIp.ipapi || {};
  const sh = primaryIp.shodan || {};
  const ab = primaryIp.abuseipdb || {};
  const mx = h.mxtoolbox || {};
  const ach = h.abusech || {};
  const uh = ach.urlhaus || {};
  const tf = ach.threatfox || {};
  const iso = d.certificados_iso || {};
  const rdap = h.rdap || {};
  const dns = h.dns_detalle || {};

  const todosPuertos = [...new Set(ips.flatMap(i => (i.shodan && i.shodan.puertos) || []))].sort((a, b) => a - b);
  const todasVulns = [...new Set(ips.flatMap(i => (i.shodan && i.shodan.vulns) || []))];
  const todosCpes = [...new Set(ips.flatMap(i => (i.shodan && i.shodan.cpes) || []))];
  const todosTags = [...new Set(ips.flatMap(i => (i.shodan && i.shodan.tags) || []))];
  const todosHosts = [...new Set(ips.flatMap(i => (i.shodan && i.shodan.hostnames) || []))];
  const maxAbuse = ips.reduce((m, i) => Math.max(m, (i.abuseipdb && i.abuseipdb.confianza_abuso) || 0), 0);
  const totalReportesAbuse = ips.reduce((m, i) => m + ((i.abuseipdb && i.abuseipdb.total_reportes) || 0), 0);
  const reportesRecientes = ips.flatMap(i => (i.abuseipdb && i.abuseipdb.reportes_recientes) || []).slice(0, 8);
  const feodoHit = ips.find(i => i.feodo && i.feodo.listada);

  let mxItems = extractMxInfo(mx.mx);
  if (!mxItems.length && Array.isArray(dns.mx) && dns.mx.length) mxItems = dns.mx.map(v => ({ clave: 'MX (DoH)', valor: v }));
  let spfItems = extractMxInfo(mx.spf);
  if (!spfItems.length && Array.isArray(dns.spf) && dns.spf.length) spfItems = dns.spf.map(v => ({ clave: 'SPF (DoH)', valor: v }));
  let dmarcItems = extractMxInfo(mx.dmarc);
  if (!dmarcItems.length && Array.isArray(dns.dmarc) && dns.dmarc.length) dmarcItems = dns.dmarc.map(v => ({ clave: 'DMARC (DoH)', valor: v }));
  const blFails = (mx.blacklist && mx.blacklist.failed) || [];

  const origenTxt = (d.nombres_origen || []).join(', ');
  const searchBlob = [
    d.dominio, origenTxt, ips.map(i => i.ip).join(' '),
    ia.pais, ia.ciudad, ia.isp, ia.org, ab.isp,
    todasVulns.join(' '), todosCpes.join(' '), rdap.registrador
  ].filter(Boolean).join(' ').toLowerCase();

  matrizRows.push(`
    <tr class="matriz-row" data-nivel="${col.label}" data-search="${esc(searchBlob)}">
      <td style="padding:8px 10px;">
        <a href="#dom-${idx}" style="color:#60a5fa;font-weight:700;text-decoration:none;">${esc(d.dominio)}</a>
        <div style="color:#94a3b8;font-size:11px;">${esc(origenTxt)}</div>
      </td>
      <td style="padding:8px 10px;"><span style="background:${col.bg};color:${col.text};padding:3px 9px;border-radius:9999px;font-weight:800;font-size:11px;white-space:nowrap;">${d.score}/100 · ${col.label}</span></td>
      <td style="padding:8px 10px;">
        <div style="font-family:monospace;color:#e2e8f0;">${esc(primaryIp.ip || '-')}</div>
        <div style="color:#94a3b8;font-size:11px;">${esc(ia.pais || ab.pais || '-')} · ${esc(ia.isp || ab.isp || sh.org || '-')}</div>
      </td>
      <td style="padding:8px 10px;">${todosPuertos.length ? todosPuertos.slice(0, 4).join(', ') + (todosPuertos.length > 4 ? '...' : '') : '0 puertos'} · ${todasVulns.length ? `<span style="color:#f87171;font-weight:700;">${todasVulns.length} CVEs</span>` : '<span style="color:#22c55e;">0 CVEs</span>'}</td>
      <td style="padding:8px 10px;"><strong style="color:${maxAbuse >= 50 ? '#ef4444' : maxAbuse >= 25 ? '#eab308' : '#22c55e'};">${maxAbuse}%</strong> (${totalReportesAbuse} rep)</td>
      <td style="padding:8px 10px;">${spfItems.length ? '🟢 SPF' : '🔴 Sin SPF'} · ${dmarcItems.length ? '🟢 DMARC' : '🟡 Sin DMARC'}</td>
      <td style="padding:8px 10px;">${rdap.estado === 'ok' && rdap.antiguedad_anios !== null ? esc(rdap.antiguedad_anios) + ' años' : '-'} ${(iso.normas && iso.normas.length) ? '· 📜 ISO' : ''}</td>
    </tr>
  `);

  // 1. FILA DE IPs Y RED (IP-API)
  const filasIps = ips.map(i => {
    const api = i.ipapi || {};
    const aip = i.abuseipdb || {};
    const shd = i.shodan || {};
    const hasIpApi = api.estado === 'ok';
    const proxyBadge = !hasIpApi ? '<span style="color:#94a3b8;">N/A</span>' : api.proxy
      ? '<span style="background:#7f1d1d;color:#fca5a5;padding:2px 6px;border-radius:4px;font-weight:600;">🔴 SÍ (Proxy/VPN/Tor)</span>'
      : '<span style="background:#064e3b;color:#a7f3d0;padding:2px 6px;border-radius:4px;font-weight:600;">🟢 NO (Directo)</span>';
    const hostingBadge = !hasIpApi ? '<span style="color:#94a3b8;">N/A</span>' : api.hosting
      ? '<span style="background:#7c2d12;color:#fdba74;padding:2px 6px;border-radius:4px;font-weight:600;">🟠 Datacenter / Cloud</span>'
      : (api.mobile ? '<span style="background:#1e3a8a;color:#93c5fd;padding:2px 6px;border-radius:4px;font-weight:600;">📱 Red Móvil</span>' : '<span style="background:#064e3b;color:#a7f3d0;padding:2px 6px;border-radius:4px;font-weight:600;">🟢 Red Propia / Corp</span>');
    const loc = api.ciudad ? `${api.ciudad}${api.region ? ', ' + api.region : ''}, ${api.pais || ''}` : (api.pais || aip.pais || shd.pais || 'Desconocido');
    return `
      <tr style="border-bottom:1px solid #1e293b;font-size:12px;">
        <td style="padding:8px 10px;font-family:monospace;font-weight:600;color:#60a5fa;">
          ${esc(i.ip)}
          ${api.reverse ? `<div style="font-size:10px;color:#94a3b8;font-weight:400;">PTR: ${esc(api.reverse)}</div>` : ''}
        </td>
        <td style="padding:8px 10px;color:#e2e8f0;">
          <div>${esc(loc)} (${esc(api.pais_codigo || '-')})</div>
          ${api.zona_horaria ? `<div style="font-size:10px;color:#94a3b8;">TZ: ${esc(api.zona_horaria)}</div>` : ''}
        </td>
        <td style="padding:8px 10px;color:#cbd5e1;">${esc(api.isp || api.org || aip.isp || shd.isp || shd.org || '-')}</td>
        <td style="padding:8px 10px;color:#94a3b8;font-family:monospace;">${esc(api.as || shd.asn || '-')}</td>
        <td style="padding:8px 10px;">${proxyBadge}</td>
        <td style="padding:8px 10px;">${hostingBadge}</td>
      </tr>
    `;
  }).join('');

  // 2. VULNERABILIDADES CVE Y SOFTWARE CPE (SHODAN)
  const cpesHtml = todosCpes.length ? `
    <div style="margin-top:8px;font-size:12px;color:#cbd5e1;">
      <strong>Software &amp; Tecnologías Detectadas (CPE):</strong>
      <div style="display:flex;gap:5px;flex-wrap:wrap;margin-top:4px;">
        ${todosCpes.map(c => `<span style="background:#1e293b;color:#93c5fd;border:1px solid #334155;padding:2px 7px;border-radius:4px;font-size:11px;font-family:monospace;">${esc(c)}</span>`).join('')}
      </div>
    </div>
  ` : '';
  const tagsHtml = todosTags.length ? `<div style="font-size:11px;color:#94a3b8;margin-top:6px;"><strong>Etiquetas Shodan:</strong> ${todosTags.map(esc).join(', ')}</div>` : '';

  const vulnsHtml = todasVulns.length ? `
    <div style="margin-top:10px;">
      <div style="font-size:12px;font-weight:600;color:#f87171;margin-bottom:6px;">⚠️ Vulnerabilidades CVE Detectadas (${todasVulns.length}):</div>
      <div style="display:flex;gap:6px;flex-wrap:wrap;">
        ${todasVulns.map(v => `
          <a href="https://nvd.nist.gov/vuln/detail/${encodeURIComponent(v)}" target="_blank" style="background:#450a0a;color:#fca5a5;border:1px solid #991b1b;padding:3px 8px;border-radius:4px;font-size:11px;font-family:monospace;text-decoration:none;font-weight:600;">
            ${esc(v)} ↗
          </a>
        `).join('')}
      </div>
    </div>
  ` : '<div style="color:#22c55e;font-size:12px;margin-top:8px;">✅ Sin vulnerabilidades CVE conocidas indexadas en Shodan.</div>';

  // 3. ABUSEIPDB DETALLE + REPORTES RECIENTES
  const abuseProgressCol = maxAbuse >= 50 ? '#ef4444' : maxAbuse >= 25 ? '#eab308' : '#22c55e';
  const recientesHtml = reportesRecientes.length ? `
    <div style="margin-top:10px;border-top:1px solid #1e293b;padding-top:8px;">
      <div style="font-size:11px;font-weight:700;color:#fca5a5;margin-bottom:4px;">📋 Últimos Incidentes / Categorías Reportadas:</div>
      ${reportesRecientes.map(r => `
        <div style="font-size:11px;color:#cbd5e1;background:#0f172a;padding:5px 8px;border-radius:4px;margin-bottom:4px;border-left:2px solid #ef4444;">
          <span style="color:#94a3b8;font-family:monospace;">[${r.fecha ? esc(new Date(r.fecha).toLocaleDateString()) : '-'}${r.pais_reportante ? ' · ' + esc(r.pais_reportante) : ''}]</span>
          <strong style="color:#fca5a5;">${(r.categorias || []).map(esc).join(', ') || 'Abuso reportado'}</strong>
          ${r.comentario ? ` — <span style="color:#94a3b8;">"${esc(r.comentario)}"</span>` : ''}
        </div>
      `).join('')}
    </div>
  ` : '';
  const abuseHtml = `
    <div style="display:flex;gap:20px;flex-wrap:wrap;align-items:center;">
      <div style="min-width:180px;">
        <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;">Nivel de Confianza de Abuso</div>
        <div style="font-size:24px;font-weight:800;color:${abuseProgressCol};">${maxAbuse}%</div>
        <div style="background:#334155;border-radius:9999px;height:8px;width:100%;overflow:hidden;margin-top:4px;">
          <div style="background:${abuseProgressCol};height:100%;width:${maxAbuse}%;"></div>
        </div>
      </div>
      <div style="font-size:12px;color:#cbd5e1;line-height:1.6;">
        <div><strong>Reportes de Ataque:</strong> ${totalReportesAbuse} reportes en los últimos 90 días</div>
        <div><strong>Denunciantes Únicos:</strong> ${ab.usuarios_distintos || 0} redes distintas · <strong>Tipo Uso:</strong> ${esc(ab.tipo_uso || 'N/A')}</div>
        <div><strong>Último Reporte:</strong> ${ab.ultimo_reporte ? esc(new Date(ab.ultimo_reporte).toLocaleString()) : 'Sin reportes recientes'}</div>
        <div><strong>Lista Blanca / Tor:</strong> ${ab.whitelisted ? '🟢 En lista blanca' : '⚪ No en lista blanca'} · ${ab.es_tor ? '🔴 Nodo Tor' : 'No Tor'}</div>
      </div>
    </div>
    ${recientesHtml}
  `;

  // 4. ABUSE.CH (FEODO + URLHAUS + THREATFOX)
  const feodoMal = feodoHit ? (feodoHit.feodo.malware || (feodoHit.feodo.detalle && feodoHit.feodo.detalle.malware) || 'Malware C2') : '';
  const feodoBadge = feodoHit
    ? `<div style="background:#7f1d1d;color:#fca5a5;padding:8px 12px;border-radius:6px;margin-bottom:8px;font-size:12px;font-weight:600;">
         🚨 ALERTA CRÍTICA: ${esc(feodoHit.ip)} figura activa como C2 de Botnet (${esc(feodoMal)})
       </div>`
    : `<div style="color:#22c55e;font-size:12px;margin-bottom:6px;">✅ Feodo Tracker: Ninguna IP asociada está listada como Command &amp; Control (C2).</div>`;

  const urlhausHtml = uh.listado ? `
    <div style="margin-top:6px;font-size:12px;color:#fca5a5;">
      ⚠️ URLhaus: <strong>${uh.urls_total}</strong> URLs detectadas (${uh.urls_online} activas online).
      Amenazas: <strong>${(uh.amenazas || []).map(esc).join(', ') || 'Malware general'}</strong>
      ${(uh.muestras || []).slice(0, 3).map(m => `
        <div style="font-family:monospace;font-size:11px;background:#1e1b4b;padding:4px 8px;border-radius:4px;margin-top:4px;word-break:break-all;">
          ${esc(m.url)} [${esc(m.estado)}] ${m.tags && m.tags.length ? '(' + m.tags.map(esc).join(', ') + ')' : ''}
        </div>
      `).join('')}
    </div>
  ` : '<div style="color:#22c55e;font-size:12px;">✅ URLhaus: Sin URLs de distribución de malware activas.</div>';

  const threatfoxHtml = tf.listado ? `
    <div style="margin-top:6px;font-size:12px;color:#fca5a5;">
      ⚠️ ThreatFox: <strong>${(tf.iocs || []).length}</strong> Indicadores de Compromiso (IOCs) asociados.
      ${(tf.iocs || []).slice(0, 3).map(ioc => `
        <div style="font-family:monospace;font-size:11px;background:#31102b;padding:4px 8px;border-radius:4px;margin-top:4px;">
          ${esc(ioc.ioc)} · ${esc(ioc.tipo)} · ${esc(ioc.malware || 'Payload')} (Confianza: ${esc(ioc.confianza)}%)
        </div>
      `).join('')}
    </div>
  ` : '<div style="color:#22c55e;font-size:12px;">✅ ThreatFox: Sin IOCs maliciosos registrados para este dominio.</div>';

  // 5. MXTOOLBOX + DNS
  const mxResumenHtml = `
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;font-size:12px;">
      <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
        <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">📬 Servidores MX Receptores:</div>
        ${mxItems.length ? mxItems.map(m => `<div style="font-family:monospace;font-size:11px;color:#e2e8f0;">• ${esc(m.valor || m.clave)}</div>`).join('') : '<div style="color:#94a3b8;">Sin registros MX reportados</div>'}
      </div>
      <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
        <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🛡️ Configuración SPF:</div>
        ${spfItems.length ? spfItems.map(s => `<div style="font-family:monospace;font-size:11px;color:#e2e8f0;word-break:break-all;">${esc(s.valor || s.desc)}</div>`).join('') : '<div style="color:#f87171;">Sin registro SPF válido detectado</div>'}
      </div>
      <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
        <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🔒 Política DMARC:</div>
        ${dmarcItems.length ? dmarcItems.map(dm => `<div style="font-family:monospace;font-size:11px;color:#e2e8f0;word-break:break-all;">${esc(dm.valor || dm.desc)}</div>`).join('') : '<div style="color:#f87171;">Sin política DMARC configurada</div>'}
      </div>
      <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
        <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🚫 Blacklists Mundiales (DNSBL):</div>
        ${blFails.length
          ? `<div style="color:#ef4444;font-weight:600;">🔴 Aparece en ${blFails.length} lista(s): ${blFails.map(esc).join(', ')}</div>`
          : (mx.blacklist && mx.blacklist.estado === 'no_disponible'
              ? `<div style="color:#fbbf24;">⚠️ Blacklist no disponible (${esc(mx.blacklist.motivo || 'cuota')})</div>`
              : '<div style="color:#22c55e;font-weight:600;">🟢 Limpio (0 de 50+ listas negras)</div>')}
      </div>
    </div>
  `;

  const nsHtml = (dns.ns && dns.ns.length) || (dns.txt_extra && dns.txt_extra.length) ? `
    <div style="margin-top:10px;background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;font-size:12px;">
      <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🌐 Servidores DNS Autoritativos (NS) &amp; TXT:</div>
      ${dns.ns && dns.ns.length ? `<div style="color:#e2e8f0;font-family:monospace;font-size:11px;"><strong>NS:</strong> ${dns.ns.map(esc).join(' · ')}</div>` : ''}
      ${dns.txt_extra && dns.txt_extra.length ? `<div style="color:#94a3b8;font-family:monospace;font-size:11px;margin-top:4px;word-break:break-all;"><strong>TXT Extras:</strong> ${dns.txt_extra.slice(0, 4).map(esc).join(' | ')}</div>` : ''}
    </div>
  ` : '';

  // 6. RDAP / WHOIS + CERTIFICACIONES ISO
  const rdapHtml = rdap.estado === 'ok' ? `
    <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;margin-bottom:10px;font-size:12px;display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:10px;">
      <div><span style="color:#94a3b8;font-size:11px;">Registrador:</span><div style="color:#f8fafc;font-weight:600;">${esc(rdap.registrador)}</div></div>
      <div><span style="color:#94a3b8;font-size:11px;">Fecha de Creación:</span><div style="color:#e2e8f0;font-weight:600;">${rdap.creacion ? esc(new Date(rdap.creacion).toLocaleDateString()) : '-'} ${rdap.antiguedad_anios !== null && rdap.antiguedad_anios !== undefined ? `(${esc(rdap.antiguedad_anios)} años)` : ''}</div></div>
      <div><span style="color:#94a3b8;font-size:11px;">Expiración:</span><div style="color:#e2e8f0;">${rdap.expiracion ? esc(new Date(rdap.expiracion).toLocaleDateString()) : '-'}</div></div>
      <div><span style="color:#94a3b8;font-size:11px;">DNSSEC / Bloqueo:</span><div style="color:#e2e8f0;">${rdap.dnssec ? '🟢 Firmado' : '⚪ Sin DNSSEC'} · ${(rdap.estados || []).some(s => String(s).includes('Prohibited')) ? '🔒 Transfer Locked' : 'Abierto'}</div></div>
    </div>
  ` : `<div style="color:#94a3b8;font-size:11px;margin-bottom:8px;">ℹ️ WHOIS/RDAP: ${esc(rdap.motivo || 'No disponible para este TLD')}.</div>`;

  const normas = iso.normas || [];
  const isoHtml = normas.length ? `
    <div style="margin-top:6px;">
      <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;">
        ${normas.map(n => `
          <span style="background:#1e3a8a;color:#bfdbfe;border:1px solid #3b82f6;padding:4px 10px;border-radius:6px;font-size:12px;font-weight:600;">
            ${esc(n.norma)} · ${esc(n.descripcion || 'Norma Internacional')} ${n.versiones && n.versiones.length ? '(' + n.versiones.map(esc).join(', ') + ')' : ''}
          </span>
        `).join('')}
      </div>
      ${normas.flatMap(n => n.evidencias || []).slice(0, 2).map(e => `
        <div style="background:#0f172a;border-left:3px solid #3b82f6;padding:6px 10px;margin-top:4px;font-size:11px;color:#cbd5e1;">
          <em>"...${esc(e.fragmento)}..."</em> <a href="${safeUrl(e.url)}" target="_blank" style="color:#60a5fa;margin-left:6px;">[Ver Fuente]</a>
        </div>
      `).join('')}
    </div>
  ` : '<div style="color:#94a3b8;font-size:12px;">No se identificaron certificaciones ISO declaradas en las páginas públicas auditadas.</div>';

  // 7. DESGLOSE DEL SCORE
  const desgloseRows = (d.score_detalle || []).map(item => `
    <tr style="border-bottom:1px solid #1e293b;font-size:12px;">
      <td style="padding:6px 10px;font-weight:700;font-family:monospace;color:${item.puntos > 0 ? '#f87171' : item.puntos < 0 ? '#4ade80' : '#94a3b8'};">
        ${item.puntos > 0 ? '+' + item.puntos : item.puntos}
      </td>
      <td style="padding:6px 10px;color:#cbd5e1;text-transform:uppercase;font-weight:600;">${esc(item.fuente)}</td>
      <td style="padding:6px 10px;color:#94a3b8;font-family:monospace;font-size:11px;">${esc(item.consulta || '-')}</td>
      <td style="padding:6px 10px;color:#e2e8f0;">${esc(item.evidencia)}</td>
    </tr>
  `).join('');

  return `
    <div id="dom-${idx}" class="domain-card dossier-card" data-nivel="${col.label}" data-search="${esc(searchBlob)}" style="background:#111827;border:1px solid #1f2937;border-radius:10px;margin-bottom:24px;overflow:hidden;box-shadow:0 4px 6px -1px rgba(0,0,0,0.3);">

      <!-- ENCABEZADO DE DOMINIO -->
      <div style="background:#1e293b;padding:16px 20px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;border-bottom:1px solid #334155;">
        <div>
          <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
            <a href="${safeUrl(d.url)}" target="_blank" style="color:#60a5fa;font-size:18px;font-weight:700;text-decoration:none;">${esc(d.dominio)}</a>
            <span style="background:#0f172a;color:#94a3b8;font-size:11px;padding:3px 8px;border-radius:4px;border:1px solid #334155;">
              Entidad: ${esc(origenTxt)}
            </span>
          </div>
          <div style="color:#94a3b8;font-size:12px;margin-top:4px;">
            🌐 IPs: <span style="color:#e2e8f0;font-family:monospace;">${ips.map(i => esc(i.ip)).join(', ') || 'Sin IPs'}</span>
            &nbsp;·&nbsp; Ubicación: <strong style="color:#e2e8f0;">${ia.ciudad ? esc(ia.ciudad) + ', ' : ''}${esc(ia.pais || ab.pais || 'Global')}</strong>
            &nbsp;·&nbsp; Red: <strong style="color:#cbd5e1;">${esc(ia.isp || ia.org || ab.isp || sh.org || 'Desconocido')}</strong>
          </div>
        </div>

        <div style="display:flex;align-items:center;gap:12px;">
          <div style="text-align:right;">
            <div style="font-size:10px;color:#94a3b8;text-transform:uppercase;">Score de Riesgo CTI</div>
            <div style="background:${col.bg};color:${col.text};border:1px solid ${col.border};padding:6px 14px;border-radius:9999px;font-size:16px;font-weight:800;display:inline-block;margin-top:2px;">
              ${d.score}/100 · ${col.label}
            </div>
          </div>
        </div>
      </div>

      <!-- BARRA DE SEÑALES RÁPIDAS -->
      <div style="background:#0f172a;padding:12px 20px;display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:12px;border-bottom:1px solid #1e293b;font-size:12px;">
        <div>
          <div style="color:#94a3b8;font-size:11px;">📡 Tipo de Red (IP-API)</div>
          <div style="color:#e2e8f0;font-weight:600;margin-top:2px;">
            ${ia.proxy ? '🔴 Proxy / VPN / Tor' : '🟢 Sin Proxy'} · ${ia.hosting ? '🟠 Datacenter' : '🟢 Corporativo'}
          </div>
        </div>
        <div>
          <div style="color:#94a3b8;font-size:11px;">🔍 Puertos &amp; CVEs (Shodan)</div>
          <div style="color:#e2e8f0;font-weight:600;margin-top:2px;">
            ${todosPuertos.length ? todosPuertos.slice(0, 4).join(', ') + (todosPuertos.length > 4 ? '...' : '') : 'Sin puertos'}
            · ${todasVulns.length ? '<span style="color:#f87171;">' + todasVulns.length + ' CVEs</span>' : '<span style="color:#22c55e;">0 CVEs</span>'}
          </div>
        </div>
        <div>
          <div style="color:#94a3b8;font-size:11px;">⚠️ Reputación (AbuseIPDB)</div>
          <div style="color:#e2e8f0;font-weight:600;margin-top:2px;">
            ${maxAbuse}% sospecha · ${totalReportesAbuse} reportes (90d)
          </div>
        </div>
        <div>
          <div style="color:#94a3b8;font-size:11px;">☣️ Ciberamenazas (Abuse.ch)</div>
          <div style="color:#e2e8f0;font-weight:600;margin-top:2px;">
            ${feodoHit ? '<span style="color:#ef4444;">🔴 Botnet C2</span>' : '🟢 Feodo Ok'} · ${uh.listado ? '<span style="color:#f87171;">' + uh.urls_total + ' URLs Maliciosas</span>' : '🟢 0 URLs'}
          </div>
        </div>
        <div>
          <div style="color:#94a3b8;font-size:11px;">✉️ Seguridad Email &amp; DNSBL</div>
          <div style="color:#e2e8f0;font-weight:600;margin-top:2px;">
            ${blFails.length ? '<span style="color:#ef4444;">🔴 Blacklist (' + blFails.length + ')</span>' : '🟢 Blacklist Ok'} · ${spfItems.length ? '🟢 SPF Ok' : '🟡 Sin SPF'}
          </div>
        </div>
      </div>

      <!-- SUITE DETALLADA EXPANDIBLE -->
      <details class="dossier-details" style="padding:16px 20px;cursor:pointer;" open>
        <summary style="font-size:13px;font-weight:700;color:#93c5fd;outline:none;user-select:none;margin-bottom:14px;">
          📊 Dossier Técnico de Inteligencia (Desplegar / Ocultar Detalles Exhaustivos)
        </summary>

        <div style="display:flex;flex-direction:column;gap:18px;margin-top:12px;">

          <!-- PANEL 1: IP-API -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              🌐 1. Infraestructura de Red &amp; Geolocalización (IP-API · Sin Cuotas)
            </div>
            <table style="width:100%;border-collapse:collapse;text-align:left;">
              <thead>
                <tr style="color:#94a3b8;font-size:11px;border-bottom:1px solid #334155;background:#0f172a;">
                  <th style="padding:6px 10px;">IP / PTR</th>
                  <th style="padding:6px 10px;">Ubicación</th>
                  <th style="padding:6px 10px;">ISP / Organización</th>
                  <th style="padding:6px 10px;">ASN</th>
                  <th style="padding:6px 10px;">Anonimizador (Proxy/VPN)</th>
                  <th style="padding:6px 10px;">Tipo Alojamiento</th>
                </tr>
              </thead>
              <tbody>${filasIps}</tbody>
            </table>
          </div>

          <!-- PANEL 2: SHODAN -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              🔍 2. Superficie de Ataque, CPEs &amp; Puertos Expuestos (Shodan)
            </div>
            <div style="font-size:12px;color:#cbd5e1;margin-bottom:6px;">
              <strong>Puertos Abiertos Detectados:</strong>
              <div style="margin-top:4px;">
                ${todosPuertos.length ? todosPuertos.map(badgePuerto).join('') : '<span style="color:#94a3b8;">Ningún puerto común detectado</span>'}
              </div>
            </div>
            ${cpesHtml}
            ${vulnsHtml}
            ${todosHosts.length ? `<div style="font-size:11px;color:#94a3b8;margin-top:8px;"><strong>Hostnames DNS asociados:</strong> ${todosHosts.map(esc).join(', ')}</div>` : ''}
            ${tagsHtml}
          </div>

          <!-- PANEL 3: ABUSEIPDB -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              🚨 3. Historial de Abuso y Reportes de Ataques (AbuseIPDB)
            </div>
            ${abuseHtml}
          </div>

          <!-- PANEL 4: ABUSE.CH -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              ☣️ 4. Amenazas Activas, Botnets &amp; Malware (Abuse.ch Suite)
            </div>
            ${feodoBadge}
            ${urlhausHtml}
            ${threatfoxHtml}
          </div>

          <!-- PANEL 5: MXTOOLBOX + DNS -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              ✉️ 5. Seguridad de Correo Electrónico, DNS &amp; Blacklists (MXToolbox + Google DoH)
            </div>
            ${mxResumenHtml}
            ${nsHtml}
          </div>

          <!-- PANEL 6: WHOIS / RDAP & ISO -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              📜 6. Registro WHOIS/RDAP, Antigüedad &amp; Cumplimiento ISO
            </div>
            ${rdapHtml}
            ${isoHtml}
          </div>

          <!-- PANEL 7: AUDITORÍA DEL SCORE -->
          <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
            <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
              ⚖️ 7. Auditoría Contable del Score (Regla Ponderada 1-100)
            </div>
            <table style="width:100%;border-collapse:collapse;text-align:left;">
              <thead>
                <tr style="color:#94a3b8;font-size:11px;border-bottom:1px solid #334155;background:#0f172a;">
                  <th style="padding:6px 10px;">Puntos</th>
                  <th style="padding:6px 10px;">Fuente</th>
                  <th style="padding:6px 10px;">Consulta</th>
                  <th style="padding:6px 10px;">Evidencia Técnica</th>
                </tr>
              </thead>
              <tbody>${desgloseRows}</tbody>
            </table>
          </div>

        </div>
      </details>

    </div>
  `;
}).join('');

const filasSinDominio = resumen.sin_dominio.map(s => `
  <tr style="border-bottom:1px solid #1e293b;">
    <td style="padding:10px 14px;color:#f8fafc;font-weight:600;">${esc(s.nombre)}</td>
    <td style="padding:10px 14px;color:#94a3b8;font-size:13px;">${esc(s.motivo)}</td>
    <td style="padding:10px 14px;color:#fbbf24;font-size:12px;">Continuado (sin impacto adverso)</td>
  </tr>
`).join('');

const html = `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SOC Threat Intelligence Suite · Dossier de Reputación</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background:#070a13; color:#f1f5f9; margin:0; padding:24px; }
    .container { max-width:1280px; margin:0 auto; }
    .card { background:#111827; border:1px solid #1f2937; border-radius:10px; padding:18px; margin-bottom:20px; }
    .metric { display:inline-block; padding:12px 18px; background:#0b0f19; border:1px solid #1e293b; border-radius:8px; margin-right:12px; margin-bottom:8px; min-width:140px; }
    .metric-val { font-size:24px; font-weight:800; color:#fff; }
    .metric-lbl { font-size:11px; color:#94a3b8; text-transform:uppercase; margin-top:4px; font-weight:600; }
    @media print { .no-print { display: none !important; } }
  </style>
</head>
<body>
  <div class="container">

    <!-- TOP HEADER -->
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:24px; flex-wrap:wrap; gap:12px;">
      <div>
        <h1 style="margin:0; font-size:24px; color:#38bdf8; display:flex; align-items:center; gap:8px;">
          🛡️ SOC Threat Intelligence Suite
        </h1>
        <div style="color:#94a3b8; font-size:13px; margin-top:4px;">
          Auditoría técnica multi-herramienta (Shodan · AbuseIPDB · IP-API · Abuse.ch · MXToolbox + DoH · RDAP · ISO) · Generado: ${new Date().toLocaleString()}
        </div>
      </div>
      <div class="no-print" style="display:flex;gap:8px;flex-wrap:wrap;">
        <button onclick="window.print()" style="background:#1e293b;color:#cbd5e1;border:1px solid #334155;padding:10px 14px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;">🖨️ Imprimir / PDF</button>
        <a href="/form/ti-dominios" style="background:#2563eb; color:#fff; padding:10px 18px; border-radius:8px; text-decoration:none; font-size:13px; font-weight:700; display:inline-block; box-shadow:0 2px 4px rgba(37,99,235,0.4);">
          + Nueva Consulta CTI
        </a>
      </div>
    </div>

    <!-- METRICS BAR -->
    <div class="card" style="padding:14px 18px;">
      <div style="display:flex; flex-wrap:wrap;">
        <div class="metric"><div class="metric-val">${resumen.nombres.length}</div><div class="metric-lbl">Entidades Entrada</div></div>
        <div class="metric"><div class="metric-val" style="color:#60a5fa;">${dominios.length}</div><div class="metric-lbl">Dominios Analizados</div></div>
        <div class="metric"><div class="metric-val" style="color:#ef4444;">${conteoNiveles.critico || 0}</div><div class="metric-lbl">Riesgo Crítico</div></div>
        <div class="metric"><div class="metric-val" style="color:#f97316;">${conteoNiveles.alto || 0}</div><div class="metric-lbl">Riesgo Alto</div></div>
        <div class="metric"><div class="metric-val" style="color:#eab308;">${conteoNiveles.medio || 0}</div><div class="metric-lbl">Riesgo Medio</div></div>
        <div class="metric"><div class="metric-val" style="color:#22c55e;">${conteoNiveles.bajo || 0}</div><div class="metric-lbl">Riesgo Bajo</div></div>
      </div>
    </div>

    <!-- MATRIZ COMPARATIVA Y FILTROS DEL LOTE -->
    ${dominios.length ? `
    <div class="card" style="padding:16px 18px;">
      <div class="no-print" style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:14px;">
        <input id="filtroInput" type="text" placeholder="🔎 Filtrar lote por dominio, entidad, IP, país, ISP o CVE..." oninput="aplicarFiltro()" style="flex:1;min-width:240px;background:#0b0f19;border:1px solid #334155;border-radius:6px;color:#f1f5f9;padding:8px 12px;font-size:13px;">
        <select id="filtroNivel" onchange="aplicarFiltro()" style="background:#0b0f19;border:1px solid #334155;border-radius:6px;color:#f1f5f9;padding:8px 12px;font-size:13px;">
          <option value="">Todos los niveles</option>
          <option value="CRÍTICO">Solo CRÍTICO</option>
          <option value="ALTO">Solo ALTO</option>
          <option value="MEDIO">Solo MEDIO</option>
          <option value="BAJO">Solo BAJO</option>
        </select>
        <button onclick="toggleTodos(true)" style="background:#1e293b;color:#cbd5e1;border:1px solid #334155;padding:8px 12px;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;">▾ Expandir todos</button>
        <button onclick="toggleTodos(false)" style="background:#1e293b;color:#cbd5e1;border:1px solid #334155;padding:8px 12px;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;">▸ Colapsar todos</button>
      </div>
      <div style="font-weight:700;font-size:13px;color:#93c5fd;margin-bottom:8px;">📋 Matriz Comparativa Rápida del Lote (clic para ir al Dossier completo)</div>
      <div style="overflow-x:auto;">
        <table style="width:100%;border-collapse:collapse;text-align:left;font-size:12px;">
          <thead>
            <tr style="background:#0f172a;color:#94a3b8;font-size:11px;text-transform:uppercase;border-bottom:1px solid #334155;">
              <th style="padding:8px 10px;">Dominio / Entidad</th>
              <th style="padding:8px 10px;">Score</th>
              <th style="padding:8px 10px;">IP / Red / País</th>
              <th style="padding:8px 10px;">Superficie (Shodan)</th>
              <th style="padding:8px 10px;">Abuso (90d)</th>
              <th style="padding:8px 10px;">Email &amp; DNS</th>
              <th style="padding:8px 10px;">RDAP / ISO</th>
            </tr>
          </thead>
          <tbody>${matrizRows.join('')}</tbody>
        </table>
      </div>
    </div>` : ''}

    <!-- LISTADO DE DOSSIERS POR DOMINIO -->
    <div style="margin-top:10px;">
      ${cardsDominiosHtml || '<div class="card" style="text-align:center;color:#94a3b8;padding:30px;">No se encontraron dominios verificados para las entidades ingresadas.</div>'}
    </div>

    <!-- ENTIDADES SIN DOMINIO -->
    ${resumen.sin_dominio.length ? `
    <div class="card" style="padding:0; overflow:hidden; margin-top:24px;">
      <div style="padding:14px 18px; border-bottom:1px solid #1e293b; font-weight:700; font-size:14px; color:#fbbf24; background:#0f172a;">
        Entidades sin Dominio Identificado (Flujo Continuado sin Fallas)
      </div>
      <table style="width:100%; border-collapse:collapse; text-align:left;">
        <thead>
          <tr style="background:#090d16; color:#94a3b8; font-size:11px; text-transform:uppercase;">
            <th style="padding:8px 14px;">Entidad Ingresada</th>
            <th style="padding:8px 14px;">Motivo Técnico</th>
            <th style="padding:8px 14px;">Estado</th>
          </tr>
        </thead>
        <tbody>${filasSinDominio}</tbody>
      </table>
    </div>` : ''}

  </div>
  <script>
    function aplicarFiltro() {
      const q = (document.getElementById('filtroInput').value || '').trim().toLowerCase();
      const niv = document.getElementById('filtroNivel').value;
      document.querySelectorAll('.dossier-card, .matriz-row').forEach(el => {
        const matchQ = !q || (el.getAttribute('data-search') || '').includes(q);
        const matchN = !niv || el.getAttribute('data-nivel') === niv;
        el.style.display = (matchQ && matchN) ? '' : 'none';
      });
    }
    function toggleTodos(abrir) {
      document.querySelectorAll('.dossier-details').forEach(d => {
        if (abrir) d.setAttribute('open', '');
        else d.removeAttribute('open');
      });
    }
  <\/script>
</body>
</html>`;

const datosFinales = {
  generado_en: new Date().toISOString(),
  resumen: {
    nombres_procesados: resumen.nombres.length,
    nombres_con_dominio: resumen.nombres.filter(n => n.estado === 'con_dominio').length,
    nombres_sin_dominio: resumen.sin_dominio.length,
    dominios_analizados: dominios.length,
    por_nivel: conteoNiveles
  },
  lista_urls: resumen.lista_urls,
  tabla: dominios.map(x => ({
    dominio: x.dominio, score: x.score, nivel: x.nivel_riesgo, confianza: x.confianza_score,
    fuentes: x.fuentes_disponibles,
    iso: (x.certificados_iso && x.certificados_iso.normas ? x.certificados_iso.normas.map(n => n.norma).join(', ') : '-'),
    estado: `SH:${x.estado_consultas.shodan} AB:${x.estado_consultas.abuseipdb} NET:${x.estado_consultas.ipapi} ACH:${x.estado_consultas.abusech.global} MX:${x.estado_consultas.mxtoolbox.global}`
  })),
  dominios,
  sin_dominio: resumen.sin_dominio,
  regla_score: cfg.pesos,
  detalle_descubrimiento: resumen.nombres,
  html
};

return [{ json: datosFinales }];
