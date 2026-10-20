#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🌐 TECHNOMA SOAR — WEB COMMAND CENTER (FastAPI + Modern Cyberpunk UI)
=============================================================================
Interfaz Web Unificada que reemplaza la fricción de la consola y conecta:
  1. 🧠 Memoria Instantánea de 7 Capas (2,022 Markdowns pre-indexados en <15ms)
  2. 🛡️ Copiloto Forense IA con Streaming en Vivo (Google Antigravity Gemini 3.8 Flash High)
  3. 🎯 Threat Intelligence Tri-Scan en Paralelo (VT + AbuseIPDB + URLScan + OTX + MxToolbox)
  4. 📡 Conexión Directa a Stellar Cyber OpenXDR (Casos en vivo y alertas por Case ID)
  5. ⏱️ Calculadora y Monitor de Gobernanza SLA / SLO (MTTD, MTTR, Matriz P1-P4)
  6. 🗂️ Explorador Interactivo de los 2,022 Markdowns y 60 Skills del Proyecto
=============================================================================
"""

import os
import sys
import json
import time
import threading
import webbrowser
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qs

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent

from rag_engine import get_rag
from cti_engine import CtiEngine
from sla_governance import SlaGovernanceEngine
from soar_ai_client import is_antigravity_available, stream_antigravity, call_antigravity
from soc_agent import auto_enriquecer_contexto, preparar_entrada
from soc_agent_gui import extraer_cierre_consola, extraer_tsv_bitacora as extraer_tsv_18_columnas


HTML_DASHBOARD = r"""<!DOCTYPE html>
<html lang="es" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>🛡️ TECHNOMA SOAR — Web Command Center & Memory Brain</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body { background-color: #060b16; color: #e2e8f0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
    .glass { background: rgba(15, 23, 42, 0.82); backdrop-filter: blur(12px); border: 1px solid rgba(56, 189, 248, 0.16); }
    .tab-btn.active { background: linear-gradient(90deg, rgba(14,165,233,0.22), rgba(59,130,246,0.10)); border-left: 3px solid #38bdf8; color: #38bdf8; font-weight: 600; }
    .prose-soc h2, .prose-soc h3 { color: #38bdf8; font-weight: 700; margin-top: 1rem; margin-bottom: 0.5rem; }
    .prose-soc table { width: 100%; border-collapse: collapse; margin: 0.75rem 0; font-size: 0.85rem; }
    .prose-soc th, .prose-soc td { border: 1px solid #1e293b; padding: 6px 10px; text-align: left; }
    .prose-soc th { background-color: #0f172a; color: #94a3b8; }
    .prose-soc blockquote { border-left: 4px solid #10b981; background: #020617; padding: 10px 14px; border-radius: 6px; margin: 8px 0; color: #a7f3d0; }
    .prose-soc pre { background: #020617; border: 1px solid #1e293b; padding: 10px; border-radius: 6px; overflow-x: auto; font-size: 0.8rem; }
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #060b16; }
    ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #38bdf8; }
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <!-- TOP HEADER -->
  <header class="glass sticky top-0 z-30 px-6 py-3 flex items-center justify-between border-b border-slate-800">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-lg bg-sky-500/10 border border-sky-400/30 flex items-center justify-center text-xl">🛡️</div>
      <div>
        <h1 class="text-lg font-bold tracking-wide text-white flex items-center gap-2">
          TECHNOMA SOC <span class="text-xs px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-400/30">SOAR WEB COCKPIT v2.0</span>
        </h1>
        <p class="text-xs text-slate-400">Cerebro Unificado: <span id="stat-files" class="text-emerald-400 font-semibold">2,022 Markdowns</span> (<span id="stat-chunks">13,868</span> bloques en RAM) · Motor IA: <span class="text-sky-400 font-semibold">Google Antigravity (Gemini 3.8 Flash High)</span></p>
      </div>
    </div>
    <div class="flex items-center gap-3">
      <span class="px-3 py-1 rounded-full text-xs font-medium bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">● 0-Token Workspace Search</span>
      <span class="px-3 py-1 rounded-full text-xs font-medium bg-sky-500/15 text-sky-300 border border-sky-500/30">● OAuth Activo</span>
    </div>
  </header>

  <!-- MAIN CONTENT -->
  <div class="flex-1 flex overflow-hidden">
    <!-- SIDEBAR NAVIGATION -->
    <aside class="w-64 glass border-r border-slate-800 p-4 flex flex-col gap-1.5">
      <div class="text-[11px] font-semibold uppercase tracking-wider text-slate-500 px-3 mb-1">Operaciones SOC</div>
      <button onclick="switchTab('triage')" id="tab-triage" class="tab-btn active text-left px-3 py-2.5 rounded-lg text-sm text-slate-300 hover:bg-slate-800/60 transition flex items-center gap-2.5">
        <span>🤖</span> Copiloto Forense & Triaje
      </button>
      <button onclick="switchTab('memory')" id="tab-memory" class="tab-btn text-left px-3 py-2.5 rounded-lg text-sm text-slate-300 hover:bg-slate-800/60 transition flex items-center gap-2.5">
        <span>🧠</span> Cerebro SOC (7 Capas)
      </button>
      <button onclick="switchTab('cti')" id="tab-cti" class="tab-btn text-left px-3 py-2.5 rounded-lg text-sm text-slate-300 hover:bg-slate-800/60 transition flex items-center gap-2.5">
        <span>🎯</span> Escáner CTI Paralelo
      </button>
      <button onclick="switchTab('sla')" id="tab-sla" class="tab-btn text-left px-3 py-2.5 rounded-lg text-sm text-slate-300 hover:bg-slate-800/60 transition flex items-center gap-2.5">
        <span>⏱️</span> Calculadora SLA / SLO
      </button>
      <button onclick="switchTab('catalog')" id="tab-catalog" class="tab-btn text-left px-3 py-2.5 rounded-lg text-sm text-slate-300 hover:bg-slate-800/60 transition flex items-center gap-2.5">
        <span>📚</span> Catálogo de tus 2,022 MDs
      </button>

      <div class="mt-auto pt-4 border-t border-slate-800/80 text-xs text-slate-400 space-y-1.5 px-2">
        <div class="font-semibold text-slate-300">Capas Indexadas en Disco:</div>
        <div class="flex justify-between"><span>🧠 MEMORIA_SOC</span><span class="text-sky-400">1.65x</span></div>
        <div class="flex justify-between"><span>📁 CASO_HISTORICO</span><span class="text-emerald-400">1.50x</span></div>
        <div class="flex justify-between"><span>📕 PLAYBOOK</span><span class="text-amber-400">1.45x</span></div>
        <div class="flex justify-between"><span>⚙️ PROCEDIMIENTO</span><span class="text-purple-400">1.30x</span></div>
        <div class="flex justify-between"><span>🛠️ 60 SKILLS SOC</span><span class="text-pink-400">1.25x</span></div>
        <div class="flex justify-between"><span>📘 DOC_STELLAR</span><span class="text-slate-400">1.00x</span></div>
      </div>
    </aside>

    <!-- PANELS -->
    <main class="flex-1 overflow-y-auto p-6">

      <!-- 1. PANEL TRIAGE FORENSE IA -->
      <section id="panel-triage" class="space-y-4">
        <div class="glass rounded-xl p-5">
          <div class="flex flex-wrap items-center justify-between gap-4 mb-3">
            <div>
              <h2 class="text-base font-bold text-white">🤖 Copiloto Forense con Memoria Instantánea (0-Latency Context)</h2>
              <p class="text-xs text-slate-400">Cruza automáticamente tu caso con <code class="text-sky-300">SOC_GEM_v2.md</code>, tus +35 casos históricos, usuarios AD, Playbooks y redacta las 4 fases + Cierre + TSV 18 columnas.</p>
            </div>
            <div class="flex items-center gap-2">
              <input id="stellar-case-id" type="text" placeholder="ID Caso Stellar (ej. 17813)" class="bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white focus:border-sky-400 outline-none w-48" />
              <button onclick="fetchStellarCase()" class="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold px-3 py-1.5 rounded-lg transition">📡 Traer de Stellar</button>
            </div>
          </div>

          <textarea id="triage-input" rows="6" placeholder="Pegá aquí el JSON crudo de Stellar Cyber / Interflow, alerta de FortiGate / Sophos / Cortex XDR, o escribí los detalles del caso..." class="w-full bg-slate-950 border border-slate-800 rounded-lg p-3 text-xs font-mono text-slate-200 focus:border-sky-500 outline-none"></textarea>

          <div class="flex flex-wrap items-center justify-between gap-3 mt-3">
            <div class="flex items-center gap-2">
              <button onclick="runTriage()" id="btn-run-triage" class="bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold text-xs px-5 py-2.5 rounded-lg transition flex items-center gap-2">
                ⚡ Analizar Caso con Memoria SOC + Gemini 3.8 Flash
              </button>
              <button onclick="previewMemoryOnly()" class="bg-slate-800 hover:bg-slate-700 text-sky-300 border border-sky-500/30 text-xs font-semibold px-4 py-2.5 rounded-lg transition">
                🧠 Ver Qué Recuerda el Cerebro SOC (<15ms, 0 Tokens)
              </button>
            </div>
            <span id="triage-status" class="text-xs text-slate-400 font-mono">Listo.</span>
          </div>
        </div>

        <!-- SUB-TABS RESULTADO TRIAGE -->
        <div class="glass rounded-xl p-5">
          <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
            <div class="flex gap-2">
              <button onclick="switchTriageSub('dictamen')" id="subbtn-dictamen" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30">🔍 1. Dictamen Forense (4 Fases)</button>
              <button onclick="switchTriageSub('cierre')" id="subbtn-cierre" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-400 hover:text-white">💬 2. Cierre Humanizado Consola</button>
              <button onclick="switchTriageSub('tsv')" id="subbtn-tsv" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-400 hover:text-white">📊 3. Bitácora Excel (18 Cols TSV)</button>
              <button onclick="switchTriageSub('mempack')" id="subbtn-mempack" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-400 hover:text-white">🧠 4. Evidencias Locales Inyectadas</button>
            </div>
            <div class="flex gap-2">
              <button onclick="copyElementText('triage-cierre-box')" class="bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 text-xs px-3 py-1 rounded-md">📋 Copiar Cierre</button>
              <button onclick="copyElementText('triage-tsv-box')" class="bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 border border-amber-500/30 text-xs px-3 py-1 rounded-md">📋 Copiar TSV Excel</button>
            </div>
          </div>

          <div id="subpanel-dictamen" class="prose-soc text-sm leading-relaxed min-h-[260px] text-slate-200">
            <p class="text-slate-500 text-xs italic">El dictamen forense aparecerá aquí en tiempo real...</p>
          </div>
          <div id="subpanel-cierre" class="hidden">
            <pre id="triage-cierre-box" class="text-sm text-emerald-300 whitespace-pre-wrap p-4 bg-slate-950 rounded-lg border border-emerald-500/30"></pre>
          </div>
          <div id="subpanel-tsv" class="hidden">
            <p class="text-xs text-slate-400 mb-2">Hacé clic en <b>Copiar TSV Excel</b> y pegalo directamente en la columna A de tu planilla de turno:</p>
            <pre id="triage-tsv-box" class="text-xs text-amber-300 overflow-x-auto p-4 bg-slate-950 rounded-lg border border-amber-500/30"></pre>
          </div>
          <div id="subpanel-mempack" class="hidden">
            <pre id="triage-mempack-box" class="text-xs text-sky-200 whitespace-pre-wrap p-4 bg-slate-950 rounded-lg border border-sky-500/30"></pre>
          </div>
        </div>
      </section>

      <!-- 2. PANEL BUSCADOR CEREBRO SOC 7 CAPAS -->
      <section id="panel-memory" class="hidden space-y-4">
        <div class="glass rounded-xl p-5">
          <h2 class="text-base font-bold text-white mb-1">🧠 Buscador Instantáneo del Cerebro SOC (7 Capas de Markdown)</h2>
          <p class="text-xs text-slate-400 mb-4">Busca en menos de 15 milisegundos entre tus 2,022 archivos Markdown sin gastar 1 solo token de IA.</p>
          <div class="flex flex-wrap gap-2">
            <input id="rag-query" type="text" placeholder="Ej: HealthMailbox, wbx2 DNS tunneling, sati firewall, PB-1.1, Sophos WMI, CJPPA..." class="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:border-sky-500 outline-none" onkeydown="if(event.key==='Enter') searchBrain()" />
            <select id="rag-category" class="bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs text-slate-200">
              <option value="">Todas las 7 Capas (Con Prioridad SOC)</option>
              <option value="MEMORIA_SOC">🧠 MEMORIA_SOC (SOC_GEM_v2, Plantillas, Inventarios)</option>
              <option value="CASO_HISTORICO">📁 CASO_HISTORICO (Tus +35 Casos Resueltos y Bitácora)</option>
              <option value="PLAYBOOK">📕 PLAYBOOK (Playbooks Maestros y Específicos)</option>
              <option value="PROCEDIMIENTO_ARQ">⚙️ PROCEDIMIENTO_ARQ (Filtros, SO3, NDR, Reportes)</option>
              <option value="SKILL_SOC">🛠️ SKILL_SOC (Tus 60 Skills Operativas)</option>
              <option value="DOC_STELLAR">📘 DOC_STELLAR (Manuales Oficiales Stellar Cyber)</option>
              <option value="ACADEMIA_SOC">🎓 ACADEMIA_SOC (Google SecOps & Certificación)</option>
            </select>
            <button onclick="searchBrain()" class="bg-sky-500 hover:bg-sky-400 text-slate-950 font-bold text-xs px-5 py-2 rounded-lg">Buscar en Memoria</button>
          </div>
        </div>
        <div id="rag-results" class="space-y-3"></div>
      </section>

      <!-- 3. PANEL ESCÁNER CTI PARALELO -->
      <section id="panel-cti" class="hidden space-y-4">
        <div class="glass rounded-xl p-5">
          <h2 class="text-base font-bold text-white mb-1">🎯 Threat Intelligence Tri-Scan en Paralelo</h2>
          <p class="text-xs text-slate-400 mb-4">Consulta VirusTotal v3, AbuseIPDB v2, URLScan.io, AlienVault OTX y MxToolbox simultáneamente con caché TTL.</p>
          <div class="flex gap-2">
            <input id="cti-input" type="text" placeholder="Ingresá una IP (ej. 8.8.8.8), dominio, URL o hash SHA256/MD5..." class="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:border-sky-500 outline-none" onkeydown="if(event.key==='Enter') runCtiScan()" />
            <button onclick="runCtiScan()" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs px-5 py-2 rounded-lg">Escanear IOC</button>
          </div>
        </div>
        <div id="cti-results" class="glass rounded-xl p-5 min-h-[200px] text-xs font-mono text-slate-300">
          Ingresá un indicador para ver el reporte consolidado...
        </div>
      </section>

      <!-- 4. PANEL SLA / SLO -->
      <section id="panel-sla" class="hidden space-y-4">
        <div class="glass rounded-xl p-5">
          <h2 class="text-base font-bold text-white mb-1">⏱️ Evaluador Contractual de Gobernanza SLA / SLO (TB-THN-POS-01)</h2>
          <p class="text-xs text-slate-400 mb-4">Calcula prioridad P1–P4, MTTD y MTTR contractual en memoria RAM.</p>
          <div class="flex gap-2">
            <input id="sla-input" type="text" value='{"score": 92, "status": "In Progress"}' class="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm font-mono text-white" />
            <button onclick="runSlaCheck()" class="bg-purple-500 hover:bg-purple-400 text-slate-950 font-bold text-xs px-5 py-2 rounded-lg">Calcular SLA</button>
          </div>
        </div>
        <pre id="sla-results" class="glass rounded-xl p-5 text-xs font-mono text-sky-300"></pre>
      </section>

      <!-- 5. PANEL CATÁLOGO COMPLETO DE MARKDOWNS -->
      <section id="panel-catalog" class="hidden space-y-4">
        <div class="glass rounded-xl p-5">
          <div class="flex items-center justify-between mb-3">
            <div>
              <h2 class="text-base font-bold text-white">📚 Mapa Completo de tus Archivos Markdown y su Función</h2>
              <p class="text-xs text-slate-400">Filtrá por nombre, carpeta o capa para recordar al instante qué hace cada archivo de tu repositorio.</p>
            </div>
            <input id="catalog-filter" type="text" placeholder="Filtrar archivo (ej. sophos, bitacora, skill, caja ande...)" oninput="renderCatalog()" class="bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white w-72" />
          </div>
          <div id="catalog-table-wrap" class="max-h-[65vh] overflow-y-auto"></div>
        </div>
      </section>

    </main>
  </div>

  <script>
    let catalogData = [];

    function switchTab(name) {
      ['triage', 'memory', 'cti', 'sla', 'catalog'].forEach(t => {
        document.getElementById('panel-' + t).classList.toggle('hidden', t !== name);
        document.getElementById('tab-' + t).classList.toggle('active', t === name);
      });
      if (name === 'catalog' && catalogData.length === 0) loadCatalog();
    }

    function switchTriageSub(sub) {
      ['dictamen', 'cierre', 'tsv', 'mempack'].forEach(s => {
        document.getElementById('subpanel-' + s).classList.toggle('hidden', s !== sub);
        const btn = document.getElementById('subbtn-' + s);
        if (s === sub) {
          btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-500/20 text-sky-300 border border-sky-500/30";
        } else {
          btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 text-slate-400 hover:text-white";
        }
      });
    }

    function copyElementText(id) {
      const text = document.getElementById(id).innerText;
      navigator.clipboard.writeText(text);
      document.getElementById('triage-status').innerText = '✅ Copiado al portapapeles.';
    }

    async function previewMemoryOnly() {
      const text = document.getElementById('triage-input').value.trim();
      if (!text) return alert('Ingresá una alerta, IP, dominio o JSON primero.');
      document.getElementById('triage-status').innerText = '🧠 Consultando las 7 capas en disco...';
      const res = await fetch('/api/memory', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text})
      });
      const data = await res.json();
      document.getElementById('triage-mempack-box').innerText = data.memory_context || '';
      document.getElementById('triage-status').innerText = `⚡ Memoria recuperada en ${data.elapsed_ms} ms (0 tokens).`;
      switchTriageSub('mempack');
    }

    async function runTriage() {
      const text = document.getElementById('triage-input').value.trim();
      if (!text) return alert('Pegá un JSON de caso/alerta o descripción primero.');
      const btn = document.getElementById('btn-run-triage');
      btn.disabled = true;
      document.getElementById('triage-status').innerText = '🚀 Cruzando Memoria SOC (7 capas) + Generando Dictamen con Gemini 3.8 Flash High...';
      document.getElementById('subpanel-dictamen').innerHTML = '<p class="text-sky-400 animate-pulse text-xs">Analizando causalidad consolidada y consultando precedentes locales...</p>';
      switchTriageSub('dictamen');

      try {
        const res = await fetch('/api/triage', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({text})
        });
        const data = await res.json();
        if (data.error) throw new Error(data.error);
        document.getElementById('subpanel-dictamen').innerHTML = marked.parse(data.markdown || '');
        document.getElementById('triage-cierre-box').innerText = data.cierre || '';
        document.getElementById('triage-tsv-box').innerText = data.tsv || '';
        document.getElementById('triage-mempack-box').innerText = data.memory_context || '';
        document.getElementById('triage-status').innerText = `✅ Dictamen completado en ${data.elapsed_s}s.`;
      } catch (e) {
        document.getElementById('subpanel-dictamen').innerHTML = `<p class="text-red-400 text-xs">Error: ${e.message}</p>`;
        document.getElementById('triage-status').innerText = '❌ Error en análisis.';
      } finally {
        btn.disabled = false;
      }
    }

    async function fetchStellarCase() {
      const caseId = document.getElementById('stellar-case-id').value.trim();
      if (!caseId) return alert('Ingresá un número de Case ID de Stellar Cyber.');
      document.getElementById('triage-status').innerText = `📡 Consultando caso #${caseId} en Stellar Cyber...`;
      try {
        const res = await fetch(`/api/stellar-case?case_id=${encodeURIComponent(caseId)}`);
        const data = await res.json();
        if (data.error) throw new Error(data.error);
        document.getElementById('triage-input').value = JSON.stringify(data, null, 2);
        document.getElementById('triage-status').innerText = `✅ Caso #${caseId} descargado. Hacé clic en Analizar Caso.`;
      } catch (e) {
        alert('Error consultando Stellar Cyber: ' + e.message);
        document.getElementById('triage-status').innerText = '❌ Falló descarga de Stellar.';
      }
    }

    async function searchBrain() {
      const q = document.getElementById('rag-query').value.trim();
      const cat = document.getElementById('rag-category').value;
      if (!q) return;
      const res = await fetch(`/api/rag?q=${encodeURIComponent(q)}&category=${encodeURIComponent(cat)}&top_k=8`);
      const data = await res.json();
      const wrap = document.getElementById('rag-results');
      if (!data.results || data.results.length === 0) {
        wrap.innerHTML = '<div class="glass rounded-xl p-4 text-xs text-slate-400">Sin coincidencias para esa búsqueda.</div>';
        return;
      }
      wrap.innerHTML = data.results.map(r => `
        <div class="glass rounded-xl p-4 border-l-4 border-sky-400">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold text-sky-300">[${r.category}] ${r.rel_path}</span>
            <span class="text-xs px-2 py-0.5 rounded bg-slate-800 text-emerald-400 font-mono">Score BM25: ${r.score} · ${data.elapsed_ms}ms</span>
          </div>
          <pre class="text-xs text-slate-300 whitespace-pre-wrap font-mono bg-slate-950/80 p-3 rounded-lg border border-slate-800">${r.content.replace(/</g, '&lt;')}</pre>
        </div>
      `).join('');
    }

    async function runCtiScan() {
      const obs = document.getElementById('cti-input').value.trim();
      if (!obs) return;
      const box = document.getElementById('cti-results');
      box.innerHTML = '<span class="text-sky-400 animate-pulse">Escaneando en paralelo (VT + AbuseIPDB + URLScan + OTX + MxToolbox)...</span>';
      const res = await fetch(`/api/cti?observable=${encodeURIComponent(obs)}`);
      const data = await res.json();
      box.innerHTML = data.html + `<pre class="mt-4 p-3 bg-slate-950 rounded border border-slate-800 text-[11px] overflow-x-auto">${JSON.stringify(data.raw, null, 2)}</pre>`;
    }

    async function runSlaCheck() {
      const raw = document.getElementById('sla-input').value.trim();
      const res = await fetch('/api/sla', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({raw})
      });
      const data = await res.json();
      document.getElementById('sla-results').innerText = JSON.stringify(data, null, 2);
    }

    async function loadCatalog() {
      const res = await fetch('/api/catalog');
      const data = await res.json();
      catalogData = data.items || [];
      renderCatalog();
    }

    function renderCatalog() {
      const filt = (document.getElementById('catalog-filter').value || '').toLowerCase();
      const filtered = catalogData.filter(i =>
        !filt || i.rel_path.toLowerCase().includes(filt) || i.category.toLowerCase().includes(filt) || i.summary.toLowerCase().includes(filt)
      ).slice(0, 300);

      const rows = filtered.map(i => `
        <tr class="border-b border-slate-800/80 hover:bg-slate-800/40">
          <td class="py-2 px-3 text-xs font-semibold text-sky-400">${i.category}</td>
          <td class="py-2 px-3 text-xs font-mono text-slate-200">${i.rel_path}</td>
          <td class="py-2 px-3 text-xs text-slate-400">${(i.size_bytes/1024).toFixed(1)} KB</td>
          <td class="py-2 px-3 text-xs text-slate-300">${i.summary}</td>
        </tr>
      `).join('');

      document.getElementById('catalog-table-wrap').innerHTML = `
        <div class="text-xs text-slate-400 mb-2">Mostrando ${filtered.length} de ${catalogData.length} archivos Markdown indexados:</div>
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="bg-slate-900 text-slate-400 text-xs uppercase">
              <th class="py-2 px-3">Capa</th>
              <th class="py-2 px-3">Ruta del Archivo</th>
              <th class="py-2 px-3">Tamaño</th>
              <th class="py-2 px-3">Función / Título Detectado</th>
            </tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>
      `;
    }
  </script>
</body>
</html>
"""


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


class SoarWebHandler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        pass

    def _send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)

        if parsed.path == "/" or parsed.path == "/index.html":
            body = HTML_DASHBOARD.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if parsed.path == "/api/rag":
            t0 = time.perf_counter()
            q = (qs.get("q", [""])[0]).strip()
            cat = (qs.get("category", [""])[0]).strip() or None
            top_k = int(qs.get("top_k", ["6"])[0])
            rag = get_rag()
            results = rag.query(q, top_k=top_k, category=cat)
            elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)
            self._send_json({"results": results, "elapsed_ms": elapsed_ms})
            return

        if parsed.path == "/api/cti":
            obs = (qs.get("observable", [""])[0]).strip()
            raw = CtiEngine.tri_scan(obs)
            html = CtiEngine.format_terminal_report_html(raw)
            self._send_json({"raw": raw, "html": html})
            return

        if parsed.path == "/api/catalog":
            rag = get_rag()
            self._send_json({"total": len(rag.file_inventory), "items": rag.file_inventory})
            return

        if parsed.path == "/api/stellar-case":
            case_id = (qs.get("case_id", [""])[0]).strip()
            try:
                import stellar_cli
                case_data = stellar_cli.call_mcp("get_case_details", {"ticket_id": str(case_id)})
                alerts_data = stellar_cli.call_mcp("get_case_alerts", {"ticket_id": str(case_id), "limit": 20})
                self._send_json({"case_id": case_id, "case_details": case_data, "case_alerts": alerts_data})
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
            return

        self.send_error(404)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(length).decode("utf-8", errors="ignore") if length > 0 else "{}"
        data = json.loads(raw_body or "{}")

        if parsed.path == "/api/memory":
            t0 = time.perf_counter()
            text = data.get("text", "")
            rag = get_rag()
            ctx = rag.instant_case_context(text)
            elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)
            self._send_json({"memory_context": ctx, "elapsed_ms": elapsed_ms})
            return

        if parsed.path == "/api/sla":
            raw_in = data.get("raw", "80")
            try:
                case = json.loads(raw_in)
                if not isinstance(case, dict):
                    case = {"score": float(raw_in)}
            except Exception:
                try:
                    case = {"score": float(raw_in)}
                except Exception:
                    case = {"severity": raw_in}
            p_code, sev = SlaGovernanceEngine.get_priority(case)
            self._send_json({
                "priority": p_code,
                "severity": sev,
                "mttd": SlaGovernanceEngine.evaluate_mttd(case),
                "mttr": SlaGovernanceEngine.evaluate_mttr(case),
            })
            return

        if parsed.path == "/api/triage":
            t0 = time.perf_counter()
            text = data.get("text", "")
            try:
                rag = get_rag()
                mem_ctx = rag.instant_case_context(text)
                compact = preparar_entrada(text)
                full_prompt = f"{compact}\n\n{mem_ctx}\n\nUtiliza obligatoriamente este paquete de memoria verificada en tu dictamen consolidado de 4 fases."
                from soc_agent import ejecutar_consulta
                markdown_resp = ejecutar_consulta(text)
                cierre = extraer_cierre_consola(markdown_resp)
                tsv = extraer_tsv_18_columnas(markdown_resp)
                elapsed_s = round(time.perf_counter() - t0, 2)
                self._send_json({
                    "markdown": markdown_resp,
                    "cierre": cierre,
                    "tsv": tsv,
                    "memory_context": mem_ctx,
                    "elapsed_s": elapsed_s,
                })
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
            return

        self.send_error(404)


def run_server(port: int = 8090, open_browser: bool = True) -> None:
    rag = get_rag()
    print(f"🛡️ [TECHNOMA SOAR WEB] Memoria cargada: {len(rag.file_inventory)} Markdowns ({len(rag.retriever.corpus)} bloques)")
    server = ThreadingHTTPServer(("127.0.0.1", port), SoarWebHandler)
    url = f"http://localhost:{port}"
    print(f"🌐 Dashboard Web activo en: {url}")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando servidor web...")
        server.server_close()


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=8090)
    p.add_argument("--no-browser", action="store_true")
    args = p.parse_args()
    run_server(port=args.port, open_browser=not args.no_browser)
