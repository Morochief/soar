# =============================================================================
# TECHNOMA SOC — CYBER TELEMETRY WIDGETS (cyber_telemetry_widgets.py)
# Widgets nativos de alta densidad cibernética para sustituir la vista de consola ASCII.
# =============================================================================

from typing import List, Tuple, Dict, Any, Optional
from PySide6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar,
    QScrollArea, QSizePolicy, QGridLayout
)
from PySide6.QtCore import Qt, QSize
import ui_theme


def _get_protocol_meta(proto_name: str) -> Tuple[str, str, str]:
    """Retorna (icono, etiqueta limpia, color semántico) para un protocolo dado."""
    name_upper = proto_name.upper().strip()
    if "DNS" in name_upper or "53" in name_upper:
        return "🌐", proto_name, ui_theme.ACCENT_CYBER
    elif "HTTPS" in name_upper or "443" in name_upper or "SSL" in name_upper:
        return "🔒", proto_name, ui_theme.COLOR_SUCCESS
    elif "LDAP" in name_upper or "389" in name_upper:
        return "🏢", proto_name, ui_theme.COLOR_PURPLE
    elif "HTTP" in name_upper or "80" in name_upper:
        return "🌐", proto_name, ui_theme.COLOR_LOW
    elif "SSH" in name_upper or "22" in name_upper:
        return "🔑", proto_name, ui_theme.COLOR_MEDIUM
    elif "FORTIGATE" in name_upper or "SYSLOG" in name_upper:
        return "📜", proto_name, ui_theme.COLOR_HIGH
    elif "EXPLOIT" in name_upper or "ATTEMPT" in name_upper or "ATTACK" in name_upper:
        return "⚡", proto_name, ui_theme.COLOR_CRITICAL
    elif "TAG:" in name_upper:
        return "🏷️", proto_name.replace("Tag:", "").strip(), ui_theme.COLOR_INDIGO
    elif "ANYDESK" in name_upper or "TAILSCALE" in name_upper:
        return "🛰️", proto_name, ui_theme.COLOR_HIGH
    else:
        return "⚙️", proto_name, ui_theme.TEXT_SECONDARY


class CyberTopProtocolsWidget(QFrame):
    """Widget de alta densidad para Top Protocolos / Aplicaciones con barras nativas y badges."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {ui_theme.BG_SURFACE};
                border: 1px solid {ui_theme.BORDER_SUBTLE};
                border-radius: 6px;
            }}
        """)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 8, 8, 8)
        self.main_layout.setSpacing(6)

        # Header con totalizador
        hdr_layout = QHBoxLayout()
        self.lbl_title = QLabel("🌐 TOP PROTOCOLOS & TRÁFICO ACTIVO")
        self.lbl_title.setStyleSheet(f"color: {ui_theme.COLOR_MEDIUM}; font-weight: bold; font-size: 11px; letter-spacing: 0.5px;")
        hdr_layout.addWidget(self.lbl_title)
        hdr_layout.addStretch()

        self.lbl_total_hits = QLabel("0 hits observados")
        self.lbl_total_hits.setStyleSheet(f"""
            background-color: {ui_theme.BG_INPUT};
            color: {ui_theme.TEXT_MUTED};
            border: 1px solid {ui_theme.BORDER_MUTED};
            border-radius: 4px;
            padding: 2px 6px;
            font-size: 10px;
            font-family: {ui_theme.FONT_MONO};
        """)
        hdr_layout.addWidget(self.lbl_total_hits)
        self.main_layout.addLayout(hdr_layout)

        # Scroll Area para filas
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
            QScrollBar:vertical {{
                border: none;
                background: {ui_theme.BG_BASE};
                width: 6px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {ui_theme.BORDER_MUTED};
                min-height: 20px;
                border-radius: 3px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {ui_theme.ACCENT_CYBER};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)

        self.container = QWidget()
        self.container.setStyleSheet("background-color: transparent;")
        self.rows_layout = QVBoxLayout(self.container)
        self.rows_layout.setContentsMargins(0, 0, 0, 0)
        self.rows_layout.setSpacing(4)
        self.scroll.setWidget(self.container)
        self.main_layout.addWidget(self.scroll)

        # Estado inicial
        self._show_placeholder("Cargando métricas de protocolos en tiempo real...")

    def _show_placeholder(self, msg: str):
        while self.rows_layout.count():
            item = self.rows_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        lbl = QLabel(msg)
        lbl.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 11px; padding: 15px; font-style: italic;")
        lbl.setAlignment(Qt.AlignCenter)
        self.rows_layout.addWidget(lbl)

    def setHtml(self, html_text: str):
        """Compatibilidad regresiva si se envía HTML plano."""
        # Se extrae contenido básico o se ignora si ya se actualizó por estructura
        pass

    def setText(self, text: str):
        self._show_placeholder(text)

    def update_protocols(self, top_apps: List[Tuple[str, int]]):
        """Actualiza la lista con datos estructurados (nombre, hits)."""
        while self.rows_layout.count():
            item = self.rows_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        if not top_apps:
            self._show_placeholder("No se registran eventos recientes de protocolos en incidentes...")
            self.lbl_total_hits.setText("0 hits")
            return

        total_hits = sum(count for _, count in top_apps) or 1
        self.lbl_total_hits.setText(f"Total: {total_hits:,} hits")

        max_val = max(count for _, count in top_apps) if top_apps else 1

        for i, (app_name, count) in enumerate(top_apps[:12], 1):
            pct_total = (count / total_hits) * 100
            pct_bar = int((count / max_val) * 100) if max_val > 0 else 0

            icon, clean_name, color = _get_protocol_meta(str(app_name))

            row = QFrame()
            row.setStyleSheet(f"""
                QFrame {{
                    background-color: {ui_theme.BG_INPUT};
                    border: 1px solid {ui_theme.BORDER_SUBTLE};
                    border-radius: 4px;
                    padding: 3px 6px;
                }}
                QFrame:hover {{
                    border: 1px solid {color};
                    background-color: {ui_theme.BG_ELEVATED};
                }}
            """)
            rl = QHBoxLayout(row)
            rl.setContentsMargins(4, 2, 4, 2)
            rl.setSpacing(6)

            # Badge de Ranking
            rank_bg = "#fbbf24" if i == 1 else ("#94a3b8" if i == 2 else ("#d97706" if i == 3 else "#334155"))
            rank_fg = "#000000" if i <= 3 else "#f8fafc"
            lbl_rank = QLabel(f"#{i}")
            lbl_rank.setStyleSheet(f"""
                background-color: {rank_bg};
                color: {rank_fg};
                font-weight: bold;
                font-size: 10px;
                border-radius: 3px;
                padding: 1px 4px;
                min-width: 22px;
            """)
            lbl_rank.setAlignment(Qt.AlignCenter)
            rl.addWidget(lbl_rank)

            # Nombre con icono
            lbl_name = QLabel(f"{icon} {clean_name}")
            lbl_name.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 11px; font-weight: 500;")
            lbl_name.setToolTip(f"Protocolo / Detección: {app_name}\nHits acumulados: {count:,} ({pct_total:.1f}% del total)")
            rl.addWidget(lbl_name, 1)

            # Barra gráfica nativa
            bar = QProgressBar()
            bar.setRange(0, 100)
            bar.setValue(pct_bar)
            bar.setTextVisible(False)
            bar.setFixedHeight(6)
            bar.setFixedWidth(80)
            bar.setStyleSheet(f"""
                QProgressBar {{
                    background-color: #0b1329;
                    border: 1px solid {ui_theme.BORDER_SUBTLE};
                    border-radius: 3px;
                }}
                QProgressBar::chunk {{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {color}, stop:1 {ui_theme.ACCENT_CYBER});
                    border-radius: 2px;
                }}
            """)
            rl.addWidget(bar)

            # Chip de métricas
            lbl_hits = QLabel(f"{count:,} hits  ({pct_total:.1f}%)")
            lbl_hits.setStyleSheet(f"""
                color: {ui_theme.ACCENT_CYBER};
                font-size: 10px;
                font-family: {ui_theme.FONT_MONO};
                font-weight: bold;
            """)
            rl.addWidget(lbl_hits)

            self.rows_layout.addWidget(row)

        self.rows_layout.addStretch()


class CyberInfrastructureHealthWidget(QFrame):
    """Monitor gráfico de Salud de Sensores e Ingesta de Pozo Global (Dynamic Pooling)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {ui_theme.BG_SURFACE};
                border: 1px solid {ui_theme.BORDER_SUBTLE};
                border-radius: 6px;
            }}
        """)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(8, 8, 8, 8)
        self.main_layout.setSpacing(6)

        # 1. Cabecera Principal
        hdr_layout = QHBoxLayout()
        lbl_title = QLabel("  INFRASTRUCTURE HEALTH & DYNAMIC POOL MONITOR")
        lbl_title.setStyleSheet(ui_theme.section_header_style(ui_theme.COLOR_CRITICAL))
        hdr_layout.addWidget(lbl_title)
        hdr_layout.addStretch()

        self.lbl_pool_status_pill = QLabel("POZO: CALCULANDO...")
        self.lbl_pool_status_pill.setStyleSheet(f"""
            background-color: {ui_theme.BG_INPUT};
            color: {ui_theme.TEXT_MUTED};
            border: 1px solid {ui_theme.BORDER_MUTED};
            border-radius: 4px;
            padding: 2px 8px;
            font-size: 10px;
            font-weight: bold;
        """)
        hdr_layout.addWidget(self.lbl_pool_status_pill)
        self.main_layout.addLayout(hdr_layout)

        # 2. Tarjeta Superior: Monitor de Pozo Global (Dynamic Pooling Contract)
        self.card_pool = QFrame()
        self.card_pool.setStyleSheet(f"""
            QFrame {{
                background-color: {ui_theme.BG_INPUT};
                border: 1px solid {ui_theme.BORDER_MUTED};
                border-left: 4px solid {ui_theme.ACCENT_CYBER};
                border-radius: 5px;
                padding: 6px 10px;
            }}
        """)
        l_pool = QVBoxLayout(self.card_pool)
        l_pool.setContentsMargins(4, 2, 4, 2)
        l_pool.setSpacing(3)

        top_pool_row = QHBoxLayout()
        lbl_pool_hdr = QLabel("📈 REPORTE DE CONSUMO DE POZO GLOBAL (DYNAMIC POOLING)")
        lbl_pool_hdr.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-weight: bold; font-size: 10px;")
        top_pool_row.addWidget(lbl_pool_hdr)
        top_pool_row.addStretch()

        self.lbl_pool_metrics = QLabel("Capacidad: 100.0 GB/día  |  Pico Real: 0.00 GB  |  Uso: 0.0%")
        self.lbl_pool_metrics.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 10px; font-family: {ui_theme.FONT_MONO}; font-weight: bold;")
        top_pool_row.addWidget(self.lbl_pool_metrics)
        l_pool.addLayout(top_pool_row)

        # Barra de progreso del pozo
        self.bar_pool = QProgressBar()
        self.bar_pool.setRange(0, 100)
        self.bar_pool.setValue(0)
        self.bar_pool.setFixedHeight(8)
        self.bar_pool.setTextVisible(False)
        self.bar_pool.setStyleSheet(f"""
            QProgressBar {{
                background-color: #0b1329;
                border: 1px solid {ui_theme.BORDER_SUBTLE};
                border-radius: 4px;
            }}
            QProgressBar::chunk {{
                background: {ui_theme.COLOR_SUCCESS};
                border-radius: 3px;
            }}
        """)
        l_pool.addWidget(self.bar_pool)

        # Desglose de tenants en chips
        self.lbl_tenants_breakdown = QLabel("Cargando métricas de clientes...")
        self.lbl_tenants_breakdown.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 9px;")
        l_pool.addWidget(self.lbl_tenants_breakdown)

        self.main_layout.addWidget(self.card_pool)

        # 3. Scroll Area para Sensores Físicos y Modulares
        self.scroll_sensors = QScrollArea()
        self.scroll_sensors.setWidgetResizable(True)
        self.scroll_sensors.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
            QScrollBar:vertical {{
                border: none;
                background: {ui_theme.BG_BASE};
                width: 6px;
            }}
            QScrollBar::handle:vertical {{
                background: {ui_theme.BORDER_MUTED};
                border-radius: 3px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {ui_theme.ACCENT_CYBER};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
        """)

        self.sensors_container = QWidget()
        self.sensors_container.setStyleSheet("background-color: transparent;")
        self.sensors_layout = QVBoxLayout(self.sensors_container)
        self.sensors_layout.setContentsMargins(0, 0, 0, 0)
        self.sensors_layout.setSpacing(6)
        self.scroll_sensors.setWidget(self.sensors_container)
        self.main_layout.addWidget(self.scroll_sensors, 1)

        # 4. Tira Inferior: Resumen Ejecutivo
        self.strip_summary = QFrame()
        self.strip_summary.setStyleSheet(f"""
            QFrame {{
                background-color: {ui_theme.BG_INPUT};
                border: 1px solid {ui_theme.BORDER_SUBTLE};
                border-radius: 4px;
                padding: 3px 8px;
            }}
        """)
        summary_layout = QHBoxLayout(self.strip_summary)
        summary_layout.setContentsMargins(4, 2, 4, 2)
        summary_layout.setSpacing(10)

        self.lbl_sum_total = QLabel("Total: 0")
        self.lbl_sum_total.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-size: 10px; font-weight: bold;")
        summary_layout.addWidget(self.lbl_sum_total)

        self.lbl_sum_online = QLabel("🟢 0 Online")
        self.lbl_sum_online.setStyleSheet(f"color: {ui_theme.COLOR_SUCCESS}; font-size: 10px; font-weight: bold;")
        summary_layout.addWidget(self.lbl_sum_online)

        self.lbl_sum_offline = QLabel("🔴 0 Inactivos")
        self.lbl_sum_offline.setStyleSheet(f"color: {ui_theme.COLOR_CRITICAL}; font-size: 10px; font-weight: bold;")
        summary_layout.addWidget(self.lbl_sum_offline)

        self.lbl_sum_uptime = QLabel("Disponibilidad: 100%")
        self.lbl_sum_uptime.setStyleSheet(f"color: {ui_theme.ACCENT_CYBER}; font-size: 10px; font-family: {ui_theme.FONT_MONO}; font-weight: bold;")
        summary_layout.addStretch()
        summary_layout.addWidget(self.lbl_sum_uptime)

        self.main_layout.addWidget(self.strip_summary)

        # Estado inicial
        self._show_placeholder("Sincronizando estado de telemetría de sensores...")

    def _show_placeholder(self, msg: str):
        while self.sensors_layout.count():
            item = self.sensors_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        lbl = QLabel(msg)
        lbl.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 11px; padding: 20px; font-style: italic;")
        lbl.setAlignment(Qt.AlignCenter)
        self.sensors_layout.addWidget(lbl)

    def setHtml(self, html_text: str):
        """Compatibilidad regresiva si el flujo legado intenta llamar setHtml."""
        pass

    def setText(self, text: str):
        self._show_placeholder(text)

    def update_telemetry(
        self,
        raw_sensors: List[Dict[str, Any]],
        tenants_data_consumo: List[Dict[str, Any]],
        cuotas_diccionario: Dict[str, int],
        peak_global_real: float,
        nivel_uso_global_pct: float,
        cuota_pool_global: float = 100.0
    ):
        """Renderiza las tarjetas modernas de sensores y actualiza los medidores de pozo."""
        # 1. Actualizar Tarjeta de Pozo Global
        self.lbl_pool_metrics.setText(
            f"Capacidad: {cuota_pool_global:.1f} GB/día  |  Pico Real: {peak_global_real:.4f} GB  |  Uso: {nivel_uso_global_pct:.1f}%"
        )
        bar_val = min(100, int(nivel_uso_global_pct))
        self.bar_pool.setValue(bar_val)

        if nivel_uso_global_pct > 100:
            status_text = "🚨 POZO DESBORDADO (EXCESO CRÍTICO)"
            status_style = f"background-color: {ui_theme.COLOR_CRITICAL}; color: #ffffff; border-radius: 4px; padding: 2px 8px; font-weight: bold;"
            bar_color = ui_theme.COLOR_CRITICAL
            card_border = ui_theme.COLOR_CRITICAL
        elif nivel_uso_global_pct > 80:
            status_text = "⚠️ POZO EN ADVERTENCIA"
            status_style = f"background-color: {ui_theme.COLOR_MEDIUM}; color: #000000; border-radius: 4px; padding: 2px 8px; font-weight: bold;"
            bar_color = ui_theme.COLOR_MEDIUM
            card_border = ui_theme.COLOR_MEDIUM
        else:
            status_text = "🟢 POZO ESTABLE"
            status_style = f"background-color: #064e3b; color: {ui_theme.COLOR_SUCCESS}; border: 1px solid {ui_theme.COLOR_SUCCESS}; border-radius: 4px; padding: 2px 8px; font-weight: bold;"
            bar_color = ui_theme.COLOR_SUCCESS
            card_border = ui_theme.COLOR_SUCCESS

        self.lbl_pool_status_pill.setText(status_text)
        self.lbl_pool_status_pill.setStyleSheet(status_style)
        self.bar_pool.setStyleSheet(f"""
            QProgressBar {{
                background-color: #0b1329;
                border: 1px solid {ui_theme.BORDER_SUBTLE};
                border-radius: 4px;
            }}
            QProgressBar::chunk {{
                background: {bar_color};
                border-radius: 3px;
            }}
        """)
        self.card_pool.setStyleSheet(f"""
            QFrame {{
                background-color: {ui_theme.BG_INPUT};
                border: 1px solid {ui_theme.BORDER_MUTED};
                border-left: 4px solid {card_border};
                border-radius: 5px;
                padding: 6px 10px;
            }}
        """)

        # Desglose de tenants
        chips = []
        for t in tenants_data_consumo:
            tname = t.get("tenant_name", "")
            if tname == "All Tenants":
                continue
            daily_arr = t.get("daily_usage", [])
            hoy = float(daily_arr[-1].get("usage", 0.0)) if daily_arr else 0.0
            chips.append(f"<b>{tname}</b>: {hoy:.3f} GB")
        if chips:
            self.lbl_tenants_breakdown.setText("  •  ".join(chips))

        # 2. Renderizar Sensores
        while self.sensors_layout.count():
            item = self.sensors_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        total = len(raw_sensors)
        online, offline, warning = 0, 0, 0

        orden_deseado = ["Sensor-Modular-CajaAnde", "VMBASE8", "technoma-sensor", "modular"]
        def sort_key(s):
            h_name = s.get("hostname") or s.get("sensor_id") or s.get("internal_sensor_id") or ""
            return orden_deseado.index(h_name) if h_name in orden_deseado else 999
        sorted_sensors = sorted(raw_sensors, key=sort_key)

        for s in sorted_sensors:
            name = s.get("hostname") or s.get("sensor_id") or s.get("internal_sensor_id") or "Sensor Desconocido"
            raw_st = str(s.get("connection_status", "")).lower()
            if raw_st in ["connected", "online"]:
                st_text = "🟢 CONECTADO"
                st_color = ui_theme.COLOR_SUCCESS
                online += 1
            elif raw_st in ["warning", "degraded"]:
                st_text = "🟡 ALERTA"
                st_color = ui_theme.COLOR_MEDIUM
                warning += 1
            else:
                st_text = "🔴 OFFLINE"
                st_color = ui_theme.COLOR_CRITICAL
                offline += 1

            cpu = float(s.get("cpu_usage", 0.0) or 0.0)
            disk = float(s.get("disk_usage", 0.0) or 0.0)
            tenant = s.get("cust_name", "(sin tenant)")
            ip_loc = s.get("local_ip_address", "N/A")
            ip_nat = s.get("nat_ip_address", "N/A")
            sw_ver = s.get("sw_version", "N/A")
            need_upg = bool(s.get("need_upgrade"))

            card = QFrame()
            card.setStyleSheet(f"""
                QFrame {{
                    background-color: {ui_theme.BG_INPUT};
                    border: 1px solid {ui_theme.BORDER_SUBTLE};
                    border-left: 3px solid {st_color};
                    border-radius: 5px;
                    padding: 6px 8px;
                }}
                QFrame:hover {{
                    border: 1px solid {ui_theme.ACCENT_CYBER};
                    background-color: {ui_theme.BG_ELEVATED};
                }}
            """)
            cl = QVBoxLayout(card)
            cl.setContentsMargins(6, 4, 6, 4)
            cl.setSpacing(4)

            # Fila 1: Nombre, Badge de Estado y Versión
            r1 = QHBoxLayout()
            lbl_name = QLabel(f"🖥️ {name}")
            lbl_name.setStyleSheet(f"color: {ui_theme.TEXT_PRIMARY}; font-weight: bold; font-size: 11px;")
            r1.addWidget(lbl_name)
            r1.addStretch()

            if need_upg:
                lbl_upg = QLabel("⚠️ ACTUALIZAR")
                lbl_upg.setStyleSheet(f"background-color: #78350f; color: {ui_theme.COLOR_MEDIUM}; font-size: 9px; font-weight: bold; padding: 1px 4px; border-radius: 3px;")
                r1.addWidget(lbl_upg)

            lbl_st = QLabel(st_text)
            lbl_st.setStyleSheet(f"color: {st_color}; font-weight: bold; font-size: 10px;")
            r1.addWidget(lbl_st)
            cl.addLayout(r1)

            # Fila 2: IPs y Tenant
            r2 = QHBoxLayout()
            lbl_ips = QLabel(f"IP: <span style='color: #ffffff;'>{ip_loc}</span>  |  NAT: <span style='color: #ffffff;'>{ip_nat}</span>  |  Tenant: <span style='color: #38bdf8;'>{tenant}</span>  |  v{sw_ver}")
            lbl_ips.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 10px;")
            r2.addWidget(lbl_ips)
            cl.addLayout(r2)

            # Fila 3: Medidores CPU y Disco
            r3 = QHBoxLayout()

            # CPU
            lbl_cpu_t = QLabel("CPU:")
            lbl_cpu_t.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 9px; font-weight: bold;")
            r3.addWidget(lbl_cpu_t)
            bar_cpu = QProgressBar()
            bar_cpu.setRange(0, 100)
            bar_cpu.setValue(int(cpu))
            bar_cpu.setFixedHeight(6)
            bar_cpu.setFixedWidth(65)
            bar_cpu.setTextVisible(False)
            cpu_c = ui_theme.COLOR_CRITICAL if cpu > 90 else (ui_theme.COLOR_MEDIUM if cpu > 70 else ui_theme.COLOR_SUCCESS)
            bar_cpu.setStyleSheet(f"""
                QProgressBar {{ background-color: #0b1329; border: none; border-radius: 3px; }}
                QProgressBar::chunk {{ background: {cpu_c}; border-radius: 3px; }}
            """)
            r3.addWidget(bar_cpu)
            lbl_cpu_v = QLabel(f"{cpu:.1f}%")
            lbl_cpu_v.setStyleSheet(f"color: {cpu_c}; font-size: 9px; font-family: {ui_theme.FONT_MONO}; font-weight: bold;")
            r3.addWidget(lbl_cpu_v)

            r3.addSpacing(10)

            # Disco
            lbl_dsk_t = QLabel("Disco:")
            lbl_dsk_t.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 9px; font-weight: bold;")
            r3.addWidget(lbl_dsk_t)
            bar_dsk = QProgressBar()
            bar_dsk.setRange(0, 100)
            bar_dsk.setValue(int(disk))
            bar_dsk.setFixedHeight(6)
            bar_dsk.setFixedWidth(65)
            bar_dsk.setTextVisible(False)
            dsk_c = ui_theme.COLOR_CRITICAL if disk > 85 else (ui_theme.COLOR_MEDIUM if disk > 65 else ui_theme.COLOR_SUCCESS)
            bar_dsk.setStyleSheet(f"""
                QProgressBar {{ background-color: #0b1329; border: none; border-radius: 3px; }}
                QProgressBar::chunk {{ background: {dsk_c}; border-radius: 3px; }}
            """)
            r3.addWidget(bar_dsk)
            lbl_dsk_v = QLabel(f"{disk:.1f}%")
            lbl_dsk_v.setStyleSheet(f"color: {dsk_c}; font-size: 9px; font-family: {ui_theme.FONT_MONO}; font-weight: bold;")
            r3.addWidget(lbl_dsk_v)

            r3.addStretch()
            cl.addLayout(r3)

            self.sensors_layout.addWidget(card)

        self.sensors_layout.addStretch()

        # 3. Actualizar Resumen Ejecutivo
        self.lbl_sum_total.setText(f"Total: {total}")
        self.lbl_sum_online.setText(f"🟢 {online} Online")
        self.lbl_sum_offline.setText(f"🔴 {offline} Inactivos")
        uptime_pct = (online / total * 100) if total > 0 else 100.0
        self.lbl_sum_uptime.setText(f"Disponibilidad: {uptime_pct:.1f}%")
