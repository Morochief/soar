# -*- coding: utf-8 -*-
"""
Mixin Modular: Métricas Ejecutivas SOC (Tab 3), Catálogo de Playbooks (Tab 4)
y Motor Nativo Anti-Sleep 24/7.
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *


class AnalyticsPlaybooksMixin:
    # =========================================================================
    # GESTIÓN Y CÓMPUTO DE MÉTRICAS EJECUTIVAS SOC (TAB 3)
    # =========================================================================
    def _on_metrics_period_changed(self, index: int):
        """Muestra u oculta selectores de fecha personalizada y recalcula métricas."""
        is_custom = (index == 5)
        self.dt_metrics_start.setVisible(is_custom)
        self.dt_metrics_end.setVisible(is_custom)
        self.recalculate_executive_metrics()

    def trigger_extended_cases_fetch(self):
        """Dispara la obtencion bajo demanda de 200 casos para analisis historico profundo."""
        if hasattr(self, 'btn_metrics_load_extended'):
            self.btn_metrics_load_extended.setEnabled(False)
            self.btn_metrics_load_extended.setText("Cargando 200 casos...")
        if hasattr(self, 'btn_load_more_cases'):
            self.btn_load_more_cases.setEnabled(False)
            self.btn_load_more_cases.setText("Cargando...")
        self._safe_kill_worker('_worker_extended_cases')
        self._worker_extended_cases = ExtendedCasesWorker()
        self._worker_extended_cases.finished_signal.connect(self.master_signal_router)
        self._worker_extended_cases.error_signal.connect(self._on_extended_cases_error)
        self._worker_extended_cases.start()

    def _on_extended_cases_error(self, err: str):
        """Maneja errores de red al solicitar historial extendido."""
        if hasattr(self, 'btn_metrics_load_extended'):
            self.btn_metrics_load_extended.setEnabled(True)
            self.btn_metrics_load_extended.setText("Cargar Historial (200)")
        if hasattr(self, 'btn_load_more_cases'):
            self.btn_load_more_cases.setEnabled(True)
            self.btn_load_more_cases.setText("+ Historial (200)")
        self.master_error_router(err)

    def _on_extended_cases_loaded(self, raw_cases: list):
        """Integra el lote extendido de 200 casos en la cache en memoria y recalcula metricas y vistas."""
        cases_dict = {c.get("_id") or c.get("ticket_id"): c for c in getattr(self, '_extended_cases_pool', []) if (c.get("_id") or c.get("ticket_id"))}
        for c in raw_cases:
            k = c.get("_id") or c.get("ticket_id")
            if k:
                cases_dict[k] = c

        def _case_sort_key(c: dict):
            try:
                s = SlaGovernanceEngine.normalize_score(c.get("score"))
            except Exception:
                s = 0.0
            try:
                ts = int(c.get("created_at") or 0)
            except Exception:
                ts = 0
            return (s, ts)

        self._extended_cases_pool = sorted(cases_dict.values(), key=_case_sort_key, reverse=True)
        if hasattr(self, 'btn_metrics_load_extended'):
            self.btn_metrics_load_extended.setEnabled(True)
            self.btn_metrics_load_extended.setText(f"Historial Cargado ({len(self._extended_cases_pool)})")
        if hasattr(self, 'btn_load_more_cases'):
            self.btn_load_more_cases.setEnabled(True)
            self.btn_load_more_cases.setText(f"+ Historial ({len(self._extended_cases_pool)})")
        self.recalculate_executive_metrics()
        self._render_cases_view()

    def _populate_analysts_dropdown(self):
        """Llena el dropdown de analistas asegurando a Kevin Moraes y el equipo consolidado."""
        if not hasattr(self, 'combo_metrics_analyst'):
            return
        curr_data = self.combo_metrics_analyst.currentData()
        self.combo_metrics_analyst.blockSignals(True)
        self.combo_metrics_analyst.clear()
        self.combo_metrics_analyst.addItem("Kevin Moraes (kevinmoraes@technoma.com.py)", "kevinmoraes@technoma.com.py")
        self.combo_metrics_analyst.addItem("Todos / Equipo Completo SOC", "TODOS")

        seen = {"kevinmoraes@technoma.com.py", "todos"}
        for item in getattr(self, '_assignees_list', []):
            if isinstance(item, dict):
                email = str(item.get("email") or item.get("username") or item.get("id") or "").strip().lower()
                name = str(item.get("name") or email).strip()
            elif isinstance(item, str):
                email = item.strip().lower()
                name = item.strip()
            else:
                continue
            if email and email not in seen and "@" in email:
                seen.add(email)
                self.combo_metrics_analyst.addItem(f"{name} ({email})", email)

        idx = self.combo_metrics_analyst.findData(curr_data)
        if idx >= 0:
            self.combo_metrics_analyst.setCurrentIndex(idx)
        else:
            self.combo_metrics_analyst.setCurrentIndex(0)
        self.combo_metrics_analyst.blockSignals(False)

    def recalculate_executive_metrics(self):
        """Ejecuta el cómputo analítico en memoria RAM de todos los KPIs ejecutivos."""
        if not hasattr(self, 'tab3'):
            return

        # 1. Recuperar casos de memoria RAM (Cero llamadas de red)
        cases_pool = getattr(self, '_extended_cases_pool', [])
        if not cases_pool:
            cases_pool = getattr(self, '_last_raw_cases', [])
        if not cases_pool and getattr(self, 'dict_casos_activos', None):
            cases_pool = list(self.dict_casos_activos.values())

        if not cases_pool:
            self.txt_metrics_analytics.setHtml("<span style='color: #64748b;'>No hay incidentes cargados en memoria. Aguarde el primer ciclo de sincronización o presione 'Cargar Historial (200)'.</span>")
            return

        # 2. Período
        period_idx = self.combo_metrics_period.currentIndex()
        now_ms = int(time.time() * 1000)
        time_from_ms = None
        time_to_ms = None
        period_desc = "Todo el Lote en Memoria"

        if period_idx == 0:  # Turno Actual (8h)
            time_from_ms = now_ms - (8 * 3600 * 1000)
            period_desc = "Turno Actual (Últimas 8 horas)"
        elif period_idx == 1:  # Últimas 24h
            time_from_ms = now_ms - (24 * 3600 * 1000)
            period_desc = "Últimas 24 Horas"
        elif period_idx == 2:  # Últimos 7 días
            time_from_ms = now_ms - (7 * 86400 * 1000)
            period_desc = "Últimos 7 Días"
        elif period_idx == 3:  # Últimos 30 días
            time_from_ms = now_ms - (30 * 86400 * 1000)
            period_desc = "Últimos 30 Días"
        elif period_idx == 4:  # Todo el lote
            time_from_ms = None
            period_desc = f"Historial Completo en RAM ({len(cases_pool)} casos)"
        elif period_idx == 5:  # Rango personalizado
            s_dt = self.dt_metrics_start.dateTime()
            e_dt = self.dt_metrics_end.dateTime()
            time_from_ms = int(s_dt.toSecsSinceEpoch() * 1000)
            time_to_ms = int(e_dt.toSecsSinceEpoch() * 1000)
            period_desc = f"Rango: {s_dt.toString('yyyy-MM-dd HH:mm')} a {e_dt.toString('yyyy-MM-dd HH:mm')}"

        # 3. Analista y Prioridad
        analyst_val = self.combo_metrics_analyst.currentData() or "kevinmoraes@technoma.com.py"
        analyst_label = self.combo_metrics_analyst.currentText()
        priority_val = self.combo_metrics_priority.currentText()

        # 4. Cálculo en memoria
        metrics = SlaGovernanceEngine.calculate_deep_metrics(
            cases=cases_pool,
            target_analyst=analyst_val,
            time_from_ms=time_from_ms,
            time_to_ms=time_to_ms,
            priority_filter=priority_val
        )
        self._last_metrics_result = metrics

        # 5. Actualizar Tarjetas KPI Ejecutivas
        self.lbl_m_mttd_val.setText(metrics["avg_mttd_str"])
        self.lbl_m_mttr_val.setText(metrics["avg_mttr_str"])
        self.lbl_m_triage_val.setText(metrics["avg_triage_str"])
        
        sla_p = metrics["sla_compliance_pct"]
        self.lbl_m_sla_val.setText(f"{sla_p}%")
        if sla_p >= 95.0:
            self.lbl_m_sla_val.setStyleSheet("color: #10b981; font-size: 18px; font-weight: bold; border: none; font-family: 'Consolas';")
        elif sla_p >= 85.0:
            self.lbl_m_sla_val.setStyleSheet("color: #f59e0b; font-size: 18px; font-weight: bold; border: none; font-family: 'Consolas';")
        else:
            self.lbl_m_sla_val.setStyleSheet("color: #ef4444; font-size: 18px; font-weight: bold; border: none; font-family: 'Consolas';")

        self.lbl_m_cases_val.setText(str(metrics["total_cases"]))
        self.lbl_m_alerts_val.setText(str(metrics["total_alerts_mitigated"]))
        self.lbl_m_prec_val.setText(f"FP {metrics['fp_pct']}% / TP {metrics['tp_pct']}%")
        self.lbl_m_vel_val.setText(f"{metrics['velocity']} /h")

        # 6. Renderizar Paneles
        html_analytics = self._render_analytics_html(metrics, period_desc, analyst_label)
        self.txt_metrics_analytics.setHtml(html_analytics)

        md_report = self._render_markdown_report(metrics, period_desc, analyst_label)
        self.txt_metrics_markdown.setPlainText(md_report)

    def _render_analytics_html(self, m: dict, period_desc: str, analyst_label: str) -> str:
        """Genera tablas analíticas con formato corporativo de alta gama en grilla 2x2 equilibrada."""
        pm = m["priority_matrix"]
        vc = m["verdict_counts"]
        tc = m["tenant_counter"]
        rc = m["threat_counter"]

        def _row(pri, sev, color):
            row_data = pm.get(pri, {})
            c_pct = row_data.get("compliance_pct", 100.0)
            color_stat = "#10b981" if c_pct >= 95.0 else ("#f59e0b" if c_pct >= 85.0 else "#ef4444")
            return f"""
            <tr style='background-color: #090e1a;'>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; font-weight: bold; color: {color}; text-align: center;'>{pri}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; color: #cbd5e1;'>{sev}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; text-align: center; color: #f8fafc; font-weight: bold;'>{row_data.get('total', 0)}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; text-align: center; color: #10b981;'>{row_data.get('compliant', 0)}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; text-align: center; color: #ef4444;'>{row_data.get('breached', 0)}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; text-align: center; color: #38bdf8;'>{row_data.get('avg_mttd_str', 'N/A')}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; text-align: center; color: #a855f7;'>{row_data.get('avg_mttr_str', 'N/A')}</td>
                <td style='padding: 6px 8px; border: 1px solid #1e293b; text-align: center; font-weight: bold; color: {color_stat};'>{c_pct}%</td>
            </tr>
            """

        rows_pri = (
            _row("P1", "Crítica (Score >= 90)", "#ef4444") +
            _row("P2", "Alta (Score 75-89)", "#f97316") +
            _row("P3", "Media (Score 41-74)", "#eab308") +
            _row("P4", "Baja / Info (Score <= 40)", "#3b82f6")
        )

        # Filas de Veredictos
        res_tot = max(1, m["status_counts"]["resolved"])
        rows_verdict = ""
        badge_colors = {
            "False Positive": "#10b981",
            "True Positive": "#ef4444",
            "Benign": "#38bdf8",
            "Sin Veredicto": "#94a3b8",
            "Otros": "#64748b"
        }
        for v_name, v_cnt in vc.items():
            pct = round((v_cnt / res_tot) * 100.0, 1)
            b_col = badge_colors.get(v_name, "#38bdf8")
            rows_verdict += f"""
            <tr style='background-color: #090e1a;'>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; color: {b_col}; font-weight: bold;'>• {v_name}</td>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; text-align: center; color: #f8fafc; font-weight: bold;'>{v_cnt}</td>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; text-align: center; color: #94a3b8;'>{pct}%</td>
            </tr>
            """

        # Filas de Clientes / Tenants
        rows_tenants = ""
        for t_name, t_cnt in tc.most_common(5):
            rows_tenants += f"""
            <tr style='background-color: #090e1a;'>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; color: #cbd5e1;'>🏢 {t_name}</td>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; text-align: center; color: #38bdf8; font-weight: bold;'>{t_cnt}</td>
            </tr>
            """
        if not rows_tenants:
            rows_tenants = "<tr><td colspan='2' style='padding: 6px; text-align: center; color: #64748b;'>Sin datos de clientes en este período</td></tr>"

        # Filas de Amenazas
        rows_threats = ""
        for r_name, r_cnt in rc.most_common(5):
            disp_r = r_name[:38] + "..." if len(r_name) > 38 else r_name
            rows_threats += f"""
            <tr style='background-color: #090e1a;'>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; color: #cbd5e1;'>⚡ {disp_r}</td>
                <td style='padding: 5px 8px; border: 1px solid #1e293b; text-align: center; color: #ec4899; font-weight: bold;'>{r_cnt}</td>
            </tr>
            """
        if not rows_threats:
            rows_threats = "<tr><td colspan='2' style='padding: 6px; text-align: center; color: #64748b;'>Sin datos de reglas</td></tr>"

        html = f"""
        <div style="font-family: Consolas, 'Segoe UI', monospace; color: #e2e8f0; line-height: 1.35; padding: 2px;">
            <!-- CABECERA PRINCIPAL -->
            <div style="background-color: #0f172a; padding: 10px 14px; border: 1px solid #1e293b; border-left: 4px solid #38bdf8; border-radius: 6px; margin-bottom: 12px;">
                <div style="font-size: 13px; font-weight: bold; color: #38bdf8; letter-spacing: 0.5px;">📊 AUDITORÍA ANALÍTICA DE RENDIMIENTO & GOBERNANZA SLA</div>
                <div style="font-size: 11px; color: #94a3b8; margin-top: 4px;">
                    <b>Operador:</b> <span style="color: #f8fafc;">{analyst_label}</span>
                    &nbsp;|&nbsp; <b>Período:</b> <span style="color: #f8fafc;">{period_desc}</span>
                    &nbsp;|&nbsp; <b>Muestra Auditada:</b> <span style="color: #38bdf8; font-weight: bold;">{m['total_cases']} casos</span>
                </div>
            </div>

            <!-- SECCIÓN 1: MATRIZ DE CUMPLIMIENTO SLA A ANCHO COMPLETO -->
            <div style="background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px; margin-bottom: 12px;">
                <div style="font-size: 11px; font-weight: bold; color: #a855f7; margin-bottom: 6px;">1. MATRIZ DE CUMPLIMIENTO SLA POR SEVERIDAD</div>
                <table style="width: 100%; border-collapse: collapse; font-size: 11px;">
                    <thead>
                        <tr style="background-color: #1e293b; color: #38bdf8;">
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 8%;">PRI</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: left; width: 28%;">SEVERIDAD</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 10%;">CASOS</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 10%;">EN SLA</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 10%;">BREACH</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 11%;">MTTD PROM</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 11%;">MTTR PROM</th>
                            <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 12%;">% CUMPL.</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows_pri}
                    </tbody>
                </table>
            </div>

            <!-- SECCIÓN 2 & 3: GRID INFERIOR EQUILIBRADA DE 2 COLUMNAS (50% / 50%) -->
            <table style="width: 100%; border-collapse: separate; border-spacing: 10px 0; margin-left: -10px; margin-right: -10px;">
                <tr>
                    <!-- COLUMNA IZQUIERDA: CALIDAD DE TRIAJE & CLIENTES IMPACTADOS -->
                    <td style="width: 50%; vertical-align: top;">
                        <!-- 2. CALIDAD DE TRIAJE -->
                        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px; margin-bottom: 12px;">
                            <div style="font-size: 11px; font-weight: bold; color: #06b6d4; margin-bottom: 6px;">2. CALIDAD DE TRIAJE & DISTRIBUCIÓN DE VEREDICTOS</div>
                            <table style="width: 100%; border-collapse: collapse; font-size: 11px;">
                                <thead>
                                    <tr style="background-color: #1e293b; color: #06b6d4;">
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: left; width: 55%;">DICTAMEN / VEREDICTO</th>
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 22%;">TOTAL</th>
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 23%;">% RESUELTO</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {rows_verdict}
                                </tbody>
                            </table>
                        </div>

                        <!-- 3. TOP CLIENTES -->
                        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px;">
                            <div style="font-size: 11px; font-weight: bold; color: #10b981; margin-bottom: 6px;">3. TOP 5 CLIENTES (TENANTS) IMPACTADOS</div>
                            <table style="width: 100%; border-collapse: collapse; font-size: 11px;">
                                <thead>
                                    <tr style="background-color: #1e293b; color: #10b981;">
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: left; width: 75%;">TENANT / CLIENTE</th>
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 25%;">CASOS</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {rows_tenants}
                                </tbody>
                            </table>
                        </div>
                    </td>

                    <!-- COLUMNA DERECHA: REGLAS DE AMENAZA DISPARADAS & NOTA DE CONFORMIDAD -->
                    <td style="width: 50%; vertical-align: top;">
                        <!-- 4. TOP REGLAS -->
                        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px; margin-bottom: 12px;">
                            <div style="font-size: 11px; font-weight: bold; color: #ec4899; margin-bottom: 6px;">4. TOP 5 REGLAS / INCIDENTES DISPARADOS</div>
                            <table style="width: 100%; border-collapse: collapse; font-size: 11px;">
                                <thead>
                                    <tr style="background-color: #1e293b; color: #ec4899;">
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: left; width: 75%;">VECTOR / REGLA DE DETECCIÓN</th>
                                        <th style="padding: 6px 8px; border: 1px solid #334155; text-align: center; width: 25%;">EVENTOS</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {rows_threats}
                                </tbody>
                            </table>
                        </div>

                        <!-- 5. DICTAMEN DE CONFORMIDAD NORMATIVA -->
                        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px; padding: 10px;">
                            <div style="font-size: 11px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;">5. DICTAMEN DE CONFORMIDAD OPERATIVA (SOC/NOC)</div>
                            <div style="background-color: #090e1a; border: 1px solid #1e293b; padding: 8px 10px; border-radius: 4px; font-size: 11px; color: #cbd5e1; line-height: 1.4;">
                                • <b>Estado Contractual:</b> <span style="color: #10b981; font-weight: bold;">CONFORME / DENTRO DE SLA</span><br>
                                • <b>Tiempo de Acuse (MTTD):</b> Auditado bajo estándar POE (< 20m P1 / < 2h P2).<br>
                                • <b>Resolución Técnica (MTTR):</b> Calibrado para soporte 24/7 sin violaciones críticas.<br>
                                • <b>Marco Regulatorio:</b> NIST SP 800-61 Rev.3 / ISO 27001 / SOC 2 Type II.
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
        </div>
        """
        return html

    def _render_markdown_report(self, m: dict, period_desc: str, analyst_label: str) -> str:
        """Construye un informe ejecutivo formal en formato Markdown para auditorías C-Level."""
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pm = m["priority_matrix"]
        vc = m["verdict_counts"]
        tc = m["tenant_counter"]
        rc = m["threat_counter"]

        sla_p = m["sla_compliance_pct"]
        badge_sla = "✅ CUMPLIDO" if sla_p >= 95.0 else ("⚠️ EN OBSERVACIÓN" if sla_p >= 85.0 else "❌ INCUMPLIDO")

        lines = [
            f"# 🛡️ INFORME EJECUTIVO DE RENDIMIENTO SOC Y GOBERNANZA SLA",
            f"**Plataforma:** STELLAR CYBER OpenXDR Command Center",
            f"**Operador Responsable:** {analyst_label}",
            f"**Fecha de Emisión:** {now_str}",
            f"**Período Auditado:** {period_desc}",
            f"**Casos Auditados:** {m['total_cases']}",
            "",
            "---",
            "",
            "## 1. RESUMEN EJECUTIVO DE INDICADORES CLAVE (KPIS)",
            "| Métrica Operativa | Valor Registrado | Meta Contractual / POE | Estado SLA |",
            "| :--- | :---: | :---: | :---: |",
            f"| **MTTD Promedio** (Tiempo Detección/Acuse) | **{m['avg_mttd_str']}** | < 20m (P1) / < 2h (P2) | Informativo |",
            f"| **MTTR Promedio** (Tiempo Resolución) | **{m['avg_mttr_str']}** | < 1h (P1) / < 4h (P2) | Informativo |",
            f"| **Duración Triaje L1** | **{m['avg_triage_str']}** | <= 15 min (POE) | POE Controlado |",
            f"| **Cumplimiento Global SLA** | **{sla_p}%** | >= 95.0% | **{badge_sla}** |",
            f"| **Total Casos Auditados** | **{m['total_cases']}** | - | Volumen Auditado |",
            f"| **Alertas Interflow Mitigadas** | **{m['total_alerts_mitigated']}** | - | Volumen Mitigado |",
            f"| **Precisión Triaje (FP / TP)** | **FP {m['fp_pct']}% / TP {m['tp_pct']}%** | Calidad SOC | Calibrado |",
            f"| **Velocidad de Procesamiento** | **{m['velocity']} casos/h** | - | Operativo Continuo |",
            "",
            "---",
            "",
            "## 2. MATRIZ DE GOBERNANZA SLA POR SEVERIDAD",
            "| Prioridad | Severidad | Casos | En SLA | Breached | MTTD Prom. | MTTR Prom. | % Cumplimiento |",
            "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |"
        ]

        for pri, sev in [("P1", "Crítica"), ("P2", "Alta"), ("P3", "Media"), ("P4", "Baja / Info")]:
            p_data = pm.get(pri, {})
            lines.append(
                f"| **{pri}** | {sev} | {p_data.get('total', 0)} | {p_data.get('compliant', 0)} | "
                f"{p_data.get('breached', 0)} | {p_data.get('avg_mttd_str', 'N/A')} | "
                f"{p_data.get('avg_mttr_str', 'N/A')} | **{p_data.get('compliance_pct', 100.0)}%** |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 3. CALIDAD OPERATIVA & DISTRIBUCIÓN DE VEREDICTOS",
            "| Dictamen / Veredicto | Total Casos | % del Total Resuelto |",
            "| :--- | :---: | :---: |"
        ])
        res_tot = max(1, m["status_counts"]["resolved"])
        for v_name, v_cnt in vc.items():
            pct = round((v_cnt / res_tot) * 100.0, 1)
            lines.append(f"| **{v_name}** | {v_cnt} | {pct}% |")

        lines.extend([
            "",
            "---",
            "",
            "## 4. IMPACTO MULTI-TENANT (TOP 5 CLIENTES)",
            "| Tenant / Cliente | Total Casos Asignados |",
            "| :--- | :---: |"
        ])
        for t_name, t_cnt in tc.most_common(5):
            lines.append(f"| {t_name} | {t_cnt} |")

        lines.extend([
            "",
            "---",
            "",
            "## 5. TOP REGLAS Y VECTORES DE AMENAZA IDENTIFICADOS",
            "| Vector de Detección / Incidente | Ocurrencias en Muestra |",
            "| :--- | :---: |"
        ])
        for r_name, r_cnt in rc.most_common(5):
            lines.append(f"| {r_name} | {r_cnt} |")

        lines.extend([
            "",
            "---",
            "*Reporte de auditoría generado automáticamente bajo estándares SOCaaS ISO/IEC 27001 & SOC 2.*"
        ])

        return "\n".join(lines)

    def export_metrics_markdown_action(self):
        """Permite guardar el reporte Markdown actual en un archivo local .md."""
        md_text = self.txt_metrics_markdown.toPlainText().strip()
        if not md_text or "Presione 'Recalcular'" in md_text:
            QMessageBox.warning(self, "Exportación Markdown", "No hay un reporte generado para exportar. Presione 'Recalcular' primero.")
            return

        ts_now = datetime.now().strftime("%Y%m%d_%H%M%S")
        sug_filename = f"Reporte_Metricas_SOC_KevinMoraes_{ts_now}.md"

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Reporte Ejecutivo de Métricas SOC",
            sug_filename,
            "Archivos Markdown (*.md);;Archivos de Texto (*.txt);;Todos los Archivos (*.*)"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(md_text)
                QMessageBox.information(self, "Exportación Exitosa", f"El informe ejecutivo ha sido exportado exitosamente a:\n\n{file_path}")
            except Exception as ex:
                QMessageBox.critical(self, "Error de Exportación", f"No se pudo guardar el archivo:\n{str(ex)}")

    def copy_metrics_markdown_action(self):
        """Copia el informe Markdown completo al Clipboard de Windows."""
        md_text = self.txt_metrics_markdown.toPlainText().strip()
        if not md_text or "Presione 'Recalcular'" in md_text:
            QMessageBox.warning(self, "Copiar Markdown", "No hay un reporte generado para copiar. Presione 'Recalcular' primero.")
            return

        clipboard = QApplication.clipboard()
        clipboard.setText(md_text)

        orig_text = self.btn_metrics_copy_md.text()
        self.btn_metrics_copy_md.setText("✅ ¡Copiado a RAM!")
        self.btn_metrics_copy_md.setStyleSheet("background-color: #065f46; color: #10b981; border: 1px solid #10b981; padding: 5px 12px; font-weight: bold;")
        QTimer.singleShot(2500, lambda: self._restore_copy_button(orig_text))

    def _restore_copy_button(self, orig_text: str):
        if hasattr(self, 'btn_metrics_copy_md'):
            self.btn_metrics_copy_md.setText(orig_text)
            self.btn_metrics_copy_md.setStyleSheet("background-color: #1e293b; color: #38bdf8; border: 1px solid #334155; padding: 5px 12px;")

    # =========================================================================
    # CONTROLADOR DE PLAYBOOKS Y REMEDIACIÓN HITL (HUMAN-IN-THE-LOOP)
    # =========================================================================
    def on_playbook_combo_changed(self, index: int):
        """Muestra el playbook seleccionado en el visor HTML."""
        if not hasattr(self, '_all_playbooks') or not self._all_playbooks:
            return
        pb_id = self.combo_playbooks.currentData()
        pb = PlaybookEngine.get_playbook_by_id(pb_id)
        if pb:
            self.txt_pb_html.setHtml(PlaybookEngine.format_playbook_html(pb))

    def trigger_recommend_active_ticket(self):
        """Recomienda el playbook óptimo para el ticket ingresado en la cola SOAR."""
        case_id, t_id = self._get_target_case_id()
        case_obj = self.dict_casos_activos.get(str(t_id), {}) if t_id else {}
        telemetry = self.txt_triage.toPlainText() if hasattr(self, 'txt_triage') else ""

        recommended = PlaybookEngine.recommend_playbook(case_obj, telemetry)
        if recommended:
            # Seleccionar en el combo
            for i in range(self.combo_playbooks.count()):
                if self.combo_playbooks.itemData(i) == recommended.get("id"):
                    self.combo_playbooks.setCurrentIndex(i)
                    break
            self.txt_pb_html.setHtml(PlaybookEngine.format_playbook_html(recommended, case_obj))
            
            # Autocompletar borrador de bitácora
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c_name = case_obj.get("name", "Incidente Activo")
            tenant = case_obj.get("tenant_name", "Cliente")
            draft = (
                f"=== BITÁCORA DE APLICACIÓN DE PLAYBOOK ===\n"
                f"• Fecha/Hora (UTC-3): {now_str}\n"
                f"• Ticket SOAR: #{t_id} | Caso: {c_name} | Tenant: {tenant}\n"
                f"• Playbook Seleccionado: [{recommended.get('priority')}] {recommended.get('title')}\n"
                f"• Marco Normativo: NIST SP 800-61 Rev.3 / MITRE {recommended.get('mitre')}\n"
                f"• Analista Responsable: {EMAIL_USUARIO}\n"
                f"--------------------------------------------------\n"
                f"[ACCIONES DE INVESTIGACIÓN & CONTENCIÓN TOMADAS]\n"
                f"[ ] Identificación de observables confirmada.\n"
                f"[ ] Reputación de IPs/Hashes validada en fuentes de CTI.\n"
                f"[ ] Aislamiento de activo / Bloqueo perimetral evaluado.\n"
                f"• Notas de Observación:\n"
            )
            self.txt_pb_evidence_notes.setPlainText(draft)
            QMessageBox.information(
                self,
                "Recomendación Adaptativa SOC",
                f"🎯 Playbook Detectado para Ticket #{t_id}:\n\n"
                f"[{recommended.get('priority')}] {recommended.get('title')}\n"
                f"MITRE: {recommended.get('mitre')}\n\n"
                f"El procedimiento y la plantilla de bitácora han sido cargados exitosamente."
            )
        else:
            QMessageBox.warning(self, "Playbook", "No se encontró coincidencia automática. Seleccione uno de la lista.")

    def trigger_quick_playbook_action(self):
        """Disparado desde el botón '📖 Playbook Sugerido' en la pestaña principal de Triaje."""
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            QMessageBox.warning(self, "Playbook Sugerido", "Ingrese o seleccione un Ticket ID activo primero.")
            return

        case_obj = self.dict_casos_activos.get(str(t_id), {})
        telemetry = self.txt_triage.toPlainText()
        recommended = PlaybookEngine.recommend_playbook(case_obj, telemetry)

        if recommended:
            # Cambiar a la pestaña de Playbooks
            self.tabs.setCurrentIndex(3)
            # Seleccionar el playbook correspondiente
            for i in range(self.combo_playbooks.count()):
                if self.combo_playbooks.itemData(i) == recommended.get("id"):
                    self.combo_playbooks.setCurrentIndex(i)
                    break
            self.trigger_recommend_active_ticket()

    def trigger_apply_playbook_hitl(self):
        """
        Ejecución Human-in-the-Loop:
        Requiere confirmación expresa del operador antes de vincular el procedimiento
        y las evidencias al campo de Nota de Resolución del caso activo.
        """
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            QMessageBox.warning(self, "Human-in-the-Loop", "Debe tener un caso activo seleccionado en el Cockpit.")
            return

        pb_id = self.combo_playbooks.currentData()
        pb = PlaybookEngine.get_playbook_by_id(pb_id)
        if not pb:
            return

        notes_content = self.txt_pb_evidence_notes.toPlainText().strip()
        if not notes_content:
            notes_content = f"Playbook aplicado: [{pb.get('priority')}] {pb.get('title')} (MITRE: {pb.get('mitre')}). Procedimiento de triaje y contención validado por analista."

        # Diálogo de confirmación HITL (Seguridad Operativa Nivel 1%)
        confirm = QMessageBox.question(
            self,
            "🛡️ AUTORIZACIÓN OPERATIVA (HUMAN-IN-THE-LOOP)",
            f"¿Confirma la aplicación formal del Playbook al Ticket #{t_id}?\n\n"
            f"• Playbook: [{pb.get('priority')}] {pb.get('title')}\n"
            f"• Operador: {EMAIL_USUARIO}\n\n"
            f"Esta acción inyectará la bitácora técnica de cumplimiento en el campo de justificación "
            f"del caso para su posterior resolución con trazabilidad contractual.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )

        if confirm == QMessageBox.Yes:
            # Trasladar el resumen al campo de notas de triaje de Tab 1
            summary_note = f"[{pb.get('id')} - {pb.get('title')}] {notes_content}"
            self.input_case_comment.setText(summary_note[:300]) # Límite sano para el input
            
            # Copiar también al clipboard para pegar en el portal web o ticket externo
            clipboard = QApplication.clipboard()
            clipboard.setText(notes_content)
            
            # Regresar al operador a la pestaña de triaje con todo listo
            self.tabs.setCurrentIndex(0)
            self.txt_triage.append(
                f"\n{'='*75}\n"
                f"[🛡️ HITL AUTORIZADO]: Playbook '{pb.get('title')}' aplicado por {EMAIL_USUARIO}.\n"
                f"La justificación técnica fue cargada en el campo 'Nota' y copiada al portapapeles.\n"
                f"{'='*75}\n"
            )
            QMessageBox.information(
                self,
                "Playbook Aplicado con Éxito",
                f"✅ El procedimiento ha sido autorizado e inyectado en el Ticket #{t_id}.\n\n"
                f"El texto completo de la bitácora ha sido copiado a su portapapeles (RAM)."
            )

    def copy_current_playbook_text(self):
        """Copia el texto plano del playbook actual al portapapeles."""
        pb_id = self.combo_playbooks.currentData()
        pb = PlaybookEngine.get_playbook_by_id(pb_id)
        if pb:
            plain_text = f"PLAYBOOK SOC: {pb.get('title')}\nPRIORIDAD: {pb.get('priority')} | MITRE: {pb.get('mitre')}\n\nOBJETIVO:\n{pb.get('objective')}\n\nPROCEDIMIENTO:\n" + "\n".join(pb.get("paragraphs", []))
            clipboard = QApplication.clipboard()
            clipboard.setText(plain_text)
            QMessageBox.information(self, "Copiado", "Guía del playbook copiada al portapapeles.")

    # =========================================================================
    # GESTION NATIVA DE ANTI-SLEEP (WINDOWS API SETTHREADEXECUTIONSTATE)
    # =========================================================================
    def _init_antisleep(self):
        """Inicializa la prevencion continua de suspension de pantalla y sistema."""
        try:
            self._antisleep_active = True
            self._apply_thread_execution_state(prevent=True)
            if hasattr(self, '_timer_antisleep'):
                self._timer_antisleep.start(60000)
            log_to_file("[ANTI-SLEEP] Prevencion nativa de suspension activada (heartbeat 60s).")
        except Exception as e:
            log_to_file(f"[ANTI-SLEEP ERROR] Fallo al inicializar SetThreadExecutionState: {e}")

    def _refresh_antisleep(self):
        """Pulso periodico para asegurar que directivas del SO no suspendan el display."""
        if getattr(self, '_antisleep_active', False):
            self._apply_thread_execution_state(prevent=True)

    def _apply_thread_execution_state(self, prevent: bool):
        """Invoca kernel32.SetThreadExecutionState de Windows de manera no bloqueante."""
        try:
            if hasattr(ctypes, 'windll') and hasattr(ctypes.windll, 'kernel32'):
                if prevent:
                    ctypes.windll.kernel32.SetThreadExecutionState(
                        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
                    )
                else:
                    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
        except Exception as e:
            log_to_file(f"[ANTI-SLEEP ERROR] Error en SetThreadExecutionState: {e}")

    def _restore_system_sleep(self):
        """Restaura las directivas normales de suspension del sistema operativo."""
        try:
            if hasattr(self, '_timer_antisleep') and self._timer_antisleep.isActive():
                self._timer_antisleep.stop()
            self._apply_thread_execution_state(prevent=False)
            self._antisleep_active = False
            log_to_file("[ANTI-SLEEP] Politicas normales de suspension restauradas.")
        except Exception as e:
            log_to_file(f"[ANTI-SLEEP ERROR] Fallo al restaurar suspension: {e}")

    def toggle_antisleep(self, force_state: Optional[bool] = None):
        """Conmuta o fuerza el estado de Anti-Sleep y sincroniza la interfaz grafica."""
        if force_state is not None:
            self._antisleep_active = force_state
        else:
            self._antisleep_active = not getattr(self, '_antisleep_active', False)

        if self._antisleep_active:
            self._apply_thread_execution_state(prevent=True)
            if hasattr(self, '_timer_antisleep') and not self._timer_antisleep.isActive():
                self._timer_antisleep.start(60000)
            if hasattr(self, 'btn_term_antisleep'):
                self.btn_term_antisleep.setText("[Anti-Sleep: ACTIVO]")
                self.btn_term_antisleep.setStyleSheet(
                    "background-color: #064e3b; color: #34d399; font-weight: bold; border: 1px solid #059669; padding: 4px 10px; border-radius: 4px; font-family: 'Consolas'; font-size: 11px;"
                )
            log_to_file("[ANTI-SLEEP] Estado conmutado a ACTIVO.")
        else:
            self._apply_thread_execution_state(prevent=False)
            if hasattr(self, '_timer_antisleep') and self._timer_antisleep.isActive():
                self._timer_antisleep.stop()
            if hasattr(self, 'btn_term_antisleep'):
                self.btn_term_antisleep.setText("[Anti-Sleep: PAUSADO]")
                self.btn_term_antisleep.setStyleSheet(
                    "background-color: #1e293b; color: #94a3b8; font-weight: bold; border: 1px solid #334155; padding: 4px 10px; border-radius: 4px; font-family: 'Consolas'; font-size: 11px;"
                )
            log_to_file("[ANTI-SLEEP] Estado conmutado a PAUSADO.")

