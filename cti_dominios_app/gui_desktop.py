# -*- coding: utf-8 -*-
"""
Aplicación de Escritorio Nativa (GUI) para Threat Intelligence de Dominios.
- Cero puertos de red abiertos (Zero Listening Sockets).
- Sin servidores web locales.
- Cumple con políticas estrictas de ciberseguridad y EDR corporativo.
"""
import os
import re
import sys
import json
import time
import threading
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Agregar directorio actual a sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from core_engine import (
    ejecutar_pipeline,
    SHODAN_KEY,
    ABUSEIPDB_KEY,
    ABUSECH_KEY,
    MXTOOLBOX_KEY
)
from html_report import generar_html_estatico

class SOCAppDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("SOC Threat Intelligence · Command Center (Offline / 0 Puertos)")
        self.root.geometry("980x720")
        self.root.minsize(800, 600)

        # Paleta SOC Dark
        self.bg_dark = "#0b0f19"
        self.card_bg = "#111827"
        self.text_light = "#f3f4f6"
        self.accent_blue = "#3b82f6"
        self.accent_hover = "#2563eb"
        self.border_col = "#1f2937"
        self.term_bg = "#05070d"

        self.root.configure(bg=self.bg_dark)
        self.ultimo_reporte = None
        self.ultimo_html_path = None

        self.setup_styles()
        self.crear_interfaz()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Configuración Treeview (Tabla)
        style.configure("Treeview",
            background="#0f172a",
            foreground="#f8fafc",
            fieldbackground="#0f172a",
            rowheight=28,
            font=("Segoe UI", 9)
        )
        style.configure("Treeview.Heading",
            background="#1e293b",
            foreground="#93c5fd",
            font=("Segoe UI", 9, "bold"),
            relief="flat"
        )
        style.map("Treeview",
            background=[("selected", "#1e3a8a")],
            foreground=[("selected", "#ffffff")]
        )

    def crear_interfaz(self):
        # 1. Header Banner
        header = tk.Frame(self.root, bg=self.card_bg, padx=16, pady=12, highlightthickness=1, highlightbackground=self.border_col)
        header.pack(fill="x", padx=12, pady=(12, 6))

        lbl_titulo = tk.Label(header, text="🛡️ Threat Intelligence · Domain Risk Assessment",
                              font=("Segoe UI", 14, "bold"), fg="#60a5fa", bg=self.card_bg)
        lbl_titulo.pack(anchor="w")

        lbl_sub = tk.Label(header, text="Modo Standalone Seguro · 0 Puertos en Escucha · Cumple políticas de SOC / EDR",
                           font=("Segoe UI", 9), fg="#9ca3af", bg=self.card_bg)
        lbl_sub.pack(anchor="w")

        # Estado de APIs
        api_bar = tk.Frame(header, bg=self.card_bg, pady=6)
        api_bar.pack(anchor="w", fill="x")

        def add_chip(parent, nombre, activo):
            col = "#10b981" if activo else "#ef4444"
            txt = "Activa" if activo else "Sin clave"
            f = tk.Frame(parent, bg="#0b0f19", padx=6, pady=2, highlightthickness=1, highlightbackground="#1f2937")
            f.pack(side="left", padx=4)
            c = tk.Canvas(f, width=8, height=8, bg="#0b0f19", highlightthickness=0)
            c.pack(side="left", padx=(0, 4))
            c.create_oval(1, 1, 7, 7, fill=col, outline=col)
            tk.Label(f, text=f"{nombre}: {txt}", font=("Segoe UI", 8), fg="#cbd5e1", bg="#0b0f19").pack(side="left")

        add_chip(api_bar, "Shodan (API/InternetDB)", True)
        add_chip(api_bar, "AbuseIPDB", bool(ABUSEIPDB_KEY))
        add_chip(api_bar, "IP-API / DoH / RDAP (Sin Cuotas)", True)
        add_chip(api_bar, "Abuse.ch", bool(ABUSECH_KEY))
        add_chip(api_bar, "MXToolbox", bool(MXTOOLBOX_KEY))

        # 2. Entrada de texto y Controles
        input_card = tk.Frame(self.root, bg=self.card_bg, padx=14, pady=10, highlightthickness=1, highlightbackground=self.border_col)
        input_card.pack(fill="x", padx=12, pady=6)

        lbl_input = tk.Label(input_card, text="Entidades o dominios a auditar de una pasada (uno por línea o separados por coma):",
                             font=("Segoe UI", 9, "bold"), fg="#e2e8f0", bg=self.card_bg)
        lbl_input.pack(anchor="w", pady=(0, 4))

        self.txt_input = tk.Text(input_card, height=4, bg="#070a13", fg="#f8fafc",
                                 font=("Consolas", 10), insertbackground="#fff",
                                 highlightthickness=1, highlightbackground="#374151")
        self.txt_input.pack(fill="x", pady=(0, 8))
        self.txt_input.insert("1.0", "Banco Central del Paraguay\nTechnoma")

        # Barra de botones
        btn_bar = tk.Frame(input_card, bg=self.card_bg)
        btn_bar.pack(fill="x")

        self.btn_ejecutar = tk.Button(btn_bar, text="⚡ Iniciar Análisis por Lote",
                                      bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8", activeforeground="#ffffff",
                                      font=("Segoe UI", 10, "bold"), relief="flat", padx=14, pady=6, cursor="hand2",
                                      command=self.iniciar_analisis_thread)
        self.btn_ejecutar.pack(side="left", padx=(0, 8))

        self.btn_cargar_txt = tk.Button(btn_bar, text="📂 Cargar Lista (.txt/.csv)",
                                        bg="#1e293b", fg="#cbd5e1", activebackground="#334155",
                                        font=("Segoe UI", 9), relief="flat", padx=10, pady=6, cursor="hand2",
                                        command=self.cargar_lista_archivo)
        self.btn_cargar_txt.pack(side="left", padx=(0, 8))

        self.btn_ver_html = tk.Button(btn_bar, text="🌐 Ver Suite HTML (Sin Puertos)",
                                      bg="#374151", fg="#93c5fd", activebackground="#4b5563",
                                      font=("Segoe UI", 9, "bold"), relief="flat", padx=12, pady=6, cursor="hand2",
                                      state="disabled", command=self.abrir_reporte_html)
        self.btn_ver_html.pack(side="left", padx=(0, 8))

        self.btn_guardar_json = tk.Button(btn_bar, text="💾 Guardar JSON",
                                          bg="#374151", fg="#cbd5e1", activebackground="#4b5563",
                                          font=("Segoe UI", 9), relief="flat", padx=12, pady=6, cursor="hand2",
                                          state="disabled", command=self.guardar_json)
        self.btn_guardar_json.pack(side="left")

        self.lbl_status = tk.Label(btn_bar, text="", font=("Segoe UI", 9, "italic"), fg="#60a5fa", bg=self.card_bg)
        self.lbl_status.pack(side="right", padx=8)

        # 3. Terminal de Logs en tiempo real
        term_frame = tk.Frame(self.root, bg=self.card_bg, padx=12, pady=8, highlightthickness=1, highlightbackground=self.border_col)
        term_frame.pack(fill="x", padx=12, pady=6)

        lbl_term = tk.Label(term_frame, text="Log de Consultas en Vivo:", font=("Segoe UI", 8, "bold"), fg="#94a3b8", bg=self.card_bg)
        lbl_term.pack(anchor="w")

        self.txt_log = tk.Text(term_frame, height=5, bg=self.term_bg, fg="#38bdf8",
                               font=("Consolas", 8), state="disabled", highlightthickness=0)
        self.txt_log.pack(fill="x", pady=(2, 0))

        # 4. Tabla de Resultados
        table_frame = tk.Frame(self.root, bg=self.card_bg, padx=12, pady=10, highlightthickness=1, highlightbackground=self.border_col)
        table_frame.pack(fill="both", expand=True, padx=12, pady=(6, 12))

        lbl_res = tk.Label(table_frame, text="Resultados del Análisis:", font=("Segoe UI", 10, "bold"), fg="#e2e8f0", bg=self.card_bg)
        lbl_res.pack(anchor="w", pady=(0, 6))

        columns = ("dominio", "entidad", "score", "nivel", "normas_iso", "ips")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)

        self.tree.heading("dominio", text="Dominio")
        self.tree.heading("entidad", text="Organización / Entidad")
        self.tree.heading("score", text="Score (1-100)")
        self.tree.heading("nivel", text="Nivel de Riesgo")
        self.tree.heading("normas_iso", text="Normas ISO Detectadas")
        self.tree.heading("ips", text="Direcciones IP")

        self.tree.column("dominio", width=160, anchor="w")
        self.tree.column("entidad", width=180, anchor="w")
        self.tree.column("score", width=90, anchor="center")
        self.tree.column("nivel", width=100, anchor="center")
        self.tree.column("normas_iso", width=170, anchor="w")
        self.tree.column("ips", width=160, anchor="w")

        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def append_log(self, mensaje):
        def _log():
            self.txt_log.config(state="normal")
            self.txt_log.insert("end", f"{mensaje}\n")
            self.txt_log.see("end")
            self.txt_log.config(state="disabled")
        self.root.after(0, _log)

    def cargar_lista_archivo(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar lista de entidades o dominios",
            filetypes=[("Archivos de texto / CSV", "*.txt *.csv"), ("Todos los archivos", "*.*")]
        )
        if filename:
            contenido = Path(filename).read_text(encoding="utf-8", errors="ignore")
            items = [x.strip() for x in re.split(r"[\r\n,;]+", contenido) if x.strip()]
            if items:
                self.txt_input.delete("1.0", "end")
                self.txt_input.insert("1.0", "\n".join(items))

    def iniciar_analisis_thread(self):
        raw_text = self.txt_input.get("1.0", "end").strip()
        if not raw_text:
            messagebox.showwarning("Atención", "Por favor ingresa al menos un nombre o dominio.")
            return

        lineas = [l.strip() for l in re.split(r"[\r\n,;]+", raw_text) if l.strip()]
        self.btn_ejecutar.config(state="disabled", text="⏳ Analizando...")
        self.lbl_status.config(text="Ejecutando pipeline de Threat Intelligence...")

        # Limpiar tabla y log
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.txt_log.config(state="normal")
        self.txt_log.delete("1.0", "end")
        self.txt_log.config(state="disabled")

        t = threading.Thread(target=self._ejecutar_en_fondo, args=(lineas,), daemon=True)
        t.start()

    def _ejecutar_en_fondo(self, lineas):
        try:
            reporte = ejecutar_pipeline(lineas, log_cb=self.append_log)
            self.ultimo_reporte = reporte

            # Generar archivo HTML estático local en disco
            html_file = BASE_DIR / "ultimo_reporte_soc.html"
            generar_html_estatico(reporte, str(html_file))
            self.ultimo_html_path = html_file

            self.root.after(0, self._actualizar_interfaz_exito, reporte)
        except Exception as e:
            self.root.after(0, self._mostrar_error, str(e))

    def _actualizar_interfaz_exito(self, reporte):
        self.btn_ejecutar.config(state="normal", text="⚡ Iniciar Análisis por Lote")
        self.lbl_status.config(text="✅ Análisis completado con éxito.")
        self.btn_ver_html.config(state="normal")
        self.btn_guardar_json.config(state="normal")

        # Cargar resultados en Treeview
        for d in reporte.get("dominios", []):
            iso_str = ", ".join(d.get("certificados_iso", [])) or "Ninguna"
            ips_str = ", ".join(d.get("ips", []))
            self.tree.insert("", "end", values=(
                d["dominio"],
                d["nombre_origen"],
                f"{d['score']} / 100",
                d["nivel"],
                iso_str,
                ips_str
            ))

        if reporte.get("sin_dominio"):
            self.append_log(f"\n[!] Advertencia: {len(reporte['sin_dominio'])} entidad(es) no resolvieron dominios válidos.")

        messagebox.showinfo("Análisis Finalizado",
                            f"Se procesaron {reporte['resumen']['nombres_procesados']} entidades.\n"
                            f"Dominios identificados y evaluados: {reporte['resumen']['dominios_analizados']}\n\n"
                            f"Haz clic en '🌐 Ver Suite HTML (Sin Puertos)' para ver el Dossier Ejecutivo completo.")

    def _mostrar_error(self, err_msg):
        self.btn_ejecutar.config(state="normal", text="⚡ Iniciar Análisis por Lote")
        self.lbl_status.config(text="❌ Error durante la ejecución.")
        messagebox.showerror("Error", f"Ocurrió un error en el motor CTI:\n{err_msg}")

    def abrir_reporte_html(self):
        if self.ultimo_html_path and self.ultimo_html_path.exists():
            # Abrir archivo estático local en el navegador por defecto (file:///)
            # CERO PUERTOS ABIERTOS
            webbrowser.open(self.ultimo_html_path.as_uri())
        else:
            messagebox.showwarning("Atención", "No hay reporte HTML generado todavía.")

    def guardar_json(self):
        if not self.ultimo_reporte:
            return
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Archivos JSON", "*.json")],
            initialfile=f"ti_dominios_{time.strftime('%Y%m%d_%H%M%S')}.json"
        )
        if filename:
            Path(filename).write_text(json.dumps(self.ultimo_reporte, indent=2, ensure_ascii=False), encoding="utf-8")
            messagebox.showinfo("Guardado", f"Reporte JSON exportado correctamente en:\n{filename}")

def main():
    root = tk.Tk()
    app = SOCAppDesktop(root)
    root.mainloop()

if __name__ == "__main__":
    main()
