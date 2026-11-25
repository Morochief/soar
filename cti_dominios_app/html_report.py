# -*- coding: utf-8 -*-
"""
Generador de Reporte HTML Estático para Threat Intelligence de Dominios.
Genera un dashboard interactivo completo (SOC Threat Intelligence Suite) que funciona abriendo
el archivo localmente (file:///) en cualquier navegador, sin servidor web ni puertos abiertos.
"""
import json
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SOC Threat Intelligence Suite · Dossier de Entidades &amp; Dominios</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg: #070a13;
      --card-bg: #111827;
      --card-inner: #090d16;
      --border: #1f2937;
      --border-light: #334155;
      --primary: #3b82f6;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
    }
    * { box-sizing: border-box; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 24px; }
    .container { max-width: 1280px; margin: 0 auto; }
    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 12px; }
    .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px; padding: 18px; margin-bottom: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); }
    .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-top: 14px; }
    .metric { background: #0b0f19; border: 1px solid var(--border); border-radius: 8px; padding: 14px; }
    .metric-val { font-size: 26px; font-weight: 800; color: #fff; }
    .metric-lbl { font-size: 11px; color: var(--text-muted); text-transform: uppercase; margin-top: 4px; font-weight: 600; }
    .btn { background: var(--primary); color: #fff; border: none; padding: 10px 16px; border-radius: 8px; font-size: 13px; font-weight: 700; cursor: pointer; text-decoration: none; display: inline-block; box-shadow: 0 2px 4px rgba(59,130,246,0.3); }
    .btn-sec { background: #1e293b; color: #cbd5e1; border: 1px solid #334155; padding: 8px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer; }
    .btn-sec:hover { background: #334155; color: #fff; }
    .domain-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px; margin-bottom: 24px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); }
    table { width: 100%; border-collapse: collapse; text-align: left; }
    th { background: #0f172a; color: var(--text-muted); font-size: 11px; text-transform: uppercase; padding: 8px 12px; border-bottom: 1px solid var(--border-light); }
    td { padding: 8px 12px; border-bottom: 1px solid #1e293b; font-size: 12px; vertical-align: middle; }
    details summary { cursor: pointer; user-select: none; outline: none; }
    .filter-bar { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-bottom: 14px; }
    .filter-input { flex: 1; min-width: 240px; background: #0b0f19; border: 1px solid #334155; border-radius: 6px; color: #f1f5f9; padding: 8px 12px; font-size: 13px; }
    .filter-select { background: #0b0f19; border: 1px solid #334155; border-radius: 6px; color: #f1f5f9; padding: 8px 12px; font-size: 13px; }
    @media print { body { background: #070a13; } .no-print { display: none !important; } }
  </style>
</head>
<body>
  <div class="container">

    <!-- TOP HEADER -->
    <div class="header">
      <div>
        <h1 style="margin:0; font-size:24px; color:#38bdf8; display:flex; align-items:center; gap:8px;">
          🛡️ SOC Threat Intelligence Suite
        </h1>
        <div style="color:var(--text-muted); font-size:13px; margin-top:4px;">
          Dossier exhaustivo multi-herramienta (Shodan · AbuseIPDB · IP-API · Abuse.ch · MXToolbox + DoH · RDAP/WHOIS · ISO) · Modo Local Seguro (Zero Listening Sockets)
        </div>
      </div>
      <div class="no-print" style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn-sec" onclick="window.print()">🖨️ Imprimir / PDF</button>
        <button class="btn" onclick="descargarJSON()">📥 Guardar JSON</button>
      </div>
    </div>

    <!-- METRICS BAR -->
    <div class="card" style="padding:14px 18px;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
        <h3 style="margin:0; font-size:15px; color:#e2e8f0;">Resumen Ejecutivo de Amenazas &amp; Cobertura</h3>
        <span id="lblFecha" style="color:var(--text-muted); font-size:12px;"></span>
      </div>
      <div class="metrics-grid">
        <div class="metric"><div class="metric-val" id="mProcesados">-</div><div class="metric-lbl">Entidades Entrada</div></div>
        <div class="metric"><div class="metric-val" style="color:#60a5fa;" id="mDominios">-</div><div class="metric-lbl">Dominios Analizados</div></div>
        <div class="metric"><div class="metric-val" style="color:#ef4444;" id="mCriticos">-</div><div class="metric-lbl">Riesgo Crítico (≥75)</div></div>
        <div class="metric"><div class="metric-val" style="color:#f97316;" id="mAltos">-</div><div class="metric-lbl">Riesgo Alto (50-74)</div></div>
        <div class="metric"><div class="metric-val" style="color:#eab308;" id="mMedios">-</div><div class="metric-lbl">Riesgo Medio (25-49)</div></div>
        <div class="metric"><div class="metric-val" style="color:#22c55e;" id="mBajos">-</div><div class="metric-lbl">Riesgo Bajo (&lt;25)</div></div>
      </div>
    </div>

    <!-- MATRIZ COMPARATIVA Y CONTROLES DE LOTE -->
    <div id="panelMatriz" class="card" style="display:none; padding:16px 18px;">
      <div class="filter-bar no-print">
        <input id="filtroInput" class="filter-input" type="text" placeholder="🔎 Filtrar lote por dominio, entidad, IP, país, ISP o CVE..." oninput="aplicarFiltro()">
        <select id="filtroNivel" class="filter-select" onchange="aplicarFiltro()">
          <option value="">Todos los niveles</option>
          <option value="CRÍTICO">Solo CRÍTICO</option>
          <option value="ALTO">Solo ALTO</option>
          <option value="MEDIO">Solo MEDIO</option>
          <option value="BAJO">Solo BAJO</option>
        </select>
        <button class="btn-sec" onclick="toggleTodos(true)">▾ Expandir todos</button>
        <button class="btn-sec" onclick="toggleTodos(false)">▸ Colapsar todos</button>
      </div>
      <div style="font-weight:700;font-size:13px;color:#93c5fd;margin-bottom:8px;">📋 Matriz Comparativa Rápida del Lote (clic para ir al Dossier completo)</div>
      <div style="overflow-x:auto;">
        <table>
          <thead>
            <tr>
              <th>Dominio / Entidad</th>
              <th>Score</th>
              <th>IP / Red / País</th>
              <th>Superficie (Shodan)</th>
              <th>Abuso (90d)</th>
              <th>Email &amp; DNS</th>
              <th>RDAP / ISO</th>
            </tr>
          </thead>
          <tbody id="tablaMatriz"></tbody>
        </table>
      </div>
    </div>

    <!-- LISTADO DE DOSSIERS POR DOMINIO -->
    <div id="contenedorDossiers"></div>

    <!-- ENTIDADES SIN DOMINIO -->
    <div class="card" id="cardSinDominio" style="display:none; padding:0; overflow:hidden; border-color:#854d0e;">
      <div style="padding:14px 18px; border-bottom:1px solid #1e293b; font-weight:700; font-size:14px; color:#fbbf24; background:#0f172a;">
        ⚠️ Entidades sin Dominio Identificado (Flujo Continuado sin Fallas)
      </div>
      <table>
        <thead>
          <tr>
            <th>Entidad Ingresada</th>
            <th>Diagnóstico Técnico</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody id="tablaSinDominio"></tbody>
      </table>
    </div>

  </div>

  <script>
    const data = __REPORT_JSON__;

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
      return /^https?:\\/\\//i.test(s) ? esc(s) : '#';
    }

    document.getElementById('lblFecha').innerText = 'Generado: ' + new Date(data.generado_en || Date.now()).toLocaleString();
    const res = data.resumen || {};
    const porNivel = res.por_nivel || {};
    document.getElementById('mProcesados').innerText = res.nombres_procesados ?? '-';
    document.getElementById('mDominios').innerText = res.dominios_analizados ?? (data.dominios || []).length;
    document.getElementById('mCriticos').innerText = porNivel['CRÍTICO'] || porNivel['critico'] || 0;
    document.getElementById('mAltos').innerText = porNivel['ALTO'] || porNivel['alto'] || 0;
    document.getElementById('mMedios').innerText = porNivel['MEDIO'] || porNivel['medio'] || 0;
    document.getElementById('mBajos').innerText = porNivel['BAJO'] || porNivel['bajo'] || 0;

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

    const dominios = (data.dominios || []).slice().sort((a, b) => (b.score || 0) - (a.score || 0));
    const container = document.getElementById('contenedorDossiers');
    const matrizBody = document.getElementById('tablaMatriz');

    if (dominios.length) {
      document.getElementById('panelMatriz').style.display = 'block';
    }

    const matrizRows = [];
    const cardsHtml = dominios.map((d, idx) => {
      const col = colorScore(d.score);
      const h = d.hallazgos || {};
      const ips = h.por_ip || [];
      const primaryIp = ips[0] || {};
      const ia = primaryIp.ipapi || {};
      const sh = primaryIp.shodan || {};
      const ab = primaryIp.abuseipdb || {};
      const mx = h.mxtoolbox || {};
      const dns = h.dns_detalle || {};
      const rdap = h.rdap || {};
      const ach = h.abusech || {};
      const uh = ach.urlhaus || {};
      const tf = ach.threatfox || {};
      const iso = d.certificados_iso_detalle || (typeof d.certificados_iso === 'object' && !Array.isArray(d.certificados_iso) ? d.certificados_iso : {});

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

      const origenTxt = d.nombre_origen || (d.nombres_origen || []).join(', ');
      const searchBlob = [
        d.dominio, origenTxt, ips.map(i => i.ip).join(' '),
        ia.pais, ia.ciudad, ia.isp, ia.org, ab.isp,
        todasVulns.join(' '), todosCpes.join(' '), rdap.registrador
      ].filter(Boolean).join(' ').toLowerCase();

      matrizRows.push(`
        <tr class="matriz-row" data-nivel="${col.label}" data-search="${esc(searchBlob)}">
          <td>
            <a href="#dom-${idx}" style="color:#60a5fa;font-weight:700;text-decoration:none;">${esc(d.dominio)}</a>
            <div style="color:#94a3b8;font-size:11px;">${esc(origenTxt)}</div>
          </td>
          <td><span style="background:${col.bg};color:${col.text};padding:3px 9px;border-radius:9999px;font-weight:800;font-size:11px;white-space:nowrap;">${d.score}/100 · ${col.label}</span></td>
          <td>
            <div style="font-family:monospace;color:#e2e8f0;">${esc((primaryIp.ip) || (d.ips && d.ips[0]) || '-')}</div>
            <div style="color:#94a3b8;font-size:11px;">${esc(ia.pais || ab.pais || '-')} · ${esc(ia.isp || ab.isp || sh.org || '-')}</div>
          </td>
          <td>${todosPuertos.length ? todosPuertos.slice(0, 4).join(', ') + (todosPuertos.length > 4 ? '...' : '') : '0 puertos'} · ${todasVulns.length ? `<span style="color:#f87171;font-weight:700;">${todasVulns.length} CVEs</span>` : '<span style="color:#22c55e;">0 CVEs</span>'}</td>
          <td><strong style="color:${maxAbuse >= 50 ? '#ef4444' : maxAbuse >= 25 ? '#eab308' : '#22c55e'};">${maxAbuse}%</strong> (${totalReportesAbuse} rep)</td>
          <td>${spfItems.length ? '🟢 SPF' : '🔴 Sin SPF'} · ${dmarcItems.length ? '🟢 DMARC' : '🟡 Sin DMARC'}</td>
          <td>${rdap.estado === 'ok' && rdap.antiguedad_anios !== null ? esc(rdap.antiguedad_anios) + ' años' : '-'} ${(iso.normas && iso.normas.length) ? '· 📜 ISO' : ''}</td>
        </tr>
      `);

      // 1. IP-API
      const filasIps = ips.map(i => {
        const api = i.ipapi || {};
        const aip = i.abuseipdb || {};
        const shd = i.shodan || {};
        const hasIpApi = api.estado === 'ok';
        const proxyBadge = !hasIpApi ? '<span style="color:#94a3b8;">N/A</span>' : api.proxy
          ? '<span style="background:#7f1d1d;color:#fca5a5;padding:2px 6px;border-radius:4px;font-weight:600;">🔴 SÍ (Proxy/VPN)</span>'
          : '<span style="background:#064e3b;color:#a7f3d0;padding:2px 6px;border-radius:4px;font-weight:600;">🟢 NO (Directo)</span>';
        const hostingBadge = !hasIpApi ? '<span style="color:#94a3b8;">N/A</span>' : api.hosting
          ? '<span style="background:#7c2d12;color:#fdba74;padding:2px 6px;border-radius:4px;font-weight:600;">🟠 Datacenter / Cloud</span>'
          : (api.mobile ? '<span style="background:#1e3a8a;color:#93c5fd;padding:2px 6px;border-radius:4px;font-weight:600;">📱 Red Móvil</span>' : '<span style="background:#064e3b;color:#a7f3d0;padding:2px 6px;border-radius:4px;font-weight:600;">🟢 Red Propia / Corp</span>');
        const loc = api.ciudad ? `${api.ciudad}${api.region ? ', ' + api.region : ''}, ${api.pais || ''}` : (api.pais || aip.pais || shd.pais || 'Desconocido');
        const ispTxt = api.isp || api.org || aip.isp || shd.isp || shd.org || '-';
        return `
          <tr style="border-bottom:1px solid #1e293b;">
            <td style="font-family:monospace;font-weight:600;color:#60a5fa;">
              ${esc(i.ip)}
              ${api.reverse ? `<div style="font-size:10px;color:#94a3b8;font-weight:400;">PTR: ${esc(api.reverse)}</div>` : ''}
            </td>
            <td>
              <div>${esc(loc)} (${esc(api.pais_codigo || '-')})</div>
              ${api.zona_horaria ? `<div style="font-size:10px;color:#94a3b8;">TZ: ${esc(api.zona_horaria)}</div>` : ''}
            </td>
            <td>${esc(ispTxt)}</td>
            <td style="font-family:monospace;">${esc(api.as || shd.asn || '-')}</td>
            <td>${proxyBadge}</td>
            <td>${hostingBadge}</td>
          </tr>
        `;
      }).join('');

      // 2. SHODAN
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

      // 3. ABUSEIPDB
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
            <div><strong>Lista Blanca / Tor:</strong> ${ab.whitelisted ? '🟢 En lista blanca (Whitelisted)' : '⚪ No en lista blanca'} · ${ab.es_tor ? '🔴 Nodo Tor' : 'No Tor'}</div>
          </div>
        </div>
        ${recientesHtml}
      `;

      // 4. ABUSE.CH
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

      // 5. MXTOOLBOX + GOOGLE DOH DNS
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
                  ? `<div style="color:#fbbf24;">⚠️ MXToolbox Blacklist no disponible (${esc(mx.blacklist.motivo || 'cuota')})</div>`
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

      // 6. RDAP / WHOIS + ISO
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
      const desgloseRows = (d.desglose || d.score_detalle || []).map(item => `
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
        <div id="dom-${idx}" class="domain-card dossier-card" data-nivel="${col.label}" data-search="${esc(searchBlob)}">

          <!-- ENCABEZADO -->
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
                ${ia.estado === 'ok' ? `${ia.proxy ? '🔴 Proxy / VPN / Tor' : '🟢 Sin Proxy'} · ${ia.hosting ? '🟠 Datacenter' : '🟢 Corporativo'}` : '⚪ IP-API no disponible'}
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

          <!-- SUITE EXPANDIBLE -->
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
                <table>
                  <thead>
                    <tr>
                      <th>IP / PTR</th>
                      <th>Ubicación</th>
                      <th>ISP / Organización</th>
                      <th>ASN</th>
                      <th>Anonimizador (Proxy/VPN)</th>
                      <th>Tipo Alojamiento</th>
                    </tr>
                  </thead>
                  <tbody>${filasIps}</tbody>
                </table>
              </div>

              <!-- PANEL 2: SHODAN -->
              <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                <div style="font-weight:700;font-size:13px;color:#38bdf8;margin-bottom:8px;">
                  🔍 2. Superficie de Ataque &amp; Puertos Expuestos (Shodan)
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

              <!-- PANEL 6: RDAP/WHOIS & ISO -->
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
                <table>
                  <thead>
                    <tr>
                      <th>Puntos</th>
                      <th>Fuente</th>
                      <th>Consulta</th>
                      <th>Evidencia Técnica</th>
                    </tr>
                  </thead>
                  <tbody>${desgloseRows}</tbody>
                </table>
              </div>

            </div>
          </details>

        </div>
      `;
    });

    matrizBody.innerHTML = matrizRows.join('');
    container.innerHTML = cardsHtml.join('') || '<div class="card" style="text-align:center;color:#94a3b8;padding:30px;">No se encontraron dominios verificados para las entidades ingresadas.</div>';

    const sinDomCard = document.getElementById('cardSinDominio');
    const sinDomBody = document.getElementById('tablaSinDominio');
    if (data.sin_dominio && data.sin_dominio.length) {
      sinDomCard.style.display = 'block';
      sinDomBody.innerHTML = data.sin_dominio.map(s => `
        <tr>
          <td style="font-weight:600;">${esc(s.nombre)}</td>
          <td style="color:#94a3b8;">${esc(s.motivo)}</td>
          <td style="color:#fbbf24; font-size:12px;">Registrado (flujo continuado)</td>
        </tr>
      `).join('');
    }

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

    function descargarJSON() {
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `dossier_cti_${new Date().toISOString().replace(/[:.-]/g, '').slice(0, 15)}.json`;
      a.click();
    }
  </script>
</body>
</html>"""


def generar_html_estatico(reporte_data, output_path=None):
    # Evitar ruptura de etiqueta <script> si alguna evidencia o comentario contiene </script>
    reporte_json = json.dumps(reporte_data, ensure_ascii=False).replace("</", "<\\/")
    html = HTML_TEMPLATE.replace("__REPORT_JSON__", reporte_json)
    if output_path:
        Path(output_path).write_text(html, encoding="utf-8")
    return html
