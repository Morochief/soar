# -*- coding: utf-8 -*-
"""
Servidor Web de Interfaz Gráfica para CTI y Scoring de Dominios.
Ejecuta el pipeline localmente sin depender de n8n activo.
"""
import os
import sys
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Agregar directorio actual a sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from core_engine import ejecutar_pipeline, SHODAN_KEY, ABUSEIPDB_KEY, ABUSECH_KEY, MXTOOLBOX_KEY
from html_report import generar_html_estatico

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>SOC Command Center · Threat Intelligence Suite</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg: #070a13;
      --card-bg: #111827;
      --border: #1f2937;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
    }
    * { box-sizing: border-box; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 24px; }
    .container { max-width: 1280px; margin: 0 auto; }
    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 12px; }
    .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); }
    textarea { width: 100%; background: #070a13; border: 1px solid #374151; border-radius: 8px; color: #fff; padding: 12px; font-size: 14px; font-family: monospace; resize: vertical; min-height: 110px; }
    textarea:focus { outline: none; border-color: var(--primary); }
    .btn { background: var(--primary); color: #fff; border: none; padding: 11px 20px; border-radius: 8px; font-size: 13px; font-weight: 700; cursor: pointer; transition: background 0.2s; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; }
    .btn:hover { background: var(--primary-hover); }
    .btn:disabled { opacity: 0.5; cursor: not-allowed; }
    .btn-secondary { background: #1e293b; border: 1px solid #334155; color: #cbd5e1; }
    .btn-secondary:hover { background: #334155; color: #fff; }
    .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-top: 16px; }
    .metric { background: #0b0f19; border: 1px solid #1e293b; border-radius: 8px; padding: 14px; }
    .metric-val { font-size: 26px; font-weight: 800; color: #fff; }
    .metric-lbl { font-size: 11px; color: var(--text-muted); text-transform: uppercase; margin-top: 4px; font-weight: 600; }
    table { width: 100%; border-collapse: collapse; text-align: left; }
    th { background: #0f172a; color: #94a3b8; font-size: 11px; text-transform: uppercase; padding: 8px 12px; border-bottom: 1px solid #334155; }
    td { padding: 8px 12px; border-bottom: 1px solid #1e293b; font-size: 12px; vertical-align: middle; }
    .pill { padding: 4px 10px; border-radius: 9999px; font-weight: 700; font-size: 12px; display: inline-block; }
    #logTerminal { background: #05070d; border: 1px solid #1e293b; border-radius: 8px; padding: 12px; color: #38bdf8; font-family: monospace; font-size: 12px; max-height: 160px; overflow-y: auto; margin-top: 14px; display: none; }
    .api-status-bar { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; font-size: 12px; }
    .api-chip { background: #0f172a; border: 1px solid #1e293b; padding: 4px 10px; border-radius: 6px; display: flex; align-items: center; gap: 6px; }
    .dot { width: 8px; height: 8px; border-radius: 50%; }
    .dot-green { background: #10b981; }
    .dot-red { background: #ef4444; }
    .filter-bar { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-bottom: 14px; }
    .filter-input { flex: 1; min-width: 220px; background: #0b0f19; border: 1px solid #334155; border-radius: 6px; color: #f1f5f9; padding: 8px 12px; font-size: 13px; }
    .filter-select { background: #0b0f19; border: 1px solid #334155; border-radius: 6px; color: #f1f5f9; padding: 8px 12px; font-size: 13px; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div>
        <h1 style="margin:0; font-size:22px; color:#38bdf8;">🛡️ SOC Threat Intelligence Suite · Command Center</h1>
        <div style="color:var(--text-muted); font-size:13px; margin-top:4px;">Pipeline por lotes multi-herramienta (Shodan · AbuseIPDB · IP-API · Abuse.ch · MXToolbox + DoH · RDAP/WHOIS · ISO)</div>
      </div>
      <div>
        <a href="/download-workflow" class="btn btn-secondary" style="font-size:12px;">📥 Descargar Workflow para n8n</a>
      </div>
    </div>

    <!-- Barra de estado de APIs -->
    <div class="api-status-bar">
      <div class="api-chip"><span class="dot __SHODAN_CLASS__"></span> Shodan API: __SHODAN_TXT__ (fallback InternetDB)</div>
      <div class="api-chip"><span class="dot __ABUSE_CLASS__"></span> AbuseIPDB: __ABUSE_TXT__</div>
      <div class="api-chip"><span class="dot dot-green"></span> IP-API / DoH / RDAP: Sin cuotas</div>
      <div class="api-chip"><span class="dot __ABUSECH_CLASS__"></span> Abuse.ch: __ABUSECH_TXT__</div>
      <div class="api-chip"><span class="dot __MX_CLASS__"></span> MXToolbox: __MX_TXT__ (fallback DoH)</div>
    </div>

    <!-- Formulario de entrada -->
    <div class="card">
      <label style="font-size:13px; font-weight:600; display:block; margin-bottom:8px; color:#e2e8f0;">
        Ingresa múltiples empresas, organismos o dominios directos para consultar de una pasada (uno por línea o separados por coma):
      </label>
      <textarea id="inputNombres" placeholder="Ejemplo:&#10;Banco Central del Paraguay&#10;Technoma&#10;pechugon.com.py&#10;mercadolibre.com">Banco Central del Paraguay
Technoma</textarea>

      <div style="margin-top:14px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
        <button id="btnEjecutar" class="btn" onclick="iniciarAnalisis()">⚡ Iniciar Análisis por Lote</button>
        <span id="txtLoading" style="color:#93c5fd; font-size:13px; display:none;">⏳ Consultando fuentes de Threat Intelligence en paralelo... por favor espera</span>
      </div>

      <div id="logTerminal"></div>
    </div>

    <!-- Resultados -->
    <div id="seccionResultados" style="display:none;">
      <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <h2 style="margin:0; font-size:16px;">Resumen Ejecutivo del Lote</h2>
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <button class="btn btn-secondary" style="font-size:12px; padding:7px 12px;" onclick="descargarHTMLOffline()">🌐 Exportar Suite HTML Offline</button>
            <button class="btn btn-secondary" style="font-size:12px; padding:7px 12px;" onclick="descargarJSON()">💾 Descargar JSON</button>
          </div>
        </div>
        <div class="metrics-grid">
          <div class="metric"><div class="metric-val" id="kpiProcesadas">0</div><div class="metric-lbl">Entidades Entrada</div></div>
          <div class="metric"><div class="metric-val" style="color:#60a5fa;" id="kpiAnalizados">0</div><div class="metric-lbl">Dominios Analizados</div></div>
          <div class="metric"><div class="metric-val" id="kpiCritico" style="color:#ef4444;">0</div><div class="metric-lbl">Riesgo Crítico</div></div>
          <div class="metric"><div class="metric-val" id="kpiAlto" style="color:#f97316;">0</div><div class="metric-lbl">Riesgo Alto</div></div>
          <div class="metric"><div class="metric-val" id="kpiMedio" style="color:#eab308;">0</div><div class="metric-lbl">Riesgo Medio</div></div>
          <div class="metric"><div class="metric-val" id="kpiBajo" style="color:#22c55e;">0</div><div class="metric-lbl">Riesgo Bajo</div></div>
        </div>
      </div>

      <div id="panelMatriz" class="card" style="display:none; padding:16px 18px;">
        <div class="filter-bar">
          <input id="filtroInput" class="filter-input" type="text" placeholder="🔎 Filtrar lote por dominio, entidad, IP, país, ISP o CVE..." oninput="aplicarFiltro()">
          <select id="filtroNivel" class="filter-select" onchange="aplicarFiltro()">
            <option value="">Todos los niveles</option>
            <option value="CRÍTICO">Solo CRÍTICO</option>
            <option value="ALTO">Solo ALTO</option>
            <option value="MEDIO">Solo MEDIO</option>
            <option value="BAJO">Solo BAJO</option>
          </select>
          <button class="btn btn-secondary" style="font-size:12px;padding:7px 10px;" onclick="toggleTodos(true)">▾ Expandir todos</button>
          <button class="btn btn-secondary" style="font-size:12px;padding:7px 10px;" onclick="toggleTodos(false)">▸ Colapsar todos</button>
        </div>
        <div style="font-weight:700;font-size:13px;color:#93c5fd;margin-bottom:8px;">📋 Matriz Comparativa Rápida del Lote</div>
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

      <div id="contenedorDossiers"></div>

      <div id="cardSinDominio" class="card" style="padding:0; overflow:hidden; display:none; border-color:#854d0e;">
        <div style="padding:14px 18px; border-bottom:1px solid var(--border); font-weight:600; font-size:14px; color:#fbbf24; background:#0f172a;">⚠️ Entidades sin Dominio Verificado (Flujo Continuado sin Fallas)</div>
        <table>
          <thead><tr><th>Nombre</th><th>Motivo</th><th>Estado</th></tr></thead>
          <tbody id="tablaSinDominio"></tbody>
        </table>
      </div>
    </div>
  </div>

  <script>
    let ultimoReporte = null;

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

    function log(msg) {
      const term = document.getElementById('logTerminal');
      term.style.display = 'block';
      const line = document.createElement('div');
      line.textContent = msg;
      term.appendChild(line);
      term.scrollTop = term.scrollHeight;
    }

    async function iniciarAnalisis() {
      const txt = document.getElementById('inputNombres').value.trim();
      if (!txt) return alert('Por favor ingresa al menos un nombre o dominio.');

      const nombres = txt.split(/[\r\n,;]+/).map(s => s.trim()).filter(Boolean);
      document.getElementById('btnEjecutar').disabled = true;
      document.getElementById('txtLoading').style.display = 'inline';
      document.getElementById('logTerminal').innerHTML = '';
      log('[*] Enviando ' + nombres.length + ' entidad(es) al motor de CTI...');

      try {
        const res = await fetch('/api/analizar', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ nombres })
        });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        const data = await res.json();
        ultimoReporte = data;
        log('[+] Análisis finalizado: ' + data.resumen.dominios_analizados + ' dominio(s) evaluados.');
        renderResultados(data);
      } catch (err) {
        log('[-] Error de ejecución: ' + err.message);
      } finally {
        document.getElementById('btnEjecutar').disabled = false;
        document.getElementById('txtLoading').style.display = 'none';
      }
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

    function renderResultados(rep) {
      document.getElementById('seccionResultados').style.display = 'block';
      document.getElementById('kpiProcesadas').textContent = rep.resumen.nombres_procesados;
      document.getElementById('kpiAnalizados').textContent = rep.resumen.dominios_analizados;
      document.getElementById('kpiCritico').textContent = rep.resumen.por_nivel['CRÍTICO'] || 0;
      document.getElementById('kpiAlto').textContent = rep.resumen.por_nivel.ALTO || 0;
      document.getElementById('kpiMedio').textContent = rep.resumen.por_nivel.MEDIO || 0;
      document.getElementById('kpiBajo').textContent = rep.resumen.por_nivel.BAJO || 0;

      const cont = document.getElementById('contenedorDossiers');
      const matrizBody = document.getElementById('tablaMatriz');
      const panelMatriz = document.getElementById('panelMatriz');

      if (!rep.dominios || !rep.dominios.length) {
        panelMatriz.style.display = 'none';
        cont.innerHTML = '<div class="card" style="text-align:center; padding:24px; color:#9ca3af;">No se encontraron dominios verificados.</div>';
      } else {
        panelMatriz.style.display = 'block';
        const matrizRows = [];
        cont.innerHTML = rep.dominios.map((d, idx) => {
          let col = { bg: '#16a34a', text: '#fff', border: '#15803d', label: 'BAJO' };
          if (d.score >= 75) col = { bg: '#dc2626', text: '#fff', border: '#b91c1c', label: 'CRÍTICO' };
          else if (d.score >= 50) col = { bg: '#ea580c', text: '#fff', border: '#c2410c', label: 'ALTO' };
          else if (d.score >= 25) col = { bg: '#ca8a04', text: '#fff', border: '#a16207', label: 'MEDIO' };

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
                <div style="font-family:monospace;color:#e2e8f0;">${esc(primaryIp.ip || (d.ips && d.ips[0]) || '-')}</div>
                <div style="color:#94a3b8;font-size:11px;">${esc(ia.pais || ab.pais || '-')} · ${esc(ia.isp || ab.isp || sh.org || '-')}</div>
              </td>
              <td>${todosPuertos.length ? todosPuertos.slice(0, 4).join(', ') + (todosPuertos.length > 4 ? '...' : '') : '0 puertos'} · ${todasVulns.length ? `<span style="color:#f87171;font-weight:700;">${todasVulns.length} CVEs</span>` : '<span style="color:#22c55e;">0 CVEs</span>'}</td>
              <td><strong style="color:${maxAbuse >= 50 ? '#ef4444' : maxAbuse >= 25 ? '#eab308' : '#22c55e'};">${maxAbuse}%</strong> (${totalReportesAbuse} rep)</td>
              <td>${spfItems.length ? '🟢 SPF' : '🔴 Sin SPF'} · ${dmarcItems.length ? '🟢 DMARC' : '🟡 Sin DMARC'}</td>
              <td>${rdap.estado === 'ok' && rdap.antiguedad_anios !== null ? esc(rdap.antiguedad_anios) + ' años' : '-'} ${(iso.normas && iso.normas.length) ? '· 📜 ISO' : ''}</td>
            </tr>
          `);

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
              <tr>
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
                ${todasVulns.map(v => `<a href="https://nvd.nist.gov/vuln/detail/${encodeURIComponent(v)}" target="_blank" style="background:#450a0a;color:#fca5a5;border:1px solid #991b1b;padding:3px 8px;border-radius:4px;font-size:11px;font-family:monospace;text-decoration:none;font-weight:600;">${esc(v)} ↗</a>`).join('')}
              </div>
            </div>
          ` : '<div style="color:#22c55e;font-size:12px;margin-top:8px;">✅ Sin vulnerabilidades CVE conocidas indexadas en Shodan.</div>';

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
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;">Confianza de Abuso</div>
                <div style="font-size:24px;font-weight:800;color:${abuseProgressCol};">${maxAbuse}%</div>
                <div style="background:#334155;border-radius:9999px;height:8px;width:100%;overflow:hidden;margin-top:4px;">
                  <div style="background:${abuseProgressCol};height:100%;width:${maxAbuse}%;"></div>
                </div>
              </div>
              <div style="font-size:12px;color:#cbd5e1;line-height:1.6;">
                <div><strong>Reportes:</strong> ${totalReportesAbuse} denuncias en últimos 90 días</div>
                <div><strong>Denunciantes Únicos:</strong> ${ab.usuarios_distintos || 0} redes distintas · <strong>Tipo Uso:</strong> ${esc(ab.tipo_uso || 'N/A')}</div>
                <div><strong>Último Reporte:</strong> ${ab.ultimo_reporte ? esc(new Date(ab.ultimo_reporte).toLocaleString()) : 'Sin reportes recientes'}</div>
                <div><strong>Lista Blanca / Tor:</strong> ${ab.whitelisted ? '🟢 Sí' : '⚪ No'} · ${ab.es_tor ? '🔴 Nodo Tor' : 'No Tor'}</div>
              </div>
            </div>
            ${recientesHtml}
          `;

          const feodoMal = feodoHit ? (feodoHit.feodo.malware || (feodoHit.feodo.detalle && feodoHit.feodo.detalle.malware) || 'C2') : '';
          const feodoBadge = feodoHit
            ? `<div style="background:#7f1d1d;color:#fca5a5;padding:8px 12px;border-radius:6px;margin-bottom:8px;font-size:12px;font-weight:600;">🚨 ALERTA CRÍTICA: ${esc(feodoHit.ip)} listada como C2 de Botnet (${esc(feodoMal)})</div>`
            : `<div style="color:#22c55e;font-size:12px;margin-bottom:6px;">✅ Feodo Tracker: Limpio (sin actividad de botnets C2).</div>`;

          const urlhausHtml = uh.listado ? `
            <div style="margin-top:6px;font-size:12px;color:#fca5a5;">
              ⚠️ URLhaus: <strong>${uh.urls_total}</strong> URLs de malware (${uh.urls_online} activas online).
              Amenazas: <strong>${(uh.amenazas || []).map(esc).join(', ') || 'Malware general'}</strong>
              ${(uh.muestras || []).slice(0, 3).map(m => `<div style="font-family:monospace;font-size:11px;background:#1e1b4b;padding:4px 8px;border-radius:4px;margin-top:4px;word-break:break-all;">${esc(m.url)} [${esc(m.estado)}] ${m.tags && m.tags.length ? '(' + m.tags.map(esc).join(', ') + ')' : ''}</div>`).join('')}
            </div>
          ` : '<div style="color:#22c55e;font-size:12px;">✅ URLhaus: Sin URLs maliciosas registradas.</div>';

          const threatfoxHtml = tf.listado ? `
            <div style="margin-top:6px;font-size:12px;color:#fca5a5;">
              ⚠️ ThreatFox: <strong>${(tf.iocs || []).length}</strong> Indicadores de Compromiso (IOCs) asociados.
              ${(tf.iocs || []).slice(0, 3).map(ioc => `<div style="font-family:monospace;font-size:11px;background:#31102b;padding:4px 8px;border-radius:4px;margin-top:4px;">${esc(ioc.ioc)} · ${esc(ioc.tipo)} · ${esc(ioc.malware || 'Payload')} (Confianza: ${esc(ioc.confianza)}%)</div>`).join('')}
            </div>
          ` : '<div style="color:#22c55e;font-size:12px;">✅ ThreatFox: Sin IOCs maliciosos registrados para este dominio.</div>';

          const mxResumenHtml = `
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;font-size:12px;">
              <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
                <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">📬 Servidores MX:</div>
                ${mxItems.length ? mxItems.map(m => `<div style="font-family:monospace;font-size:11px;color:#e2e8f0;">• ${esc(m.valor || m.clave)}</div>`).join('') : '<div style="color:#94a3b8;">Sin datos MX</div>'}
              </div>
              <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
                <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🛡️ SPF:</div>
                ${spfItems.length ? spfItems.map(s => `<div style="font-family:monospace;font-size:11px;color:#e2e8f0;word-break:break-all;">${esc(s.valor || s.desc)}</div>`).join('') : '<div style="color:#f87171;">Sin SPF</div>'}
              </div>
              <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
                <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🔒 DMARC:</div>
                ${dmarcItems.length ? dmarcItems.map(dm => `<div style="font-family:monospace;font-size:11px;color:#e2e8f0;word-break:break-all;">${esc(dm.valor || dm.desc)}</div>`).join('') : '<div style="color:#f87171;">Sin DMARC</div>'}
              </div>
              <div style="background:#0f172a;border:1px solid #1e293b;border-radius:6px;padding:10px;">
                <div style="font-weight:700;color:#93c5fd;margin-bottom:4px;">🚫 Blacklists (DNSBL):</div>
                ${blFails.length ? `<div style="color:#ef4444;font-weight:600;">🔴 ${blFails.length} lista(s): ${blFails.map(esc).join(', ')}</div>` : (mx.blacklist && mx.blacklist.estado === 'no_disponible' ? `<div style="color:#fbbf24;">⚠️ Blacklist no disponible (${esc(mx.blacklist.motivo || 'cuota')})</div>` : '<div style="color:#22c55e;font-weight:600;">🟢 Limpio (0/50+)</div>')}
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
                ${normas.map(n => `<span style="background:#1e3a8a;color:#bfdbfe;border:1px solid #3b82f6;padding:4px 10px;border-radius:6px;font-size:12px;font-weight:600;">${esc(n.norma)} · ${esc(n.descripcion || 'Norma Internacional')} ${n.versiones && n.versiones.length ? '(' + n.versiones.map(esc).join(', ') + ')' : ''}</span>`).join('')}
              </div>
              ${normas.flatMap(n => n.evidencias || []).slice(0, 2).map(e => `<div style="background:#0f172a;border-left:3px solid #3b82f6;padding:6px 10px;margin-top:4px;font-size:11px;color:#cbd5e1;"><em>"...${esc(e.fragmento)}..."</em> <a href="${safeUrl(e.url)}" target="_blank" style="color:#60a5fa;margin-left:6px;">[Ver Fuente]</a></div>`).join('')}
            </div>
          ` : '<span style="color:#94a3b8;font-size:12px;">No se identificaron certificaciones ISO declaradas en las páginas públicas auditadas.</span>';

          const desgloseRows = (d.desglose || []).map(item => `
            <tr>
              <td style="font-weight:700;font-family:monospace;color:${item.puntos > 0 ? '#f87171' : item.puntos < 0 ? '#4ade80' : '#94a3b8'};">${item.puntos > 0 ? '+' + item.puntos : item.puntos}</td>
              <td style="color:#cbd5e1;text-transform:uppercase;font-weight:600;">${esc(item.fuente)}</td>
              <td style="color:#94a3b8;font-family:monospace;font-size:11px;">${esc(item.consulta || '-')}</td>
              <td style="color:#e2e8f0;">${esc(item.evidencia)}</td>
            </tr>
          `).join('');

          return `
            <div id="dom-${idx}" class="card dossier-card" data-nivel="${col.label}" data-search="${esc(searchBlob)}" style="padding:0; overflow:hidden; margin-bottom:24px;">
              <div style="background:#1e293b;padding:16px 20px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;border-bottom:1px solid #334155;">
                <div>
                  <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
                    <a href="${safeUrl(d.url)}" target="_blank" style="color:#60a5fa; font-weight:700; font-size:18px; text-decoration:none;">${esc(d.dominio)}</a>
                    <span style="background:#0f172a;color:#94a3b8;font-size:11px;padding:3px 8px;border-radius:4px;border:1px solid #334155;">Entidad: ${esc(origenTxt)}</span>
                  </div>
                  <div style="color:#94a3b8; font-size:12px; margin-top:4px;">🌐 IPs: <span style="font-family:monospace;color:#e2e8f0;">${d.ips.map(esc).join(', ')}</span> · Ubicación: <strong style="color:#e2e8f0;">${ia.ciudad ? esc(ia.ciudad) + ', ' : ''}${esc(ia.pais || ab.pais || 'Global')}</strong> · Red: <strong style="color:#cbd5e1;">${esc(ia.isp || ia.org || ab.isp || sh.org || 'ISP')}</strong></div>
                </div>
                <span class="pill" style="background:${col.bg}; color:${col.text}; font-size:15px; padding:6px 14px;">${d.score}/100 · ${col.label}</span>
              </div>

              <div style="background:#0f172a;padding:12px 20px;display:grid;grid-template-columns:repeat(auto-fit, minmax(170px, 1fr));gap:10px;border-bottom:1px solid #1e293b;font-size:12px;">
                <div><span style="color:#94a3b8;font-size:11px;">📡 Red:</span> ${ia.proxy ? '🔴 Proxy' : '🟢 Directo'} · ${ia.hosting ? '🟠 Cloud' : '🟢 Propia'}</div>
                <div><span style="color:#94a3b8;font-size:11px;">🔍 Puertos:</span> ${todosPuertos.slice(0,5).join(', ') || 'Ninguno'} (${todasVulns.length} CVEs)</div>
                <div><span style="color:#94a3b8;font-size:11px;">⚠️ Abuso:</span> ${maxAbuse}% (${totalReportesAbuse} rep)</div>
                <div><span style="color:#94a3b8;font-size:11px;">☣️ Malware:</span> ${feodoHit ? '🔴 C2' : '🟢 Feodo'} · ${uh.listado ? '🔴 ' + uh.urls_total + ' URLs' : '🟢 Limpio'}</div>
                <div><span style="color:#94a3b8;font-size:11px;">✉️ Email:</span> ${blFails.length ? '🔴 Blacklist' : '🟢 Limpio'} · ${spfItems.length ? '🟢 SPF' : '🟡 No SPF'}</div>
              </div>

              <details class="dossier-details" style="padding:16px 20px; cursor:pointer;" open>
                <summary style="color:#93c5fd; font-size:13px; font-weight:700; margin-bottom:12px;">📊 Dossier Técnico de Inteligencia (Desplegar / Ocultar Detalles Exhaustivos)</summary>
                <div style="display:flex;flex-direction:column;gap:16px;margin-top:12px;">
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">🌐 1. Infraestructura de Red &amp; Geolocalización (IP-API · Sin Cuotas)</div>
                    <table><thead><tr><th>IP / PTR</th><th>Ubicación</th><th>ISP / Org</th><th>ASN</th><th>Proxy/VPN</th><th>Alojamiento</th></tr></thead><tbody>${filasIps}</tbody></table>
                  </div>
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">🔍 2. Superficie de Ataque, CPEs &amp; Vulnerabilidades CVE (Shodan)</div>
                    <div>${todosPuertos.length ? todosPuertos.map(badgePuerto).join('') : '<span style="color:#94a3b8;font-size:12px;">Sin puertos expuestos</span>'}</div>
                    ${cpesHtml}${vulnsHtml}
                    ${todosHosts.length ? `<div style="font-size:11px;color:#94a3b8;margin-top:8px;"><strong>Hostnames DNS:</strong> ${todosHosts.map(esc).join(', ')}</div>` : ''}
                    ${tagsHtml}
                  </div>
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">🚨 3. Historial de Abuso y Reportes (AbuseIPDB)</div>
                    ${abuseHtml}
                  </div>
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">☣️ 4. Amenazas Activas, Botnets &amp; Malware (Abuse.ch Suite)</div>
                    ${feodoBadge}${urlhausHtml}${threatfoxHtml}
                  </div>
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">✉️ 5. Seguridad de Correo Electrónico, DNS &amp; Blacklists (MXToolbox + Google DoH)</div>
                    ${mxResumenHtml}${nsHtml}
                  </div>
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">📜 6. Registro WHOIS/RDAP, Antigüedad &amp; Cumplimiento ISO</div>
                    ${rdapHtml}${isoHtml}
                  </div>
                  <div style="background:#090d16;border:1px solid #1e293b;border-radius:8px;padding:14px;">
                    <div style="font-weight:700;color:#38bdf8;font-size:13px;margin-bottom:8px;">⚖️ 7. Auditoría Contable del Score (Regla Ponderada 1-100)</div>
                    <table><thead><tr><th>Puntos</th><th>Fuente</th><th>Consulta</th><th>Evidencia Técnica</th></tr></thead><tbody>${desgloseRows}</tbody></table>
                  </div>
                </div>
              </details>
            </div>
          `;
        }).join('');
        matrizBody.innerHTML = matrizRows.join('');
      }

      const sinDomCard = document.getElementById('cardSinDominio');
      const sinDomBody = document.getElementById('tablaSinDominio');
      if (rep.sin_dominio && rep.sin_dominio.length) {
        sinDomCard.style.display = 'block';
        sinDomBody.innerHTML = rep.sin_dominio.map(s => `
          <tr>
            <td style="font-weight:600;">${esc(s.nombre)}</td>
            <td style="color:#94a3b8;">${esc(s.motivo)}</td>
            <td style="color:#fbbf24; font-size:12px;">Registrado (flujo continuado)</td>
          </tr>
        `).join('');
      } else {
        sinDomCard.style.display = 'none';
      }
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
      if (!ultimoReporte) return;
      const blob = new Blob([JSON.stringify(ultimoReporte, null, 2)], { type: 'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `ti_dominios_${new Date().toISOString().replace(/[:.-]/g, '').slice(0, 15)}.json`;
      a.click();
    }

    async function descargarHTMLOffline() {
      if (!ultimoReporte) return;
      try {
        const res = await fetch('/api/export-html', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(ultimoReporte)
        });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        const htmlText = await res.text();
        const blob = new Blob([htmlText], { type: 'text/html;charset=utf-8' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = `dossier_cti_${new Date().toISOString().replace(/[:.-]/g, '').slice(0, 15)}.html`;
        a.click();
      } catch (e) {
        alert('No se pudo exportar HTML: ' + e.message);
      }
    }
  </script>
</body>
</html>"""

class WebHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Silenciar logs ruidosos de consola

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            def tag(val):
                return ("dot-green", "Activa") if val else ("dot-red", "Sin clave")

            sh_cl, sh_tx = tag(SHODAN_KEY)
            ab_cl, ab_tx = tag(ABUSEIPDB_KEY)
            ach_cl, ach_tx = tag(ABUSECH_KEY)
            mx_cl, mx_tx = tag(MXTOOLBOX_KEY)

            html = HTML_TEMPLATE
            html = html.replace("__SHODAN_CLASS__", sh_cl).replace("__SHODAN_TXT__", sh_tx)
            html = html.replace("__ABUSE_CLASS__", ab_cl).replace("__ABUSE_TXT__", ab_tx)
            html = html.replace("__ABUSECH_CLASS__", ach_cl).replace("__ABUSECH_TXT__", ach_tx)
            html = html.replace("__MX_CLASS__", mx_cl).replace("__MX_TXT__", mx_tx)

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif self.path == "/download-workflow":
            wf_path = Path(__file__).parent / "workflow_n8n_listo_para_importar.json"
            if wf_path.exists():
                data = wf_path.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Disposition", 'attachment; filename="workflow_ti_dominios.json"')
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_response(404)
                self.end_headers()
        elif self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/analizar":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            data = json.loads(body)
            nombres = data.get("nombres", [])

            reporte = ejecutar_pipeline(nombres)

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(reporte, ensure_ascii=False).encode("utf-8"))
        elif self.path == "/api/export-html":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            reporte = json.loads(body)
            html_out = generar_html_estatico(reporte)

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_out.encode("utf-8"))
        elif self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def main():
    port = 5050
    server = HTTPServer(("127.0.0.1", port), WebHandler)
    url = f"http://127.0.0.1:{port}"
    print("=" * 65)
    print(f"   SOC COMMAND CENTER · CTI & DOMAIN INTELLIGENCE GUI")
    print("=" * 65)
    print(f"[*] Servidor iniciado exitosamente en: {url}")
    print("[*] Abriendo interfaz gráfica en tu navegador...")
    print("[*] Presiona Ctrl + C en esta ventana para detener el servidor.")
    print("=" * 65)

    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Servidor detenido.")
        server.server_close()

if __name__ == "__main__":
    main()
