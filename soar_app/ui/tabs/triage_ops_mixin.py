# -*- coding: utf-8 -*-
"""
Mixin Modular: Operaciones de Triaje, Cola SOAR, Auto-Remediadores,
Notificaciones Móviles, Salud de Sensores y Playbook 6.3 (Gobernanza de Ingesta).
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *
from soar_app.workers.auto_remediators import *
from collections import Counter


class TriageOpsMixin:
    # -----------------------------------------------------------------------------
    def _update_soar_menu_label(self):
        """Actualiza el texto y estilo del boton desplegable con la cantidad de motores SOAR activos."""
        total = 5
        active = sum([
            bool(getattr(self, 'action_soar_guardia', None) and self.action_soar_guardia.isChecked()),
            bool(getattr(self, 'action_soar_hm', None) and self.action_soar_hm.isChecked()),
            bool(getattr(self, 'action_soar_translate', None) and self.action_soar_translate.isChecked()),
            bool(getattr(self, 'action_soar_sati', None) and self.action_soar_sati.isChecked()),
            bool(getattr(self, 'action_soar_dpapi', None) and self.action_soar_dpapi.isChecked())
        ])
        if hasattr(self, 'btn_soar_menu'):
            if active == total:
                self.btn_soar_menu.setText(f"SOAR: {active}/{total} Activos \u25be")
                self.btn_soar_menu.setStyleSheet("""
                    QToolButton {
                        background-color: #0f172a;
                        color: #38bdf8;
                        border: 1px solid #0284c7;
                        border-radius: 4px;
                        padding: 4px 10px;
                        font-family: 'Consolas';
                        font-size: 11px;
                        font-weight: bold;
                    }
                    QToolButton:hover {
                        background-color: #1e293b;
                        border-color: #38bdf8;
                    }
                """)
            elif active > 0:
                self.btn_soar_menu.setText(f"SOAR: {active}/{total} Activos \u25be")
                self.btn_soar_menu.setStyleSheet("""
                    QToolButton {
                        background-color: #1e1b4b;
                        color: #fbbf24;
                        border: 1px solid #d97706;
                        border-radius: 4px;
                        padding: 4px 10px;
                        font-family: 'Consolas';
                        font-size: 11px;
                        font-weight: bold;
                    }
                    QToolButton:hover {
                        background-color: #312e81;
                        border-color: #f59e0b;
                    }
                """)
            else:
                self.btn_soar_menu.setText(f"SOAR: 0/{total} Inactivo \u25be")
                self.btn_soar_menu.setStyleSheet("""
                    QToolButton {
                        background-color: #1c1917;
                        color: #ef4444;
                        border: 1px solid #b91c1c;
                        border-radius: 4px;
                        padding: 4px 10px;
                        font-family: 'Consolas';
                        font-size: 11px;
                        font-weight: bold;
                    }
                    QToolButton:hover {
                        background-color: #292524;
                        border-color: #dc2626;
                    }
                """)

    def _update_triage_countdown_tick(self):
        """Actualiza cada segundo la barra de estado de SLA/SLO y el POE de Triaje L1 (15 min)."""
        if not self.triage_poe_deadline:
            return
            
        now = int(time.time() * 1000)
        poe_remaining_ms = self.triage_poe_deadline - now
        sla_remaining_ms = self.triage_sla_deadline - now
        
        ticket_str = f"Ticket {self.triage_active_ticket}" if self.triage_active_ticket else "Caso Activo"
        poe_time_str = SlaGovernanceEngine.format_duration(poe_remaining_ms)
        sla_time_str = SlaGovernanceEngine.format_duration(sla_remaining_ms)
        
        if poe_remaining_ms > 0:
            if poe_remaining_ms <= 3 * 60 * 1000:  # Últimos 3 minutos de triaje
                color = "#f59e0b"
                bg = "#451a03"
                if not self._poe_warning_sounded:
                    ejecutar_beep(600, 300)
                    self._poe_warning_sounded = True
                if not getattr(self, '_mobile_poe_warning_sent', False) and hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
                    self._mobile_poe_warning_sent = True
                    MobileAlertsNotifier.send_notification(
                        title=f"[TRIAJE POE EN RIESGO] {ticket_str}",
                        message=f"Atención: Quedan solo {poe_time_str} para concluir el Triaje L1 del {ticket_str} ({self.triage_priority}).",
                        priority="high",
                        tags="warning,hourglass"
                    )
                status_text = f"  ⚠️ [{self.triage_priority}] {ticket_str} | ⏳ POE TRIAJE L1 RESTANTE: {poe_time_str} | 🎯 SLA MTTR: {sla_time_str} restante"
            else:
                color = "#10b981"
                bg = "#064e3b"
                status_text = f"  🟢 [{self.triage_priority}] {ticket_str} | ⏱️ POE TRIAJE L1 EN CURSO: {poe_time_str} | 🎯 SLA MTTR: {sla_time_str} restante"
        else:
            color = "#ef4444"
            bg = "#450a0a"
            status_text = f"  🔴 [{self.triage_priority}] {ticket_str} | ❌ POE TRIAJE L1 EXPIRADO (+{poe_time_str}) | 🎯 SLA MTTR: {sla_time_str}"
            if not self._poe_breach_sounded:
                ejecutar_beep(400, 600)
                self._poe_breach_sounded = True
                self.enviar_notificacion_popup(
                    "⚠️ EXCESO DE TIEMPO DE TRIAJE L1 (POE 15 MIN)",
                    f"El tiempo operativo de Triaje L1 (15 min) para el Ticket {self.triage_active_ticket} ha expirado.\nProceda a generar reporte y escalar/cerrar el caso inmediatamente."
                )
            if not getattr(self, '_mobile_poe_breach_sent', False) and hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
                self._mobile_poe_breach_sent = True
                MobileAlertsNotifier.send_notification(
                    title=f"[TRIAJE POE EXPIRADO] {ticket_str}",
                    message=f"El tiempo de Triaje L1 para el {ticket_str} ha expirado (+{poe_time_str}). Procede al cierre o escalamiento urgente.",
                    priority="urgent",
                    tags="warning,alarm_clock"
                )

        self.lbl_triage_sla_status.setStyleSheet(
            f"color: {color}; background-color: {bg}; padding: 6px 10px; border-radius: 4px; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: 1px solid {color};"
        )
        self.lbl_triage_sla_status.setText(status_text)

    def view_comments_action(self):
        t_id = self.input_case_ticket.text().strip()
        if not t_id:
            QMessageBox.warning(self, "Error", "Debe ingresar el ID del caso.")
            return
            
        case_uuid, clean_id = self._get_target_case_id()
        if not case_uuid:
            case_uuid = t_id.lstrip("#").strip()
            
        worker = GetCommentsWorker(params={"case_id": case_uuid})
        worker.signals.finished_signal.connect(self.master_signal_router)
        worker.signals.error_signal.connect(self.master_error_router)
        QThreadPool.globalInstance().start(worker)

    def _get_target_case_id(self):
        t_id = self.input_case_ticket.text().strip()
        if not t_id:
            return None, None
        clean_id = t_id.lstrip("#")
        for key in (t_id, clean_id):
            if key in self.dict_casos_activos:
                return self.dict_casos_activos[key].get("_id"), key

        # Revisar en el pool extendido en memoria si ya fue descargado
        for c in getattr(self, '_extended_cases_pool', []):
            cid = str(c.get("ticket_id", "")).strip().lstrip("#")
            if cid == clean_id:
                self.dict_casos_activos[clean_id] = c
                self.dict_casos_activos[t_id] = c
                return c.get("_id"), clean_id

        # Búsqueda On-Demand directa a la API de Stellar Cyber para tickets históricos (ej. casos antiguos)
        try:
            manager = RestSessionManager()
            headers = manager.get_headers()
            lookup_url = f"https://{HOST}/connect/api/v1/cases?ticket_id={clean_id}"
            r = manager.session.get(lookup_url, headers=headers, verify=True, timeout=12)
            if r.status_code == 200:
                cases = (r.json().get("data", {}) or {}).get("cases", [])
                if cases:
                    c = cases[0]
                    self.dict_casos_activos[clean_id] = c
                    self.dict_casos_activos[t_id] = c
                    return c.get("_id"), clean_id
        except Exception as e:
            log_to_file(f"[ON-DEMAND CASE LOOKUP ERROR] Ticket {clean_id}: {e}")

        return None, None

    # Workers que NO deben destruirse: son persistentes y se reutilizan cada ciclo
    PERSISTENT_WORKERS = {'worker_health', 'worker_cases'}

    def _safe_kill_worker(self, attr_name: str) -> bool:
        """
        Destruye el worker anterior de forma síncrona y segura.
        Workers persistentes solo se cancelan cooperativamente — nunca se destruyen.
        Workers efímeros se desconectan y destruyen con deleteLater.
        """
        worker = getattr(self, attr_name, None)
        if worker is None:
            return True

        if attr_name in self.PERSISTENT_WORKERS:
            # Solo cancelar, nunca destruir: el objeto se reutiliza
            if worker.isRunning():
                worker._is_killed = True
                worker.quit()
                worker.wait(2000)
            return True

        # Workers efímeros: manejar QThread y QRunnable de forma polimórfica
        if hasattr(worker, '_is_killed'):
            worker._is_killed = True  # Cancelación cooperativa (funciona para QThread y QRunnable)

        if isinstance(worker, QThread) and worker.isRunning():
            worker.quit()
            if not worker.wait(2000):
                worker.terminate()
                worker.wait(500)

        # Desconexión polimórfica: QThread usa señales directas, QRunnable las tiene en worker.signals
        signal_sources = [worker]
        if hasattr(worker, 'signals'):
            signal_sources.append(worker.signals)
        for source in signal_sources:
            for signal_name in ('finished_signal', 'error_signal', 'analysis_finished', 'analysis_failed'):
                sig = getattr(source, signal_name, None)
                if sig is not None:
                    try:
                        sig.disconnect()
                    except RuntimeError:
                        pass

        if hasattr(worker, 'deleteLater'):
            worker.deleteLater()
        setattr(self, attr_name, None)
        return True

    def trigger_top_apps_refresh(self):
        """Refresco ultra-ligero en memoria para no saturar la API."""
        if hasattr(self, '_last_cases_data'):
            self.display_cases_results_wrapper()

    def trigger_health_refresh(self):
        """Reutiliza el worker persistente. Ignora el tick si aún está procesando."""
        if self.worker_health.isRunning():
            return
        self.worker_health.start()

    def trigger_cases_refresh(self):
        """Reutiliza el worker persistente. Ignora el tick si aún está procesando."""
        if self.worker_cases.isRunning():
            if hasattr(self, 'btn_manual_refresh'):
                self.btn_manual_refresh.setText("Actualizando...")
            return
        if hasattr(self, 'btn_manual_refresh'):
            self.btn_manual_refresh.setText("Cargando...")
            self.btn_manual_refresh.setEnabled(False)
        self.worker_cases.start()


    # -----------------------------------------------------------------------------
    # CONTROLADORES DE ACCIONES TÁCTICAS INTERACTIVAS SOAR (SISTEMA CACHÉ INYECTADO)
    # -----------------------------------------------------------------------------
    def launch_triage_action(self):
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            self.txt_triage.setText("[!] Error: Ingrese un Ticket ID activo de la cola superior.")
            return
        
        # Actualizar banner de SLA en tiempo real con datos en memoria del caso
        case_obj = self.dict_casos_activos.get(str(t_id), {})
        mttd_info = SlaGovernanceEngine.evaluate_mttd(case_obj)
        mttr_info = SlaGovernanceEngine.evaluate_mttr(case_obj)
        priority = mttd_info["priority"]
        st = str(case_obj.get("status", "New")).strip()

        if mttr_info["breached"]:
            color = "#ef4444"
            bg = "#450a0a"
            sla_text = f"  🔴 [{priority}] Ticket {t_id} ({st}) | ❌ MTTR VENCIDO ({mttr_info['remaining_str']} | Total: {mttr_info['elapsed_str']}) | Límite SLA: {mttr_info['limit_str']}"
        elif mttr_info["warning"]:
            color = "#f59e0b"
            bg = "#451a03"
            sla_text = f"  ⚠️ [{priority}] Ticket {t_id} ({st}) | ⏳ MTTR EN RIESGO: {mttr_info['remaining_str']} restante | Límite SLA: {mttr_info['limit_str']}"
        else:
            color = "#38bdf8"
            bg = "#0c4a6e"
            sla_text = f"  ℹ️ [{priority}] Ticket {t_id} ({st}) | ⏱️ SLA MTTR Restante: {mttr_info['remaining_str']} | Límite SLA: {mttr_info['limit_str']}"

        self.lbl_triage_sla_status.setStyleSheet(
            f"color: {color}; background-color: {bg}; padding: 6px 10px; border-radius: 4px; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: 1px solid {color};"
        )
        self.lbl_triage_sla_status.setText(sla_text)
        
        if t_id in self.cache_triage:
            self.txt_triage.clear()
            self.txt_triage.append(self.cache_triage[t_id])
            self.txt_triage.append(f"\n{'-'*75}\n[+] MEMORIA SOAR: Datos recuperados instantáneamente desde el caché RAM.")
            return

        
        self._safe_kill_worker('worker_triage')
            
        self.txt_triage.setText(f"[*] Fase 1: Extrayendo Metadatos y evidencias de observables para Ticket {t_id}...")
        self.worker_triage = TriageWorker(params={"case_id": case_id})
        self.worker_triage.signals.finished_signal.connect(self.master_signal_router)
        self.worker_triage.signals.error_signal.connect(self.master_error_router)
        QThreadPool.globalInstance().start(self.worker_triage)

    def trigger_ai_normal(self):
        self.launch_ai_analysis(force_refresh=False)

    def trigger_ai_forced(self):
        self.launch_ai_analysis(force_refresh=True)

    def trigger_ueba_profiling(self):
        entity = self.input_ueba.text().strip()
        if not entity:
            self.txt_ueba.setText("[!] Por favor ingrese una entidad (Usuario, IP o Hostname).")
            return
            
        self.btn_ueba_search.setEnabled(False)
        self.txt_ueba.setHtml(f"<br><span style='color: #fbbf24;'>Recolectando telemetría histórica de {entity} en Stellar Cyber...</span>")
        
        self._safe_kill_worker('_worker_ueba')
        self._worker_ueba = EntityProfileWorker(params={"entity": entity})
        self._worker_ueba.signals.finished_signal.connect(self.master_signal_router)
        self._worker_ueba.signals.error_signal.connect(lambda e: self.display_ueba_profile(f"Error: {e}"))
        QThreadPool.globalInstance().start(self._worker_ueba)

    def trigger_stellar_autotriage(self):
        """Obtiene el resumen de IA nativo de Stellar Cyber para el ticket activo."""
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            self.txt_triage.setText("[!] Error: Ingrese un Ticket ID activo para usar la IA de Stellar.")
            return
        self.txt_triage.setText(f"[*] Consultando motor AutoTriage de Stellar Cyber para Ticket {t_id}...")
        self._safe_kill_worker('worker_stellar_autotriage')
        self.worker_stellar_autotriage = AutoTriageStellarWorker(params={"case_id": case_id})
        self.worker_stellar_autotriage.signals.finished_signal.connect(self.master_signal_router)
        self.worker_stellar_autotriage.signals.error_signal.connect(self.master_error_router)
        QThreadPool.globalInstance().start(self.worker_stellar_autotriage)

    def _load_assignees_on_startup(self):
        """Carga la lista de analistas desde la API una vez al iniciar el Cockpit."""
        self._worker_assignees = AssigneesWorker()
        self._worker_assignees.signals.finished_signal.connect(self.master_signal_router)
        self._worker_assignees.signals.error_signal.connect(lambda e: None)
        QThreadPool.globalInstance().start(self._worker_assignees)


    def launch_ai_analysis(self, force_refresh=False, target_t_id=None):
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            self.txt_triage.setText("[!] Error: Ingrese un Ticket ID activo para auditar con IA.")
            return
            
        if target_t_id and t_id != target_t_id:
            # El ticket cambió en la GUI durante el lapso de delay, abortamos análisis de IA cruzado
            return
        
        if force_refresh and t_id in self.cache_ai:
            del self.cache_ai[t_id]
            log_to_file(f"[AI CACHE BYPASS] Forzando re-consulta asíncrona para Ticket {t_id}. Caché RAM purgado.")
        
        if not force_refresh and t_id in self.cache_ai:
            self.txt_triage.clear()
            self.txt_triage.append(self.cache_ai[t_id])
            self.txt_triage.append(f"\n{'-'*75}\n[AI PERSISTENCIA]: Reporte forense cargado desde la memoria local (0 tokens consumidos).")
            return
        
        contenido_actual = self.txt_triage.toPlainText().strip()
        if not contenido_actual or "[*]" in contenido_actual or "=========================" not in contenido_actual:
            self.txt_triage.setText(f"[*] Extrayendo datos base de telemetria previos para pasarselos a la IA...")
            self.pending_ai_after_triage = True
            self.launch_triage_action()
            return
            
        self.txt_triage.setText(f"[AI] Conectando en vivo con Gemini 3.8 Flash (Antigravity OAuth) + Cerebro RAG...\n")
        
        contenido_sanitizado = sanitizar_interflow(contenido_actual)
        log_to_file(f"[AI LAUNCH] Contenido original: {len(contenido_actual)} chars. Sanitizado: {len(contenido_sanitizado)} chars.")
        
        if hasattr(self, 'worker_ai') and self.worker_ai.isRunning(): return
        self._safe_kill_worker('worker_ai')
        
        self._ai_stream_started = False
        self.worker_ai = AiAnalysisWorker(contenido_sanitizado)
        self.worker_ai.analysis_status.connect(self.slot_ai_status)
        self.worker_ai.analysis_chunk.connect(self.slot_ai_chunk)
        self.worker_ai.analysis_finished.connect(self.display_ai_results)
        self.worker_ai.analysis_failed.connect(self.slot_ai_failed)
        self.worker_ai.start()

    @Slot(str)
    def slot_ai_status(self, status_msg):
        self.txt_triage.append(status_msg)

    @Slot(str)
    def slot_ai_chunk(self, chunk_text):
        if not getattr(self, '_ai_stream_started', False):
            self._ai_stream_started = True
            self.txt_triage.clear()
        cursor = self.txt_triage.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(chunk_text)
        self.txt_triage.setTextCursor(cursor)
        self.txt_triage.ensureCursorVisible()

    @Slot(str)
    def slot_ai_failed(self, error_msg):
        self.txt_triage.append(f"\n[AI CRITICAL ERROR]: {error_msg}")
        ejecutar_beep(400, 500)

    def take_case_action(self):
        if hasattr(self, 'worker_take') and self.worker_take.isRunning(): return
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            self.txt_triage.setText("[!] Error: Ingrese un Ticket ID válido de la cola superior para tomarlo.")
            return
        
        self._safe_kill_worker('worker_take')
            
        case_obj = self.dict_casos_activos.get(str(t_id), {})
        mttd_info = SlaGovernanceEngine.evaluate_mttd(case_obj)
        mttr_info = SlaGovernanceEngine.evaluate_mttr(case_obj)
        priority = mttd_info["priority"]
        
        # Iniciar temporizador de cuenta regresiva POE de 15 min de Triaje L1
        _, _, triage_limit_ms = SlaGovernanceEngine.get_sla_limits(priority)
        now_ms = int(time.time() * 1000)
        self.triage_active_case_id = case_id
        self.triage_active_ticket = t_id
        self.triage_priority = priority
        self.triage_poe_deadline = now_ms + triage_limit_ms
        self.triage_sla_deadline = now_ms + mttr_info["remaining_ms"]
        self._poe_warning_sounded = False
        self._poe_breach_sounded = False
        self._mobile_poe_warning_sent = False
        self._mobile_poe_breach_sent = False
        self.timer_triage_countdown.start()
        self._update_triage_countdown_tick()
        
        self.txt_triage.append(f"\n[*] Solicitando comando PUT de asignación para Ticket {t_id} a operador {EMAIL_USUARIO}...")
        
        # Auditoría visual y acústica del acuse MTTD
        if mttd_info["breached"]:
            ejecutar_beep(400, 600)
            self.txt_triage.append(
                f"[!] ALERTA CRÍTICA SLA: Acuse fuera de tiempo (SLO MTTD VIOLADO)\n"
                f"    Prioridad: {priority} ({mttd_info['severity_label']}) | Límite SLO: {mttd_info['limit_str']} | Demora: {mttd_info['elapsed_str']}\n"
                f"    Tiempo excedido: {mttd_info['remaining_str']}"
            )
            self.enviar_notificacion_popup(
                "⚠️ ALERTA: BRECHA DE SLO MTTD",
                f"Ticket {t_id} ({priority}): Acuse realizado en {mttd_info['elapsed_str']}.\n"
                f"Límite contractual SLO: {mttd_info['limit_str']}.\n"
                f"Proceda inmediatamente con el triaje rápido y RFA."
            )
        else:
            ejecutar_beep(900, 250)
            self.txt_triage.append(
                f"[+] SLO MTTD CUMPLIDO: Acuse registrado exitosamente en {mttd_info['elapsed_str']}.\n"
                f"    Prioridad: {priority} ({mttd_info['severity_label']}) | Margen restante: {mttd_info['remaining_str']}\n"
                f"    Iniciando protocolo de triaje rápido L1 (15 minutos)."
            )

        payload = {"assignee": EMAIL_USUARIO}
        self.worker_take = UpdateCaseWorker(payload=payload, params={"case_id": case_id})
        self.worker_take.finished_signal.connect(self.master_signal_router)
        self.worker_take.error_signal.connect(self.master_error_router)
        self.worker_take.start()

        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(t_id) not in self._mobile_notified_assigned:
                self._mobile_notified_assigned.add(str(t_id))
            MobileAlertsNotifier.send_notification(
                title=f"[CASO TOMADO/ASIGNADO] #{t_id} ({priority})",
                message=f"Has tomado el caso #{t_id}. Triaje L1 en curso.\nMTTR restante: {mttr_info['remaining_str']} de {mttr_info['limit_str']}.",
                priority="high",
                tags="briefcase,bell"
            )

    def _populate_reassign_menu(self):
        """Llena dinámicamente el menú de reasignación con los analistas del equipo SOC."""
        if not hasattr(self, 'menu_reassign'):
            return
        self.menu_reassign.clear()

        # Miembros oficiales del equipo Technoma SOC
        team_members = [
            ("Ángel Insaurralde", "angelinsaurralde@technoma.com.py"),
            ("Armando Saucedo", "armandosaucedo@technoma.com.py"),
            ("Guillermo Cabañas", "guillermocabanas@technoma.com.py"),
            ("Hermes Sánchez", "hermessanchez@technoma.com.py"),
            ("Igor Mayor", "igormayor@technoma.com.py"),
            ("Iván Centurión", "ivancenturion@technoma.com.py"),
            ("José Durand", "josedurand@technoma.com.py"),
            ("Kevin Moraes", "kevinmoraes@technoma.com.py"),
            ("SOC General", "soc@technoma.com.py"),
        ]

        seen_emails = {email.lower() for _, email in team_members}

        # Analistas adicionales provenientes de la API si no están en la lista estática
        extra_members = []
        for item in getattr(self, '_assignees_list', []):
            if isinstance(item, dict):
                email = str(item.get("email") or item.get("username") or item.get("id") or "").strip().lower()
                name = str(item.get("name") or email).strip()
            elif isinstance(item, str):
                email = item.strip().lower()
                name = item.strip()
            else:
                continue
            if email and email not in seen_emails and "@" in email and email != "todos":
                seen_emails.add(email)
                extra_members.append((name, email))

        # Acciones para cada analista
        for name, email in team_members + extra_members:
            icon_tag = "👤" if email != "soc@technoma.com.py" else "🏢"
            act = self.menu_reassign.addAction(f"{icon_tag} {name}")
            act.setToolTip(email)
            act.triggered.connect(lambda checked=False, e=email, n=name: self.reassign_case_action(e, n))

        self.menu_reassign.addSeparator()

        # Opción para liberar / quitar asignación
        act_unassign = self.menu_reassign.addAction("🔓 Liberar Caso (Sin Asignar)")
        act_unassign.setToolTip("Quita la asignación actual del caso dejándolo libre en la cola")
        act_unassign.triggered.connect(lambda checked=False: self.reassign_case_action("", "Sin Asignar"))

    def reassign_case_action(self, target_email: str, target_name: str):
        """Ejecuta la reasignación de un caso hacia otro compañero del equipo o lo libera."""
        if hasattr(self, 'worker_take') and self.worker_take.isRunning():
            return
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            self.txt_triage.setText("[!] Error: Ingrese un Ticket ID válido de la cola superior para reasignarlo.")
            ejecutar_beep(400, 300)
            return

        self._safe_kill_worker('worker_take')

        target_display = target_name if target_email else "Sin Asignar (Liberado)"
        email_display = f"({target_email})" if target_email else "(Cola General)"

        self.txt_triage.append(
            f"\n[*] Solicitando PUT de reasignación para Ticket #{t_id} a: {target_display} {email_display}..."
        )

        payload = {"assignee": target_email}
        self.worker_take = UpdateCaseWorker(payload=payload, params={"case_id": case_id})
        self.worker_take.finished_signal.connect(self.master_signal_router)
        self.worker_take.error_signal.connect(self.master_error_router)
        self.worker_take.start()

        ejecutar_beep(800, 150)

        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            MobileAlertsNotifier.send_notification(
                title=f"[CASO REASIGNADO] #{t_id}",
                message=f"El caso #{t_id} fue reasignado a {target_display}.",
                priority="normal",
                tags="bust_in_silhouette,arrows_counterclockwise"
            )

    def extract_interflow_action(self):
        case_id, t_id = self._get_target_case_id()
        if not case_id: return
        limit_input = self.input_case_limit.text().strip()
        limit_val = int(limit_input) if limit_input.isdigit() else 15
        cache_key = f"{t_id}_{limit_val}"
        
        if cache_key in self.cache_interflow:
            self.txt_triage.clear()
            self.txt_triage.append(self.cache_interflow[cache_key])
            self.txt_triage.append(f"\n{'-'*75}\n[+] MEMORIA SOAR: Logs de Interflow recuperados desde el caché RAM.")
            return

        if hasattr(self, 'worker_interflow') and self.worker_interflow.isRunning(): return
        
        self._safe_kill_worker('worker_interflow')
            
        self.txt_triage.setText(f"[*] Fase 2: Interrogando sub-indice crudo. Descargando {limit_val} JSONs de Interflow...")
        self.worker_interflow = InterflowWorker(payload={"limit": str(limit_val), "skip": "0"}, params={"case_id": case_id})
        self.worker_interflow.finished_signal.connect(self.master_signal_router)
        self.worker_interflow.error_signal.connect(self.master_error_router)
        self.worker_interflow.start()

    def copy_triage_pane_text(self):
        texto_crudo = self.txt_triage.toPlainText().strip()
        if not texto_crudo: return
        try:
            QApplication.clipboard().setText(texto_crudo)
            self.txt_triage.append(f"\n{'-'*75}\n[+] NOTA: El bloque visible superior fue copiado exitosamente al Clipboard (RAM).")
        except Exception:
            self.txt_triage.append(f"\n{'-'*75}\n[!] AVISO: No se pudo acceder al portapapeles (bloqueado por otra app). Intente de nuevo.")

    def download_triage_pane_text(self):
        texto_crudo = self.txt_triage.toPlainText().strip()
        if not texto_crudo: 
            return
        
        # Default filename based on ticket ID if available
        default_name = "reporte.md"
        t_id = self.input_case_ticket.text().strip()
        if t_id:
            case_name = ""
            try:
                logs_text = self.txt_cases.toPlainText()
                for line in logs_text.split('\n'):
                    if line.startswith(f"  {t_id}") and "|" in line:
                        parts = line.split("|")
                        if len(parts) >= 5:
                            raw_name = parts[4].strip()
                            clean_name = re.sub(r'\[.*?\]', '', raw_name)
                            clean_name = re.sub(r'[^\w\s-]', '', clean_name).strip()
                            case_name = re.sub(r'\s+', '_', clean_name)
                            break
                        elif len(parts) >= 4:
                            raw_name = parts[3].strip()
                            case_name = re.sub(r'[\\/*?:"<>|]', "", raw_name).replace(" ", "_")
                            break
            except Exception as e:
                pass
            
            if case_name:
                default_name = f"{t_id}_{case_name}.md"
            else:
                default_name = f"{t_id}.md"
            
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar reporte como Markdown",
            default_name,
            "Archivos Markdown (*.md);;Todos los archivos (*.*)"
        )
        
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(texto_crudo)
                self.txt_triage.append(f"\n{'-'*75}\n[+] NOTA: Reporte guardado exitosamente en:\n{file_path}")
            except Exception as e:
                self.txt_triage.append(f"\n{'-'*75}\n[!] ERROR guardando archivo:\n{str(e)}")

    def show_obfuscated_json_action(self):
        contenido_actual = self.txt_triage.toPlainText().strip()
        if not contenido_actual or "[*]" in contenido_actual or " AUDITORÍA" in contenido_actual:
            self.txt_triage.setText("[!] Error: No hay telemetría base cargada en pantalla. Presione primero 'Ver Triage/Obs' o 'Ver Interflow' antes de auditar.")
            return
        try:
            import re
            # Extraer bloques JSON de la pantalla
            json_blocks = re.findall(r'(\{(?:[^{}]|(?:\{[^{}]*\}))*\})', contenido_actual, re.DOTALL)
            if not json_blocks:
                try:
                    json.loads(contenido_actual)
                    json_blocks = [contenido_actual]
                except json.JSONDecodeError:
                    self.txt_triage.setText("[!] Error: La estructura en pantalla no contiene bloques JSON válidos para anonimizar.")
                    return
            
            demo_engine = SecurityMaskingEngine()
            
            # Inicializar buffer visual limpio de auditoría
            sb_ui = []
            sb_ui.append("=========================================================================")
            sb_ui.append("    AUDITORÍA DE PRIVACIDAD EN CURSO - PROTOCOLO DE EXCLUSIÓN PERIMETRAL")
            sb_ui.append("   Demostración de anonimización para la jefatura del SOC Technoma.")
            sb_ui.append("   Este es el payload exacto que recibirá el núcleo externo de Gemini.")
            sb_ui.append("=========================================================================\n")
            
            for block in json_blocks:
                try:
                    obj = json.loads(block)
                    podado = clean_forensic_data(obj)
                    if podado:
                        # Aplicar el nuevo motor robusto por Regex
                        anonimizado = demo_engine.procesar_diccionario(podado)
                        sb_ui.append(json.dumps(anonimizado, indent=4, ensure_ascii=False))
                        sb_ui.append("\n" + "-"*75 + "\n")
                except json.JSONDecodeError:
                    continue
                    
            sb_ui.append("[+] AUDITORÍA FINALIZADA EXITOSAMENTE: Toda IP, Usuario, Dominio, Hostname y Descripción textual real ha sido removida de la memoria intermedia.")
            
            # REEMPLAZAR TODO EL TEXTO DE LA PANTALLA CON LA DATA ANONIMIZADA REAL
            self.txt_triage.setPlainText("\n".join(sb_ui))
            
        except Exception as e:
            self.txt_triage.setText(f"[!] Error crítico en el motor de simulación de ofuscación: {str(e)}")

    @Slot(str)
    def validar_justificacion(self, text):
        """Habilita el botón de resolver solo si hay texto real en la nota de justificación."""
        self.btn_resolve.setEnabled(bool(text.strip()))

    def resolve_case_action(self):
        if hasattr(self, 'worker_resolve') and self.worker_resolve.isRunning(): return
        case_id, t_id = self._get_target_case_id()
        if not case_id:
            self.txt_triage.append("\n[!] Error: Seleccione un Ticket ID válido para resolver.")
            return
        
        self._safe_kill_worker('worker_resolve')
            
        veredicto_seleccionado = self.combo_verdict.currentText()
        comment_text = self.input_case_comment.text().strip()
        
        case_obj = self.dict_casos_activos.get(str(t_id), {})
        mttr_info = SlaGovernanceEngine.evaluate_mttr(case_obj)
        priority = mttr_info["priority"]
        dictamen_sla = "VIOLADO" if mttr_info["breached"] else "CUMPLIDO"

        # Detener temporizador de triaje si corresponde a este ticket
        if str(self.triage_active_ticket) == str(t_id):
            self.timer_triage_countdown.stop()
            self.lbl_triage_sla_status.setText(f"  🟢 TICKET {t_id} RESUELTO | Dictamen SLA MTTR: {dictamen_sla} ({mttr_info['elapsed_str']} de {mttr_info['limit_str']})")
            self.lbl_triage_sla_status.setStyleSheet("color: #10b981; background-color: #064e3b; padding: 6px 10px; border-radius: 4px; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: 1px solid #10b981;")

        self.txt_triage.append(f"\n[*] Enviando orden de cierre definitivo para Ticket {t_id} con veredicto: {veredicto_seleccionado}...")
        self.txt_triage.append(f"[AUDITORÍA SLA] MTTR Total: {mttr_info['elapsed_str']} (Límite {mttr_info['limit_str']}) -> Dictamen: {dictamen_sla}")
        
        payload = {
            "status": "Resolved",
            "resolution": veredicto_seleccionado
        }
        
        params = {
            "case_id": case_id,
            "comment": comment_text if comment_text else None
        }
        
        # Actualizar de inmediato el estado en la memoria local para reflejarlo instantáneamente en la GUI
        if str(t_id) in self.dict_casos_activos:
            self.dict_casos_activos[str(t_id)]["status"] = "Resolved"
            self.dict_casos_activos[str(t_id)]["resolution"] = veredicto_seleccionado
            if hasattr(self, '_last_cases_data'):
                # Actualizar el pool en memoria
                for c in self._last_cases_data.get("cases", {}).get("data", {}).get("cases", []):
                    if str(c.get("ticket_id")) == str(t_id) or str(c.get("_id")) == str(case_id):
                        c["status"] = "Resolved"
                        c["resolution"] = veredicto_seleccionado
                        break
            self.display_cases_results_wrapper()

        self.worker_resolve = UpdateCaseWorker(payload=payload, params=params)
        self.worker_resolve.finished_signal.connect(self.master_signal_router)
        self.worker_resolve.error_signal.connect(self.master_error_router)
        self.worker_resolve.start()

        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(t_id) not in self._mobile_notified_auto_closed:
                self._mobile_notified_auto_closed.add(str(t_id))
            MobileAlertsNotifier.send_notification(
                title=f"[CASO RESUELTO] #{t_id} ({veredicto_seleccionado})",
                message=f"El caso #{t_id} ha sido resuelto y cerrado exitosamente.\nDictamen SLA: {dictamen_sla} (MTTR: {mttr_info['elapsed_str']}).",
                priority="default",
                tags="white_check_mark,clipboard"
            )
        
        if mttr_info["breached"]:
            ejecutar_beep(400, 600)
            self.enviar_notificacion_popup(
                "⚠️ ALERTA: CIERRE CON BRECHA DE SLA MTTR",
                f"El Ticket {t_id} ({priority}) ha sido cerrado pero excedió el límite SLA de MTTR.\n"
                f"MTTR: {mttr_info['elapsed_str']} (Límite: {mttr_info['limit_str']}).\n"
                f"La auditoría formal quedó registrada en las notas del caso."
            )
        else:
            ejecutar_beep(1000, 250)

        if t_id in self.cache_triage: del self.cache_triage[t_id]
        if t_id in self.cache_ai: del self.cache_ai[t_id]
        self.input_case_comment.clear()

    # -----------------------------------------------------------------------------
    # ROUTER ASINCRÓNICA CENTRALIZADO DE SEÑALES (MÓDULOS INTERNOS DE LA CLASE)
    # -----------------------------------------------------------------------------
    @Slot(str)
    def display_ai_results(self, text_output):
        t_id = self.input_case_ticket.text().strip()
        if not getattr(self, '_ai_stream_started', False):
            self.txt_triage.clear()
            self.txt_triage.append(text_output)
        
        if t_id:
            self.cache_ai[t_id] = text_output
            
        self.txt_triage.append(f"\n{'-'*75}\n[AI] EXITOSO: El reporte forense completo ha sido generado. Use 'Copiar Pantalla' para exportar.")

    @Slot(str)
    def master_error_router(self, error_msg):
        log_to_file(f"[SOAR API ERROR] {error_msg}")
        if hasattr(self, 'btn_manual_refresh'):
            self.btn_manual_refresh.setText("Refrescar Cola")
            self.btn_manual_refresh.setEnabled(True)

        # Si el error es un ReadTimeout o conexión de fondo en polling automático (Casos o Salud),
        # NO interrumpir al operador con pitidos ni ensuciar la ventana activa de triaje.
        es_timeout_fondo = any(k in error_msg for k in ["Read timed out", "timeout=12", "timeout=20", "timeout=25", "data_sensors", "storage-usages"])
        if es_timeout_fondo:
            if hasattr(self, 'btn_manual_refresh'):
                self.btn_manual_refresh.setText("Cola (Reconectando...)")
            if hasattr(self, 'lbl_api_health'):
                self.lbl_api_health.setText("🟡 RECONECTANDO API...")
                self.lbl_api_health.setStyleSheet("color: #f59e0b; font-size: 11px; font-weight: bold; padding: 2px 8px; background-color: #451a03; border-radius: 4px; border: 1px solid #f59e0b; font-family: 'Consolas';")
            return

        self.txt_triage.append(f"\n{'-'*75}\n[!] ERROR DE CONEXIÓN CON API (SOAR):\n{error_msg}\n[!] Sugerencia: Verifique su conexión de red, VPN o si '{HOST}' responde a ping.")
        ejecutar_beep(400, 500)

    @Slot(dict)
    def master_signal_router(self, result):
        action = result.get("action")
        t_id = self.input_case_ticket.text().strip()
        
        if action == "get_comments":
            comments_res = result.get("comments", {})
            comments_list = comments_res.get("data", comments_res) if isinstance(comments_res, dict) else comments_res
            if not comments_list or not isinstance(comments_list, list):
                QMessageBox.information(self, "Comentarios", "No hay comentarios registrados en este caso.")
                return
            formatted = []
            for c in comments_list:
                author = c.get("user", "Desconocido")
                text = c.get("comment", "")
                
                # Stellar Cyber devuelve created_at como un timestamp (ej: 1684534... milisegundos o segundos)
                raw_ts = c.get("created_at")
                if raw_ts:
                    # Si es muy grande asumimos que son milisegundos
                    ts_val = float(raw_ts)
                    if ts_val > 9999999999: 
                        ts_val /= 1000.0
                    from datetime import datetime
                    ts = datetime.fromtimestamp(ts_val).strftime("%Y-%m-%d %H:%M")
                else:
                    ts = "Sin fecha"
                    
                formatted.append(f"[{ts}] {author}:\n{text}\n")
            from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton
            
            dialog = QDialog(self)
            dialog.setWindowTitle(f"Comentarios del Caso {t_id}")
            dialog.resize(700, 500)
            layout = QVBoxLayout(dialog)
            
            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setPlainText("\n---\n".join(formatted))
            # Ajustar fuente para mayor legibilidad
            font = text_edit.font()
            font.setPointSize(10)
            text_edit.setFont(font)
            
            layout.addWidget(text_edit)
            
            btn_close = QPushButton("Cerrar")
            btn_close.clicked.connect(dialog.accept)
            layout.addWidget(btn_close)
            
            dialog.exec()
            return

        if action == "triage":
            self.txt_triage.clear()
            details_raw = result.get("details_text") or "{}"
            sb = []
            
            # Stellar Cyber 7.0.0s (AELDEV-66747): Métricas y SLAs Nativos
            try:
                dt_obj = json.loads(details_raw)
                metrics = dt_obj.get("data", {}).get("details", {}).get("metrics") or dt_obj.get("metrics") or {}
                if metrics and isinstance(metrics, dict):
                    sb.append("=========================================================================")
                    sb.append("  [STELLAR CYBER 7.0.0s] MÉTRICAS Y TIEMPOS OPERATIVOS (SLA NATIVO)")
                    sb.append("=========================================================================")
                    for m_id, m_val in metrics.items():
                        if isinstance(m_val, dict):
                            m_name = m_val.get("name", m_id)
                            elapsed_sec = round(m_val.get("elapsed_ms", 0) / 1000.0, 1)
                            elapsed_min = round(elapsed_sec / 60.0, 1)
                            m_state = m_val.get("state", "N/A").upper()
                            sb.append(f"  * {m_name:<28}: {elapsed_sec:>6}s ({elapsed_min:>4} min)  [ESTADO: {m_state}]")
                    sb.append("=========================================================================\n")
            except Exception:
                pass

            sb.append("=========================================================================")
            sb.append("  [FASE 1] RAW JSON - DETALLES E INSPECCIÓN ESTRUCTURAL DEL CASO")
            sb.append("=========================================================================\n")
            sb.append(details_raw)
            sb.append("\n=========================================================================")
            sb.append("  [FASE 1] RAW JSON - MATRIZ DE EVIDENCIAS DE OBSERVABLES INDEXADOS")
            sb.append("=========================================================================\n")
            sb.append(result.get("observables_text") or "{}")
            
            full_text = "\n".join(sb)
            self.txt_triage.append(full_text)
            if t_id:
                self.cache_triage[t_id] = full_text
                
            # Relanzamiento automático de IA si estaba pendiente
            if self.pending_ai_after_triage:
                self.pending_ai_after_triage = False
                ticket_snapshot = t_id
                QTimer.singleShot(100, lambda t=ticket_snapshot: self.launch_ai_analysis(force_refresh=False, target_t_id=t))
            
        elif action == "interflow":
            self.txt_triage.clear()
            alerts_text = result.get("alerts_text") or "[]"
            sb = []
            
            # Stellar Cyber 7.0.0s (AELDEV-72713): Payload Imprimible en Alertas IDS
            try:
                alt_obj = json.loads(alerts_text)
                alerts_list = alt_obj if isinstance(alt_obj, list) else alt_obj.get("data", {}).get("alerts", [])
                ids_payloads = []
                for idx, alt in enumerate(alerts_list, 1):
                    src = alt.get("_source", {}) if isinstance(alt, dict) else {}
                    p_print = src.get("ids", {}).get("payload_details", {}).get("payload_printable")
                    if p_print:
                        ev_name = src.get("xdr_event", {}).get("display_name") or src.get("event_name", f"Alerta #{idx}")
                        ids_payloads.append((idx, ev_name, p_print))
                if ids_payloads:
                    sb.append("=========================================================================")
                    sb.append("  [STELLAR CYBER 7.0.0s] PAYLOADS IMPRIMIBLES DE ALERTAS IDS DETECTADOS")
                    sb.append("=========================================================================")
                    for idx, ev_name, p_print in ids_payloads:
                        sb.append(f"  [Alerta #{idx}] {ev_name}:")
                        preview = p_print if len(p_print) <= 500 else p_print[:500] + "... [TRUNCADO]"
                        sb.append(f"  {preview}\n")
                    sb.append("=========================================================================\n")
            except Exception:
                pass

            sb.append("=========================================================================")
            sb.append("  [FASE 2] RAW JSON - LOTE COMPLETO DE ALERTAS NATIVAS DE INTERFLOW")
            sb.append("=========================================================================\n")
            sb.append(alerts_text)
            
            full_text = "\n".join(sb)
            self.txt_triage.append(full_text)
            
            limit_input = self.input_case_limit.text().strip()
            limit_val = int(limit_input) if limit_input.isdigit() else 15
            cache_key = f"{t_id}_{limit_val}"
            if t_id:
                self.cache_interflow[cache_key] = full_text

        elif action == "update":
            if result.get("status") == 200:
                self.txt_triage.append("\n[+] REPORTE: Caso e historial de notas impactados con exito en el backend.")
                QTimer.singleShot(200, self.trigger_cases_refresh)  # Evita reentrada en lifecycle del worker persistente
            else:
                self.txt_triage.append("\n[!] ERROR: El perimetro del Gateway rechazo la orden PUT.")

        elif action == "entity_profile":
            if not result.get("found", False):
                self.txt_ueba.setHtml(f"<br><span style='color: #ef4444;'>{result.get('results_text', '')}</span>")
                self.btn_ueba_search.setEnabled(True)
                return
            
            # Mostrar la telemetría en bruto primero
            self.txt_ueba.setPlainText(result.get("results_text"))
            
            # Cambiar botón para análisis IA
            self.btn_ueba_search.setText("Analizar Telemetría con IA (Gemini)")
            self.btn_ueba_search.setStyleSheet("background-color: #10b981; font-weight: bold; color: white;")
            try:
                self.btn_ueba_search.clicked.disconnect()
            except Exception:
                pass
            
            # Hacemos closure seguro con partial o lambda
            entity = result.get("entity")
            payload = result.get("results_text")
            self.btn_ueba_search.clicked.connect(lambda e=entity, p=payload: self.launch_ueba_gemini(e, p))
            self.btn_ueba_search.setEnabled(True)

        elif action == "stellar_autotriage":
            self.txt_triage.clear()
            summary = result.get("summary_text") or "{}"
            self.txt_triage.append("=" * 75)
            self.txt_triage.append("  [AUTOTRIAGE STELLAR CYBER] RESUMEN GENERADO POR IA NATIVA")
            self.txt_triage.append("=" * 75 + "\n")
            self.txt_triage.append(summary)
            self.txt_triage.append(f"\n{'-'*75}\n[+] IA Stellar: Analisis completado. Compare con el reporte Gemini para doble validacion.")

        elif action == "extended_cases":
            cases_payload = result.get("cases", {})
            raw_cases = []
            if cases_payload and "data" in cases_payload and "cases" in cases_payload["data"]:
                raw_cases = cases_payload["data"]["cases"]
            self._on_extended_cases_loaded(raw_cases)

        elif action == "assignees_loaded":
            try:
                raw = result.get("assignees_raw", [])
                if isinstance(raw, list):
                    self._assignees_list = raw
                elif isinstance(raw, dict):
                    self._assignees_list = raw.get("data", raw.get("assignees", []))
                else:
                    self._assignees_list = []
            except Exception:
                self._assignees_list = []
            self._populate_analysts_dropdown()
            self._populate_reassign_menu()

        elif action == "top_apps":
            self.display_top_protocols(result.get("top_apps", []))

    def launch_ueba_gemini(self, entity: str, payload: str):
        self.btn_ueba_search.setEnabled(False)
        self.txt_ueba.setHtml("<br><span style='color: #38bdf8;'>Analizando comportamiento anómalo (UEBA) con Gemini + RAG...</span>")
        
        self._safe_kill_worker('_worker_gemini_ueba')
        
        class UebaGeminiWorker(QRunnable):
            class Signals(QObject):
                finished = Signal(str)
                error = Signal(str)
            def __init__(self, e, p):
                super().__init__()
                self.entity = e
                self.payload = p
                self.signals = self.Signals()
            def run(self):
                try:
                    import os
                    # Instantiate orchestrator correctly
                    api_key = os.environ.get("GEMINI_API_KEY")
                    orchestrator = StellarGeminiOrchestrator(api_key=api_key)
                    
                    # Prepend UEBA specific instruction to the telemetry payload
                    custom_payload = (
                        f"INSTRUCCIÓN ESPECÍFICA PARA ESTE ANÁLISIS:\n"
                        f"Genera un perfil de riesgo conductual (UEBA) exhaustivo para la entidad '{self.entity}' "
                        f"determinando si es un Insider Threat o si está comprometida.\n\n"
                        f"TELEMETRÍA CRUDA:\n{self.payload}"
                    )
                    
                    resp = orchestrator.enviar_a_gemini(custom_payload)
                    self.signals.finished.emit(resp)
                except Exception as ex:
                    self.signals.error.emit(str(ex))
        
        self._worker_gemini_ueba = UebaGeminiWorker(entity, payload)
        self._worker_gemini_ueba.signals.finished.connect(self.display_ueba_profile)
        self._worker_gemini_ueba.signals.error.connect(lambda err: self.display_ueba_profile(f"Error de Gemini: {err}"))
        QThreadPool.globalInstance().start(self._worker_gemini_ueba)

    @Slot(str)
    def display_ueba_profile(self, response: str):
        self.btn_ueba_search.setEnabled(True)
        self.btn_ueba_search.setText("🔍 Generar Perfil de Riesgo")
        self.btn_ueba_search.setStyleSheet("background-color: #7e22ce; font-weight: bold;")
        try:
            self.btn_ueba_search.clicked.disconnect()
        except Exception:
            pass
        self.btn_ueba_search.clicked.connect(self.trigger_ueba_profiling)

        html_response = response.replace('\n', '<br>')
        self.txt_ueba.setHtml(f"<div style='font-family: Arial; font-size: 13px; color: #f8fafc;'>{html_response}</div>")

    def update_kpi_metrics(self, raw_cases: list):
        """Calcula métricas clave del SOC y gobernanza SLA 100% en memoria RAM sin llamadas a la API."""
        if not hasattr(self, 'kpi_crit_high'):
            return

        crit_high = 0
        unassigned = 0
        in_progress = 0
        resolved_24h = 0
        total_alerts = 0
        scores = []
        mttd_samples = []
        compliant_sla_count = 0
        total_sla_evaluated = 0

        import time
        limite_24h = int(time.time() * 1000) - (24 * 60 * 60 * 1000)

        for c in raw_cases:
            st = str(c.get("status", "")).strip().lower()
            sev = str(c.get("severity", "")).strip().lower()
            created_at = c.get("created_at", 0)

            mttd_info = SlaGovernanceEngine.evaluate_mttd(c)
            mttr_info = SlaGovernanceEngine.evaluate_mttr(c)

            if mttd_info["is_acknowledged"]:
                mttd_samples.append(mttd_info["elapsed_ms"])

            # Casos cerrados / resueltos en últimas 24h
            if st in ["resolved", "cancelled", "closed"]:
                if created_at >= limite_24h:
                    resolved_24h += 1
                    total_sla_evaluated += 1
                    if not mttr_info["breached"]:
                        compliant_sla_count += 1
                continue

            # Casos activos:
            total_sla_evaluated += 1
            if not mttr_info["breached"] and not (not mttd_info["is_acknowledged"] and mttd_info["breached"]):
                compliant_sla_count += 1

            if sev in ["critical", "high"] or mttd_info["priority"] in ["P1", "P2"]:
                crit_high += 1

            if st == "in progress":
                in_progress += 1
            elif st == "new":
                assignee = c.get("assignee_name") or c.get("assignee")
                if not assignee or str(assignee).strip().lower() in ["unassigned", "none", "libre", ""]:
                    unassigned += 1

            # Alertas agrupadas
            sz = c.get("size", 1)
            if isinstance(sz, int):
                total_alerts += sz

            # Score de riesgo normalizado
            sc = c.get("score")
            if sc is not None:
                scores.append(SlaGovernanceEngine.normalize_score(sc))

        avg_score = f"{sum(scores) / len(scores):.1f}" if scores else "0.0"

        # MTTD Promedio
        if mttd_samples:
            avg_mttd_ms = int(sum(mttd_samples) / len(mttd_samples))
            avg_mttd_str = SlaGovernanceEngine.format_duration(avg_mttd_ms)
        else:
            avg_mttd_str = "0m"

        # SLA Compliance %
        if total_sla_evaluated > 0:
            sla_pct = (compliant_sla_count / total_sla_evaluated) * 100.0
            sla_pct_str = f"{sla_pct:.1f}%"
        else:
            sla_pct = 100.0
            sla_pct_str = "100%"

        self.kpi_crit_high.setText(str(crit_high))
        self.kpi_unassigned.setText(str(unassigned))
        self.kpi_in_progress.setText(str(in_progress))
        self.kpi_resolved.setText(str(resolved_24h))
        if hasattr(self, 'kpi_avg_mttd'):
            self.kpi_avg_mttd.setText(avg_mttd_str)
        if hasattr(self, 'kpi_sla_compliance'):
            self.kpi_sla_compliance.setText(sla_pct_str)
            if sla_pct >= 90.0:
                self.kpi_sla_compliance.setStyleSheet("color: #10b981; font-size: 20px; font-weight: bold; border: none; font-family: 'Consolas';")
            elif sla_pct >= 75.0:
                self.kpi_sla_compliance.setStyleSheet("color: #f59e0b; font-size: 20px; font-weight: bold; border: none; font-family: 'Consolas';")
            else:
                self.kpi_sla_compliance.setStyleSheet("color: #ef4444; font-size: 20px; font-weight: bold; border: none; font-family: 'Consolas';")

        self.kpi_risk_score.setText(f"{avg_score}")
        self.kpi_total_alerts.setText(str(total_alerts))

        # Alerta visual dinámica: si hay casos críticos/altos abiertos, destacar en rojo
        if crit_high > 0:
            self.kpi_crit_high.setStyleSheet("color: #ef4444; font-size: 22px; font-weight: bold; border: none; font-family: 'Consolas';")
        else:
            self.kpi_crit_high.setStyleSheet("color: #10b981; font-size: 20px; font-weight: bold; border: none; font-family: 'Consolas';")

    # -------------------------------------------------------------------------
    # NAVEGACION Y PAGINACION DE CASOS SOAR
    # -------------------------------------------------------------------------
    def _on_cases_filter_changed(self):
        """Reinicia a la primera pagina y re-aplica los filtros seleccionados en RAM."""
        self._cases_current_page = 1
        self._render_cases_view()

    def _on_cases_search_return_pressed(self):
        """Si el usuario presiona Enter en el buscador con un ID de ticket numérico, intenta cargarlo on-demand."""
        query = self.input_cases_search.text().strip() if hasattr(self, 'input_cases_search') else ""
        if not query:
            return
        clean_id = query.lstrip("#").strip()
        if clean_id.isdigit():
            # Auto-asignar al input de ticket para acción inmediata
            if hasattr(self, 'input_case_ticket'):
                self.input_case_ticket.setText(clean_id)
            # Verificar si ya está en memoria
            pool = getattr(self, '_extended_cases_pool', []) or []
            found = any(str(c.get("ticket_id", "")).strip().lstrip("#") == clean_id for c in pool)
            if not found:
                try:
                    manager = RestSessionManager()
                    headers = manager.get_headers()
                    lookup_url = f"https://{HOST}/connect/api/v1/cases?ticket_id={clean_id}"
                    r = manager.session.get(lookup_url, headers=headers, verify=True, timeout=10)
                    if r.status_code == 200:
                        cases = (r.json().get("data", {}) or {}).get("cases", [])
                        if cases:
                            c = cases[0]
                            if not hasattr(self, '_extended_cases_pool') or self._extended_cases_pool is None:
                                self._extended_cases_pool = []
                            self._extended_cases_pool.insert(0, c)
                            if not hasattr(self, 'dict_casos_activos') or self.dict_casos_activos is None:
                                self.dict_casos_activos = {}
                            self.dict_casos_activos[clean_id] = c
                            self.dict_casos_activos[f"#{clean_id}"] = c
                            # Cambiar filtro de tiempo a 'Todo el Historial' para que no lo oculte el cutoff
                            if hasattr(self, 'combo_cases_time'):
                                self.combo_cases_time.blockSignals(True)
                                self.combo_cases_time.setCurrentIndex(5) # "Tiempo: Todo el Historial"
                                self.combo_cases_time.blockSignals(False)
                            self._render_cases_view()
                            if hasattr(self, 'lbl_cases_count_info'):
                                self.lbl_cases_count_info.setText(f"✓ Ticket #{clean_id} descargado on-demand desde Stellar Cyber API")
                except Exception as e:
                    log_to_file(f"[SEARCH RETURN PRESSED LOOKUP ERROR] Ticket {clean_id}: {e}")

    def _on_cases_page_size_changed(self):
        """Ajusta el tamano de pagina y re-renderiza la vista."""
        self._cases_current_page = 1
        self._render_cases_view()

    def _on_cases_first_page(self):
        self._cases_current_page = 1
        self._render_cases_view()

    def _on_cases_prev_page(self):
        if getattr(self, '_cases_current_page', 1) > 1:
            self._cases_current_page -= 1
            self._render_cases_view()

    def _on_cases_next_page(self):
        total_pages = getattr(self, '_cases_total_pages', 1)
        if getattr(self, '_cases_current_page', 1) < total_pages:
            self._cases_current_page += 1
            self._render_cases_view()

    def _on_cases_last_page(self):
        total_pages = getattr(self, '_cases_total_pages', 1)
        self._cases_current_page = total_pages
        self._render_cases_view()

    def display_cases_results_wrapper(self):
        """Llamado rapido para re-renderizar la vista en RAM con cero latencia."""
        self._render_cases_view()

    def _render_cases_view(self):
        """Filtra, ordena y pagina los casos en memoria RAM para renderizado instantaneo."""
        try:
            raw_cases = getattr(self, '_last_raw_cases', []) or []
            pool = getattr(self, '_extended_cases_pool', []) or raw_cases

            # 1. Filtro por Estado (Activos, Cerrados, Todos)
            status_filter = self.combo_cases_status.currentText() if hasattr(self, 'combo_cases_status') else "Activos"
            if status_filter == "Cerrados":
                filtered = [
                    c for c in pool
                    if str(c.get("status", "")).strip().lower() in ["resolved", "cancelled", "closed"]
                ]
            elif status_filter == "Todos":
                filtered = list(pool)
            else: # "Activos"
                filtered = [
                    c for c in pool
                    if str(c.get("status", "")).strip().lower() not in ["resolved", "cancelled", "closed"]
                ]

            # 1.1 Filtro por Ventana Temporal (1HR, 12HR, 24HR, 7D, 30D, Todo el Historial)
            time_filter = self.combo_cases_time.currentText() if hasattr(self, 'combo_cases_time') else "Tiempo: 24 Horas"
            search_text = self.input_cases_search.text().strip().lower() if hasattr(self, 'input_cases_search') else ""
            if not search_text and "Todo el Historial" not in time_filter:
                now_ms = int(time.time() * 1000)
                if "1 Hora" in time_filter:
                    cutoff = now_ms - (3600 * 1000)
                    filtered = [c for c in filtered if int(c.get("created_at") or 0) >= cutoff]
                elif "12 Horas" in time_filter:
                    cutoff = now_ms - (12 * 3600 * 1000)
                    filtered = [c for c in filtered if int(c.get("created_at") or 0) >= cutoff]
                elif "24 Horas" in time_filter:
                    cutoff = now_ms - (24 * 3600 * 1000)
                    filtered = [c for c in filtered if int(c.get("created_at") or 0) >= cutoff]
                elif "7 Días" in time_filter or "7 Dias" in time_filter:
                    cutoff = now_ms - (7 * 86400 * 1000)
                    filtered = [c for c in filtered if int(c.get("created_at") or 0) >= cutoff]
                elif "30 Días" in time_filter or "30 Dias" in time_filter:
                    cutoff = now_ms - (30 * 86400 * 1000)
                    filtered = [c for c in filtered if int(c.get("created_at") or 0) >= cutoff]

            # 2. Filtro de Texto (Ticket ID, Alerta, Tenant, Analista, Tags, Descripcion)
            search_text = self.input_cases_search.text().strip().lower() if hasattr(self, 'input_cases_search') else ""
            if search_text:
                matched = []
                for c in filtered:
                    t_id = str(c.get("ticket_id") or c.get("_id") or "")
                    name = str(c.get("name") or "")
                    tenant = str(c.get("tenant_name") or "")
                    assignee = str(c.get("assignee_name") or c.get("assignee") or "")
                    desc = str(c.get("description") or "")
                    tags = " ".join(str(t) for t in c.get("tags", []))
                    haystack = f"{t_id} {name} {tenant} {assignee} {desc} {tags}".lower()
                    if search_text in haystack:
                        matched.append(c)
                filtered = matched

            # 3. Filtro de Prioridad SLA
            pri_filter = self.combo_cases_priority.currentText() if hasattr(self, 'combo_cases_priority') else "Prioridad: Todas"
            if pri_filter != "Prioridad: Todas":
                target_pri = pri_filter.split()[0]
                filtered = [
                    c for c in filtered 
                    if SlaGovernanceEngine.evaluate_mttd(c)["priority"] == target_pri
                ]

            # 4. Filtro de Asignacion
            ass_filter = self.combo_cases_assignee.currentText() if hasattr(self, 'combo_cases_assignee') else "Asignacion: Todas"
            if ass_filter == "Solo Libres":
                filtered = [
                    c for c in filtered
                    if not (c.get("assignee_name") or c.get("assignee")) or str(c.get("assignee_name") or c.get("assignee")).strip().lower() in ["unassigned", "none", "libre", ""]
                ]
            elif ass_filter == "Asignados a Mi":
                my_email = str(EMAIL_USUARIO or "kevinmoraes").lower()
                filtered = [
                    c for c in filtered
                    if my_email in str(c.get("assignee_name") or c.get("assignee") or "").lower() or "kevinmoraes" in str(c.get("assignee_name") or c.get("assignee") or "").lower()
                ]
            elif ass_filter == "Asignados a Otros":
                my_email = str(EMAIL_USUARIO or "kevinmoraes").lower()
                filtered = [
                    c for c in filtered
                    if (c.get("assignee_name") or c.get("assignee")) 
                    and str(c.get("assignee_name") or c.get("assignee")).strip().lower() not in ["unassigned", "none", "libre", ""]
                    and my_email not in str(c.get("assignee_name") or c.get("assignee") or "").lower()
                    and "kevinmoraes" not in str(c.get("assignee_name") or c.get("assignee") or "").lower()
                ]

            # 5. Ordenamiento Multi-criterio
            sort_mode = self.combo_cases_sort.currentText() if hasattr(self, 'combo_cases_sort') else "Orden: Mayor Score"
            if sort_mode == "Orden: Menor Score":
                filtered.sort(key=lambda c: (SlaGovernanceEngine.normalize_score(c.get("score")), int(c.get("created_at") or 0)), reverse=False)
            elif sort_mode == "Orden: Mas Recientes":
                filtered.sort(key=lambda c: int(c.get("created_at") or 0), reverse=True)
            elif sort_mode == "Orden: Mas Antiguos":
                filtered.sort(key=lambda c: int(c.get("created_at") or 0), reverse=False)
            elif sort_mode == "Orden: Urgencia SLA":
                def _sla_urgency_key(c: dict):
                    mttd = SlaGovernanceEngine.evaluate_mttd(c)
                    mttr = SlaGovernanceEngine.evaluate_mttr(c)
                    is_breached = mttd["breached"] or mttr["breached"]
                    is_warning = mttd["warning"] or mttr["warning"]
                    risk_lvl = 2 if is_breached else (1 if is_warning else 0)
                    rem_ms = mttd.get("remaining_ms", 0)
                    rem_sec = rem_ms / 1000.0 if rem_ms > 0 else 0
                    return (risk_lvl, -rem_sec)
                filtered.sort(key=_sla_urgency_key, reverse=True)
            elif sort_mode == "Orden: Ticket ID":
                def _tid_key(c: dict):
                    raw = str(c.get("ticket_id") or c.get("_id") or "0")
                    digits = re.sub(r'\D', '', raw)
                    return int(digits) if digits else 0
                filtered.sort(key=_tid_key, reverse=True)
            else:
                # Default: Mayor Score descendente
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
                filtered.sort(key=_case_sort_key, reverse=True)

            self._cases_filtered_list = filtered
            total_filtered = len(filtered)

            # 6. Paginacion
            page_size_str = self.combo_cases_page_size.currentText() if hasattr(self, 'combo_cases_page_size') else "25 por pagina"
            if "Todos" in page_size_str:
                page_size = max(1, total_filtered) if total_filtered > 0 else 25
            else:
                try:
                    page_size = int(page_size_str.split()[0])
                except Exception:
                    page_size = 25

            total_pages = max(1, math.ceil(total_filtered / page_size)) if total_filtered > 0 else 1
            self._cases_total_pages = total_pages
            self._cases_current_page = max(1, min(getattr(self, '_cases_current_page', 1), total_pages))

            start_idx = (self._cases_current_page - 1) * page_size
            end_idx = min(start_idx + page_size, total_filtered)
            page_slice = filtered[start_idx:end_idx] if total_filtered > 0 else []

            # Actualizar indicadores visuales de paginacion
            if hasattr(self, 'lbl_cases_count_info'):
                tot_pool = len(pool)
                disp_start = start_idx + 1 if total_filtered > 0 else 0
                self.lbl_cases_count_info.setText(f"Mostrando {disp_start}-{end_idx} de {total_filtered} casos (Pool: {tot_pool})")
            if hasattr(self, 'lbl_cases_page_indicator'):
                self.lbl_cases_page_indicator.setText(f"Pagina {self._cases_current_page} de {total_pages}")
            if hasattr(self, 'btn_cases_first_page'):
                self.btn_cases_first_page.setEnabled(self._cases_current_page > 1)
                self.btn_cases_prev_page.setEnabled(self._cases_current_page > 1)
                self.btn_cases_next_page.setEnabled(self._cases_current_page < total_pages)
                self.btn_cases_last_page.setEnabled(self._cases_current_page < total_pages)

            # 7. Renderizado HTML en txt_cases
            self.dict_casos_activos = {}
            html_rows = []
            header_str = f"  {'TICKET ID'.ljust(10)} | {'PRI'.ljust(4)} | {'TENANT'.ljust(12)} | {'SCORE'.ljust(5)} | {'NOMBRE DEL INCIDENTE'.ljust(44)} | {'ASIGNADO'.ljust(14)} | {'ESTADO SLA / TIEMPO RESTANTE'}"
            sep_str = f"  {'-' * 127}"
            html_rows.append(f"<span style='color: #38bdf8; font-weight: bold;'>{header_str}</span>")
            html_rows.append(f"<span style='color: #334155;'>{sep_str}</span>")

            new_breached_count = 0
            for c in page_slice:
                t_id = str(c.get("ticket_id", "N/A")).strip()
                tenant = str(c.get("tenant_name", "Global")).strip()
                raw_score = c.get("score", 0)
                norm_score = SlaGovernanceEngine.normalize_score(raw_score)
                name = str(c.get("name", "Sin Nombre")).strip()
                raw_assignee = c.get("assignee_name") or c.get("assignee")
                
                if not raw_assignee or str(raw_assignee).strip().lower() in ["unassigned", "none", "libre", ""]:
                    assignee = "Libre"
                else:
                    assignee = str(raw_assignee).strip()
                
                self.dict_casos_activos[t_id] = c
                clean_tid = t_id.lstrip("#")
                if clean_tid != t_id:
                    self.dict_casos_activos[clean_tid] = c

                # Clasificacion de anomalia de autenticacion y HealthMailbox
                is_auth_anomaly = self._is_auth_anomaly_case(c)
                is_hm = False

                if is_auth_anomaly:
                    cached_info = self._case_identity_cache.get(t_id)
                    if cached_info is not None:
                        if cached_info.get("pure_hm"):
                            is_hm = True
                            badge = "[HM] "
                            row_color = "#10b981"
                            font_weight = "normal"
                        elif cached_info.get("has_hm"):
                            badge = "[HM+MIX] "
                            row_color = "#f43f5e"
                            font_weight = "bold"
                        else:
                            badge = "[NO-HM] "
                            row_color = "#f43f5e"
                            font_weight = "bold"
                    else:
                        if "healthmailbox" in name.lower():
                            is_hm = True
                            badge = "[HM] "
                            row_color = "#10b981"
                            font_weight = "normal"
                        else:
                            badge = "[AUDIT] "
                            row_color = "#38bdf8"
                            font_weight = "normal"
                else:
                    if self._is_sophos_translate_candidate(c):
                        badge = "[TRANS] "
                        row_color = "#06b6d4"
                        font_weight = "normal"
                    elif self._is_sati_vpn_candidate(c):
                        badge = "[SATI] "
                        row_color = "#38bdf8"
                        font_weight = "normal"
                    elif self._is_dpapi_storage_candidate(c):
                        badge = "[DPAPI] "
                        row_color = "#a78bfa"
                        font_weight = "normal"
                    else:
                        badge = ""

                full_name_display = f"{badge}{name}"
                if len(full_name_display) > 44:
                    name_display = full_name_display[:41] + "..."
                else:
                    name_display = full_name_display

                if len(tenant) > 11:
                    tenant_display = tenant[:9] + ".."
                else:
                    tenant_display = tenant

                if len(assignee) > 13:
                    assignee_display = assignee[:11] + ".."
                else:
                    assignee_display = assignee

                mttd_info = SlaGovernanceEngine.evaluate_mttd(c)
                mttr_info = SlaGovernanceEngine.evaluate_mttr(c)
                pri = mttd_info["priority"]
                
                # Extracción complementaria de métricas oficiales de caso Stellar Cyber 7.0.0s (AELDEV-66747)
                stellar_metrics = c.get("metrics") or c.get("details", {}).get("metrics", {})
                stellar_tta_suffix = ""
                if isinstance(stellar_metrics, dict):
                    for m_val in stellar_metrics.values():
                        if isinstance(m_val, dict) and "acknowledge" in str(m_val.get("name", "")).lower():
                            el_ms = m_val.get("elapsed_ms", 0)
                            if el_ms > 0:
                                el_min = round(el_ms / 60000.0, 1)
                                stellar_tta_suffix = f" | TTA: {el_min}m"
                                break

                st = str(c.get("status", "")).strip().lower()
                if st in ["resolved", "cancelled", "closed"]:
                    if mttr_info["breached"]:
                        sla_display = f"CERRADO (SLA VIOLADO {mttr_info['remaining_str']} | MTTR: {mttr_info['elapsed_str']}{stellar_tta_suffix})"
                    else:
                        sla_display = f"CERRADO (MTTR: {mttr_info['elapsed_str']}{stellar_tta_suffix})"
                    row_color = "#64748b"
                    font_weight = "normal"
                else:
                    if assignee == "Libre":
                        if mttd_info["breached"]:
                            sla_display = f"MTTD VENCIDO ({mttd_info['remaining_str']} | Total: {mttd_info['elapsed_str']}{stellar_tta_suffix})"
                            if pri in ["P1", "P2"]:
                                new_breached_count += 1
                        elif mttd_info["warning"]:
                            sla_display = f"MTTD RIESGO ({mttd_info['remaining_str']}{stellar_tta_suffix})"
                        else:
                            sla_display = f"MTTD OK ({mttd_info['remaining_str']}{stellar_tta_suffix})"
                    else:
                        if mttr_info["breached"]:
                            sla_display = f"MTTR VENCIDO ({mttr_info['remaining_str']} | Total: {mttr_info['elapsed_str']}{stellar_tta_suffix})"
                            if pri in ["P1", "P2"]:
                                new_breached_count += 1
                        elif mttr_info["warning"]:
                            sla_display = f"MTTR RIESGO ({mttr_info['remaining_str']}{stellar_tta_suffix})"
                        else:
                            sla_display = f"MTTR OK ({mttr_info['remaining_str']}{stellar_tta_suffix})"

                    if is_auth_anomaly and not is_hm:
                        cached_info = self._case_identity_cache.get(t_id)
                        if cached_info is not None:
                            row_color = "#f43f5e"
                            font_weight = "bold"
                        else:
                            row_color = "#38bdf8"
                            font_weight = "normal"
                    elif is_auth_anomaly and is_hm:
                        row_color = "#10b981"
                        font_weight = "normal"
                    elif mttd_info["breached"] or mttr_info["breached"]:
                        row_color = "#ef4444"
                        font_weight = "bold"
                    elif mttd_info["warning"] or mttr_info["warning"]:
                        row_color = "#f59e0b"
                        font_weight = "bold"
                    else:
                        row_color = "#38bdf8"
                        font_weight = "normal"

                row_str = f"  {t_id.ljust(10)} | {pri.ljust(4)} | {tenant_display.ljust(12)} | {str(norm_score).ljust(5)} | {name_display.ljust(44)} | {assignee_display.ljust(14)} | {sla_display}"
                html_rows.append(f"<span style='color: {row_color}; font-weight: {font_weight};'>{row_str}</span>")

            # Alerta acustica si aparecen casos criticos/altos en brecha
            prev_breached = getattr(self, '_prev_sla_breached_count', 0)
            if new_breached_count > prev_breached and new_breached_count > 0:
                ejecutar_beep(400, 600)
            self._prev_sla_breached_count = new_breached_count

            if not page_slice:
                html_rows.append("<span style='color: #64748b;'>  (Sin casos que coincidan con los filtros seleccionados)</span>")

            full_html = f"<pre style=\"font-family: 'Consolas', 'Courier New', monospace; font-size: 12px; margin: 0; line-height: 1.35;\">" + "\n".join(html_rows) + "</pre>"
            self.txt_cases.setHtml(full_html)

        except Exception as e:
            log_to_file(f"[ERROR _render_cases_view] {e}")
            self.txt_cases.setPlainText(f"Error al renderizar casos: {e}")

    @Slot(dict)
    def display_cases_results(self, data):
        try:
            self._last_cases_data = data # Guardar en memoria intermedia para evitar llamadas fantasmas a la API
            cases_payload = data.get("cases", {})
            raw_cases = []
            if cases_payload and "data" in cases_payload and "cases" in cases_payload["data"]:
                raw_cases = cases_payload["data"]["cases"]

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

            raw_cases.sort(key=_case_sort_key, reverse=True)

            # Actualizacion instantanea en memoria de las tarjetas KPI (Cero llamadas de API)
            self.update_kpi_metrics(raw_cases)

            # Mantener el pool de casos en memoria actualizado sin duplicados y ordenado por score
            self._last_raw_cases = raw_cases
            cases_dict = {c.get("_id") or c.get("ticket_id"): c for c in getattr(self, '_extended_cases_pool', []) if (c.get("_id") or c.get("ticket_id"))}
            for c in raw_cases:
                k = c.get("_id") or c.get("ticket_id")
                if k:
                    cases_dict[k] = c
            self._extended_cases_pool = sorted(cases_dict.values(), key=_case_sort_key, reverse=True)

            # Si la pestaña 3 de metricas esta activa o es el primer calculo, refrescar en segundo plano
            if hasattr(self, 'tab3') and (self.tabs.currentIndex() == 2 or getattr(self, '_last_metrics_result', None) is None):
                self.recalculate_executive_metrics()

            # Derivacion ultra-ligera en RAM de Top Protocolos / Amenazas
            from collections import Counter
            proto_counter = Counter()
            for c in raw_cases:
                c_name = str(c.get("name", "")).strip()
                if " and " in c_name:
                    c_name = c_name.split(" and ")[0]
                if c_name:
                    proto_counter[c_name] += c.get("size", 1)
                for tag in c.get("tags", []):
                    proto_counter[f"Tag: {tag}"] += 1
            if proto_counter:
                self.display_top_protocols(proto_counter.most_common(10))
            
            # Renderizado paginado y filtrado en memoria
            self._render_cases_view()

            # Ejecutar evaluacion de Auto-Guardia SLA y Auto-Remediacion HM
            self._process_auto_guardia_and_hm(raw_cases)

            # Evaluar y despachar notificaciones push moviles hacia ntfy.sh
            self._process_mobile_notifications(raw_cases)
        except Exception as e:
            log_to_file(f"[ERROR display_cases_dynamic] {e}")
            self.txt_cases.setPlainText(f"Error al procesar casos dinamicos: {e}")
        finally:
            if hasattr(self, 'btn_manual_refresh'):
                self.btn_manual_refresh.setText("Refrescar Cola")
                self.btn_manual_refresh.setEnabled(True)
            if hasattr(self, 'lbl_api_health'):
                self.lbl_api_health.setText("API EN LINEA")
                self.lbl_api_health.setStyleSheet("color: #10b981; font-size: 11px; font-weight: bold; padding: 2px 8px; background-color: #064e3b; border-radius: 4px; border: 1px solid #10b981; font-family: 'Consolas';")

    def _on_cases_cursor_changed(self):
        """Auto-detecta y prellena el Ticket ID al hacer clic en cualquier línea de la cola de incidentes."""
        try:
            cursor = self.txt_cases.textCursor()
            line_text = cursor.block().text().strip()
            if "|" in line_text:
                candidate = line_text.split("|")[0].strip()
                if candidate and candidate != "TICKET ID" and not candidate.startswith("-"):
                    clean_id = candidate.lstrip("#")
                    if candidate in self.dict_casos_activos or clean_id in self.dict_casos_activos:
                        self.input_case_ticket.setText(clean_id)
        except Exception:
            pass

    def _is_auth_anomaly_case(self, case: dict) -> bool:
        """Determina si el incidente corresponde a una anomalía de autenticación/credenciales."""
        name = str(case.get("name", "")).lower()
        tags = " ".join(str(t).lower() for t in case.get("tags", []))
        combined = f"{name} {tags}"
        return any(k in combined for k in [
            "login", "user_login_fail", "account login", "credential", 
            "auth", "kerberos", "ntlm", "4776", "4768", "stuffing", 
            "brute force", "fuerza bruta"
        ])

    def _is_healthmailbox_candidate(self, case: dict) -> bool:
        """Determina si el incidente involucra sondas de salud HealthMailbox de Exchange."""
        t_id = str(case.get("ticket_id") or case.get("_id"))
        cached = self._case_identity_cache.get(t_id)
        if cached is not None:
            return bool(cached.get("pure_hm"))
        name = str(case.get("name", "")).lower()
        src_user = str(case.get("srcip_username") or "").lower()
        user = str(case.get("username") or case.get("user") or "").lower()
        tags = " ".join(str(t).lower() for t in case.get("tags", []))
        desc = str(case.get("description") or "").lower()
        combined = f"{name} {src_user} {user} {tags} {desc}"
        return "healthmailbox" in combined

    def _is_sophos_translate_candidate(self, case: dict) -> bool:
        """Determina si el incidente parece involucrar alertas de Sophos Web Control o Google Translate."""
        name = str(case.get("name", "")).lower()
        src_user = str(case.get("srcip_username") or "").lower()
        user = str(case.get("username") or case.get("user") or "").lower()
        tags = " ".join(str(t).lower() for t in case.get("tags", []))
        desc = str(case.get("description") or "").lower()
        combined = f"{name} {src_user} {user} {tags} {desc}"
        return (
            "translate.google.com" in combined or
            "webcontrolviolation" in combined or
            ("user execution" in combined and "sophos" in combined)
        )

    def _is_sati_vpn_candidate(self, case: dict) -> bool:
        """Determina si el incidente involucra consultas DNS denegadas en firewall de la cuenta SATI (Odoo VPN)."""
        name = str(case.get("name", "")).lower()
        src_user = str(case.get("srcip_username") or "").lower()
        user = str(case.get("username") or case.get("user") or "").lower()
        tags = " ".join(str(t).lower() for t in case.get("tags", []))
        desc = str(case.get("description") or "").lower()
        combined = f"{name} {src_user} {user} {tags} {desc}"

        is_sati_user = "sati" in combined
        is_fw_denial = (
            "firewall denial" in combined or 
            "internal firewall denial" in combined or 
            "denial anomaly" in combined or 
            "policyid" in combined or
            "denial" in combined
        )
        return is_sati_user and (is_fw_denial or "10.212.134" in combined or "dns" in combined)

    def _is_dpapi_storage_candidate(self, case: dict) -> bool:
        """Determina si el incidente involucra accesos a protected_storage / IPC$ en VMBASE8 (DPAPI)."""
        name = str(case.get("name", "")).lower()
        src_user = str(case.get("srcip_username") or "").lower()
        user = str(case.get("username") or case.get("user") or "").lower()
        tags = " ".join(str(t).lower() for t in case.get("tags", []))
        desc = str(case.get("description") or "").lower()
        combined = f"{name} {src_user} {user} {tags} {desc}"

        return (
            "protected_storage" in combined or
            "sensitive windows network share" in combined or
            ("network share" in combined and "ipc$" in combined) or
            "windows_security_5145" in combined or
            ("5145" in combined and "share" in combined)
        )

    def _process_auto_guardia_and_hm(self, raw_cases: list):
        """
        Evalúa en cada ciclo de telemetría:
        1. Sondeo asíncrono ultra-rápido de alertas crudas para casos de autenticación.
        2. Auto-remediación SOAR de HealthMailbox bajo la Ley de Oro (cierre automático como FP).
        3. Auto-remediación SOAR de Sophos WebControl (Google Translate con cierre automático como FP o alerta si no es Translate).
        4. Auto-remediación SOAR de SATI VPN (consultas DNS hacia DC interno bloqueadas por failover en firewall).
        5. Auto-Guardia de SLA para el turno: si un caso libre se acerca al vencimiento de MTTD
           y ningún compañero lo tomó, se auto-asigna a kevinmoraes@technoma.com.py para blindar el SLA.
        """
        if not raw_cases:
            return

        session_mgr = RestSessionManager()
        headers = session_mgr.get_headers()
        session = session_mgr.session

        # 1. DISPARAR SONDEO ASÍNCRONO DE IDENTIDADES PARA CASOS DE AUTENTICACIÓN
        for c in raw_cases:
            st = str(c.get("status", "")).strip().lower()
            if st in ["resolved", "cancelled", "closed"]:
                continue
            if self._is_auth_anomaly_case(c):
                t_id = str(c.get("ticket_id") or c.get("_id"))
                case_id = c.get("_id") or t_id
                if t_id not in self._case_identity_cache and t_id not in self._active_probe_workers:
                    probe = CaseIdentityProbeWorker(case_id, t_id, session, headers)
                    probe.probe_finished.connect(self._on_identity_probe_finished)
                    probe.probe_failed.connect(self._on_identity_probe_failed)
                    self._active_probe_workers[t_id] = probe
                    probe.start()

        # 2. EVALUAR AUTO-REMEDIACIÓN HEALTHMAILBOX
        if hasattr(self, 'check_auto_healthmailbox') and self.check_auto_healthmailbox.isChecked():
            for c in raw_cases:
                st = str(c.get("status", "")).strip().lower()
                if st in ["resolved", "cancelled", "closed"]:
                    continue

                if self._is_healthmailbox_candidate(c):
                    t_id = str(c.get("ticket_id") or c.get("_id"))
                    if t_id not in self._remediated_cases:
                        # Lanzar worker si no hay otro en ejecución
                        if self._worker_hm_remediator is None or not self._worker_hm_remediator.isRunning():
                            self._remediated_cases.add(t_id)
                            log_to_file(f"[SOAR AUTO-REMEDIATION] Iniciando verificación de Ley de Oro para Caso #{t_id}...")
                            self._worker_hm_remediator = HealthMailboxAutoRemediatorWorker(
                                case_obj=c,
                                session=session,
                                headers=headers
                            )
                            self._worker_hm_remediator.remediation_finished.connect(self._on_hm_remediation_finished)
                            self._worker_hm_remediator.remediation_failed.connect(self._on_hm_remediation_failed)
                            self._worker_hm_remediator.start()
                            break # Uno por ciclo para control estricto de concurrencia

        # 2.1 EVALUAR AUTO-REMEDIACIÓN SOPHOS WEB CONTROL (GOOGLE TRANSLATE)
        if hasattr(self, 'check_auto_sophos_translate') and self.check_auto_sophos_translate.isChecked():
            for c in raw_cases:
                st = str(c.get("status", "")).strip().lower()
                if st in ["resolved", "cancelled", "closed"]:
                    continue

                if self._is_sophos_translate_candidate(c):
                    t_id = str(c.get("ticket_id") or c.get("_id"))
                    if t_id not in self._remediated_translate_cases:
                        if self._worker_sophos_translate_remediator is None or not self._worker_sophos_translate_remediator.isRunning():
                            self._remediated_translate_cases.add(t_id)
                            log_to_file(f"[SOAR TRANSLATE] Iniciando verificación WebControl para Caso #{t_id}...")
                            self._worker_sophos_translate_remediator = SophosTranslateAutoRemediatorWorker(
                                case_obj=c,
                                session=session,
                                headers=headers
                            )
                            self._worker_sophos_translate_remediator.remediation_finished.connect(self._on_translate_remediation_finished)
                            self._worker_sophos_translate_remediator.remediation_failed.connect(self._on_translate_remediation_failed)
                            self._worker_sophos_translate_remediator.alert_non_translate.connect(self._on_non_translate_detected)
                            self._worker_sophos_translate_remediator.start()
                            break # Uno por ciclo para control estricto de concurrencia

        # 2.2 EVALUAR AUTO-REMEDIACIÓN SATI VPN DNS (SOPORTE ODOO)
        if hasattr(self, 'check_auto_sati') and self.check_auto_sati.isChecked():
            for c in raw_cases:
                st = str(c.get("status", "")).strip().lower()
                if st in ["resolved", "cancelled", "closed"]:
                    continue

                if self._is_sati_vpn_candidate(c):
                    t_id = str(c.get("ticket_id") or c.get("_id"))
                    if t_id not in self._remediated_sati_cases:
                        if self._worker_sati_remediator is None or not self._worker_sati_remediator.isRunning():
                            self._remediated_sati_cases.add(t_id)
                            log_to_file(f"[SOAR SATI] Iniciando auditoria de DNS VPN para Caso #{t_id}...")
                            self._worker_sati_remediator = SatiDnsAutoRemediatorWorker(
                                case_obj=c,
                                session=session,
                                headers=headers
                            )
                            self._worker_sati_remediator.remediation_finished.connect(self._on_sati_remediation_finished)
                            self._worker_sati_remediator.remediation_failed.connect(self._on_sati_remediation_failed)
                            self._worker_sati_remediator.alert_non_sati_dns.connect(self._on_non_sati_dns_detected)
                            self._worker_sati_remediator.start()
                            break # Uno por ciclo para control estricto de concurrencia

        # 2.3 EVALUAR AUTO-REMEDIACIÓN DPAPI (PROTECTED_STORAGE)
        if hasattr(self, 'check_auto_dpapi') and self.check_auto_dpapi.isChecked():
            for c in raw_cases:
                st = str(c.get("status", "")).strip().lower()
                if st in ["resolved", "cancelled", "closed"]:
                    continue

                if self._is_dpapi_storage_candidate(c):
                    t_id = str(c.get("ticket_id") or c.get("_id"))
                    if t_id not in self._remediated_dpapi_cases:
                        if self._worker_dpapi_remediator is None or not self._worker_dpapi_remediator.isRunning():
                            self._remediated_dpapi_cases.add(t_id)
                            log_to_file(f"[SOAR DPAPI] Iniciando auditoria de protected_storage para Caso #{t_id}...")
                            self._worker_dpapi_remediator = DPAPIStorageAutoRemediatorWorker(
                                case_obj=c,
                                session=session,
                                headers=headers
                            )
                            self._worker_dpapi_remediator.remediation_finished.connect(self._on_dpapi_remediation_finished)
                            self._worker_dpapi_remediator.remediation_failed.connect(self._on_dpapi_remediation_failed)
                            self._worker_dpapi_remediator.alert_non_dpapi.connect(self._on_non_dpapi_detected)
                            self._worker_dpapi_remediator.start()
                            break # Uno por ciclo para control estricto de concurrencia

        # 3. EVALUAR AUTO-GUARDIA SLA (PROTECCIÓN DE TURNO Y MTTD)
        if hasattr(self, 'check_auto_guardia') and self.check_auto_guardia.isChecked():
            for c in raw_cases:
                st = str(c.get("status", "")).strip().lower()
                if st in ["resolved", "cancelled", "closed"]:
                    continue

                raw_assignee = c.get("assignee_name") or c.get("assignee")
                is_libre = (not raw_assignee) or str(raw_assignee).strip().lower() in ["unassigned", "none", "libre", ""]
                if not is_libre:
                    continue

                # Si es un caso de HealthMailbox, WebControl Translate, SATI VPN o DPAPI, esperar a sus módulos SOAR
                t_id = str(c.get("ticket_id") or c.get("_id"))
                if hasattr(self, 'check_auto_healthmailbox') and self.check_auto_healthmailbox.isChecked():
                    if self._is_healthmailbox_candidate(c) or t_id in self._active_probe_workers:
                        continue
                if hasattr(self, 'check_auto_sophos_translate') and self.check_auto_sophos_translate.isChecked():
                    if self._is_sophos_translate_candidate(c):
                        continue
                if hasattr(self, 'check_auto_sati') and self.check_auto_sati.isChecked():
                    if self._is_sati_vpn_candidate(c):
                        continue
                if hasattr(self, 'check_auto_dpapi') and self.check_auto_dpapi.isChecked():
                    if self._is_dpapi_storage_candidate(c):
                        continue

                # Evaluar MTTD para casos generales no asignados
                mttd_info = SlaGovernanceEngine.evaluate_mttd(c)
                needs_guardia = (
                    mttd_info["breached"] or 
                    mttd_info["warning"] or 
                    mttd_info["remaining_ms"] <= 5 * 60 * 1000 or 
                    mttd_info["elapsed_ms"] >= (mttd_info["limit_ms"] * 0.70)
                )

                if needs_guardia:
                    case_id = c.get("_id") or t_id
                    if t_id not in self._auto_assigned_cases:
                        self._auto_assigned_cases.add(t_id)
                        log_to_file(f"[AUTO-GUARDIA SLA] Caso #{t_id} en riesgo de MTTD ({mttd_info['remaining_str']} restantes). Auto-asignando a {EMAIL_USUARIO}...")
                        worker = AutoAssignWorker(
                            case_id=case_id,
                            ticket_id=t_id,
                            session=session,
                            headers=headers
                        )
                        worker.assigned_signal.connect(self._on_auto_guardia_assigned)
                        worker.error_signal.connect(self._on_auto_guardia_error)
                        self._auto_guardia_workers.append(worker)
                        worker.start()

    def _on_identity_probe_finished(self, info: dict):
        t_id = info.get("ticket_id")
        self._active_probe_workers.pop(t_id, None)
        self._case_identity_cache[t_id] = info
        log_to_file(f"[PROBE IDENTIDAD] Caso #{t_id} auditado: usuarios={info.get('users')} | pure_hm={info.get('pure_hm')}")

        # Si se confirma que es 100% puro HealthMailbox y está activo el checkbox, disparar auto-remediación
        if info.get("pure_hm") and hasattr(self, 'check_auto_healthmailbox') and self.check_auto_healthmailbox.isChecked():
            if t_id not in self._remediated_cases:
                if self._worker_hm_remediator is None or not self._worker_hm_remediator.isRunning():
                    self._remediated_cases.add(t_id)
                    c_obj = self.dict_casos_activos.get(t_id, {"_id": info.get("case_id"), "ticket_id": t_id})
                    log_to_file(f"[SOAR AUTO-REMEDIATION] Disparando auto-remediador para caso verificado #{t_id}...")
                    self._worker_hm_remediator = HealthMailboxAutoRemediatorWorker(
                        case_obj=c_obj,
                        session=RestSessionManager().session,
                        headers=RestSessionManager().get_headers()
                    )
                    self._worker_hm_remediator.remediation_finished.connect(self._on_hm_remediation_finished)
                    self._worker_hm_remediator.remediation_failed.connect(self._on_hm_remediation_failed)
                    self._worker_hm_remediator.start()

        # Re-renderizar la cola para reflejar 🟢 [HM] o ⚠️ [NO-HM] inmediatamente
        self.display_cases_results_wrapper()

    def _on_identity_probe_failed(self, ticket_id: str, error_msg: str):
        self._active_probe_workers.pop(ticket_id, None)
        log_to_file(f"[PROBE ERROR] Fallo al sondear caso #{ticket_id}: {error_msg}")

    def _on_hm_remediation_finished(self, result: dict):
        t_id = result.get("ticket_id", "N/A")
        proto = result.get("protocol", "Desconocido")
        users = ", ".join(result.get("users", []))
        log_msg = f"[SOAR AUTO-REMEDIATION] Caso #{t_id} RESUELTO EXITOSAMENTE (False Positive) | Protocolo: {proto} | Usuarios: {users}"
        log_to_file(log_msg)
        ejecutar_beep(800, 200)
        ejecutar_beep(1200, 250)
        self.enviar_notificacion_popup(
            f"⚡ Caso #{t_id} Auto-Remediado",
            f"Verificado bajo Ley de Oro ({proto}). Cerrado como False Positive."
        )
        # Notificación push móvil
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(t_id) not in self._mobile_notified_auto_closed:
                self._mobile_notified_auto_closed.add(str(t_id))
                MobileAlertsNotifier.send_notification(
                    title=f"[AUTO-REMEDIADO] Caso #{t_id} Resuelto",
                    message=f"Caso #{t_id} cerrado automáticamente como False Positive bajo la Ley de Oro ({proto}).\nUsuarios: {users}",
                    priority="default",
                    tags="robot,check"
                )
        # Actualizar de inmediato el estado en la memoria local para reflejarlo instantáneamente en la GUI
        if str(t_id) in self.dict_casos_activos:
            self.dict_casos_activos[str(t_id)]["status"] = "Resolved"
            self.dict_casos_activos[str(t_id)]["resolution"] = "False Positive"
        if hasattr(self, '_last_cases_data'):
            for c in self._last_cases_data.get("cases", {}).get("data", {}).get("cases", []):
                if str(c.get("ticket_id")) == str(t_id):
                    c["status"] = "Resolved"
                    c["resolution"] = "False Positive"
                    break
        self.display_cases_results_wrapper()

        # Refrescar cola de casos con el backend para sincronización completa
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_hm_remediation_failed(self, ticket_id: str, error_msg: str):
        log_msg = f"[SOAR AUTO-REMEDIATION ALERTA] Fallo en caso #{ticket_id}: {error_msg}"
        log_to_file(log_msg)
        ejecutar_beep(450, 500)
        self.enviar_notificacion_popup(
            f"⚠️ Atención: Caso #{ticket_id}",
            f"No se auto-resolvió: {error_msg[:120]}"
        )
        # Refrescar para ver el caso asignado
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_translate_remediation_finished(self, result: dict):
        t_id = result.get("ticket_id", "N/A")
        users = ", ".join(result.get("users", [])) or "Usuario corporativo"
        hosts = ", ".join(result.get("hosts", [])) or "Host"
        count = result.get("alert_count", 1)
        log_msg = f"[SOAR TRANSLATE] Caso #{t_id} RESUELTO EXITOSAMENTE (False Positive) | Host: {hosts} | Usuarios: {users} | Alertas: {count}"
        log_to_file(log_msg)
        ejecutar_beep(850, 200)
        ejecutar_beep(1150, 250)
        self.enviar_notificacion_popup(
            f"⚡ Caso #{t_id} Auto-Remediado",
            f"WebControl Google Translate verificado ({hosts} / {users}). Cerrado como False Positive."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(t_id) not in self._mobile_notified_auto_closed:
                self._mobile_notified_auto_closed.add(str(t_id))
                MobileAlertsNotifier.send_notification(
                    title=f"[AUTO-REMEDIADO] Caso #{t_id} (Translate)",
                    message=f"Caso #{t_id} ({hosts} / {users}) cerrado automáticamente como False Positive.\nDestino: translate.google.com ({count} alertas mitigadas).",
                    priority="default",
                    tags="robot,check"
                )
        if str(t_id) in self.dict_casos_activos:
            self.dict_casos_activos[str(t_id)]["status"] = "Resolved"
            self.dict_casos_activos[str(t_id)]["resolution"] = "False Positive"
        if hasattr(self, '_last_cases_data'):
            for c in self._last_cases_data.get("cases", {}).get("data", {}).get("cases", []):
                if str(c.get("ticket_id")) == str(t_id):
                    c["status"] = "Resolved"
                    c["resolution"] = "False Positive"
                    break
        self.display_cases_results_wrapper()
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_translate_remediation_failed(self, ticket_id: str, error_msg: str):
        log_msg = f"[SOAR TRANSLATE ERROR] Fallo en caso #{ticket_id}: {error_msg}"
        log_to_file(log_msg)
        ejecutar_beep(450, 500)
        self.enviar_notificacion_popup(
            f"⚠️ Atención: Caso #{ticket_id}",
            f"No se auto-resolvió WebControl: {error_msg[:120]}"
        )
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_non_translate_detected(self, alert_info: dict):
        t_id = alert_info.get("ticket_id", "N/A")
        users = ", ".join(alert_info.get("users", [])) or "Desconocido"
        hosts = ", ".join(alert_info.get("hosts", [])) or "Desconocido"
        details = alert_info.get("details", "")
        log_msg = f"[SOAR TRANSLATE ALERTA CRÍTICA] Caso #{t_id} ({hosts} / {users}) NO ES GOOGLE TRANSLATE: {details}. Asignado para triaje manual."
        log_to_file(log_msg)
        ejecutar_beep(1000, 300)
        ejecutar_beep(600, 400)
        self.enviar_notificacion_popup(
            f"⚠️ ALERTA: Caso #{t_id} NO es Google Translate",
            f"Host: {hosts} | Usuario: {users}\nActividad detectada: {details[:120]}\nRequiere análisis manual."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            MobileAlertsNotifier.send_notification(
                title=f"⚠️ [ATENCIÓN] Caso #{t_id} WebControl NO es Translate",
                message=f"Host: {hosts} | Usuario: {users}\nActividad: {details}\nEl caso NO fue auto-cerrado y quedó asignado en 'In Progress' para tu revisión.",
                priority="high",
                tags="warning,rotating_light"
            )
        self.display_cases_results_wrapper()
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_sati_remediation_finished(self, result: dict):
        t_id = result.get("ticket_id", "N/A")
        users = ", ".join(result.get("users", [])) or "sati"
        hosts = ", ".join(result.get("hosts", [])) or "Estacion remota"
        count = result.get("alert_count", 1)
        log_msg = f"[SOAR SATI] Caso #{t_id} RESUELTO EXITOSAMENTE (False Positive) | Host: {hosts} | Usuario: {users} | Alertas: {count}"
        log_to_file(log_msg)
        ejecutar_beep(850, 200)
        ejecutar_beep(1200, 250)
        self.enviar_notificacion_popup(
            f"Caso #{t_id} Auto-Remediado (SATI)",
            f"Falso positivo operacional DNS VPN verificado ({hosts} / {users}). Cerrado como False Positive."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(t_id) not in self._mobile_notified_auto_closed:
                self._mobile_notified_auto_closed.add(str(t_id))
                MobileAlertsNotifier.send_notification(
                    title=f"[AUTO-REMEDIADO] Caso #{t_id} (SATI VPN)",
                    message=f"Caso #{t_id} ({hosts} / {users}) cerrado automaticamente como False Positive.\nConsultas DNS denegadas por failover ({count} alertas mitigadas).",
                    priority="default",
                    tags="robot,check"
                )
        if str(t_id) in self.dict_casos_activos:
            self.dict_casos_activos[str(t_id)]["status"] = "Resolved"
            self.dict_casos_activos[str(t_id)]["resolution"] = "False Positive"
        if hasattr(self, '_last_cases_data'):
            for c in self._last_cases_data.get("cases", {}).get("data", {}).get("cases", []):
                if str(c.get("ticket_id")) == str(t_id):
                    c["status"] = "Resolved"
                    c["resolution"] = "False Positive"
                    break
        self.display_cases_results_wrapper()
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_sati_remediation_failed(self, ticket_id: str, error_msg: str):
        log_msg = f"[SOAR SATI ERROR] Fallo en caso #{ticket_id}: {error_msg}"
        log_to_file(log_msg)
        ejecutar_beep(450, 500)
        self.enviar_notificacion_popup(
            f"Atencion: Caso #{ticket_id}",
            f"No se auto-resolvio SATI VPN: {error_msg[:120]}"
        )
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_non_sati_dns_detected(self, alert_info: dict):
        t_id = alert_info.get("ticket_id", "N/A")
        users = ", ".join(alert_info.get("users", [])) or "Desconocido"
        hosts = ", ".join(alert_info.get("hosts", [])) or "Desconocido"
        details = alert_info.get("details", "")
        log_msg = f"[SOAR SATI ALERTA CRITICA] Caso #{t_id} ({hosts} / {users}) CONTIENE ACTIVIDAD NO DNS O NO SATI: {details}. Asignado para triaje manual."
        log_to_file(log_msg)
        ejecutar_beep(1000, 300)
        ejecutar_beep(600, 400)
        self.enviar_notificacion_popup(
            f"ALERTA: Caso #{t_id} SATI Sospechoso",
            f"Host: {hosts} | Usuario: {users}\nActividad denegada fuera de DNS: {details[:120]}\nRequiere analisis manual."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            MobileAlertsNotifier.send_notification(
                title=f"[ATENCION] Caso #{t_id} SATI Sospechoso",
                message=f"Host: {hosts} | Usuario: {users}\nActividad denegada fuera de DNS: {details}\nEl caso requiere triaje manual inmediato.",
                priority="high",
                tags="warning,rotating_light"
            )
        self.display_cases_results_wrapper()
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_dpapi_remediation_finished(self, result: dict):
        t_id = result.get("ticket_id", "N/A")
        users = ", ".join(result.get("users", [])) or "Usuario corporativo"
        hosts = ", ".join(result.get("hosts", [])) or "VMBASE8"
        count = result.get("alert_count", 1)
        log_msg = f"[SOAR DPAPI] Caso #{t_id} RESUELTO EXITOSAMENTE (False Positive) | Host: {hosts} | Usuario: {users} | Alertas: {count}"
        log_to_file(log_msg)
        ejecutar_beep(850, 200)
        ejecutar_beep(1200, 250)
        self.enviar_notificacion_popup(
            f"⚡ Caso #{t_id} Auto-Remediado (DPAPI)",
            f"Falso positivo DPAPI protected_storage verificado ({hosts} / {users}). Cerrado como False Positive."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(t_id) not in self._mobile_notified_auto_closed:
                self._mobile_notified_auto_closed.add(str(t_id))
                MobileAlertsNotifier.send_notification(
                    title=f"[AUTO-REMEDIADO] Caso #{t_id} (DPAPI)",
                    message=f"Caso #{t_id} ({hosts} / {users}) cerrado automáticamente como False Positive.\nSincronización legítima Windows DPAPI ({count} alertas mitigadas).",
                    priority="default",
                    tags="robot,check"
                )
        if str(t_id) in self.dict_casos_activos:
            self.dict_casos_activos[str(t_id)]["status"] = "Resolved"
            self.dict_casos_activos[str(t_id)]["resolution"] = "False Positive"
        if hasattr(self, '_last_cases_data'):
            for c in self._last_cases_data.get("cases", {}).get("data", {}).get("cases", []):
                if str(c.get("ticket_id")) == str(t_id):
                    c["status"] = "Resolved"
                    c["resolution"] = "False Positive"
                    break
        self.display_cases_results_wrapper()
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_dpapi_remediation_failed(self, ticket_id: str, error_msg: str):
        log_msg = f"[SOAR DPAPI ERROR] Fallo en caso #{ticket_id}: {error_msg}"
        log_to_file(log_msg)
        ejecutar_beep(450, 500)
        self.enviar_notificacion_popup(
            f"Atención: Caso #{ticket_id}",
            f"No se auto-resolvió DPAPI: {error_msg[:120]}"
        )
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_non_dpapi_detected(self, alert_info: dict):
        t_id = alert_info.get("ticket_id", "N/A")
        users = ", ".join(alert_info.get("users", [])) or "Desconocido"
        hosts = ", ".join(alert_info.get("hosts", [])) or "Desconocido"
        details = alert_info.get("details", "")
        log_msg = f"[SOAR DPAPI ALERTA CRÍTICA] Caso #{t_id} ({hosts} / {users}) CONTIENE ACTIVIDAD NO DPAPI: {details}. Asignado para triaje manual."
        log_to_file(log_msg)
        ejecutar_beep(1000, 300)
        ejecutar_beep(600, 400)
        self.enviar_notificacion_popup(
            f"⚠️ ALERTA: Caso #{t_id} DPAPI Sospechoso",
            f"Host: {hosts} | Usuario: {users}\nActividad fuera de protected_storage: {details[:120]}\nRequiere análisis manual."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            MobileAlertsNotifier.send_notification(
                title=f"⚠️ [ATENCIÓN] Caso #{t_id} DPAPI Sospechoso",
                message=f"Host: {hosts} | Usuario: {users}\nActividad fuera de protected_storage: {details}\nEl caso requiere triaje manual inmediato.",
                priority="high",
                tags="warning,rotating_light"
            )
        self.display_cases_results_wrapper()
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_auto_guardia_assigned(self, ticket_id: str, assignee: str):
        log_msg = f"[AUTO-GUARDIA SLA] Caso #{ticket_id} asignado con éxito a {assignee} para proteger el cumplimiento de MTTD."
        log_to_file(log_msg)
        ejecutar_beep(600, 250)
        self.enviar_notificacion_popup(
            f"🛡️ Auto-Guardia SLA: Caso #{ticket_id}",
            f"Caso asignado a ti para evitar expiración del MTTD."
        )
        if hasattr(self, 'check_mobile_alerts') and self.check_mobile_alerts.isChecked():
            if str(ticket_id) not in self._mobile_notified_assigned:
                self._mobile_notified_assigned.add(str(ticket_id))
                MobileAlertsNotifier.send_notification(
                    title=f"[AUTO-GUARDIA ASIGNADO] #{ticket_id}",
                    message=f"El caso #{ticket_id} ha sido auto-asignado a tu guardia para proteger el MTTD.",
                    priority="high",
                    tags="shield,briefcase"
                )
        QTimer.singleShot(1500, self.trigger_cases_refresh)

    def _on_auto_guardia_error(self, ticket_id: str, error_msg: str):
        log_to_file(f"[AUTO-GUARDIA SLA ERROR] No se pudo auto-asignar caso #{ticket_id}: {error_msg}")

    # =========================================================================
    # MOTOR DE DESPACHO DE NOTIFICACIONES PUSH MÓVILES (ntfy.sh)
    # =========================================================================
    def _process_mobile_notifications(self, raw_cases: list):
        """
        Evalúa y despacha notificaciones push móviles hacia ntfy.sh:
        1. Alerta temprana si POE / MTTD está en riesgo o vencido (casos libres).
        2. Alerta SLA si MTTR está en riesgo o vencido (casos asignados).
        3. Notificación cuando un caso es asignado a kevinmoraes@technoma.com.py.
        4. Notificación cuando ingresa un nuevo caso a la cola.
        Deduplicación 100% en RAM: Cero spam repetitivo en el celular.
        """
        if not hasattr(self, 'check_mobile_alerts') or not self.check_mobile_alerts.isChecked():
            return
        if not raw_cases:
            return

        initial_sync = not getattr(self, '_mobile_initial_sync_done', False)

        for c in raw_cases:
            t_id = str(c.get("ticket_id") or c.get("_id") or "").strip()
            if not t_id:
                continue
            
            st = str(c.get("status", "")).strip().lower()
            is_closed = st in ["resolved", "cancelled", "closed"]
            
            raw_assignee = c.get("assignee_name") or c.get("assignee")
            if not raw_assignee or str(raw_assignee).strip().lower() in ["unassigned", "none", "libre", ""]:
                assignee = "Libre"
            else:
                assignee = str(raw_assignee).strip()

            norm_score = SlaGovernanceEngine.normalize_score(c.get("score"))
            mttd_info = SlaGovernanceEngine.evaluate_mttd(c)
            mttr_info = SlaGovernanceEngine.evaluate_mttr(c)
            pri = mttd_info["priority"]
            name = str(c.get("name", "Sin Nombre")).strip()
            tenant = str(c.get("tenant_name", "Global")).strip()

            prev_info = self._case_history_status.get(t_id)

            # --- 1. DETECCIÓN DE NUEVOS CASOS EN COLA ---
            if initial_sync:
                self._seen_case_ids.add(t_id)
            else:
                if t_id not in self._seen_case_ids and not is_closed:
                    self._seen_case_ids.add(t_id)
                    MobileAlertsNotifier.send_notification(
                        title=f"[NUEVO CASO] #{t_id} ({pri})",
                        message=f"Nuevo incidente en cola: #{t_id} - {name}\nTenant: {tenant} | Score: {norm_score} | Asignado: {assignee}",
                        priority="default",
                        tags="new,ticket"
                    )

            # --- 2. DETECCIÓN DE CASO CERRADO / RESUELTO ---
            if not initial_sync and prev_info is not None:
                prev_st = prev_info.get("status", "")
                if prev_st not in ["resolved", "cancelled", "closed"] and is_closed:
                    if t_id not in self._mobile_notified_auto_closed:
                        self._mobile_notified_auto_closed.add(t_id)
                        res_val = c.get("resolution") or "Resuelto"
                        MobileAlertsNotifier.send_notification(
                            title=f"[CASO CERRADO] #{t_id} ({res_val})",
                            message=f"El caso #{t_id} ({name}) ha sido cerrado en el sistema.\nTenant: {tenant} | Estado: {st.capitalize()}",
                            priority="default",
                            tags="white_check_mark,clipboard"
                        )

            # --- 3. DETECCIÓN DE CASO ASIGNADO A KEVIN ---
            ass_lower = assignee.lower()
            is_assigned_to_me = (ass_lower == EMAIL_USUARIO.lower()) or ("kevin" in ass_lower and "moraes" in ass_lower) or ("kevin" in ass_lower)
            prev_ass = prev_info.get("assignee", "") if prev_info else ""
            if is_assigned_to_me and not is_closed:
                if t_id not in self._mobile_notified_assigned or (prev_ass and prev_ass != assignee):
                    self._mobile_notified_assigned.add(t_id)
                    if not initial_sync:
                        MobileAlertsNotifier.send_notification(
                            title=f"[CASO ASIGNADO] #{t_id} ({pri})",
                            message=f"Se te ha asignado el caso #{t_id} - {name}\nTenant: {tenant} | Score: {norm_score} | SLA MTTR: {mttr_info['limit_str']}",
                            priority="high",
                            tags="briefcase,bell"
                        )

            # Registrar estado en el historial en memoria para el siguiente ciclo
            self._case_history_status[t_id] = {"status": st, "assignee": assignee}

            if is_closed:
                continue

            # --- 3. POE / MTTD EN PELIGRO (Casos libres sin tomar) ---
            if assignee == "Libre":
                if mttd_info["breached"] or mttd_info["warning"]:
                    if t_id not in self._mobile_notified_mttd_risk:
                        self._mobile_notified_mttd_risk.add(t_id)
                        estado = "VENCIDO" if mttd_info["breached"] else "EN RIESGO"
                        prio = "urgent" if mttd_info["breached"] else "high"
                        MobileAlertsNotifier.send_notification(
                            title=f"[MTTD {estado}] #{t_id} ({pri})",
                            message=f"Alerta temprana POE: Caso #{t_id} ({name}) de {tenant} está {estado.lower()}.\nTiempo restante: {mttd_info['remaining_str']}. ¡Tomar de inmediato!",
                            priority=prio,
                            tags="warning,hourglass"
                        )

            # --- 4. MTTR EN PELIGRO (Casos en progreso o asignados) ---
            else:
                if mttr_info["breached"] or mttr_info["warning"]:
                    if t_id not in self._mobile_notified_mttr_risk:
                        self._mobile_notified_mttr_risk.add(t_id)
                        estado = "VENCIDO" if mttr_info["breached"] else "EN RIESGO"
                        prio = "urgent" if mttr_info["breached"] else "high"
                        MobileAlertsNotifier.send_notification(
                            title=f"[MTTR {estado}] #{t_id} ({pri})",
                            message=f"Alerta SLA MTTR: Caso #{t_id} ({name}) asignado a {assignee} está {estado.lower()}.\nTiempo restante: {mttr_info['remaining_str']} de {mttr_info['limit_str']}.",
                            priority=prio,
                            tags="warning,clock"
                        )

        if initial_sync:
            self._mobile_initial_sync_done = True

    def test_mobile_notification_action(self):
        """Dispara una notificación inmediata de comprobación hacia el teléfono móvil."""
        topic = MobileAlertsNotifier.get_topic()
        MobileAlertsNotifier.send_notification(
            title="Technoma SOC - Enlace Móvil OK",
            message=f"Prueba exitosa. Tu dispositivo móvil está recibiendo alertas del Cockpit en el canal '{topic}'.",
            priority="high",
            tags="shield,bell"
        )
        self.txt_triage.append(f"\n[*] Notificación push de prueba enviada al canal móvil: https://ntfy.sh/{topic}")
        self.enviar_notificacion_popup(
            "Notificación Móvil Enviada",
            f"Se envió una notificación push de prueba al canal:\nhttps://ntfy.sh/{topic}\n\nRevisa la app ntfy en tu teléfono móvil."
        )

    def display_top_protocols(self, top_apps):
        if hasattr(self.txt_protocols, "update_protocols"):
            self.txt_protocols.update_protocols(top_apps)
            return

        html_lines = []
        html_lines.append("<b style='color: #eab308;'>=========================================================</b>")
        html_lines.append("<b style='color: #ffffff;'>           TOP PROTOCOLOS / APLICACIONES ACTIVAS       </b>")
        html_lines.append("<b style='color: #eab308;'>=========================================================</b><br>")
        
        if not top_apps:
            html_lines.append("<span style='color: #9ca3af;'>No hay datos suficientes recientes en incidentes...</span>")
        else:
            for i, (app, count) in enumerate(top_apps, 1):
                html_lines.append(f"  <span style='color: #00ffff;'>#{i}</span> <span style='color: #ffffff;'>{app.ljust(30)}</span> <span style='color: #3b82f6;'>[{count} hits]</span>")
                
        self.txt_protocols.setHtml("<br>".join(html_lines))

    @Slot(dict)
    def display_health_results(self, data):
        html_lines = []
        sensores_caidos_alerta = []
        timestamp_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        raw_sensors = []
        tenants_data_consumo = []
        cuotas_diccionario = {}
        peak_global_real = 0.0
        nivel_uso_global_pct = 0.0
        
        try:
            sensors_payload = data.get("sensors", {})
            raw_sensors = sensors_payload.get("data", []) or sensors_payload.get("sensors", [])
            orden_deseado = ["Sensor-Modular-CajaAnde", "VMBASE8", "technoma-sensor", "modular"]
            
            def sort_key(s):
                h_name = s.get("hostname") or s.get("sensor_id") or s.get("internal_sensor_id") or ""
                return orden_deseado.index(h_name) if h_name in orden_deseado else 999
            raw_sensors.sort(key=sort_key)
            
            html_lines.append("<b style='color: #00ffff;'>=========================================================</b>")
            html_lines.append("<b style='color: #ec4899;'>         INVENTARIO COMPLETO DE SENSORES DE PRODUCCIÓN    </b>")
            html_lines.append("<b style='color: #00ffff;'>=========================================================</b><br>")
            
            total = len(raw_sensors)
            online, offline, warning, upgrade = 0, 0, 0, 0
            
            for idx, s in enumerate(raw_sensors, 1):
                os_type = s.get("os", "N/A")
                platform = s.get("platform", "N/A")
                mode = s.get("mode", "N/A")
                name = s.get("hostname") or s.get("sensor_id") or s.get("internal_sensor_id") or f"Server-Agent ({os_type} / {platform})"
                ip_local = s.get("local_ip_address", "N/A")
                ip_nat = s.get("nat_ip_address", "N/A")
                tenant = s.get("cust_name", "(sin tenant)")
                sw = s.get("sw_version", "N/A")
                profile = s.get("sensor_profile_name", "Default")
                feature = str(s.get("feature", "DS")).upper()
                
                cpu = safe_float(s.get("cpu_usage"))
                disk = safe_float(s.get("disk_usage"))
                in_bytes = format_bytes(s.get("inbytes_total"))
                out_bytes = format_bytes(s.get("outbytes_total"))
                
                if s.get("need_upgrade"):
                    need_upg = "<span style='color: #eab308;'>SI  &lt;-- ACTUALIZAR</span>"
                    upgrade += 1
                else:
                    need_upg = "<span style='color: #6b7280;'>No</span>"
                    
                raw_status = str(s.get("connection_status", "")).lower()
                if raw_status in ["connected", "online"]:
                    status_text, status_color = "[+] CONECTADO", "#22c55e"
                    online += 1
                    esta_conectado = True
                elif raw_status in ["warning", "degraded"]:
                    status_text, status_color = "[!] ALERTA", "#eab308"
                    warning += 1
                    esta_conectado = True
                else:
                    status_text, status_color = "[-] INACTIVO", "#ef4444"
                    offline += 1
                    esta_conectado = False
                    
                if name in orden_deseado:
                    if name not in self.estados_anteriores:
                        self.estados_anteriores[name] = esta_conectado
                    
                    if not self.primer_ciclo:
                        if self.estados_anteriores[name] and not esta_conectado:
                            log_to_file(f"[{timestamp_log}] [ALERTA] El sensor critico '{name}' se ha DESCONECTADO (Estado: {status_text})")
                            self.estados_anteriores[name] = False
                            self.enviar_notificacion_popup("ALERTA CRÍTICA - NOC INFRAESTRUCTURA", f"El servidor agente crítico '{name}' se ha DESCONECTADO del perímetro.")
                        elif not self.estados_anteriores[name] and esta_conectado:
                            log_to_file(f"[{timestamp_log}] [RECUPERADO] [RECUPERADO] El sensor critico '{name}' vuelve a estar ONLINE (Estado: {status_text})")
                            self.estados_anteriores[name] = True
                            self.enviar_notificacion_popup("NOC - INFRAESTRUCTURA ESTABLE", f"El servidor agente crítico '{name}' ha retornado ONLINE con éxito.")
                    
                    if not esta_conectado:
                        sensores_caidos_alerta.append(name)
                    
                # V3-03: html.escape() en todos los valores provenientes de la API (anti-XSS)
                name_h    = he(str(name))
                tenant_h  = he(str(tenant))
                profile_h = he(str(profile))
                feature_h = he(str(feature))
                mode_h    = he(str(mode))
                ip_local_h = he(str(ip_local))
                ip_nat_h  = he(str(ip_nat))
                sw_h      = he(str(sw))

                html_lines.append(f"  <span style='color: #00ffff;'>SENSOR #{idx}</span> <span style='color: #6b7280;'>-------------------------------------------------------------</span>")
                html_lines.append(f"  Nombre      : <span style='color: #ffffff;'>{name_h}</span>")
                html_lines.append(f"  Estado      : <span style='color: {status_color}; font-weight: bold;'>{status_text}</span>")
                html_lines.append(f"  Tenant      : {tenant_h}   |  Perfil: {profile_h}   |  Tipo: {feature_h}  ({mode_h})")
                html_lines.append(f"  IP Local    : {ip_local_h}   |  IP NAT: {ip_nat_h} | Version SW: {sw_h}")
                html_lines.append(f"  Necesita SW : {need_upg}")

                if cpu is not None:
                    cpu_color = "#ef4444" if cpu > 90 else ("#eab308" if cpu > 70 else "#22c55e")
                    html_lines.append(f"  CPU         : <span style='color: {cpu_color};'>{get_bar(cpu)} {cpu:.1f}%</span>")
                else: html_lines.append("  CPU         : <span style='color: #6b7280;'>[N/A]</span>")

                if disk is not None:
                    dsk_color = "#ef4444" if disk > 85 else ("#eab308" if disk > 65 else "#22c55e")
                    html_lines.append(f"  Disco       : <span style='color: {dsk_color};'>{get_bar(disk)} {disk:.1f}%</span>")
                else: html_lines.append("  Disco       : <span style='color: #6b7280;'>[N/A]</span>")

                html_lines.append(f"  Trafico     : Recibido = <span style='color: #ffffff;'>{in_bytes}</span>   |   Enviado al DP = <span style='color: #ffffff;'>{out_bytes}</span><br>")

            # Resumen Ejecutivo
            html_lines.append("<b style='color: #00ffff;'>=========================================================</b>")
            html_lines.append("<b style='color: #00ffff;'>  RESUMEN EJECUTIVO - ESTADO GENERAL DEL PARQUE DE SENSORES</b>")
            html_lines.append("<b style='color: #00ffff;'>=========================================================</b><br>")
            html_lines.append(f"  Total Sensores  : <span style='color: #ffffff;'>{total}</span>")
            html_lines.append(f"  <span style='color: #22c55e;'>[+] Conectados  : {online}</span>")
            html_lines.append(f"  <span style='color: #ef4444;'>[-] Inactivos   : {offline}</span>")
            html_lines.append(f"  <span style='color: #eab308;'>[!] En Alerta   : {warning}</span>")
            html_lines.append(f"  <span style='color: #eab308;'>[^] Con Upgrade : {upgrade}</span><br>")
             
            if total > 0:
                pct = (online / total) * 100
                bar_color = "#22c55e" if pct > 90 else ("#eab308" if pct > 70 else "#ef4444")
                html_lines.append(f"  Disponibilidad  : <span style='color: {bar_color};'>{get_bar(pct, 25)} ({pct:.1f}% de conectividad)</span><br>")
                 
            if sensores_caidos_alerta:
                ejecutar_beep(800, 400)
        except Exception:
            pass

        # --- BLOQUE 2: Pozo Global --- (indentación correcta: mismo nivel que try anterior)
        try:
            cuotas_diccionario = {}
            lista_t = data["tenants"].get("tenants", []) or data["tenants"].get("data", [])
            for t in lista_t:
                cuotas_diccionario[t.get("cust_name")] = int(t.get("ingestion_limit", 0)) if t.get("ingestion_limit") is not None else 0

            tenants_data_consumo = data["usage"].get("data", [])
            if tenants_data_consumo:
                html_lines.append("<span style='color: #00ffff;'>-------------------------------------------------------------------------</span>")
                html_lines.append("<b style='color: #00ffff;'>  AUDITORIA DE LICENCIAS - CAPACIDAD DE INGESTA DIARIA ASIGNADA</b>")
                html_lines.append("<span style='color: #00ffff;'>-------------------------------------------------------------------------</span><br>")
                total_licencia_distributed = 0
                for t in tenants_data_consumo:
                    t_name = t.get("tenant_name", "")
                    if t_name == "All Tenants": continue
                    limite_asignado = cuotas_diccionario.get(t_name, 0)
                    total_licencia_distributed += limite_asignado
                    t_name_h = he(str(t_name))
                    html_lines.append(f"  - Tenant: <span style='color: #ffffff;'>{t_name_h.ljust(15)}</span> | Limite Asignado: <span style='color: #eab308;'>{limite_asignado} GB/dia</span>")
                html_lines.append(f"<br>  Capacidad Total Distribuida: <span style='color: #ffffff;'>{total_licencia_distributed} GB/dia parametrizados.</span><br>")

                html_lines.append("<span style='color: #00ffff;'>-------------------------------------------------------------------------</span>")
                html_lines.append("<b style='color: #ffffff; background-color: #00557f;'>  CUADRO DE MANDO: REPORTE DE CONSUMO DE POZO GLOBAL (DYNAMIC POOLING)  </b>")
                html_lines.append("<span style='color: #00ffff;'>-------------------------------------------------------------------------</span><br>")
                obj_all_tenants = next((item for item in tenants_data_consumo if item.get("tenant_name") == "All Tenants"), None)
                if obj_all_tenants and "daily_usage" in obj_all_tenants:
                    valores_globales = [safe_float(day.get("usage")) for day in obj_all_tenants.get("daily_usage", []) if safe_float(day.get("usage")) is not None]
                    if valores_globales:
                        peak_global_real = max(valores_globales)
                        nivel_uso_global_pct = (peak_global_real / CUOTA_POOL_GLOBAL) * 100
                        html_lines.append(f"  <span style='color: #6b7280;'>[ESTADO DEL CONTRATO GLOBAL (POOL)]</span>")
                        html_lines.append(f"  - Capacidad Total del Pozo  : <span style='color: #00ffff;'>{CUOTA_POOL_GLOBAL} GB/dia</span>")
                        html_lines.append(f"  - Consumo Pico Real (Peak)  : <span style='color: #ffffff;'>{peak_global_real:.4f} GB</span>")
                        if nivel_uso_global_pct > 100:
                            html_lines.append(f"  - Nivel de Uso de Licencia  : <span style='color: #ffffff; background-color: #ef4444; font-weight: bold;'>{nivel_uso_global_pct:.1f}%</span> <span style='color: #ef4444;'>&lt;-- POZO DESBORDADO / EXCESO CRITICO</span>")
                            if not self.pool_excedido_anterior:
                                log_to_file(f"[{timestamp_log}] [ALERTA LICENCIA] El pozo global de licencias ingreso en sobreconsumo ({nivel_uso_global_pct:.1f}% de uso).")
                                self.pool_excedido_anterior = True
                                if not self.primer_ciclo:
                                    self.enviar_notificacion_popup("AVISO SOC - SOBRECONSUMO DE LICENCIA", f"Atención: Se ha superado el pozo de ingesta de la organización. Nivel actual: {nivel_uso_global_pct:.1f}%. Playbook 6.3 activado.")
                        else:
                            html_lines.append(f"  - Nivel de Uso de Licencia  : <span style='color: #22c55e;'>{nivel_uso_global_pct:.1f}%</span>")
                            if self.pool_excedido_anterior:
                                log_to_file(f"[{timestamp_log}] [ESTABLE LICENCIA] El pozo global retornó a parámetros normales ({nivel_uso_global_pct:.1f}% de uso).")
                                self.pool_excedido_anterior = False
                                if not self.primer_ciclo:
                                    self.enviar_notificacion_popup("SOC - LICENCIA INFRAESTRUCTURA", "El volumen de ingesta del pozo global ha retornado dentro de los márgenes estables.")

                        # Disparador central Playbook 6.3: Detección, Bitácora TSV y Ticket
                        self._procesar_playbook_63_ingesta(tenants_data_consumo, cuotas_diccionario, peak_global_real, nivel_uso_global_pct, timestamp_log)
                        html_lines.append("")

                html_lines.append("  <span style='color: #6b7280;'>[DESGLOSE DE INGESTA DIARIA ACTUAL Y RECORD DE POZO (PEAK)]</span>")
                for tenant in tenants_data_consumo:
                    t_name = tenant.get("tenant_name", "")
                    if t_name == "All Tenants": continue
                    t_name_h = he(str(t_name))
                    daily_array = tenant.get("daily_usage", [])
                    consumo_hoy = float(daily_array[-1].get("usage", 0.0)) if daily_array else 0.0
                    valores_diarios = [safe_float(day.get("usage")) for day in daily_array if safe_float(day.get("usage")) is not None]
                    peak_usage_tenant = max(valores_diarios) if valores_diarios else 0.0
                    acumulado_mes = float(tenant.get("monthly_usage", 0.0))
                    html_lines.append(f"  • <span style='color: #ffffff;'>{t_name_h.ljust(12)}</span> | Hoy: <span style='color: #00ffff;'>{consumo_hoy:.4f} GB</span> | Pico Max: <span style='color: #eab308;'>{peak_usage_tenant:.4f} GB</span> | Mes: <span style='color: #6b7280;'>{acumulado_mes:.2f} GB</span>")

                html_lines.append("")
                html_lines.append("<span style='color: #a855f7;'>-------------------------------------------------------------------------</span>")
                html_lines.append("<b style='color: #a855f7;'>  ACCESO RÁPIDO: CENTRO DE TELEMETRÍA, CONECTORES & LOG FILTERS</b>")
                html_lines.append("<span style='color: #a855f7;'>-------------------------------------------------------------------------</span>")
                html_lines.append("  • <i>Haga clic en <b>'🔍 Telemetría & Log Filters'</b> en la barra inferior para ver el desglose en tiempo real por sensor/tipo de log, salud de conectores y auditoría de los 65 filtros con detección de cegueras SOC.</i><br>")
        except Exception:
            pass

        # --- CIERRE: render y flag ---
        if hasattr(self.txt_health, "update_telemetry"):
            try:
                self.txt_health.update_telemetry(
                    raw_sensors=raw_sensors,
                    tenants_data_consumo=tenants_data_consumo,
                    cuotas_diccionario=cuotas_diccionario,
                    peak_global_real=peak_global_real,
                    nivel_uso_global_pct=nivel_uso_global_pct,
                    cuota_pool_global=CUOTA_POOL_GLOBAL
                )
            except Exception:
                self.txt_health.setHtml("<br>".join(html_lines))
        else:
            self.txt_health.setHtml("<br>".join(html_lines))
        self.primer_ciclo = False

    def enviar_notificacion_popup(self, titulo, mensaje):
        from PySide6.QtWidgets import QMessageBox
        from PySide6.QtCore import Qt
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setWindowModality(Qt.NonModal)
        msg_box.show()

    # =========================================================================
    # PLAYBOOK 6.3: GESTIÓN DE CAPACIDAD DE INGESTA, BITÁCORA Y TICKETS
    # =========================================================================
    def _procesar_playbook_63_ingesta(self, tenants_data_consumo: list, cuotas_diccionario: dict, peak_global_real: float, nivel_uso_global_pct: float, timestamp_log: str):
        """
        Automatización integral del Playbook 6.3 (Agente o cliente supera capacidad de ingesta).
        Identifica automáticamente al tenant causal, formula el ticket de escalación a N2,
        genera la fila de 18 columnas para la Bitácora del SOC (TSV) y despacha notificación push móvil.
        """
        try:
            # 1. Identificar el tenant que genera el mayor exceso respecto a su cuota
            culprit_tenant = "technoma"
            max_excess = -999999.0
            culprit_usage = 0.0
            culprit_limit = 8.0
            desglose_tenants_lines = []

            for tenant in tenants_data_consumo:
                t_name = tenant.get("tenant_name", "")
                if t_name == "All Tenants":
                    continue
                daily_array = tenant.get("daily_usage", [])
                consumo_hoy = float(daily_array[-1].get("usage", 0.0)) if daily_array else 0.0
                limite = float(cuotas_diccionario.get(t_name, 0))
                exceso = consumo_hoy - limite
                pct_tenant = (consumo_hoy / limite * 100.0) if limite > 0 else 0.0
                estado_txt = "DESBORDADO" if consumo_hoy > limite else "NORMAL"
                desglose_tenants_lines.append(f"  • Tenant '{t_name}': {consumo_hoy:.4f} GB/día (Límite: {limite:.1f} GB/día - {pct_tenant:.1f}%) [{estado_txt}]")

                if exceso > max_excess:
                    max_excess = exceso
                    culprit_tenant = t_name
                    culprit_usage = consumo_hoy
                    culprit_limit = limite

            es_critico = (nivel_uso_global_pct > 100.0)
            es_advertencia = (nivel_uso_global_pct >= 85.0)

            # 2. Formular la estructura formal de Ticket THN-SOC (Playbook 6.3)
            fecha_ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            suffix_dia = datetime.now().strftime("%Y%m%d")
            ticket_id = f"THN-SOC-ING-{suffix_dia}"
            prioridad = "Alta 🔴" if es_critico else "Media 🟡"

            desc_narrativa = (
                f"Detección de anomalía volumétrica en la plataforma Stellar Cyber OpenXDR superando el límite contratado "
                f"del pozo global ({CUOTA_POOL_GLOBAL:.1f} GB/día), alcanzando un pico de {peak_global_real:.4f} GB "
                f"({nivel_uso_global_pct:.1f}% de utilización operativa).\n\n"
                f"Conforme a la Fase 1 del Playbook 6.3, se identificó en el módulo de Licensing que el principal generador del "
                f"sobreconsumo es el Tenant '{culprit_tenant}', el cual registró un volumen de {culprit_usage:.4f} GB/día sobre su límite "
                f"asignado de {culprit_limit:.1f} GB/día ({(culprit_usage/culprit_limit*100) if culprit_limit else 0:.1f}% de su cuota)."
            )

            evidencia_tecnica = (
                f"Consola Central Stellar Cyber OpenXDR — Módulo de Licenciamiento y Capacidad (Licensing / Volume Usage):\n"
                f"• Estado del Pozo Global: {peak_global_real:.4f} GB / {CUOTA_POOL_GLOBAL:.1f} GB ({nivel_uso_global_pct:.1f}% de capacidad contratada)\n"
                + "\n".join(desglose_tenants_lines) + "\n\n"
                f"Auditoría técnica de fuentes de tráfico y telemetría (Sensor Modular {culprit_tenant}-sensor 192.168.15.70):\n"
                f"1. Ráfagas masivas de consultas DNS locales (UDP 53) entre Controladores de Dominio (10.11.1.1 <-> 10.11.1.2) "
                f"generando alertas repetitivas de tráfico Interflow.\n"
                f"2. Bucle de Denegaciones en Firewall Interno (Action: Deny) desde 10.212.134.201 y 192.168.169.8.\n"
                f"3. Ráfagas de eventos Windows Event ID 4776 (Validación de credenciales NTLM) de sondas HealthMailbox hacia VM-MARANDU.\n"
                f"4. Sensor modular con modo de captura completa activado en perfil 'profile-modular-sensor-technoma'."
            )

            solicitud_accion = (
                f"Acciones de Contención y Mitigación N2 / Ingeniería (Playbook 6.3 - Fases 2 y 3):\n"
                f"1. Pre-DPI / Drop Rule: Incorporar en el perfil del sensor modular regla de descarte para tráfico DNS entre los DCs (host 10.11.1.1 and host 10.11.1.2 and udp 53).\n"
                f"2. Filtrado de Logs: Ajustar regla de descarte en el colector central para denegaciones repetitivas de firewall en puertos no críticos y ráfagas de Event ID 4776.\n"
                f"3. Tuning de Sensor: Evaluar optimización de captura de logs crudos en el colector de Technoma.\n"
                f"4. Validación y Cierre: Monitorear en el panel de Licensing la normalización del consumo diario por debajo de {culprit_limit:.1f} GB/día."
            )

            self.last_ingestion_ticket_data = {
                "ticket_id": ticket_id,
                "prioridad": prioridad,
                "tenant": culprit_tenant,
                "id_caso": "N/A",
                "fuente_deteccion": "Stellar Cyber",
                "tipo_evento": f"Capacidad Ingesta Excedida ({nivel_uso_global_pct:.1f}%)",
                "asunto": f"[SALUD SOC] - Exceso de Ingesta en Tenant {culprit_tenant} ({nivel_uso_global_pct:.1f}% Pozo Global)",
                "activos": f"Plataforma Stellar Cyber OpenXDR / Tenant: {culprit_tenant} (Pozo Global {CUOTA_POOL_GLOBAL:.1f} GB/día)",
                "descripcion": desc_narrativa,
                "evidencia": evidencia_tecnica,
                "solicitud_accion": solicitud_accion,
                "estado": "En Seguimiento",
                "url": f"https://{HOST}/#/system/licensing",
                "gen_ticket": "SI",
                "ticket_ext": ticket_id,
                "playbook": "Playbook 6.3",
                "analista": EMAIL_USUARIO or "Kevin Moraes",
                "fecha_hora": fecha_ahora
            }

            # 3. Generar la Fila Oficial de Bitácora de 18 Columnas (TSV)
            self.last_ingestion_bitacora_row = TechnomaTicketEngine.to_bitacora_row(self.last_ingestion_ticket_data)

            # 3B. Auto-exportar documento formal en PDF
            try:
                dir_pdf = os.path.join(SCRIPT_DIR, "tickets_pdf")
                os.makedirs(dir_pdf, exist_ok=True)
                pdf_file = os.path.join(dir_pdf, f"{ticket_id}.pdf")
                TechnomaTicketEngine.export_to_pdf(self.last_ingestion_ticket_data, pdf_file)
                self.last_ingestion_pdf_path = pdf_file
            except Exception as ex_pdf:
                log_to_file(f"[PDF AUTO-EXPORT ERROR]: {ex_pdf}")

            # 4. Actualizar badge y botones de la UI en el panel Health
            if hasattr(self, 'lbl_ingestion_badge'):
                if es_critico:
                    self.lbl_ingestion_badge.setText(f"🔴 SOBRECONSUMO ({nivel_uso_global_pct:.1f}%)")
                    self.lbl_ingestion_badge.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 11px; background-color: #ef4444; padding: 4px 8px; border-radius: 3px; border: 1px solid #ef4444; font-family: 'Consolas';")
                    self.btn_copiar_bitacora_ingesta.setEnabled(True)
                    self.btn_abrir_ticket_ingesta.setEnabled(True)
                    if hasattr(self, 'btn_export_pdf_ingesta'):
                        self.btn_export_pdf_ingesta.setEnabled(True)
                elif es_advertencia:
                    self.lbl_ingestion_badge.setText(f"🟡 ADVERTENCIA ({nivel_uso_global_pct:.1f}%)")
                    self.lbl_ingestion_badge.setStyleSheet("color: #0f172a; font-weight: bold; font-size: 11px; background-color: #eab308; padding: 4px 8px; border-radius: 3px; border: 1px solid #ca8a04; font-family: 'Consolas';")
                    self.btn_copiar_bitacora_ingesta.setEnabled(True)
                    self.btn_abrir_ticket_ingesta.setEnabled(True)
                    if hasattr(self, 'btn_export_pdf_ingesta'):
                        self.btn_export_pdf_ingesta.setEnabled(True)
                else:
                    self.lbl_ingestion_badge.setText(f"🟢 INGESTA NORMAL ({nivel_uso_global_pct:.1f}%)")
                    self.lbl_ingestion_badge.setStyleSheet("color: #10b981; font-weight: bold; font-size: 11px; background-color: #064e3b; padding: 4px 8px; border-radius: 3px; border: 1px solid #10b981; font-family: 'Consolas';")
                    self.btn_copiar_bitacora_ingesta.setEnabled(True)
                    self.btn_abrir_ticket_ingesta.setEnabled(True)
                    if hasattr(self, 'btn_export_pdf_ingesta'):
                        self.btn_export_pdf_ingesta.setEnabled(True)

            # 5. Si está desbordado, persistir automáticamente en bitacora_auto_export.tsv
            if es_critico:
                self._persistir_bitacora_auto(self.last_ingestion_bitacora_row, ticket_id)

                # Despachar notificación push móvil a ntfy (máximo 1 vez por día por evento)
                hoy_iso = datetime.now().strftime("%Y-%m-%d")
                if self.last_ingestion_alert_dispatched_date != hoy_iso:
                    self.last_ingestion_alert_dispatched_date = hoy_iso
                    msg_push = (
                        f"Pozo Global al {nivel_uso_global_pct:.1f}% (Pico: {peak_global_real:.2f} GB / {CUOTA_POOL_GLOBAL:.1f} GB).\n"
                        f"Tenant causal: {culprit_tenant} ({culprit_usage:.2f} GB vs límite {culprit_limit:.1f} GB).\n"
                        f"Playbook 6.3 ejecutado. Registro listo para Bitácora, Ticket y PDF en Cockpit."
                    )
                    MobileNotificationDispatcher.send_notification(
                        title="🚨 [SALUD SOC] Exceso de Ingesta Stellar Cyber",
                        message=msg_push,
                        priority="urgent",
                        tags="warning,fire"
                    )
                    log_to_file(f"[{timestamp_log}] [PUSH DISPATCH] Alerta Playbook 6.3 enviada a ntfy ({culprit_tenant} al {nivel_uso_global_pct:.1f}%).")

        except Exception as ex:
            log_to_file(f"[{timestamp_log}] [ERROR PLAYBOOK 6.3 INGESTA]: {ex}")

    def _copiar_bitacora_ingesta_clip(self):
        """Copia al portapapeles la fila TSV de 18 columnas para la Bitácora oficial del SOC."""
        if not self.last_ingestion_bitacora_row:
            QMessageBox.warning(self, "Aviso", "Aún no se ha completado el cálculo de métricas de ingesta.")
            return
        QApplication.clipboard().setText(self.last_ingestion_bitacora_row)
        self.btn_copiar_bitacora_ingesta.setText("✅ ¡Fila Bitácora Copiada!")
        QTimer.singleShot(3000, lambda: self.btn_copiar_bitacora_ingesta.setText("📋 Copiar Bitácora (PB 6.3)"))
        QMessageBox.information(
            self,
            "Bitácora Copiada (1-Clic TSV)",
            "La fila de 18 columnas de Playbook 6.3 ha sido copiada al portapapeles con éxito.\n\n"
            "Vaya a la hoja de cálculo de Bitácora del SOC (Excel o Google Sheets),\n"
            "seleccione la celda en la Columna A de la fila deseada y presione Ctrl+V."
        )

    def _abrir_ticket_ingesta_dialog(self):
        """Abre la ventana interactiva del Generador de Tickets con los datos pre-cargados (vía SOCWindowManager sin bloqueo modal)."""
        if not self.last_ingestion_ticket_data:
            QMessageBox.warning(self, "Aviso", "No hay datos de sobreconsumo disponibles.")
            return
        try:
            self.window_manager.open_module(
                module_key="thn_ticket_ingesta_pb63",
                title="🎫 Ticket de Escalación N2 (Playbook 6.3 Sobreconsumo) — Technoma SOC",
                short_title="🎫 Ticket PB 6.3",
                accent_color=ui_theme.COLOR_CRITICAL,
                factory_fn=lambda: TechnomaTicketGeneratorDialog(None, initial_data=self.last_ingestion_ticket_data),
                default_size=(1180, 820),
                force_recreate=True
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el ticket de escalación: {e}")

    def _abrir_pdf_ingesta(self):
        """Abre o exporta el ticket formal de Playbook 6.3 en documento PDF."""
        if not self.last_ingestion_ticket_data:
            QMessageBox.warning(self, "Aviso", "No hay datos de sobreconsumo disponibles para exportar.")
            return

        pdf_path = getattr(self, "last_ingestion_pdf_path", "")
        if not pdf_path or not os.path.exists(pdf_path):
            dir_pdf = os.path.join(SCRIPT_DIR, "tickets_pdf")
            os.makedirs(dir_pdf, exist_ok=True)
            ticket_id = self.last_ingestion_ticket_data.get("ticket_id", "THN-SOC-INGESTA")
            pdf_path = os.path.join(dir_pdf, f"{ticket_id}.pdf")
            try:
                TechnomaTicketEngine.export_to_pdf(self.last_ingestion_ticket_data, pdf_path)
                self.last_ingestion_pdf_path = pdf_path
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo generar el PDF: {e}")
                return

        ret = QMessageBox.question(
            self,
            "Ticket en PDF Generado",
            f"El documento formal en PDF se encuentra disponible en:\n\n{pdf_path}\n\n"
            "¿Desea abrir el archivo PDF ahora?",
            QMessageBox.Yes | QMessageBox.No
        )
        if ret == QMessageBox.Yes:
            QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def _abrir_auditoria_ingesta_dialog(self):
        """Abre la ventana interactiva de Auditoría Forense de Ingesta, Conectores y Log Filters (vía SOCWindowManager sin bloqueo modal)."""
        try:
            from ingestion_audit_dialog import IngestionAuditDialog
            self.window_manager.open_module(
                module_key="ingestion_audit",
                title="📊 Centro de Auditoría Forense de Ingesta, Conectores & Log Filters — Technoma SOC",
                short_title="📊 Ingesta & Cuota",
                accent_color=ui_theme.ACCENT_PRIMARY,
                factory_fn=lambda: IngestionAuditDialog(None),
                default_size=(1380, 860)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el Centro de Auditoría de Ingesta: {e}")

    def open_log_filter_creator(self):
        """Abre la ventana interactiva del Creador y Gestor de Log Filters Quirúrgicos (vía SOCWindowManager sin bloqueo modal)."""
        try:
            from log_filter_creator_dialog import LogFilterCreatorDialog
            self.window_manager.open_module(
                module_key="log_filter_creator",
                title="🛡️ Creador y Gestor de Log Filters Quirúrgicos (API Stellar Cyber)",
                short_title="➕ Creador Log Filters",
                accent_color=ui_theme.ACCENT_CYBER,
                factory_fn=lambda: LogFilterCreatorDialog(None),
                default_size=(1060, 740)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error Creador de Filtros", f"No se pudo abrir el Creador de Log Filters:\n\n{e}")

    def _persistir_bitacora_auto(self, tsv_row: str, ticket_id: str):
        """Guarda persistentemente el registro de bitácora generado en bitacora_auto_export.tsv."""
        try:
            archivo_tsv = os.path.join(SCRIPT_DIR, "bitacora_auto_export.tsv")
            existe = os.path.exists(archivo_tsv)
            hoy_str = datetime.now().strftime("%d/%m/%Y")

            ya_registrado = False
            if existe:
                with open(archivo_tsv, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    if ticket_id in contenido and hoy_str in contenido:
                        ya_registrado = True

            if not ya_registrado:
                with open(archivo_tsv, "a", encoding="utf-8") as f:
                    if not existe:
                        headers = [
                            "Fecha y Hora", "Analista", "Tenant", "ID del caso", "Fuente de Detección",
                            "Nro. Ticket", "Prioridad", "Tipo de evento", "Asunto", "Activos",
                            "Descripción", "Evidencia (Logs, etc.)", "Solicitud de Acción", "Estado",
                            "URL", "Generación de Ticket", "TICKET", "Playbook"
                        ]
                        f.write("\t".join(headers) + "\n")
                    f.write(tsv_row + "\n")
                log_to_file(f"[BITACORA AUTO-EXPORT] Registro {ticket_id} (Playbook 6.3) persistido en {archivo_tsv}.")
        except Exception as e:
            log_to_file(f"[BITACORA AUTO-EXPORT ERROR] No se pudo guardar TSV: {e}")

