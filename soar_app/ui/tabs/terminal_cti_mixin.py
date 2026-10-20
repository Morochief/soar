# -*- coding: utf-8 -*-
"""
Mixin Modular: Consola de Investigación Forense & Threat Hunting (Tab 5),
15 Presets de Reconocimiento, Decodificador Forense, Bloqueo FortiGate CLI
y Lanzadores Estandarizados de Módulos Satélites (SOCWindowManager).
"""
from soar_app.core.infra import *
from soar_app.workers.api_workers import *
import urllib.parse
import html
from PySide6.QtWidgets import QInputDialog


class TerminalCtiMixin:
    # =========================================================================
    # TAB 5: CONSOLA DE INVESTIGACIÓN FORENSE & THREAT HUNTING (DFIR)
    # =========================================================================
    def _init_tab5_terminal(self):
        """Inicializa la Pestaña 5: Consola Integrada de Investigación Forense y Threat Hunting."""
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab5, "🔬 Consola & Threat Hunting")
        layout_tab5 = QVBoxLayout(self.tab5)
        layout_tab5.setContentsMargins(10, 8, 10, 8)
        layout_tab5.setSpacing(8)

        # 1. Barra Superior de Control de Motor y Lanzadores Externos
        frame_term_top = QFrame()
        frame_term_top.setFixedHeight(44)
        frame_term_top.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_term_top = QHBoxLayout(frame_term_top)
        layout_term_top.setContentsMargins(8, 2, 8, 2)
        layout_term_top.setSpacing(6)

        lbl_engine = QLabel("Motor Shell:")
        lbl_engine.setStyleSheet("color: #38bdf8; font-weight: bold; border: none; font-size: 11px;")

        self.combo_term_engine = QComboBox()
        self.combo_term_engine.addItem("⚡ Windows PowerShell", "powershell")
        self.combo_term_engine.addItem("🐧 Linux WSL (Ubuntu)", "wsl")
        self.combo_term_engine.setStyleSheet("""
            QComboBox {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 3px 8px;
                font-family: 'Consolas';
                font-size: 11px;
                min-width: 190px;
            }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #0f172a;
                color: #f8fafc;
                selection-background-color: #1e293b;
                selection-color: #38bdf8;
                border: 1px solid #334155;
            }
        """)
        self.combo_term_engine.currentIndexChanged.connect(self.on_term_engine_changed)

        lbl_ws = QLabel("📁 soc-env")
        lbl_ws.setStyleSheet("color: #94a3b8; font-family: 'Consolas'; font-size: 11px; border: none;")

        self.btn_term_launch_ps_admin = QPushButton("⚡ PowerShell (Admin)")
        self.btn_term_launch_ps_admin.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_term_launch_ps_admin.setToolTip("Abre una ventana externa de PowerShell o Windows Terminal con elevación de Administrador (UAC)")
        self.btn_term_launch_ps_admin.clicked.connect(self.launch_external_ps_admin)

        self.btn_term_launch_wsl = QPushButton("🐧 WSL Terminal")
        self.btn_term_launch_wsl.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_term_launch_wsl.setToolTip("Abre la terminal interactiva de Ubuntu WSL2 en ventana completa")
        self.btn_term_launch_wsl.clicked.connect(self.launch_external_wsl)

        self.btn_term_antisleep = QPushButton("[Anti-Sleep: ACTIVO]")
        self.btn_term_antisleep.setStyleSheet(f"background-color: #064e3b; color: #34d399; font-weight: bold; border: 1px solid #059669; padding: 4px 10px; border-radius: 4px; font-family: {ui_theme.FONT_MAIN}; font-size: 11px;")
        self.btn_term_antisleep.setToolTip("Mantiene el sistema y pantalla despiertos continuamente mientras el Cockpit este activo. Clic para alternar.")
        self.btn_term_antisleep.clicked.connect(self.toggle_antisleep)

        self.btn_term_copy_all = QPushButton("📋 Copiar Salida")
        self.btn_term_copy_all.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_term_copy_all.clicked.connect(self.copy_terminal_output)

        self.btn_term_clear = QPushButton("🧹 Limpiar")
        self.btn_term_clear.setStyleSheet(ui_theme.secondary_tool_btn_style())
        self.btn_term_clear.clicked.connect(self.clear_terminal_output)

        self.btn_term_email_analyzer = QPushButton("📬 Analizador Cabeceras (.eml)")
        self.btn_term_email_analyzer.setStyleSheet(ui_theme.chip_button_style(ui_theme.ACCENT_CYBER))
        self.btn_term_email_analyzer.setToolTip("Abre el analizador forense de cabeceras de correo para detección de phishing y spoofing en memoria")
        self.btn_term_email_analyzer.clicked.connect(self.open_email_header_analyzer)

        self.btn_term_thn_ticket = QPushButton("🎫 Ticket Technoma (THN-SOC)")
        self.btn_term_thn_ticket.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_HIGH))
        self.btn_term_thn_ticket.setToolTip("Generador de Tickets de Escalación THN-SOC y sincronizador de Bitácora (18 Col)")
        self.btn_term_thn_ticket.clicked.connect(self.open_thn_ticket_generator)

        self.btn_term_feeds = QPushButton("📡 Feeds CTI")
        self.btn_term_feeds.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_PURPLE))
        self.btn_term_feeds.setToolTip("Módulo de Inteligencia de Amenazas CTI (15 Feeds RSS/Atom, SQLite y Reportes con IA)")
        self.btn_term_feeds.clicked.connect(self.open_feeds_intel_module)

        self.btn_term_abuse_report = QPushButton("📧 Reportes de Abuso")
        self.btn_term_abuse_report.setStyleSheet(ui_theme.chip_button_style(ui_theme.COLOR_CRITICAL))
        self.btn_term_abuse_report.setToolTip("Generador y formateador automático de notificaciones de abuso para IPs atacantes/escaneo en Interflow")
        self.btn_term_abuse_report.clicked.connect(self.open_abuse_report_dialog)

        layout_term_top.addWidget(lbl_engine)
        layout_term_top.addWidget(self.combo_term_engine)
        layout_term_top.addWidget(lbl_ws)
        layout_term_top.addStretch()
        layout_term_top.addWidget(self.btn_term_feeds)
        layout_term_top.addWidget(self.btn_term_thn_ticket)
        layout_term_top.addWidget(self.btn_term_email_analyzer)
        layout_term_top.addWidget(self.btn_term_abuse_report)
        layout_term_top.addWidget(self.btn_term_launch_ps_admin)
        layout_term_top.addWidget(self.btn_term_launch_wsl)
        layout_term_top.addWidget(self.btn_term_antisleep)
        layout_term_top.addWidget(self.btn_term_copy_all)
        layout_term_top.addWidget(self.btn_term_clear)

        layout_tab5.addWidget(frame_term_top)

        # 2. Barra de Presets Forenses Rápidos (Estructura de 2 Niveles - Máximo Espacio y Organización)
        frame_term_presets = QFrame()
        frame_term_presets.setFixedHeight(74)
        frame_term_presets.setStyleSheet(f"background-color: {ui_theme.BG_SURFACE}; border: 1px solid {ui_theme.BORDER_SUBTLE}; border-radius: 6px;")
        layout_presets_outer = QVBoxLayout(frame_term_presets)
        layout_presets_outer.setContentsMargins(8, 4, 8, 4)
        layout_presets_outer.setSpacing(4)

        # Fila 1: Campo de Objetivo Expandible + Acciones Primarias de Triaje
        row1_widget = QWidget()
        row1_layout = QHBoxLayout(row1_widget)
        row1_layout.setContentsMargins(0, 0, 0, 0)
        row1_layout.setSpacing(6)

        lbl_target = QLabel("🎯 Objetivo:")
        lbl_target.setStyleSheet(ui_theme.section_header_style(ui_theme.ACCENT_CYBER))

        self.input_term_target = QLineEdit()
        self.input_term_target.setPlaceholderText("Ingrese IP, Dominio, URL sospechosa, Hash SHA256 o CVE...")
        self.input_term_target.setStyleSheet(f"""
            QLineEdit {{
                background-color: {ui_theme.BG_INPUT};
                color: {ui_theme.ACCENT_CYBER};
                border: 1px solid {ui_theme.BORDER_MUTED};
                border-radius: 4px;
                padding: 3px 8px;
                font-family: {ui_theme.FONT_MONO};
                font-size: 11px;
            }}
            QLineEdit:focus {{
                border: 1px solid {ui_theme.ACCENT_PRIMARY};
            }}
        """)

        btn_clear_target = QPushButton("✕")
        btn_clear_target.setToolTip("Limpiar campo objetivo")
        btn_clear_target.setFixedSize(22, 22)
        btn_clear_target.setStyleSheet(f"background-color: {ui_theme.BG_ELEVATED}; color: {ui_theme.TEXT_MUTED}; border: 1px solid {ui_theme.BORDER_MUTED}; border-radius: 3px; font-size: 10px; font-weight: bold;")
        btn_clear_target.clicked.connect(self.input_term_target.clear)

        btn_preset_auto_360 = QPushButton("🚀 Auto-Investigar 360°")
        btn_preset_auto_360.setStyleSheet(ui_theme.primary_action_btn_style())
        btn_preset_auto_360.setToolTip("Orquestador inteligente: Detecta automáticamente si es IP (privada/pública) o Dominio (PaaS/Propio) y dispara la suite forense exacta en un solo clic")
        btn_preset_auto_360.clicked.connect(self.run_preset_auto_investigate_360)

        btn_preset_triscan = QPushButton("⚡ Tri-Scan CTI")
        btn_preset_triscan.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_HIGH))
        btn_preset_triscan.setToolTip("Escaneo 360 integral de reputación en VirusTotal, AbuseIPDB, URLScan y MxToolbox")
        btn_preset_triscan.clicked.connect(self.run_preset_triscan)

        btn_preset_anti_spoofing = QPushButton("📧 Anti-Spoofing (TXT)")
        btn_preset_anti_spoofing.setStyleSheet(ui_theme.preset_button_style(ui_theme.ACCENT_CYBER))
        btn_preset_anti_spoofing.setToolTip("Verifica registros TXT para SPF, DMARC (_dmarc) y registros MX de forma nativa en WSL o PowerShell")
        btn_preset_anti_spoofing.clicked.connect(self.run_preset_anti_spoofing)

        btn_preset_unmask = QPushButton("🕵️ Desemmascarar Origen")
        btn_preset_unmask.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_PURPLE))
        btn_preset_unmask.setToolTip("Audita el dominio en busca de la IP real de origen eludiendo el proxy de Cloudflare/CDN (Fugas MX _dc-mx, SPF y subdominios sin proxy)")
        btn_preset_unmask.clicked.connect(self.run_preset_unmask_origin)

        btn_preset_dnstwist = QPushButton("🔀 DNS Twist")
        btn_preset_dnstwist.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_HIGH))
        btn_preset_dnstwist.setToolTip("Caza activa de dominios similares, suplantaciones (typosquatting), combo-squatting y phishing")
        btn_preset_dnstwist.clicked.connect(self.run_preset_dnstwist)

        btn_preset_phishing = QPushButton("📬 MxToolbox")
        btn_preset_phishing.setStyleSheet(ui_theme.preset_button_style(ui_theme.ACCENT_CYBER))
        btn_preset_phishing.clicked.connect(self.run_preset_mxtoolbox)

        row1_layout.addWidget(lbl_target)
        row1_layout.addWidget(self.input_term_target)
        row1_layout.addWidget(btn_clear_target)
        row1_layout.addWidget(btn_preset_auto_360)
        row1_layout.addWidget(btn_preset_triscan)
        row1_layout.addWidget(btn_preset_anti_spoofing)
        row1_layout.addWidget(btn_preset_unmask)
        row1_layout.addWidget(btn_preset_dnstwist)
        row1_layout.addWidget(btn_preset_phishing)

        # Fila 2: Herramientas Agrupadas por Dominio Forense
        row2_widget = QWidget()
        row2_layout = QHBoxLayout(row2_widget)
        row2_layout.setContentsMargins(0, 0, 0, 0)
        row2_layout.setSpacing(4)

        lbl_net = QLabel("🌐 Red/Shell:")
        lbl_net.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 10px; font-weight: bold; border: none; font-family: {ui_theme.FONT_MAIN};")

        btn_preset_dns = QPushButton("DNS")
        btn_preset_dns.setStyleSheet(ui_theme.preset_button_style(ui_theme.ACCENT_CYBER))
        btn_preset_dns.clicked.connect(self.run_preset_dns)

        btn_preset_ptr = QPushButton("PTR")
        btn_preset_ptr.setStyleSheet(ui_theme.preset_button_style(ui_theme.ACCENT_CYBER))
        btn_preset_ptr.setToolTip("Resolución inversa DNS (PTR) para identificar el hostname real de una dirección IP")
        btn_preset_ptr.clicked.connect(self.run_preset_ptr)

        btn_preset_whois = QPushButton("WHOIS")
        btn_preset_whois.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_SUCCESS))
        btn_preset_whois.clicked.connect(self.run_preset_whois)

        btn_preset_ping = QPushButton("Ping")
        btn_preset_ping.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_MEDIUM))
        btn_preset_ping.clicked.connect(self.run_preset_ping)

        btn_preset_curl = QPushButton("CURL")
        btn_preset_curl.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_PURPLE))
        btn_preset_curl.clicked.connect(self.run_preset_curl)

        btn_preset_grep = QPushButton("Grep Casos")
        btn_preset_grep.setStyleSheet(ui_theme.preset_button_style(ui_theme.TEXT_MUTED))
        btn_preset_grep.setToolTip("Busca si este IOC o IP ya apareció antes en tus informes de casos, playbooks o bitácora local de soc-env")
        btn_preset_grep.clicked.connect(self.run_preset_grep)

        sep1 = QFrame()
        sep1.setFrameShape(QFrame.VLine)
        sep1.setStyleSheet(f"color: {ui_theme.BORDER_MUTED}; margin: 0 4px;")

        lbl_cti = QLabel("🛡️ CTI Intel:")
        lbl_cti.setStyleSheet(f"color: {ui_theme.TEXT_MUTED}; font-size: 10px; font-weight: bold; border: none; font-family: {ui_theme.FONT_MAIN};")

        btn_preset_abuse = QPushButton("AbuseIPDB")
        btn_preset_abuse.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_SUCCESS))
        btn_preset_abuse.clicked.connect(self.run_preset_abuseipdb)

        btn_preset_vt = QPushButton("VirusTotal")
        btn_preset_vt.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_HIGH))
        btn_preset_vt.clicked.connect(self.run_preset_virustotal)

        btn_preset_urlscan = QPushButton("URLScan")
        btn_preset_urlscan.setStyleSheet(ui_theme.preset_button_style(ui_theme.ACCENT_CYBER))
        btn_preset_urlscan.clicked.connect(self.run_preset_urlscan)

        btn_preset_cve = QPushButton("NVD CVE")
        btn_preset_cve.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_CRITICAL))
        btn_preset_cve.clicked.connect(self.run_preset_cve)

        btn_preset_so = QPushButton("🧅 SecOnion")
        btn_preset_so.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_PURPLE))
        btn_preset_so.clicked.connect(self.run_preset_security_onion)

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.VLine)
        sep2.setStyleSheet(f"color: {ui_theme.BORDER_MUTED}; margin: 0 4px;")

        # Botón Menú Desplegable de Sandboxes y Pivotes Web
        btn_pivots = QPushButton("🚀 Sandboxes & Pivotes ▼")
        btn_pivots.setStyleSheet(ui_theme.preset_button_style(ui_theme.COLOR_INDIGO))
        menu_pivots = QMenu(btn_pivots)
        menu_pivots.setStyleSheet("""
            QMenu {
                background-color: #0f172a;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 6px;
                padding: 6px 4px;
                font-size: 11px;
            }
            QMenu::item {
                background-color: transparent;
                color: #f8fafc;
                padding: 6px 22px 6px 22px;
                border-radius: 4px;
                margin: 2px 4px;
            }
            QMenu::item:selected {
                background-color: #1e293b;
                color: #38bdf8;
            }
        """)

        act_talos = menu_pivots.addAction("🦊 Cisco Talos Intelligence")
        act_talos.triggered.connect(lambda: self.pivot_to_external_service("talos"))

        act_anyrun = menu_pivots.addAction("⚡ Any.Run Interactive Sandbox")
        act_anyrun.triggered.connect(lambda: self.pivot_to_external_service("anyrun"))

        act_browserling = menu_pivots.addAction("🌐 Browserling (Navegador Aislado)")
        act_browserling.triggered.connect(lambda: self.pivot_to_external_service("browserling"))

        act_hybrid = menu_pivots.addAction("🦅 Hybrid Analysis (Falcon Sandbox)")
        act_hybrid.triggered.connect(lambda: self.pivot_to_external_service("hybrid_analysis"))

        act_mb = menu_pivots.addAction("🦠 MalwareBazaar (abuse.ch Hashes)")
        act_mb.triggered.connect(lambda: self.pivot_to_external_service("malwarebazaar"))

        act_tf = menu_pivots.addAction("🦊 ThreatFox IoC Search (abuse.ch)")
        act_tf.triggered.connect(lambda: self.pivot_to_external_service("threatfox"))

        act_uh = menu_pivots.addAction("☣️ URLhaus Malware URLs (abuse.ch)")
        act_uh.triggered.connect(lambda: self.pivot_to_external_service("urlhaus"))

        act_crt = menu_pivots.addAction("📜 crt.sh (Certificate Transparency)")
        act_crt.triggered.connect(lambda: self.pivot_to_external_service("crtsh"))

        act_shodan = menu_pivots.addAction("🔎 Shodan Host Intelligence")
        act_shodan.triggered.connect(lambda: self.pivot_to_external_service("shodan"))

        act_ipinfo = menu_pivots.addAction("🔍 IPinfo.io Geolocation")
        act_ipinfo.triggered.connect(lambda: self.pivot_to_external_service("ipinfo"))

        act_mx = menu_pivots.addAction("📬 MxToolbox SuperTool Web")
        act_mx.triggered.connect(lambda: self.pivot_to_external_service("mxtoolbox_web"))

        act_chef = menu_pivots.addAction("🍳 CyberChef (Decodificador Web)")
        act_chef.triggered.connect(lambda: self.pivot_to_external_service("cyberchef"))

        menu_pivots.addSeparator()
        act_unmask = menu_pivots.addAction("🕵️ Desemmascarar Origen (Bypass Cloudflare/CDN)")
        act_unmask.triggered.connect(self.run_preset_unmask_origin)

        act_twist = menu_pivots.addAction("🔀 Caza de Typosquatting (DNS Twist)")
        act_twist.triggered.connect(self.run_preset_dnstwist)

        act_sectrails = menu_pivots.addAction("🛡️ SecurityTrails (Histórico DNS)")
        act_sectrails.triggered.connect(lambda: self.pivot_to_external_service("securitytrails"))

        act_viewdns = menu_pivots.addAction("📜 ViewDNS (IP History)")
        act_viewdns.triggered.connect(lambda: self.pivot_to_external_service("viewdns"))

        act_censys = menu_pivots.addAction("🌐 Censys Search (Certificados SSL & Hosts)")
        act_censys.triggered.connect(lambda: self.pivot_to_external_service("censys"))

        act_decode_local = menu_pivots.addAction("🔓 Decodificar Objetivo Local (B64/URL/Hex)")
        act_decode_local.triggered.connect(lambda: self._execute_forensic_decode(self._get_active_target_or_observable()))

        menu_pivots.addSeparator()
        act_fg_domain = menu_pivots.addAction("🔥 [FortiGate] Bloquear Dominio Malicioso (7.0.0s)")
        act_fg_domain.triggered.connect(lambda: self.execute_fortigate_block("domain"))

        act_fg_url = menu_pivots.addAction("🛑 [FortiGate] Bloquear URL de Phishing (7.0.0s)")
        act_fg_url.triggered.connect(lambda: self.execute_fortigate_block("url"))

        btn_pivots.setMenu(menu_pivots)

        row2_layout.addWidget(lbl_net)
        row2_layout.addWidget(btn_preset_dns)
        row2_layout.addWidget(btn_preset_ptr)
        row2_layout.addWidget(btn_preset_whois)
        row2_layout.addWidget(btn_preset_ping)
        row2_layout.addWidget(btn_preset_curl)
        row2_layout.addWidget(btn_preset_grep)
        row2_layout.addWidget(sep1)
        row2_layout.addWidget(lbl_cti)
        row2_layout.addWidget(btn_preset_abuse)
        row2_layout.addWidget(btn_preset_vt)
        row2_layout.addWidget(btn_preset_urlscan)
        row2_layout.addWidget(btn_preset_cve)
        row2_layout.addWidget(btn_preset_so)
        row2_layout.addWidget(sep2)
        row2_layout.addWidget(btn_pivots)
        row2_layout.addStretch()

        layout_presets_outer.addWidget(row1_widget)
        layout_presets_outer.addWidget(row2_widget)

        layout_tab5.addWidget(frame_term_presets)

        # 3. Visor de Salida de Terminal (Dark Hacker Theme)
        self.txt_terminal_output = QTextEdit()
        self.txt_terminal_output.setReadOnly(True)
        self.txt_terminal_output.setStyleSheet("""
            QTextEdit {
                background-color: #020617;
                color: #10b981;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 11px;
                border: 1px solid #1e293b;
                border-radius: 6px;
                padding: 10px;
                line-height: 1.4;
            }
        """)

        banner = (
            "========================================================================================\n"
            "STELLAR CYBER OPENXDR — DFIR & THREAT HUNTING CONSOLE\n"
            "[*] Motores disponibles: Windows PowerShell 5.1/7 & Linux WSL2 (Ubuntu)\n"
            "[*] CTI Threat Intel: VirusTotal v3 | AbuseIPDB v2 | URLScan.io v1 | MxToolbox v1 | NVD NIST v2\n"
            f"[*] Directorio de Trabajo: {os.path.abspath('.')}\n"
            "[*] Anti-Sleep: Activo en segundo plano (Windows SetThreadExecutionState)\n"
            "[*] Presets: DNS, WHOIS, Ping, Grep | CTI: AbuseIPDB, VirusTotal, URLScan, Tri-Scan, MxToolbox, NVD CVE\n"
            "[*] DNS Twist: 'twist <domain>' | Caza de dominios falsos, typosquatting y phishing lookalikes\n"
            "[*] CLI CTI: 'vt <ioc>', 'abuse <ip>', 'urlscan <url>', 'cti <ioc>', 'cve <cve-id>', 'phishing <domain>'\n"
            "[*] DNS/Mail: 'spf <domain>', 'dmarc <domain>', 'mx <domain>'\n"
            "[*] Control de Sistema: 'antisleep [on|off|status]'\n"
            "[*] Historial: Presione [↑] y [↓] en el campo de comando para navegar comandos previos.\n"
            "========================================================================================\n\n"
        )
        self.txt_terminal_output.setPlainText(banner)
        layout_tab5.addWidget(self.txt_terminal_output, 1)

        # 4. Línea de Comandos Interactiva
        frame_term_cli = QFrame()
        frame_term_cli.setFixedHeight(44)
        frame_term_cli.setStyleSheet("background-color: #0b1120; border: 1px solid #1e293b; border-radius: 6px;")
        layout_term_cli = QHBoxLayout(frame_term_cli)
        layout_term_cli.setContentsMargins(8, 4, 8, 4)
        layout_term_cli.setSpacing(6)

        self.lbl_term_prompt = QLabel("PS >")
        self.lbl_term_prompt.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")

        self.input_term_cmd = QLineEdit()
        self.input_term_cmd.setPlaceholderText("Escriba un comando y presione Enter (ej. Get-Process, Test-NetConnection, curl, whois)...")
        self.input_term_cmd.setStyleSheet("""
            QLineEdit {
                background-color: #020617;
                color: #f8fafc;
                border: 1px solid #334155;
                border-radius: 4px;
                padding: 4px 8px;
                font-family: 'Consolas';
                font-size: 11px;
            }
        """)
        self.input_term_cmd.returnPressed.connect(self.execute_terminal_input)
        self.input_term_cmd.installEventFilter(self)

        self.btn_term_run = QPushButton("▶ Ejecutar")
        self.btn_term_run.setStyleSheet("background-color: #059669; color: #ffffff; font-weight: bold; padding: 4px 12px; border-radius: 4px;")
        self.btn_term_run.clicked.connect(self.execute_terminal_input)

        self.btn_term_stop = QPushButton("⏹ Detener")
        self.btn_term_stop.setEnabled(False)
        self.btn_term_stop.setStyleSheet("background-color: #b91c1c; color: #ffffff; font-weight: bold; padding: 4px 10px; border-radius: 4px;")
        self.btn_term_stop.clicked.connect(self.stop_terminal_process)

        layout_term_cli.addWidget(self.lbl_term_prompt)
        layout_term_cli.addWidget(self.input_term_cmd, 1)
        layout_term_cli.addWidget(self.btn_term_run)
        layout_term_cli.addWidget(self.btn_term_stop)

        layout_tab5.addWidget(frame_term_cli)

        # Variables internas de consola
        self._cmd_history = []
        self._cmd_history_idx = -1
        self._term_process = QProcess(self)
        self._term_process.readyReadStandardOutput.connect(self._on_term_stdout)
        self._term_process.readyReadStandardError.connect(self._on_term_stderr)
        self._term_process.finished.connect(self._on_term_finished)

    def eventFilter(self, obj, event):
        if hasattr(self, 'input_term_cmd') and obj == self.input_term_cmd and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Up:
                self._navigate_cmd_history(-1)
                return True
            elif event.key() == Qt.Key_Down:
                self._navigate_cmd_history(1)
                return True
        return super().eventFilter(obj, event)

    def _navigate_cmd_history(self, delta: int):
        if not getattr(self, '_cmd_history', []):
            return
        new_idx = self._cmd_history_idx + delta
        if 0 <= new_idx < len(self._cmd_history):
            self._cmd_history_idx = new_idx
            self.input_term_cmd.setText(self._cmd_history[self._cmd_history_idx])
        elif new_idx >= len(self._cmd_history):
            self._cmd_history_idx = len(self._cmd_history)
            self.input_term_cmd.clear()

    def on_term_engine_changed(self, index: int):
        engine = self.combo_term_engine.currentData()
        if engine == "wsl":
            self.lbl_term_prompt.setText("wsl$")
            self.lbl_term_prompt.setStyleSheet("color: #f59e0b; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")
        else:
            self.lbl_term_prompt.setText("PS >")
            self.lbl_term_prompt.setStyleSheet("color: #38bdf8; font-weight: bold; font-family: 'Consolas'; font-size: 12px; border: none;")

    def execute_terminal_input(self):
        cmd = self.input_term_cmd.text().strip()
        if not cmd:
            return
        if not self._cmd_history or self._cmd_history[-1] != cmd:
            self._cmd_history.append(cmd)
        self._cmd_history_idx = len(self._cmd_history)
        self.input_term_cmd.clear()
        self.execute_terminal_command(cmd)

    def execute_terminal_command(self, cmd_str: str):
        if self._term_process.state() == QProcess.Running:
            QMessageBox.warning(self, "Proceso en Ejecución", "Ya hay un comando ejecutándose. Deténgalo o espere a que finalice.")
            return

        clean_cmd = cmd_str.strip()
        clean_lower = clean_cmd.lower()

        # Comando CLI Anti-Sleep
        if clean_lower.startswith("antisleep"):
            parts = clean_cmd.split()
            arg = parts[1].lower() if len(parts) > 1 else "toggle"
            if arg in ["on", "enable", "activar", "start", "1"]:
                self.toggle_antisleep(force_state=True)
            elif arg in ["off", "disable", "desactivar", "stop", "pause", "0"]:
                self.toggle_antisleep(force_state=False)
            elif arg in ["status", "check", "info", "state"]:
                pass
            else:
                self.toggle_antisleep()

            estado_str = "ACTIVO (Prevencion de suspension y pantalla habilitada)" if self._antisleep_active else "PAUSADO (Directivas normales de energia)"
            color_str = "#34d399" if self._antisleep_active else "#94a3b8"
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(
                f"<br><span style='color: {color_str}; font-weight: bold;'>[SISTEMA ANTI-SLEEP]: {estado_str}</span><br>"
                f"<span style='color: #64748b; font-size: 11px;'>Windows API: SetThreadExecutionState | Heartbeat: 60s | Bloqueo de reposo: {'SI' if self._antisleep_active else 'NO'}</span><br>"
            )
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            return

        # Conmutación inteligente al tipear 'wsl', 'bash' o 'powershell' directamente en la consola
        if clean_lower in ["wsl", "bash", "sh"]:
            self.combo_term_engine.setCurrentIndex(1) # Cambiar a WSL
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(
                "<br><span style='color: #f59e0b; font-weight: bold;'>[🐧 MOTOR CONMUTADO]: Modo cambiado a Linux WSL (Ubuntu).</span><br>"
                "<span style='color: #94a3b8;'>Todos los comandos se ejecutarán en tu distribución Ubuntu. "
                "Para una sesión interactiva completa a pantalla completa, haz clic en el botón <b>[🐧 WSL Terminal]</b> arriba.</span><br>"
            )
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            return

        # Intercepción de Decodificación Forense en Memoria (Base64, URL, Hex, Defang/Refang)
        decode_prefixes = ["decode ", "b64 ", "b64d ", "urldecode ", "hex ", "defang ", "refang "]
        for dpfx in decode_prefixes:
            if clean_lower.startswith(dpfx):
                payload_arg = clean_cmd[len(dpfx):].strip()
                self._execute_forensic_decode(payload_arg)
                return
        if clean_lower in ["decode", "b64", "urldecode", "defang", "refang"]:
            self._execute_forensic_decode("")
            return

        # Intercepción de Desenmascarar Origen / CDN Bypass
        unmask_prefixes = ["unmask ", "origin ", "desenmascarar "]
        for upfx in unmask_prefixes:
            if clean_lower.startswith(upfx):
                domain_arg = clean_cmd[len(upfx):].strip()
                if domain_arg:
                    self.input_term_target.setText(domain_arg)
                self.run_preset_unmask_origin()
                return
        if clean_lower in ["unmask", "origin", "desenmascarar"]:
            self.run_preset_unmask_origin()
            return

        # Intercepción de Caza de Typosquatting / DNS Twist
        twist_prefixes = ["twist ", "dnstwist ", "typosquat ", "lookalike "]
        for tpfx in twist_prefixes:
            if clean_lower.startswith(tpfx):
                domain_arg = clean_cmd[len(tpfx):].strip()
                if domain_arg:
                    self.input_term_target.setText(domain_arg)
                self.run_preset_dnstwist()
                return
        if clean_lower in ["twist", "dnstwist", "typosquat", "lookalikes", "lookalike"]:
            self.run_preset_dnstwist()
            return

        # Atajo CLI para abrir el Analizador de Cabeceras
        if clean_lower in ["email", "eml", "analyzer", "cabeceras", "phishing"]:
            self.open_email_header_analyzer()
            return

        # Atajo CLI para abrir el Generador de Tickets Technoma SOC
        if clean_lower in ["ticket", "tickets", "thn", "thn-soc", "escalacion", "bitacora"]:
            self.open_thn_ticket_generator()
            return

        # Atajo CLI para abrir el Generador de Reportes de Abuso
        if clean_lower in ["abuso", "reporte-abuso", "scan-abuse", "abuse-report"]:
            self.open_abuse_report_dialog()
            return

        # Atajo CLI para abrir el Creador y Gestor de Log Filters API
        if clean_lower in ["filter", "filtros", "logfilter", "creadorfiltro", "crearfiltro", "crear-filtro"]:
            self.open_log_filter_creator()
            return

        # Intercepción inteligente de comandos CTI Directos
        # Permite al operador tipear 'vt 8.8.8.8', 'abuse 45.148.10.238', 'urlscan example.com', 'cti 1.1.1.1'
        cti_prefixes = {
            "vt ": ("virustotal", 3),
            "virustotal ": ("virustotal", 11),
            "abuse ": ("abuseipdb", 6),
            "abuseipdb ": ("abuseipdb", 10),
            "urlscan ": ("urlscan", 8),
            "cti ": ("triscan", 4),
            "triscan ": ("triscan", 8),
            "phishing ": ("phishing", 9),
            "mxtoolbox ": ("mxtoolbox", 10),
            "spf ": ("spf", 4),
            "dmarc ": ("dmarc", 6),
            "mx ": ("mx", 3),
            "cve ": ("cve", 4),
            "nvd ": ("cve", 4),
        }
        # También permitir ingresar directamente 'CVE-2024-XXXX' sin comando previo
        if clean_lower.startswith("cve-"):
            self.input_term_target.setText(clean_cmd)
            self.run_cti_async("cve", clean_cmd)
            return

        for pfx, (cti_mode, pfx_len) in cti_prefixes.items():
            if clean_lower.startswith(pfx):
                target_arg = clean_cmd[pfx_len:].strip()
                if not target_arg:
                    target_arg = self._get_active_target_or_observable()
                if not target_arg:
                    QMessageBox.warning(self, "CTI Console", f"Especifique un observable después de '{pfx.strip()}' o ingréselo en el campo objetivo.")
                    return
                self.input_term_target.setText(target_arg)
                self.run_cti_async(cti_mode, target_arg)
                return

        if clean_lower in ["powershell", "pwsh", "cmd"]:
            self.combo_term_engine.setCurrentIndex(0) # Cambiar a PowerShell
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(
                "<br><span style='color: #38bdf8; font-weight: bold;'>[⚡ MOTOR CONMUTADO]: Modo cambiado a Windows PowerShell.</span><br>"
            )
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            return

        engine = self.combo_term_engine.currentData()

        # Intercepción de comando WHOIS para motor forense enriquecido (BGP, RDAP y Titularidad Dual)
        if clean_lower.startswith("whois "):
            target_arg = clean_cmd[6:].strip()
            py_exec = os.path.join(SCRIPT_DIR, "venv", "Scripts", "python.exe")
            if not os.path.exists(py_exec):
                py_exec = sys.executable if sys.executable else "python"
            whois_script = os.path.join(SCRIPT_DIR, "whois_recon.py")
            if engine == "wsl":
                cmd_str = f"python3 whois_recon.py {target_arg} 2>/dev/null || whois {target_arg}"
            else:
                cmd_str = f"& '{py_exec}' '{whois_script}' {target_arg}"

        # Enrutamiento inteligente a WSL: Si el operador está en PowerShell y tipea 'dig <host>' o 'traceroute <ip>',
        # enrutarlo automáticamente a Ubuntu WSL para que funcione inmediatamente en lugar de arrojar CommandNotFoundException.
        run_in_wsl = (engine == "wsl")
        if engine == "powershell" and (clean_lower.startswith("dig ") or clean_lower.startswith("traceroute ")):
            run_in_wsl = True
            prompt = "wsl:auto-route$ "
        else:
            prompt = "wsl:ubuntu$ " if engine == "wsl" else "PS > "

        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertHtml(f"<br><span style='color: #38bdf8; font-weight: bold;'>{he(prompt)}</span> <span style='color: #f8fafc;'>{he(cmd_str)}</span><br>")
        self.txt_terminal_output.moveCursor(QTextCursor.End)

        workdir = os.path.abspath(".")
        self._term_process.setWorkingDirectory(workdir)

        if run_in_wsl:
            program = "wsl.exe"
            args = ["-d", "Ubuntu", "-e", "bash", "-c", cmd_str]
        else:
            program = "powershell.exe"
            # Configurar codificación UTF-8 en PowerShell para preservar tildes, eñes y caracteres especiales
            ps_cmd = f"[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; {cmd_str}"
            args = ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_cmd]

        self.btn_term_run.setEnabled(False)
        self.btn_term_stop.setEnabled(True)
        self._term_process.start(program, args)

    def _decode_term_bytes(self, data: bytes) -> str:
        for enc in ("utf-8", "cp850", "cp1252", "latin-1"):
            try:
                return data.decode(enc)
            except Exception:
                pass
        return data.decode("latin-1", errors="replace")

    def _on_term_stdout(self):
        raw = self._term_process.readAllStandardOutput().data()
        text = self._decode_term_bytes(raw)
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertPlainText(text)
        self.txt_terminal_output.moveCursor(QTextCursor.End)

    def _on_term_stderr(self):
        raw = self._term_process.readAllStandardError().data()
        text = self._decode_term_bytes(raw)
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertHtml(f"<span style='color: #ef4444;'>{he(text)}</span>")
        self.txt_terminal_output.moveCursor(QTextCursor.End)

    def _on_term_finished(self, exit_code: int, exit_status):
        self.btn_term_run.setEnabled(True)
        self.btn_term_stop.setEnabled(False)
        color = "#10b981" if exit_code == 0 else "#f59e0b"
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertHtml(f"<span style='color: {color};'>\n[Proceso completado con código de salida {exit_code}]</span><br>")
        self.txt_terminal_output.moveCursor(QTextCursor.End)

    def stop_terminal_process(self):
        if self._term_process.state() == QProcess.Running:
            self._term_process.kill()
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml("<span style='color: #ef4444;'><br>[Proceso abortado manualmente por el analista]<br></span>")
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.btn_term_run.setEnabled(True)
            self.btn_term_stop.setEnabled(False)

    def clear_terminal_output(self):
        self.txt_terminal_output.clear()

    def copy_terminal_output(self):
        text = self.txt_terminal_output.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Terminal", "Salida de la consola copiada al portapapeles.")

    def launch_external_ps_admin(self):
        workdir = os.path.abspath(".")
        wt_path = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe")
        try:
            if os.path.exists(wt_path):
                ctypes.windll.shell32.ShellExecuteW(None, "runas", wt_path, f"-d \"{workdir}\" -p \"Windows PowerShell\"", None, 1)
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", "powershell.exe", f"-NoExit -Command \"Set-Location '{workdir}'\"", None, 1)
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(f"<span style='color: #38bdf8;'><br>[+] Solicitando elevación UAC: Ventana externa de PowerShell (Admin) en: {he(workdir)}<br></span>")
            self.txt_terminal_output.moveCursor(QTextCursor.End)
        except Exception as e:
            QMessageBox.warning(self, "PowerShell Admin", f"No se pudo elevar el proceso: {e}")

    def launch_external_wsl(self):
        workdir = os.path.abspath(".")
        wt_path = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe")
        try:
            if os.path.exists(wt_path):
                subprocess.Popen([wt_path, "-p", "Ubuntu", "-d", workdir])
            else:
                subprocess.Popen(["cmd.exe", "/c", "start", "wsl.exe", "-d", "Ubuntu"], cwd=workdir)
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(f"<span style='color: #f59e0b;'><br>[+] Ventana interactiva de Ubuntu WSL2 lanzada en: {he(workdir)}<br></span>")
            self.txt_terminal_output.moveCursor(QTextCursor.End)
        except Exception as e:
            QMessageBox.warning(self, "WSL Terminal", f"No se pudo lanzar la terminal de WSL: {e}")

    def _get_active_target_or_observable(self) -> str:
        target = self.input_term_target.text().strip()
        if not target:
            t_id = self.input_case_ticket.text().strip()
            if t_id and t_id in getattr(self, 'dict_casos_activos', {}):
                c = self.dict_casos_activos[t_id]
                for fld in ["srcip", "dstip", "domain", "host", "hostname"]:
                    if c.get(fld):
                        target = str(c[fld]).strip()
                        break
                if not target:
                    target = str(c.get("name", "")).strip()
        return target

    def run_preset_dns(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset DNS", "Ingrese una IP, dominio o hostname en el campo objetivo.")
            return
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        obs_type = CtiEngine.detect_observable_type(clean_target)
        engine = self.combo_term_engine.currentData()

        if obs_type == "ip":
            if engine == "wsl":
                cmd = (
                    f"echo '=== CONSULTA DNS REVERSA & DNSBL (IP: {clean_target}) ===' && "
                    f"ptr=$(dig -x {clean_target} +short @8.8.8.8) && "
                    f"if [ -n \"$ptr\" ]; then echo \"[+] PTR (Hostname): $ptr\"; else echo \"[-] PTR (Hostname): Sin PTR declarado (NXDOMAIN)\"; fi && "
                    f"rev_ip=$(echo {clean_target} | awk -F. '{{print $4\".\"$3\".\"$2\".\"$1\".zen.spamhaus.org\"}}') && "
                    f"sbl=$(dig +short $rev_ip @8.8.8.8) && "
                    f"if [ -n \"$sbl\" ]; then echo \"[!] SPAMHAUS ZEN DNSBL: LISTADA ($sbl)\"; else echo \"[+] SPAMHAUS ZEN DNSBL: Limpia / No listada\"; fi"
                )
            else:
                cmd = (
                    f"Write-Host '=== CONSULTA DNS REVERSA & DNSBL (IP: {clean_target}) ===' -ForegroundColor Cyan; "
                    f"$ptr = (Resolve-DnsName -Name '{clean_target}' -Type PTR -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty NameHost); "
                    f"if ($ptr) {{ Write-Host ('[+] PTR (Hostname): ' + $ptr) -ForegroundColor Green }} else {{ Write-Host '[-] PTR (Hostname): Sin PTR declarado (NXDOMAIN)' -ForegroundColor Yellow }}; "
                    f"$parts = '{clean_target}'.Split('.'); "
                    f"if ($parts.Count -eq 4) {{ "
                    f"$rev = ($parts[3] + '.' + $parts[2] + '.' + $parts[1] + '.' + $parts[0] + '.zen.spamhaus.org'); "
                    f"$sbl = (Resolve-DnsName -Name $rev -Type A -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty IPAddress); "
                    f"if ($sbl) {{ Write-Host ('[!] SPAMHAUS ZEN DNSBL: LISTADA (' + ($sbl -join ', ') + ')') -ForegroundColor Red }} else {{ Write-Host '[+] SPAMHAUS ZEN DNSBL: Limpia / No listada' -ForegroundColor Green }} }}"
                )
        else:
            if engine == "wsl":
                cmd = (
                    f"if ! command -v dig >/dev/null 2>&1; then "
                    f"echo '[!] ERROR: El comando \"dig\" (dnsutils) no está instalado en tu WSL (Ubuntu).' && "
                    f"echo '    -> Solución 1 (Inmediata): Cambia el selector de Terminal a \"PowerShell (Windows)\" (100% nativo y funcional).' && "
                    f"echo '    -> Solución 2: En WSL ejecuta: sudo apt update && sudo apt install -y dnsutils' && "
                    f"exit 1; fi && "
                    f"echo '=== RECONOCIMIENTO DNS FORENSE: {clean_target} ===' && "
                    f"echo '--- [1] Registros A / AAAA (IPs) ---' && "
                    f"a_recs=$(dig +short {clean_target} A @8.8.8.8) && "
                    f"if [ -n \"$a_recs\" ]; then echo \"[+] A: $(echo $a_recs | tr '\\n' ' ')\"; else echo \"[-] Sin registros A (Posible NXDOMAIN)\"; fi && "
                    f"echo '--- [2] Registros MX (Correo) ---' && "
                    f"mx_recs=$(dig +short {clean_target} MX @8.8.8.8) && "
                    f"if [ -n \"$mx_recs\" ]; then echo \"[+] MX: $(echo $mx_recs | tr '\\n' ' ')\"; else echo \"[-] Sin registros MX\"; fi && "
                    f"echo '--- [3] Registros NS (Servidores Autoritativos) ---' && "
                    f"ns_recs=$(dig +short {clean_target} NS @8.8.8.8) && "
                    f"if [ -n \"$ns_recs\" ]; then echo \"[+] NS: $(echo $ns_recs | tr '\\n' ' ')\"; else echo \"[-] Sin registros NS\"; fi && "
                    f"echo '--- [4] Registros TXT (SPF/DMARC/Verificaciones) ---' && "
                    f"txt_recs=$(dig +short {clean_target} TXT @8.8.8.8) && "
                    f"if [ -n \"$txt_recs\" ]; then echo \"[+] TXT: $txt_recs\"; else echo \"[-] Sin registros TXT\"; fi"
                )
            else:
                cmd = (
                    f"Write-Host '=== RECONOCIMIENTO DNS FORENSE: {clean_target} ===' -ForegroundColor Cyan; "
                    f"Write-Host '--- [1] Registros A / AAAA (IPs) ---' -ForegroundColor DarkGray; "
                    f"$a = (Resolve-DnsName -Name '{clean_target}' -Type A -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty IPAddress); "
                    f"if ($a) {{ Write-Host ('[+] A: ' + ($a -join ', ')) -ForegroundColor Green }} else {{ Write-Host '[-] Sin registros A (Posible NXDOMAIN)' -ForegroundColor Yellow }}; "
                    f"Write-Host '--- [2] Registros MX (Correo) ---' -ForegroundColor DarkGray; "
                    f"$mx = (Resolve-DnsName -Name '{clean_target}' -Type MX -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -Property Preference, NameExchange); "
                    f"if ($mx) {{ $mx | ForEach-Object {{ Write-Host ('[+] MX (Pref ' + $_.Preference + '): ' + $_.NameExchange) -ForegroundColor Green }} }} else {{ Write-Host '[-] Sin registros MX' -ForegroundColor DarkGray }}; "
                    f"Write-Host '--- [3] Registros NS (Servidores Autoritativos) ---' -ForegroundColor DarkGray; "
                    f"$ns = (Resolve-DnsName -Name '{clean_target}' -Type NS -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty NameHost); "
                    f"if ($ns) {{ Write-Host ('[+] NS: ' + ($ns -join ', ')) -ForegroundColor Cyan }} else {{ Write-Host '[-] Sin registros NS' -ForegroundColor DarkGray }}; "
                    f"Write-Host '--- [4] Registros TXT (SPF/DMARC/Verificaciones) ---' -ForegroundColor DarkGray; "
                    f"$txt = (Resolve-DnsName -Name '{clean_target}' -Type TXT -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Strings); "
                    f"if ($txt) {{ $txt | ForEach-Object {{ Write-Host ('[+] TXT: ' + $_) -ForegroundColor Yellow }} }} else {{ Write-Host '[-] Sin registros TXT' -ForegroundColor DarkGray }}"
                )
        self.execute_terminal_command(cmd)

    def run_preset_ptr(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset PTR", "Ingrese una dirección IP o dominio en el campo objetivo para consultar su resolución inversa (PTR).")
            return
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        obs_type = CtiEngine.detect_observable_type(clean_target)
        engine = self.combo_term_engine.currentData()

        if obs_type == "ip":
            if engine == "wsl":
                cmd = (
                    f"echo '=== RESOLUCIÓN INVERSA DNS (PTR) ===' && "
                    f"ptr=$(dig -x {clean_target} +short @8.8.8.8) && "
                    f"if [ -n \"$ptr\" ]; then echo \"[+] Hostname PTR: $ptr\"; else "
                    f"echo '[!] Sin registro PTR declarado (NXDOMAIN)' && "
                    f"echo '[i] Nota SOC: CDNs/WAFs como Cloudflare, Fastly o AWS no publican registros PTR para IPs proxy compartidas.'; fi"
                )
            else:
                cmd = (
                    f"Write-Host '=== RESOLUCIÓN INVERSA DNS (PTR) ===' -ForegroundColor Cyan; "
                    f"$ptr = (Resolve-DnsName -Name '{clean_target}' -Type PTR -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty NameHost); "
                    f"if ($ptr) {{ Write-Host ('[+] Hostname PTR: ' + $ptr) -ForegroundColor Green }} else {{ "
                    f"Write-Host '[!] Sin registro PTR declarado (NXDOMAIN)' -ForegroundColor Yellow; "
                    f"Write-Host '[i] Nota SOC: CDNs/WAFs como Cloudflare, Fastly o AWS no publican registros PTR para IPs proxy compartidas.' -ForegroundColor DarkGray }}"
                )
        else:
            if engine == "wsl":
                cmd = (
                    f"if ! command -v dig >/dev/null 2>&1; then "
                    f"echo '[!] ERROR: El comando \"dig\" (dnsutils) no está instalado en tu WSL (Ubuntu).' && "
                    f"echo '    -> Solución 1 (Inmediata): Cambia el selector de Terminal a \"PowerShell (Windows)\" (100% nativo y funcional).' && "
                    f"echo '    -> Solución 2: En WSL ejecuta: sudo apt update && sudo apt install -y dnsutils' && "
                    f"exit 1; fi && "
                    f"echo '=== RESOLUCIÓN INVERSA DNS (PTR) DE DOMINIO ===' && "
                    f"echo '[*] Objetivo es un Dominio ({clean_target}). Resolviendo registros A...' && "
                    f"ips=$(dig +short {clean_target} @8.8.8.8 | grep -E '^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+') && "
                    f"if [ -z \"$ips\" ]; then echo '[!] No se resolvieron IPs A para {clean_target}'; else "
                    f"echo \"[+] IPs resueltas: $(echo $ips | tr '\\n' ' ')\" && echo '--- Consultando PTR de cada IP ---' && "
                    f"for ip in $ips; do ptr=$(dig -x \"$ip\" +short @8.8.8.8); "
                    f"if [ -n \"$ptr\" ]; then echo \"[+] $ip -> $ptr\"; else "
                    f"echo \"[-] $ip -> [Sin registro PTR / Común en Cloudflare o CDNs]\"; fi; done; fi"
                )
            else:
                cmd = (
                    f"Write-Host '=== RESOLUCIÓN INVERSA DNS (PTR) DE DOMINIO ===' -ForegroundColor Cyan; "
                    f"Write-Host '[*] Objetivo es un Dominio ({clean_target}). Resolviendo registros A...' -ForegroundColor Gray; "
                    f"$ips = (Resolve-DnsName -Name '{clean_target}' -Type A -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty IPAddress); "
                    f"if (-not $ips) {{ Write-Host '[!] No se resolvieron IPs A para {clean_target}' -ForegroundColor Red }} else {{ "
                    f"Write-Host ('[+] IPs resueltas: ' + ($ips -join ', ')) -ForegroundColor Green; "
                    f"Write-Host '--- Consultando PTR de cada IP ---' -ForegroundColor Cyan; "
                    f"foreach ($ip in $ips) {{ "
                    f"$ptr = (Resolve-DnsName -Name $ip -Type PTR -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty NameHost); "
                    f"if ($ptr) {{ Write-Host ('[+] ' + $ip + ' -> ' + $ptr) -ForegroundColor Green }} else {{ "
                    f"Write-Host ('[-] ' + $ip + ' -> [Sin registro PTR / Comun en Cloudflare o CDNs]') -ForegroundColor Yellow }} }} }}"
                )
        self.execute_terminal_command(cmd)

    def run_preset_whois(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset WHOIS", "Ingrese una IP o dominio en el campo objetivo.")
            return
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        engine = self.combo_term_engine.currentData()
        py_exec = os.path.join(SCRIPT_DIR, "venv", "Scripts", "python.exe")
        if not os.path.exists(py_exec):
            py_exec = sys.executable if sys.executable else "python"
        whois_script = os.path.join(SCRIPT_DIR, "whois_recon.py")

        if engine == "wsl":
            cmd = f"python3 whois_recon.py '{clean_target}' 2>/dev/null || python whois_recon.py '{clean_target}' 2>/dev/null || whois '{clean_target}'"
        else:
            cmd = f"& '{py_exec}' '{whois_script}' '{clean_target}'"
        self.execute_terminal_command(cmd)

    def run_preset_ping(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset Conexión", "Ingrese una IP o host en el campo objetivo.")
            return
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        engine = self.combo_term_engine.currentData()
        if engine == "wsl":
            cmd = (
                f"echo '=== DIAGNÓSTICO DE CONECTIVIDAD & PUERTOS: {clean_target} ===' && "
                f"echo '[*] [1/2] Probando ICMP Echo (Ping)...' && "
                f"if ping -c 2 -W 1 {clean_target} >/dev/null 2>&1; then "
                f"echo '[+] ICMP: ALCANZABLE (Host responde ping)'; else "
                f"echo '[-] ICMP: INALCANZABLE (ICMP bloqueado o host apagado)'; fi && "
                f"echo '[*] [2/2] Sondeo rápido de puertos perimetrales (80, 443, 22, 3389, 8080)...' && "
                f"for p in 80 443 22 3389 8080; do "
                f"if nc -z -w 1 {clean_target} $p 2>/dev/null; then echo \"  [+] Puerto $p/TCP: ABIERTO\"; else echo \"  [-] Puerto $p/TCP: Cerrado/Filtrado\"; fi; done"
            )
        else:
            cmd = (
                f"Write-Host '=== DIAGNÓSTICO DE CONECTIVIDAD & PUERTOS: {clean_target} ===' -ForegroundColor Cyan; "
                f"Write-Host '[*] [1/2] Probando ICMP Echo (Ping rápido)...' -ForegroundColor Gray; "
                f"$null = ping.exe -n 2 -w 1000 {clean_target}; "
                f"if ($LASTEXITCODE -eq 0) {{ Write-Host '[+] ICMP: ALCANZABLE (Host activo y responde a echo)' -ForegroundColor Green }} else {{ Write-Host '[-] ICMP: INALCANZABLE (ICMP bloqueado por firewall o host offline)' -ForegroundColor Yellow }}; "
                f"Write-Host '[*] [2/2] Sondeo perimetral de puertos TCP comunes (Timeout 600ms):' -ForegroundColor Gray; "
                f"$ports = @(80, 443, 22, 3389, 8080); "
                f"foreach ($p in $ports) {{ "
                f"$tcp = New-Object System.Net.Sockets.TcpClient; "
                f"$ar = $tcp.BeginConnect('{clean_target}', $p, $null, $null); "
                f"if ($ar.AsyncWaitHandle.WaitOne(600, $false) -and $tcp.Connected) {{ "
                f"$tcp.EndConnect($ar); "
                f"Write-Host ('  [+] Puerto ' + $p + '/TCP: ABIERTO') -ForegroundColor Green "
                f"}} else {{ "
                f"Write-Host ('  [-] Puerto ' + $p + '/TCP: Cerrado / Filtrado') -ForegroundColor DarkGray "
                f"}}; "
                f"$tcp.Close() }}"
            )
        self.execute_terminal_command(cmd)

    def run_preset_curl(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset CURL", "Ingrese una URL o dirección IP en el campo objetivo.")
            return
        raw_target = target.strip()
        has_scheme = raw_target.lower().startswith("http://") or raw_target.lower().startswith("https://")
        clean_target = re.sub(r"^https?://", "", raw_target).rstrip("/")
        engine = self.combo_term_engine.currentData()

        if has_scheme or ":" in clean_target:
            url_to_test = raw_target if has_scheme else f"http://{clean_target}"
            if engine == "wsl":
                cmd = (
                    f"echo '=== INSPECCIÓN HTTP/S HEADERS: {url_to_test} ===' && "
                    f"curl -I -s -k --connect-timeout 3 --max-time 6 \"{url_to_test}\" || "
                    f"echo '[!] Tiempo de conexión agotado o puerto no responde (Timeout 3s).'"
                )
            else:
                cmd = (
                    f"Write-Host '=== INSPECCIÓN HTTP/S HEADERS: {url_to_test} ===' -ForegroundColor Cyan; "
                    f"$res = curl.exe -I -s -k --connect-timeout 3 --max-time 6 \"{url_to_test}\"; "
                    f"if ($res) {{ $res | Out-String | Write-Host -ForegroundColor Gray }} else {{ "
                    f"Write-Host '[!] Conexión agotada o puerto no responde (Timeout 3s).' -ForegroundColor Yellow }}"
                )
        else:
            if engine == "wsl":
                cmd = (
                    f"echo '=== INSPECCIÓN WEB HTTP / HTTPS: {clean_target} ===' && "
                    f"echo '[*] Probando HTTPS (Puerto 443, Timeout 3s)...' && "
                    f"https_out=$(curl -I -s -k --connect-timeout 3 --max-time 5 \"https://{clean_target}\") && "
                    f"if [ -n \"$https_out\" ]; then echo \"[+] Respuesta HTTPS (443):\" && echo \"$https_out\"; else "
                    f"echo '[-] Sin respuesta HTTPS (443). Probando HTTP plano (Puerto 80)...' && "
                    f"http_out=$(curl -I -s -k --connect-timeout 3 --max-time 5 \"http://{clean_target}\") && "
                    f"if [ -n \"$http_out\" ]; then echo \"[+] Respuesta HTTP (80):\" && echo \"$http_out\"; else "
                    f"echo '[!] Puertos web 80 y 443 cerrados o filtrados (Host no aloja web pública).'; fi; fi"
                )
            else:
                cmd = (
                    f"Write-Host '=== INSPECCIÓN WEB HTTP / HTTPS: {clean_target} ===' -ForegroundColor Cyan; "
                    f"Write-Host '[*] Probando HTTPS (Puerto 443, Timeout 3s)...' -ForegroundColor Gray; "
                    f"$httpsOut = curl.exe -I -s -k --connect-timeout 3 --max-time 5 \"https://{clean_target}\"; "
                    f"if ($httpsOut) {{ "
                    f"Write-Host '[+] Respuesta HTTPS (443):' -ForegroundColor Green; "
                    f"$httpsOut | Out-String | Write-Host -ForegroundColor Gray "
                    f"}} else {{ "
                    f"Write-Host '[-] Sin respuesta HTTPS (443). Probando HTTP plano (Puerto 80)...' -ForegroundColor Yellow; "
                    f"$httpOut = curl.exe -I -s -k --connect-timeout 3 --max-time 5 \"http://{clean_target}\"; "
                    f"if ($httpOut) {{ "
                    f"Write-Host '[+] Respuesta HTTP (80):' -ForegroundColor Green; "
                    f"$httpOut | Out-String | Write-Host -ForegroundColor Gray "
                    f"}} else {{ "
                    f"Write-Host '[!] Puertos web 80 y 443 cerrados o filtrados (Host no aloja web pública).' -ForegroundColor Yellow "
                    f"}} }}"
                )
        self.execute_terminal_command(cmd)

    def run_preset_grep(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset Grep", "Ingrese un IOC, IP o término a buscar en los logs.")
            return
        clean_target = target.strip()
        engine = self.combo_term_engine.currentData()
        if engine == "wsl":
            cmd = (
                f"echo '=== HISTORIAL DE IOC EN CASOS SOC & LOGS ===' && "
                f"grep -rn --exclude-dir=.git --exclude-dir=.venv --exclude-dir=__pycache__ '{clean_target}' . 2>/dev/null | head -n 30 || "
                f"echo '[!] No se encontró este IOC en casos anteriores.'"
            )
        else:
            cmd = (
                f"Write-Host '=== HISTORIAL DE IOC EN CASOS SOC & INFORMES ===' -ForegroundColor Cyan; "
                f"$found = Get-ChildItem -Recurse -File -Include *.md,*.json,*.txt -Exclude *venv*,*.git* | Select-String -Pattern '{clean_target}' | Select-Object -First 25; "
                f"if ($found) {{ $found | ForEach-Object {{ Write-Host ($_.Path.Replace($PWD.Path, '.') + ':' + $_.LineNumber) -ForegroundColor Yellow; Write-Host ('  ' + $_.Line.Trim()) -ForegroundColor Gray }} }} else {{ Write-Host '[!] No se encontró este IOC en casos anteriores.' -ForegroundColor DarkGray }}"
            )
        self.execute_terminal_command(cmd)

    def run_preset_anti_spoofing(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset Anti-Spoofing", "Ingrese un dominio o URL en el campo objetivo para verificar SPF/DMARC/MX.")
            return
        clean_target = target.strip()
        clean_target = re.sub(r"^https?://", "", clean_target).split("/")[0].split(":")[0]
        engine = self.combo_term_engine.currentData()
        if engine == "wsl":
            cmd = (
                f"if ! command -v dig >/dev/null 2>&1; then "
                f"echo '[!] ERROR: El comando \"dig\" (dnsutils) no está instalado en tu WSL (Ubuntu).' && "
                f"echo '    -> Solución 1 (Inmediata): Cambia el selector de Terminal a \"PowerShell (Windows)\" (100% nativo y funcional).' && "
                f"echo '    -> Solución 2: En WSL ejecuta: sudo apt update && sudo apt install -y dnsutils' && "
                f"exit 1; fi && "
                f"echo '=== [1/3] REGISTRO SPF (DNS TXT) ===' && "
                f"(dig +short TXT {clean_target} @8.8.8.8 | grep -i 'v=spf1' || echo '[!] Sin registro SPF declarado') && "
                f"echo '' && echo '=== [2/3] POLÍTICA DMARC (_dmarc.{clean_target}) ===' && "
                f"(dig +short TXT _dmarc.{clean_target} @8.8.8.8 || echo '[!] Sin registro DMARC declarado (VULNERABLE A SUPLANTACIÓN)') && "
                f"echo '' && echo '=== [3/3] SERVIDORES MX ===' && "
                f"(dig +short MX {clean_target} @8.8.8.8 || echo '[!] Sin servidores MX configurados')"
            )
        else:
            cmd = (
                f"Write-Host '=== [1/3] REGISTRO SPF (DNS TXT) ===' -ForegroundColor Cyan; "
                f"$spf = (Resolve-DnsName -Name '{clean_target}' -Type TXT -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.Strings -like '*v=spf1*' }} | Select-Object -ExpandProperty Strings); "
                f"if ($spf) {{ $spf }} else {{ Write-Host '[!] Sin registro SPF declarado' -ForegroundColor Yellow }}; "
                f"Write-Host '`n=== [2/3] POLÍTICA DMARC (_dmarc) ===' -ForegroundColor Magenta; "
                f"$dmarc = (Resolve-DnsName -Name '_dmarc.{clean_target}' -Type TXT -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Strings); "
                f"if ($dmarc) {{ $dmarc }} else {{ Write-Host '[!] Sin registro DMARC declarado (VULNERABLE A SUPLANTACIÓN)' -ForegroundColor Red }}; "
                f"Write-Host '`n=== [3/3] SERVIDORES MX ===' -ForegroundColor Green; "
                f"$mx = (Resolve-DnsName -Name '{clean_target}' -Type MX -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -Property NameExchange, Preference); "
                f"if ($mx) {{ $mx | Format-Table -AutoSize }} else {{ Write-Host '[!] Sin servidores MX configurados' -ForegroundColor Yellow }}"
            )
        self.execute_terminal_command(cmd)

    def run_preset_unmask_origin(self):
        """Audita el dominio en busca de la IP real de origen eludiendo el proxy de Cloudflare/CDN."""
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Desemmascarar Origen", "Ingrese un nombre de dominio o URL en el campo objetivo (ej. msb365.blog).")
            return
        if hasattr(self, "tabs") and hasattr(self, "tab5"):
            self.tabs.setCurrentWidget(self.tab5)
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        obs_type = CtiEngine.detect_observable_type(clean_target)

        if obs_type == "ip":
            QMessageBox.information(
                self,
                "Desemmascarar Origen",
                f"El objetivo '{clean_target}' ya es una dirección IP.\n\n"
                f"Esta función está diseñada para desenmascarar DOMINIOS que se ocultan detrás de Cloudflare (ej. msb365.blog).\n\n"
                f"Para esta IP se ejecutará la resolución inversa (PTR) y consulta de Hosting..."
            )
            self.run_preset_ptr()
            return

        # Detección inteligente de Dominio Raíz (Apex) si el objetivo es un subdominio
        parts = clean_target.split(".")
        cc_tlds = {"com", "edu", "gov", "gob", "org", "net", "co", "mil", "nom"}
        if len(parts) >= 3 and parts[-2].lower() in cc_tlds:
            root_domain = ".".join(parts[-3:])
        elif len(parts) > 2:
            root_domain = ".".join(parts[-2:])
        else:
            root_domain = clean_target

        is_sub = (root_domain.lower() != clean_target.lower())

        # Detección de plataformas multi-inquilino / PaaS públicas (GitHub Pages, Vercel, Netlify, etc.)
        public_paas_domains = {
            "github.io", "gitlab.io", "netlify.app", "vercel.app", "pages.dev",
            "firebaseapp.com", "web.app", "azureedge.net", "cloudfront.net",
            "s3.amazonaws.com", "herokuapp.com", "wixsite.com", "wordpress.com",
            "blogspot.com", "myshopify.com", "render.com", "fly.dev", "pantheonsite.io"
        }
        is_paas = root_domain.lower() in public_paas_domains

        engine = self.combo_term_engine.currentData()

        # Regex unificado de CDNs conocidas (Cloudflare, Fastly, GitHub Pages, etc.)
        cdn_rgx_wsl = r'^(104\.|172\.(6[4-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-7])\.|162\.15[89]\.|185\.199\.(108|109|110|111)\.|151\.101\.|199\.232\.|198\.41\.|188\.114\.|141\.101\.)'
        cdn_rgx_ps = r'^(104\.|172\.(6[4-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-7])\.|162\.15[89]\.|185\.199\.(108|109|110|111)\.|151\.101\.|199\.232\.|198\.41\.|188\.114\.|141\.101\.)'

        if engine == "wsl":
            if is_paas:
                sub_notice = (
                    f"echo 'ℹ️ [PLATAFORMA PAAS / HOSTING COMPARTIDO]: {clean_target} está alojado en {root_domain}'; "
                    f"echo '   El dominio raíz pertenece a un proveedor público y no representa servidores privados del atacante.'; echo ''; "
                )
            elif is_sub:
                sub_notice = f"echo 'ℹ️ [SUBDOMINIO DETECTADO]: Auditando subdominio y dominio raíz ({root_domain})'; echo ''; "
            else:
                sub_notice = ""

            paas_step4 = (
                f"echo '  [i] Barrido pasivo de subdominios omitido: {root_domain} es una plataforma SaaS/PaaS pública.'; "
                f"echo '      Barrer subdominios en {root_domain} descubriría la CDN del proveedor y causaría falsos positivos.'; "
            ) if is_paas else (
                f"sub_candidates='mail webmail cpanel direct origin ftp autodiscover smtp vpn admin dev ns1 ns2'; "
                f"for sub in $sub_candidates; do fqdn=\"$sub.{root_domain}\"; "
                f"sub_ip=$(dig +short \"$fqdn\" @8.8.8.8 | grep -E '^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' | head -n 1 || true); "
                f"if [ -n \"$sub_ip\" ]; then "
                f"ptr=$(dig -x \"$sub_ip\" +short @8.8.8.8 || true); "
                f"if [[ \"$sub_ip\" =~ {cdn_rgx_wsl} ]] || [[ \"$ptr\" =~ (cdn|cloudflare|fastly|akamai|cloudfront|github|edgekey) ]]; then "
                f"echo \"  [-] $fqdn -> $sub_ip (CDN / Proxy Activo)\"; else "
                f"echo \"  [🚨 ORIGEN ENCONTRADO]: $fqdn -> $sub_ip\"; "
                f"[ -n \"$ptr\" ] && echo \"     [+] PTR: $ptr\"; "
                f"isp=$(curl -s \"https://ipinfo.io/$sub_ip/json\" 2>/dev/null | grep -o '\"org\": \"[^\"]*' | cut -d'\"' -f4 || true); "
                f"[ -n \"$isp\" ] && echo \"     [+] ISP/Hosting: $isp\"; fi; fi; done; "
            )

            cmd = (
                f"if ! command -v dig >/dev/null 2>&1; then "
                f"echo '[!] ERROR: El comando \"dig\" (dnsutils) no está instalado en tu WSL (Ubuntu).' && "
                f"echo '    -> Solución 1 (Inmediata): Cambia el selector de Terminal a \"PowerShell (Windows)\" (100% nativo y funcional).' && "
                f"echo '    -> Solución 2: En WSL ejecuta: sudo apt update && sudo apt install -y dnsutils' && "
                f"exit 1; fi; "
                f"echo '============================================================='; "
                f"echo '🕵️ [AUDITORÍA DE ORIGEN & BYPASS DE CDN / CLOUDFLARE]'; "
                f"echo 'Objetivo analizado: {clean_target}'; "
                f"echo '============================================================='; echo ''; "
                f"{sub_notice}"
                f"echo '[1/4] Comprobando IPs Web actuales...'; "
                f"web_ips=$(dig +short {clean_target} @8.8.8.8 | grep -E '^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' || true); "
                f"if [ -z \"$web_ips\" ]; then echo '  [!] No se resolvieron IPs A para este objetivo.'; else "
                f"for wip in $web_ips; do echo \"  -> IP Web: $wip\"; "
                f"if [[ \"$wip\" =~ {cdn_rgx_wsl} ]]; then "
                f"echo '     [!] Pertenece a Anycast CDN / Proxy Activo (Cloudflare/Fastly/GitHub Pages)'; fi; done; fi; echo ''; "
                f"echo '[2/4] Buscando Fugas en Registros de Correo (MX / Direct Connect)...'; "
                f"mx_target='{clean_target}'; "
                f"mx_records=$(dig +short MX \"$mx_target\" @8.8.8.8 | awk '{{print $2}}' | sed 's/\\.$//' || true); "
                f"if [ -z \"$mx_records\" ] && [ '{clean_target}' != '{root_domain}' ] && [ '{str(is_paas)}' != 'True' ]; then "
                f"echo '  [i] Sin MX en subdominio; comprobando dominio raíz ({root_domain})...'; "
                f"mx_records=$(dig +short MX {root_domain} @8.8.8.8 | awk '{{print $2}}' | sed 's/\\.$//' || true); fi; "
                f"if [ -n \"$mx_records\" ]; then for mx in $mx_records; do echo \"  -> Registro MX: $mx\"; "
                f"if [[ \"$mx\" =~ ^_dc-mx\\. ]]; then echo '     [🚨 FUGA CRÍTICA]: Cloudflare Direct Connect MX detectado (_dc-mx)!'; fi; "
                f"mx_ip=$(dig +short \"$mx\" @8.8.8.8 | grep -E '^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+' | head -n 1 || true); "
                f"if [ -n \"$mx_ip\" ]; then echo \"     [🎯 IP DE ORIGEN / CORREO]: $mx_ip\"; "
                f"ptr=$(dig -x \"$mx_ip\" +short @8.8.8.8 || true); [ -n \"$ptr\" ] && echo \"     [+] Hostname PTR: $ptr\"; "
                f"isp=$(curl -s \"https://ipinfo.io/$mx_ip/json\" 2>/dev/null | grep -o '\"org\": \"[^\"]*' | cut -d'\"' -f4 || true); "
                f"[ -n \"$isp\" ] && echo \"     [+] ISP/Hosting: $isp\"; fi; done; "
                f"else echo '  [!] No se detectaron servidores MX en el objetivo ni en el dominio raíz.'; fi; echo ''; "
                f"echo '[3/4] Analizando Registro SPF (ip4: autorizadas)...'; "
                f"spf_ips=$(dig +short TXT {clean_target} @8.8.8.8 | grep -i 'v=spf1' | grep -o -E 'ip4:[^ ]+' | sed 's/ip4://' || true); "
                f"if [ -z \"$spf_ips\" ] && [ '{clean_target}' != '{root_domain}' ] && [ '{str(is_paas)}' != 'True' ]; then "
                f"echo '  [i] Sin SPF en subdominio; comprobando dominio raíz ({root_domain})...'; "
                f"spf_ips=$(dig +short TXT {root_domain} @8.8.8.8 | grep -i 'v=spf1' | grep -o -E 'ip4:[^ ]+' | sed 's/ip4://' || true); fi; "
                f"if [ -n \"$spf_ips\" ]; then for sip in $spf_ips; do echo \"  [🚨 RANGO IP DECLARADO EN SPF]: $sip\"; "
                f"sip_clean=$(echo \"$sip\" | cut -d'/' -f1); "
                f"isp=$(curl -s \"https://ipinfo.io/$sip_clean/json\" 2>/dev/null | grep -o '\"org\": \"[^\"]*' | cut -d'\"' -f4 || true); "
                f"[ -n \"$isp\" ] && echo \"     [+] ISP/Hosting: $isp\"; done; "
                f"else echo '  [!] No se encontraron directivas ip4: en SPF.'; fi; echo ''; "
                f"echo '[4/4] Barrido Pasivo de Subdominios Comunes en {root_domain} (Nube Gris)...'; "
                f"{paas_step4}echo ''; "
                f"echo '============================================================='; "
                f"echo '🔗 PIVOTES OSINT HISTÓRICOS 100% GRATUITOS (SIN PAYWALL):'; "
                f"echo '  ViewDNS (IP History)           : https://viewdns.info/iphistory/?domain={root_domain}'; "
                f"echo '  URLScan.io (Histórico & Scans) : https://urlscan.io/search/#page.domain%3A{root_domain}'; "
                f"echo '  VirusTotal (Passive DNS)       : https://www.virustotal.com/gui/domain/{root_domain}/relations'; "
                f"echo '  crt.sh (Subdominios & SSL)     : https://crt.sh/?q=%25.{root_domain}'; "
                f"echo '  Shodan (SSL Search)            : https://www.shodan.io/search?query=ssl%3A%22{clean_target}%22'; "
                f"echo '  Wayback Machine (Historial Web): https://web.archive.org/web/*/{clean_target}'; "
                f"echo '============================================================='"
            )
        else:
            if is_paas:
                sub_notice_ps = (
                    f"Write-Host 'ℹ️ [PLATAFORMA PAAS / HOSTING COMPARTIDO]: {clean_target} está alojado en {root_domain}' -ForegroundColor DarkCyan; "
                    f"Write-Host '   El dominio raíz pertenece a un proveedor público y no representa servidores privados del atacante.' -ForegroundColor DarkGray; Write-Host ''; "
                )
            elif is_sub:
                sub_notice_ps = f"Write-Host 'ℹ️ [SUBDOMINIO DETECTADO]: Auditando subdominio y dominio raíz ({root_domain})' -ForegroundColor DarkCyan; Write-Host ''; "
            else:
                sub_notice_ps = ""

            paas_step4_ps = (
                f"Write-Host '  [i] Barrido pasivo de subdominios omitido: {root_domain} es una plataforma SaaS/PaaS pública.' -ForegroundColor DarkCyan; "
                f"Write-Host '      Barrer subdominios en {root_domain} descubriría la CDN del proveedor y causaría falsos positivos.' -ForegroundColor DarkGray; "
            ) if is_paas else (
                f"$sub_candidates = @('mail', 'webmail', 'cpanel', 'direct', 'origin', 'ftp', 'autodiscover', 'smtp', 'vpn', 'admin', 'dev', 'ns1', 'ns2'); "
                f"foreach ($sub in $sub_candidates) {{ $fqdn = \"$sub.{root_domain}\"; "
                f"$sub_rec = (Resolve-DnsName -Name $fqdn -Type A -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.IP4Address -or $_.IPAddress }} | Select-Object -First 1); "
                f"$sub_ip = if ($sub_rec) {{ if ($sub_rec.IP4Address) {{ $sub_rec.IP4Address }} else {{ $sub_rec.IPAddress }} }} else {{ $null }}; "
                f"if ($sub_ip) {{ "
                f"$ptr = (Resolve-DnsName -Name $sub_ip -Type PTR -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.NameHost }} | Select-Object -First 1 -ExpandProperty NameHost); "
                f"if ($sub_ip -match '{cdn_rgx_ps}' -or ($ptr -and $ptr -match '(cdn|cloudflare|fastly|akamai|cloudfront|github|edgekey)')) {{ "
                f"Write-Host ('  [-] ' + $fqdn + ' -> ' + $sub_ip + ' (CDN / Proxy Activo)') -ForegroundColor DarkGray }} else {{ "
                f"Write-Host ('  [🚨 ORIGEN ENCONTRADO]: ' + $fqdn + ' -> ' + $sub_ip) -ForegroundColor Red; "
                f"if ($ptr) {{ Write-Host ('     [+] PTR: ' + $ptr) -ForegroundColor Cyan }}; "
                f"try {{ $isp = (Invoke-RestMethod -Uri \"https://ipinfo.io/$sub_ip/json\" -TimeoutSec 3 -ErrorAction SilentlyContinue).org; "
                f"if ($isp) {{ Write-Host ('     [+] ISP/Hosting: ' + $isp) -ForegroundColor Magenta }} }} catch {{}} }} }} }}; "
            )

            cmd = (
                f"Write-Host '=============================================================' -ForegroundColor Cyan; "
                f"Write-Host '🕵️ [AUDITORIA DE ORIGEN & BYPASS DE CDN / CLOUDFLARE]' -ForegroundColor Cyan; "
                f"Write-Host 'Objetivo analizado: {clean_target}' -ForegroundColor Yellow; "
                f"Write-Host '=============================================================' -ForegroundColor Cyan; "
                f"Write-Host ''; "
                f"{sub_notice_ps}"
                f"Write-Host '[1/4] Comprobando IPs Web actuales...' -ForegroundColor Gray; "
                f"$web_ips = (Resolve-DnsName -Name '{clean_target}' -Type A -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.IP4Address -or $_.IPAddress }} | ForEach-Object {{ if ($_.IP4Address) {{ $_.IP4Address }} else {{ $_.IPAddress }} }}); "
                f"if (-not $web_ips) {{ Write-Host '  [!] No se resolvieron IPs A para este objetivo.' -ForegroundColor DarkGray }} else {{ "
                f"foreach ($wip in $web_ips) {{ Write-Host ('  -> IP Web: ' + $wip) -ForegroundColor White; "
                f"if ($wip -match '{cdn_rgx_ps}') {{ "
                f"Write-Host '     [!] Pertenece a Anycast CDN / Proxy Activo (Cloudflare/Fastly/GitHub Pages)' -ForegroundColor Yellow }} }} }}; "
                f"Write-Host ''; Write-Host '[2/4] Buscando Fugas en Registros de Correo (MX / Direct Connect)...' -ForegroundColor Gray; "
                f"$mx_records = (Resolve-DnsName -Name '{clean_target}' -Type MX -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.NameExchange }} | Select-Object -ExpandProperty NameExchange); "
                f"if (-not $mx_records -and '{clean_target}' -ne '{root_domain}' -and '{str(is_paas)}' -ne 'True') {{ "
                f"Write-Host '  [i] Sin MX en subdominio; comprobando dominio raíz ({root_domain})...' -ForegroundColor DarkCyan; "
                f"$mx_records = (Resolve-DnsName -Name '{root_domain}' -Type MX -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.NameExchange }} | Select-Object -ExpandProperty NameExchange) }}; "
                f"if ($mx_records) {{ foreach ($mx in $mx_records) {{ Write-Host ('  -> Registro MX: ' + $mx) -ForegroundColor White; "
                f"if ($mx -like '_dc-mx.*') {{ Write-Host '     [🚨 FUGA CRITICA]: Cloudflare Direct Connect MX detectado (_dc-mx)!' -ForegroundColor Red }}; "
                f"$mx_rec = (Resolve-DnsName -Name $mx -Type A -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.IP4Address -or $_.IPAddress }} | Select-Object -First 1); "
                f"$mx_ip = if ($mx_rec) {{ if ($mx_rec.IP4Address) {{ $mx_rec.IP4Address }} else {{ $mx_rec.IPAddress }} }} else {{ $null }}; "
                f"if ($mx_ip) {{ Write-Host ('     [🎯 IP DE ORIGEN / CORREO]: ' + $mx_ip) -ForegroundColor Green; "
                f"$ptr = (Resolve-DnsName -Name $mx_ip -Type PTR -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.NameHost }} | Select-Object -First 1 -ExpandProperty NameHost); "
                f"if ($ptr) {{ Write-Host ('     [+] Hostname PTR: ' + $ptr) -ForegroundColor Cyan }}; "
                f"try {{ $isp = (Invoke-RestMethod -Uri \"https://ipinfo.io/$mx_ip/json\" -TimeoutSec 3 -ErrorAction SilentlyContinue).org; "
                f"if ($isp) {{ Write-Host ('     [+] ISP/Hosting: ' + $isp) -ForegroundColor Magenta }} }} catch {{}} }} }} }} else {{ "
                f"Write-Host '  [!] No se detectaron servidores MX en el objetivo ni en el dominio raíz.' -ForegroundColor DarkGray }}; "
                f"Write-Host ''; Write-Host '[3/4] Analizando Registro SPF (ip4: autorizadas)...' -ForegroundColor Gray; "
                f"$spf = (Resolve-DnsName -Name '{clean_target}' -Type TXT -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.Strings -like '*v=spf1*' }} | Select-Object -ExpandProperty Strings); "
                f"if (-not $spf -and '{clean_target}' -ne '{root_domain}' -and '{str(is_paas)}' -ne 'True') {{ "
                f"Write-Host '  [i] Sin SPF en subdominio; comprobando dominio raíz ({root_domain})...' -ForegroundColor DarkCyan; "
                f"$spf = (Resolve-DnsName -Name '{root_domain}' -Type TXT -Server 8.8.8.8 -ErrorAction SilentlyContinue | Where-Object {{ $_.Strings -like '*v=spf1*' }} | Select-Object -ExpandProperty Strings) }}; "
                f"$spf_ips = if ($spf) {{ [regex]::Matches($spf, 'ip4:([^\\s]+)') | ForEach-Object {{ $_.Groups[1].Value }} }} else {{ $null }}; "
                f"if ($spf_ips) {{ foreach ($sip in $spf_ips) {{ Write-Host ('  [🚨 RANGO IP DECLARADO EN SPF]: ' + $sip) -ForegroundColor Yellow; "
                f"$sip_clean = $sip.Split('/')[0]; "
                f"try {{ $isp = (Invoke-RestMethod -Uri \"https://ipinfo.io/$sip_clean/json\" -TimeoutSec 3 -ErrorAction SilentlyContinue).org; "
                f"if ($isp) {{ Write-Host ('     [+] ISP/Hosting: ' + $isp) -ForegroundColor Magenta }} }} catch {{}} }} }} else {{ "
                f"Write-Host '  [!] No se encontraron directivas ip4: en SPF.' -ForegroundColor DarkGray }}; "
                f"Write-Host ''; Write-Host '[4/4] Barrido Pasivo de Subdominios Comunes en {root_domain} (Nube Gris)...' -ForegroundColor Gray; "
                f"{paas_step4_ps}"
                f"Write-Host ''; Write-Host '=============================================================' -ForegroundColor Cyan; "
                f"Write-Host '🔗 PIVOTES OSINT HISTORICOS 100% GRATUITOS (SIN PAYWALL):' -ForegroundColor Cyan; "
                f"Write-Host '  ViewDNS (IP History)           : https://viewdns.info/iphistory/?domain={root_domain}' -ForegroundColor Yellow; "
                f"Write-Host '  URLScan.io (Historico & Scans) : https://urlscan.io/search/#page.domain%3A{root_domain}' -ForegroundColor Yellow; "
                f"Write-Host '  VirusTotal (Passive DNS)       : https://www.virustotal.com/gui/domain/{root_domain}/relations' -ForegroundColor Yellow; "
                f"Write-Host '  crt.sh (Subdominios & SSL)     : https://crt.sh/?q=%25.{root_domain}' -ForegroundColor Yellow; "
                f"Write-Host '  Shodan (SSL Search)            : https://www.shodan.io/search?query=ssl%3A%22{clean_target}%22' -ForegroundColor Yellow; "
                f"Write-Host '  Wayback Machine (Historial Web): https://web.archive.org/web/*/{clean_target}' -ForegroundColor Yellow; "
                f"Write-Host '=============================================================' -ForegroundColor Cyan;"
            )
        self.execute_terminal_command(cmd)

    def run_preset_dnstwist(self):
        """Ejecuta el cazador nativo multihilo de DNS Twist / Typosquatting / Phishing Lookalikes."""
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "DNS Twist", "Ingrese un nombre de dominio o URL en el campo objetivo (ej. betonline.ag).")
            return
        if hasattr(self, "tabs") and hasattr(self, "tab5"):
            self.tabs.setCurrentWidget(self.tab5)
        clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        obs_type = CtiEngine.detect_observable_type(clean_target)

        if obs_type == "ip":
            QMessageBox.information(
                self,
                "DNS Twist",
                f"El objetivo '{clean_target}' es una dirección IP.\n\n"
                f"DNS Twist requiere un nombre de dominio o marca (ej. betonline.ag) para generar variaciones tipográficas y lookalikes.\n\n"
                f"Para esta IP se ejecutará la resolución inversa (PTR)..."
            )
            self.run_preset_ptr()
            return

        engine = self.combo_term_engine.currentData()
        script_path = os.path.join(os.path.abspath("."), "dnstwist_recon.py")
        venv_py = os.path.join(os.path.abspath("."), "venv", "Scripts", "python.exe")

        if engine == "wsl":
            cmd = f"python3 -u dnstwist_recon.py {clean_target} || python -u dnstwist_recon.py {clean_target}"
        else:
            if os.path.exists(venv_py):
                cmd = f"& '{venv_py}' -u '{script_path}' {clean_target}"
            else:
                cmd = f"python -u '{script_path}' {clean_target}"

        self.execute_terminal_command(cmd)

    def open_email_header_analyzer(self):
        """Abre la ventana interactiva del Analizador Forense de Cabeceras (.eml) vía SOCWindowManager."""
        try:
            self._email_analyzer_dlg = self.window_manager.open_module(
                module_key="email_header_analyzer",
                title="📬 DFIR Phishing Header Inspector (.eml / SPF / DKIM / DMARC) — Technoma SOC",
                short_title="✉️ Phishing Headers",
                accent_color=ui_theme.ACCENT_CYBER,
                factory_fn=lambda: PhishingHeaderAnalyzerDialog(None),
                default_size=(1220, 800)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el analizador de cabeceras: {e}")

    def open_thn_ticket_generator(self):
        """Abre la ventana interactiva del Generador de Tickets de Escalación Technoma SOC vía SOCWindowManager."""
        try:
            self._thn_ticket_dlg = self.window_manager.open_module(
                module_key="thn_ticket_generator",
                title="🎫 Generador Oficial de Tickets Technoma SOC (FL-THN-POS-01 & Bitácora)",
                short_title="🎫 Ticket THN",
                accent_color=ui_theme.COLOR_HIGH,
                factory_fn=lambda: TechnomaTicketGeneratorDialog(None),
                default_size=(1200, 820)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el generador de tickets Technoma: {e}")

    def open_abuse_report_dialog(self):
        """Abre la ventana interactiva del Generador de Reportes de Abuso vía SOCWindowManager."""
        try:
            self._abuse_report_dlg = self.window_manager.open_module(
                module_key="abuse_report_dialog",
                title="🚨 Generador y Despachador de Reportes de Abuso & Escaneo — Technoma SOC",
                short_title="🚨 Reporte Abuso",
                accent_color=ui_theme.COLOR_CRITICAL,
                factory_fn=lambda: AbuseReportDialog(None),
                default_size=(1260, 820)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el generador de reportes de abuso: {e}")

    def _auto_sync_feeds_background(self):
        """Ejecuta en segundo plano la sincronización diaria de Feeds CTI e IOCs de TweetFeed sin bloquear la UI."""
        import threading
        try:
            from feeds_engine import sync_all_feeds_headless
            def _worker():
                try:
                    res = sync_all_feeds_headless()
                    new_iocs = res.get("new_items_inserted", 0)
                    if new_iocs > 0:
                        print(f"[SOAR CTI Feeds] Ingesta automática completada: {new_iocs} nuevos IOCs/alertas indexados.")
                except Exception as e:
                    print(f"[SOAR CTI Feeds] Advertencia en sincronización de fondo: {e}")
            t = threading.Thread(target=_worker, daemon=True, name="SOAR_Feeds_Sync_Worker")
            t.start()
        except Exception as e:
            print(f"[SOAR CTI Feeds] Error iniciando sincronizador: {e}")

    def open_feeds_intel_module(self):
        """Abre la ventana interactiva del Módulo de Feeds CTI y Reportes de Vulnerabilidad con IA vía SOCWindowManager."""
        try:
            self._feeds_intel_dlg = self.window_manager.open_module(
                module_key="feeds_intel_module",
                title="🌐 Módulo de Inteligencia de Amenazas, Feeds CTI & Alertas de Vulnerabilidad",
                short_title="🌐 CTI Feeds",
                accent_color=ui_theme.COLOR_PURPLE,
                factory_fn=lambda: FeedsIntelDialog(None),
                default_size=(1360, 860)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el módulo de feeds CTI: {e}")

    def open_stellar_hunter_window(self):
        """Abre el Centro de Gobernabilidad de Queries, Cobertura de Dominios y Threat Hunting en ventana o pestaña."""
        try:
            from soar_app.ui.tabs.stellar_hunter_tab import StellarHunterAndGovernanceWidget
            self.window_manager.open_module(
                module_key="stellar_hunter_governance",
                title="🔍 Stellar Hunter, Cobertura de Dominios & Gobernabilidad de Queries/Filtros",
                short_title="🔍 Queries & Hunter",
                accent_color=ui_theme.ACCENT_CYBER,
                factory_fn=lambda: StellarHunterAndGovernanceWidget(None),
                default_size=(1340, 840)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir Stellar Hunter & Queries: {e}")

    def open_soc_agent_window(self):
        """Abre la interfaz gráfica del Agente Autónomo SOC (soc_agent_gui.py) integrada en SOCWindowManager."""
        try:
            from soc_agent_gui import MainWindow as SocAgentMainWindow
            self.window_manager.open_module(
                module_key="soc_autonomous_agent",
                title="🤖 SOC Autonomous AI Agent & Playbook Orchestrator — Technoma SOC",
                short_title="🤖 Agente SOC IA",
                accent_color=ui_theme.COLOR_SUCCESS,
                factory_fn=lambda: SocAgentMainWindow(),
                default_size=(1280, 820)
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el Agente SOC IA: {e}")

    def run_preset_abuseipdb(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset AbuseIPDB", "Ingrese una dirección IP en el campo objetivo o seleccione un caso.")
            return
        obs_type = CtiEngine.detect_observable_type(target)
        if obs_type != "ip":
            QMessageBox.warning(self, "AbuseIPDB", f"AbuseIPDB requiere una dirección IP IPv4 válida. '{target}' fue clasificado como '{obs_type}'.")
            return
        self.run_cti_async("abuseipdb", target)

    def run_preset_virustotal(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset VirusTotal", "Ingrese un observable (IP, Dominio, Hash o URL) en el campo objetivo.")
            return
        self.run_cti_async("virustotal", target)

    def run_preset_urlscan(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset URLScan", "Ingrese una URL, dominio o IP en el campo objetivo.")
            return
        self.run_cti_async("urlscan", target)

    def run_preset_auto_investigate_360(self):
        """Orquestador inteligente que clasifica el objetivo (IP privada/pública, PaaS, Dominio) y dispara la suite forense exacta."""
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Auto-Investigar 360°", "Ingrese un observable (IP, Dominio, URL o Hash) en el campo objetivo.")
            return

        import re
        import ipaddress

        clean = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
        
        # 1. Determinar si es una dirección IP
        try:
            ip_obj = ipaddress.ip_address(clean)
            is_ip = True
            is_private = ip_obj.is_private
        except ValueError:
            is_ip = False
            is_private = False

        if is_ip:
            if is_private:
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.txt_terminal_output.insertHtml(
                    f"<br><span style='color: #38bdf8; font-weight: bold;'>[🚀 SUITE THREAT HUNTING: IP PRIVADA / LAN]</span> "
                    f"Objetivo: <b>{clean}</b> (RFC 1918)<br>"
                    f"<span style='color: #94a3b8;'>Disparando: PTR Local + Port Sweep Rápido + Grep de Casos Internos...</span><br>"
                )
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                # Ejecutar PTR y conectividad local
                self.run_preset_ptr()
            else:
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.txt_terminal_output.insertHtml(
                    f"<br><span style='color: #ec4899; font-weight: bold;'>[🚀 SUITE THREAT HUNTING: IP PÚBLICA DE INTERNET]</span> "
                    f"Objetivo: <b>{clean}</b><br>"
                    f"<span style='color: #94a3b8;'>Disparando: Tri-Scan CTI (AbuseIPDB + VirusTotal) + PTR Inverso + Conectividad...</span><br>"
                )
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.run_cti_async("triscan", clean)
        else:
            # 2. Es un Dominio o Subdominio
            paas_suffixes = (
                "netlify.app", "vercel.app", "github.io", "pages.dev", "firebaseapp.com",
                "azureedge.net", "s3.amazonaws.com", "herokuapp.com", "render.com", "fly.dev"
            )
            is_paas = any(clean.lower().endswith(p) for p in paas_suffixes)

            if is_paas:
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.txt_terminal_output.insertHtml(
                    f"<br><span style='color: #f59e0b; font-weight: bold;'>[🚀 SUITE THREAT HUNTING: SUBDOMINIO PAAS / HOSTING PÚBLICO]</span> "
                    f"Objetivo: <b>{clean}</b><br>"
                    f"<span style='color: #94a3b8;'>Disparando: Reconocimiento DNS + URLScan.io + VirusTotal (Omitiendo SPF/DMARC de PaaS)...</span><br>"
                )
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.run_cti_async("triscan", clean)
            else:
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.txt_terminal_output.insertHtml(
                    f"<br><span style='color: #a855f7; font-weight: bold;'>[🚀 SUITE THREAT HUNTING: DOMINIO CORPORATIVO / PRIVADO]</span> "
                    f"Objetivo: <b>{clean}</b><br>"
                    f"<span style='color: #94a3b8;'>Disparando: Desemmascarar Origen (Bypass Cloudflare) + Anti-Spoofing (SPF/DMARC) + Tri-Scan CTI...</span><br>"
                )
                self.txt_terminal_output.moveCursor(QTextCursor.End)
                self.run_preset_unmask_origin()

    def run_preset_triscan(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset Tri-Scan CTI", "Ingrese un observable (IP, Dominio o URL) en el campo objetivo.")
            return
        self.run_cti_async("triscan", target)

    def run_preset_mxtoolbox(self):
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset MxToolbox", "Ingrese un dominio o URL sospechosa de phishing en el campo objetivo.")
            return
        self.run_cti_async("phishing", target)

    def run_preset_cve(self):
        target = self._get_active_target_or_observable()
        is_cve_pattern = bool(target and re.match(r"^(CVE[-_])?\d{4}-\d{4,}$", target.strip(), re.IGNORECASE))

        if not target or not is_cve_pattern:
            from PySide6.QtWidgets import QInputDialog
            default_val = target if is_cve_pattern else ""
            cve_input, ok = QInputDialog.getText(
                self,
                "Consulta de Vulnerabilidad (NVD NIST)",
                f"El objetivo actual ('{target or 'Vacío'}') no es un identificador CVE válido.\n\n"
                "NVD NIST consulta la base de vulnerabilidades por código CVE.\n"
                "Ingrese el código CVE a consultar (ej: CVE-2024-3400):",
                text=default_val
            )
            if not ok or not cve_input.strip():
                return
            target = cve_input.strip()

        self.run_cti_async("cve", target)

    def run_preset_security_onion(self):
        """Pivotea automáticamente a Tab 7 y dispara la caza forense del objetivo en Security Onion."""
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Preset Security Onion", "Ingrese una IP, dominio o hash en el campo objetivo.")
            return
        self.pivot_to_security_onion(target)

    def pivot_to_external_service(self, service: str):
        """Abre herramientas externas de Sandboxing y Threat Intelligence en el navegador predeterminado."""
        import urllib.parse
        target = self._get_active_target_or_observable()
        if not target:
            QMessageBox.warning(self, "Pivote Externo", "Ingrese un objetivo (IP, Dominio, URL o Hash) en el campo superior.")
            return

        clean_target = target.strip()
        encoded = urllib.parse.quote(clean_target)
        clean_domain = re.sub(r"^https?://", "", clean_target).split("/")[0].split(":")[0]
        obs_type = CtiEngine.detect_observable_type(clean_target)

        urls = {
            "talos": f"https://talosintelligence.com/reputation_center/lookup?search={encoded}",
            "anyrun": "https://app.any.run/",
            "browserling": f"https://www.browserling.com/browse/win/7/chrome/90/{encoded}" if clean_target.startswith("http") else "https://www.browserling.com/",
            "hybrid_analysis": f"https://www.hybrid-analysis.com/search?query={encoded}",
            "malwarebazaar": f"https://bazaar.abuse.ch/browse.php?search={encoded}",
            "threatfox": f"https://threatfox.abuse.ch/browse.php?search={encoded}",
            "urlhaus": f"https://urlhaus.abuse.ch/browse.php?search={encoded}",
            "crtsh": f"https://crt.sh/?q=%25.{urllib.parse.quote(clean_domain)}",
            "shodan": f"https://www.shodan.io/host/{clean_target}" if obs_type == "ip" else f"https://www.shodan.io/search?query=hostname%3A{encoded}",
            "ipinfo": f"https://ipinfo.io/{clean_target}",
            "mxtoolbox_web": f"https://mxtoolbox.com/SuperTool.aspx?action=mx%3a{encoded}&run=toolpage",
            "cyberchef": f"https://gchq.github.io/CyberChef/#recipe=URL_Decode()&input={encoded}",
            "securitytrails": f"https://securitytrails.com/domain/{clean_domain}/history/dns",
            "viewdns": f"https://viewdns.info/iphistory/?domain={clean_domain}",
            "censys": f"https://search.censys.io/certificates?q={clean_domain}"
        }

        target_url = urls.get(service)
        if target_url:
            QDesktopServices.openUrl(QUrl(target_url))
            service_names = {
                "talos": "🦊 Cisco Talos Intelligence",
                "anyrun": "⚡ Any.Run Interactive Sandbox",
                "browserling": "🌐 Browserling (Navegador Aislado)",
                "hybrid_analysis": "🦅 Hybrid Analysis (Falcon Sandbox)",
                "malwarebazaar": "🦠 MalwareBazaar (abuse.ch Hashes)",
                "threatfox": "🦊 ThreatFox IOC Search (abuse.ch)",
                "urlhaus": "☣️ URLhaus Malware URLs (abuse.ch)",
                "crtsh": "📜 crt.sh (Certificados SSL & Subdominios)",
                "shodan": "🔎 Shodan Host Intelligence",
                "ipinfo": "🔍 IPinfo.io Geolocation",
                "mxtoolbox_web": "📬 MxToolbox SuperTool Web",
                "cyberchef": "🍳 CyberChef (Navaja Suiza Forense)",
                "securitytrails": "🛡️ SecurityTrails (Histórico DNS)",
                "viewdns": "📜 ViewDNS (Histórico de IPs)",
                "censys": "🌐 Censys Search (Certificados SSL & Hosts)"
            }
            s_name = service_names.get(service, service.upper())
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(
                f"<br><span style='color: #a5b4fc; font-weight: bold;'>[🚀 PIVOTE EXTERNO LANZADO]:</span> "
                f"<span style='color: #38bdf8;'>{he(s_name)}</span> para objetivo: <b>{he(clean_target)}</b><br>"
            )
            self.txt_terminal_output.moveCursor(QTextCursor.End)

    def execute_fortigate_block(self, target_type: str = "domain"):
        """
        Ejecuta la orden de contención activa en FortiGate vía Stellar Cyber 7.0.0s (AELDEV-67465).
        Permite bloquear dominios de C2 o URLs de phishing en el firewall perimetral.
        """
        target = self._get_active_target_or_observable()
        if target:
            if target_type == "domain":
                clean_target = re.sub(r"^https?://", "", target.strip(), flags=re.IGNORECASE).rstrip("/").split("/")[0].split(":")[0]
            else:
                clean_target = target.strip()
        else:
            clean_target = ""

        label_type = "Dominio Malicioso" if target_type == "domain" else "URL de Phishing"
        val, ok = QInputDialog.getText(
            self,
            f"FortiGate Responder (Stellar 7.0.0s) - Bloqueo de {label_type}",
            f"Confirme o ingrese el {label_type} a bloquear en FG-Technoma:",
            QLineEdit.Normal,
            clean_target
        )
        if not ok or not val.strip():
            return

        target_to_block = val.strip()
        confirm = QMessageBox.question(
            self,
            "Confirmar Bloqueo Perimetral FortiGate",
            f"¿Confirma el envío de la orden de contención inmediata al Firewall FortiGate?\n\n"
            f"• Tipo de Objeto: {label_type}\n"
            f"• Valor: {target_to_block}\n"
            f"• Dispositivo: FG-Technoma\n"
            f"• Conector: Stellar Cyber OpenXDR 7.0.0s\n\n"
            f"Esta acción aplicará la directiva de denegación en el firewall.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        if hasattr(self, "tabs") and hasattr(self, "tab5"):
            self.tabs.setCurrentWidget(self.tab5)

        script_path = os.path.join(os.path.abspath("."), "stellar_cli.py")
        venv_py = os.path.join(os.path.abspath("."), "venv", "Scripts", "python.exe")
        if not os.path.exists(venv_py):
            venv_py = os.path.join(os.path.abspath("."), "Scripts", "python.exe")
        if not os.path.exists(venv_py):
            venv_py = sys.executable if sys.executable else "python"

        flag = "--block-domain" if target_type == "domain" else "--block-url"
        cmd = f"& '{venv_py}' -u '{script_path}' {flag} '{target_to_block}'"
        
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertHtml(
            f"<br><span style='color: #ef4444; font-weight: bold;'>[🛡️ RESPONDER FORTIGATE 7.0.0s]:</span> "
            f"Despachando bloqueo de {he(label_type)} <b>{he(target_to_block)}</b> en FG-Technoma...<br>"
        )
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.execute_terminal_command(cmd)

    def _execute_forensic_decode(self, payload: str, mode: str = "auto"):
        """Decodifica strings ofuscadas (Base64 UTF-8/UTF-16LE, URL encode, Hex, Defang/Refang) en memoria sin disparar alertas EDR."""
        if not payload or not payload.strip():
            target = self._get_active_target_or_observable()
            if target:
                payload = target
            else:
                QMessageBox.warning(self, "Decodificador Forense", "Ingrese una cadena ofuscada o seleccione un observable en el campo objetivo.")
                return

        clean_payload = payload.strip()
        import base64
        import urllib.parse
        import html

        results = []

        # 1. URL Decode
        try:
            url_decoded = urllib.parse.unquote(clean_payload)
            if url_decoded != clean_payload:
                results.append(("URL Decode", url_decoded))
        except Exception:
            pass

        # 2. Base64 Decode (UTF-8 y PowerShell UTF-16LE)
        try:
            b64_str = clean_payload.replace(" ", "+")
            rem = len(b64_str) % 4
            if rem > 0:
                b64_str += "=" * (4 - rem)
            raw_bytes = base64.b64decode(b64_str, validate=False)

            # UTF-8
            try:
                utf8_str = raw_bytes.decode("utf-8")
                if any(c.isprintable() for c in utf8_str) and len(utf8_str) >= 2:
                    results.append(("Base64 (UTF-8 Estándar)", utf8_str))
            except Exception:
                pass

            # UTF-16LE (PowerShell -EncodedCommand)
            try:
                utf16_str = raw_bytes.decode("utf-16le")
                if any(c.isprintable() for c in utf16_str) and len(utf16_str) >= 2 and utf16_str != utf8_str:
                    results.append(("Base64 (PowerShell UTF-16LE)", utf16_str))
            except Exception:
                pass
        except Exception:
            pass

        # 3. Hex Decode
        try:
            hex_cand = clean_payload.replace("0x", "").replace("\\x", "").replace(" ", "").replace(":", "")
            if len(hex_cand) >= 4 and len(hex_cand) % 2 == 0 and all(c in "0123456789abcdefABCDEF" for c in hex_cand):
                hex_bytes = bytes.fromhex(hex_cand)
                try:
                    hex_str = hex_bytes.decode("utf-8")
                    if any(c.isprintable() for c in hex_str):
                        results.append(("Hexadecimal (ASCII / UTF-8)", hex_str))
                except Exception:
                    pass
        except Exception:
            pass

        # 4. Defang / Refang
        refanged = clean_payload.replace("[.]", ".").replace("(.)", ".").replace("hxxp://", "http://").replace("hxxps://", "https://").replace("[at]", "@")
        if refanged != clean_payload:
            results.append(("Refanged (Formato Real En Vivo)", refanged))
        else:
            defanged = clean_payload.replace(".", "[.]").replace("http://", "hxxp://").replace("https://", "hxxps://").replace("@", "[at]")
            results.append(("Defanged (Formato Seguro)", defanged))

        # Renderizar salida en consola
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        out = ["<br><div style='background-color: #0f172a; border: 1px solid #3b82f6; border-radius: 6px; padding: 10px; margin: 6px 0;'>"]
        out.append(f"<span style='color: #60a5fa; font-weight: bold; font-size: 13px;'>🔓 DECODIFICADOR FORENSE SOC (En Memoria - 0 Alertas EDR)</span><br>")
        out.append(f"<span style='color: #94a3b8; font-size: 11px;'>Entrada: <code>{html.escape(clean_payload[:140])}{'...' if len(clean_payload) > 140 else ''}</code></span><hr style='border: 0; border-top: 1px solid #1e293b; margin: 6px 0;'>")

        if not results:
            out.append("<span style='color: #f59e0b;'>[!] No se detectó codificación válida estándar (Base64, URL, Hex ni Defang).</span>")
        else:
            for label, val in results:
                esc_val = html.escape(val)
                out.append(f"<div style='margin-bottom: 8px;'>")
                out.append(f"<span style='color: #38bdf8; font-weight: bold; font-size: 11px;'>▶ {html.escape(label)}:</span><br>")
                out.append(f"<pre style='background-color: #020617; color: #a7f3d0; padding: 6px; border-radius: 4px; border: 1px solid #1e293b; font-family: monospace; white-space: pre-wrap; word-break: break-all; margin: 2px 0;'>{esc_val}</pre>")
                out.append(f"</div>")

        out.append("</div><br>")
        self.txt_terminal_output.insertHtml("".join(out))
        self.txt_terminal_output.moveCursor(QTextCursor.End)

    def run_cti_async(self, mode: str, observable: str):
        """Ejecuta una consulta CTI asincrónica mediante CtiQueryWorker sin bloquear la interfaz."""
        if hasattr(self, '_worker_cti') and self._worker_cti and self._worker_cti.isRunning():
            QMessageBox.warning(self, "CTI en Curso", "Ya existe una consulta CTI en ejecución. Aguarde unos segundos.")
            return

        obs_type = CtiEngine.detect_observable_type(observable)
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertHtml(
            f"<br><span style='color: #c084fc; font-weight: bold;'>[⚡ CONSULTA CTI ASINCRÓNICA DISPARADA]</span> "
            f"<span style='color: #38bdf8;'>[{mode.upper()}]</span> "
            f"Observable: <b>{he(observable)}</b> (Tipo detectado: <span style='color: #f59e0b;'>{obs_type}</span>)...<br>"
        )
        self.txt_terminal_output.moveCursor(QTextCursor.End)

        self._worker_cti = CtiQueryWorker(mode, observable)
        self._worker_cti.query_finished.connect(self._on_cti_finished)
        self._worker_cti.query_failed.connect(self._on_cti_failed)
        self._worker_cti.start()

    def _on_cti_finished(self, result: Dict[str, Any]):
        mode = result.get("mode", "triscan")
        self.txt_terminal_output.moveCursor(QTextCursor.End)

        if mode == "triscan":
            html_rep = CtiEngine.format_terminal_report_html(result)
            self.txt_terminal_output.insertHtml(html_rep + "<br>")
        elif mode == "virustotal":
            vt = result.get("virustotal", {})
            obs = result.get("observable", "")
            if vt.get("status") == "success":
                col = vt.get("color", "#38bdf8")
                html = (
                    f"<div style='background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; padding: 8px; margin: 4px 0; font-family: Consolas; font-size: 11px;'>"
                    f"<span style='color: #fb923c; font-weight: bold;'>🦠 VIRUSTOTAL v3 RESULT: {he(obs)}</span><br>"
                    f"Veredicto: <b style='color: {col};'>{vt.get('verdict')}</b> | Ratio de Detección: <b>{vt.get('detection_ratio')}</b> motores maliciosos | Reputación: {vt.get('reputation')}<br>"
                    f"AS / Red: <b>{he(str(vt.get('as_owner')))}</b> ({vt.get('country')}) | Tags: {', '.join(vt.get('tags', [])) or 'N/A'}"
                    f"</div><br>"
                )
            elif vt.get("status") == "not_found":
                html = f"<span style='color: #94a3b8;'><br>[🦠 VirusTotal]: El observable <b>{he(obs)}</b> no tiene registros previos en la base de VT.<br></span>"
            else:
                html = f"<span style='color: #ef4444;'><br>[🦠 VirusTotal Error]: {he(vt.get('error', 'Error desconocido'))}<br></span>"
            self.txt_terminal_output.insertHtml(html)

        elif mode == "abuseipdb":
            abuse = result.get("abuseipdb", {})
            obs = result.get("observable", "")
            if abuse.get("status") == "success":
                col = abuse.get("color", "#38bdf8")
                html = (
                    f"<div style='background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; padding: 8px; margin: 4px 0; font-family: Consolas; font-size: 11px;'>"
                    f"<span style='color: #34d399; font-weight: bold;'>🛡️ ABUSEIPDB v2 RESULT: {he(obs)}</span><br>"
                    f"Veredicto: <b style='color: {col};'>{abuse.get('verdict')}</b> | Confianza de Abuso: <b style='color: {col};'>{abuse.get('score')}%</b> | Reportes acumulados: <b>{abuse.get('total_reports')}</b><br>"
                    f"ISP: <b>{he(str(abuse.get('isp')))}</b> ({abuse.get('country')}) | Dominio: {he(str(abuse.get('domain')))} | Whitelist: {abuse.get('is_whitelisted')}<br>"
                    f"Último Reporte: {abuse.get('last_reported')}"
                    f"</div><br>"
                )
            else:
                html = f"<span style='color: #ef4444;'><br>[🛡️ AbuseIPDB Error]: {he(abuse.get('error', 'Error desconocido'))}<br></span>"
            self.txt_terminal_output.insertHtml(html)

        elif mode == "urlscan":
            us = result.get("urlscan", {})
            html = CtiEngine.format_urlscan_detailed_html(us)
            self.txt_terminal_output.insertHtml(html + "<br>")

        elif mode == "mxtoolbox_phishing":
            mx = result.get("mxtoolbox", {})
            html = CtiEngine.format_mxtoolbox_detailed_html(mx)
            self.txt_terminal_output.insertHtml(html + "<br>")

        elif mode == "mxtoolbox_cmd":
            mx = result.get("mxtoolbox", {})
            html = CtiEngine.format_mxtoolbox_detailed_html(mx)
            self.txt_terminal_output.insertHtml(html + "<br>")

        elif mode == "cve":
            cve_res = result.get("cve", {})
            html = CtiEngine.format_cve_detailed_html(cve_res)
            self.txt_terminal_output.insertHtml(html + "<br>")

        self.txt_terminal_output.moveCursor(QTextCursor.End)

    def _on_cti_failed(self, error_msg: str):
        self.txt_terminal_output.moveCursor(QTextCursor.End)
        self.txt_terminal_output.insertHtml(f"<span style='color: #ef4444;'><br>[❌ FALLO EN CONSULTA CTI]: {he(error_msg)}<br></span>")
        self.txt_terminal_output.moveCursor(QTextCursor.End)

    def trigger_quick_terminal_investigation(self):
        case_id, t_id = self._get_target_case_id()
        self.tabs.setCurrentIndex(4) # Cambiar a Tab 5
        if t_id and t_id in getattr(self, 'dict_casos_activos', {}):
            c = self.dict_casos_activos[t_id]
            target = ""
            for fld in ["srcip", "dstip", "domain", "hostname", "ip"]:
                if c.get(fld):
                    target = str(c[fld]).strip()
                    break
            if not target:
                target = str(c.get("name", "")).strip()
            self.input_term_target.setText(target)
            self.txt_terminal_output.moveCursor(QTextCursor.End)
            self.txt_terminal_output.insertHtml(f"<span style='color: #38bdf8;'><br>[🎯 PIVOTE DESDE TRIAJE]: Investigando caso #{t_id} — Objetivo detectado: <b>{he(target)}</b><br></span>")
            self.txt_terminal_output.moveCursor(QTextCursor.End)

