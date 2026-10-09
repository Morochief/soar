import datetime
import time
import requests
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import pandas as pd
import sys
import subprocess

class CVEFetcherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SOC CVE Intel Fetcher")
        self.root.geometry("700x620")
        self.root.configure(bg="#1e222b")

        # Variables de control
        self.vulnerabilidades = []
        self.headers = {
            "User-Agent": "CVE-Markdown-Fetcher-Script",
            "apiKey": "ce79f233-34e5-4445-a3fd-84a8cd00beb6"
        }
        self.var_critical = tk.BooleanVar(value=True)
        self.var_high = tk.BooleanVar(value=True)
        self.var_medium = tk.BooleanVar(value=False)
        self.var_low = tk.BooleanVar(value=False)

        # Configuración del Tema y Estilos
        self.setup_styles()

        # Contenedor Principal con márgenes
        main_container = tk.Frame(root, bg="#1e222b", padx=20, pady=15)
        main_container.pack(fill="both", expand=True)

        # 1. Encabezado / Titulo
        header_frame = tk.Frame(main_container, bg="#1e222b")
        header_frame.pack(fill="x", pady=(0, 10))
        
        lbl_title = tk.Label(header_frame, text="🛡️ SOC VULNERABILITY INTEL FETCH", font=("Segoe UI", 14, "bold"), fg="#5294e2", bg="#1e222b")
        lbl_title.pack(anchor="w")
        
        lbl_subtitle = tk.Label(header_frame, text="Extracción automatizada de vulnerabilidades críticas y altas desde NVD.", font=("Segoe UI", 9), fg="#abb2bf", bg="#1e222b")
        lbl_subtitle.pack(anchor="w", pady=(2, 0))

        # 2. Panel de Configuración
        frame_config = tk.Frame(main_container, bg="#282c34", highlightbackground="#3e4452", highlightthickness=1, bd=0)
        frame_config.pack(fill="x", pady=(0, 10))
        
        # Grid interno para configuración
        inner_grid = tk.Frame(frame_config, bg="#282c34", padx=15, pady=15)
        inner_grid.pack(fill="x")

        # Fecha Inicio
        tk.Label(inner_grid, text="Fecha Inicio (DD-MM-YYYY):", font=("Segoe UI", 10), fg="#abb2bf", bg="#282c34").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_inicio = tk.Entry(inner_grid, font=("Segoe UI", 10), fg="#ffffff", bg="#1e222b", insertbackground="white", bd=1, relief="flat", width=16)
        self.entry_inicio.insert(0, "01-11-2025")
        self.entry_inicio.grid(row=0, column=1, padx=(10, 30), pady=5)

        # Fecha Fin
        tk.Label(inner_grid, text="Fecha Fin (DD-MM-YYYY):", font=("Segoe UI", 10), fg="#abb2bf", bg="#282c34").grid(row=0, column=2, sticky="w", pady=5)
        self.entry_fin = tk.Entry(inner_grid, font=("Segoe UI", 10), fg="#ffffff", bg="#1e222b", insertbackground="white", bd=1, relief="flat", width=16)
        self.entry_fin.insert(0, datetime.date.today().strftime("%d-%m-%Y"))
        self.entry_fin.grid(row=0, column=3, padx=10, pady=5)

        # Severidades
        tk.Label(inner_grid, text="Severidad:", font=("Segoe UI", 10), fg="#abb2bf", bg="#282c34").grid(row=1, column=0, sticky="w", pady=5)
        frame_sev = tk.Frame(inner_grid, bg="#282c34")
        frame_sev.grid(row=1, column=1, columnspan=3, sticky="w", padx=(10, 0), pady=5)
        
        tk.Checkbutton(frame_sev, text="Crítica", variable=self.var_critical, font=("Segoe UI", 9), fg="#e06c75", bg="#282c34", selectcolor="#1e222b", activebackground="#282c34", activeforeground="#e06c75").pack(side="left", padx=(0, 10))
        tk.Checkbutton(frame_sev, text="Alta", variable=self.var_high, font=("Segoe UI", 9), fg="#d19a66", bg="#282c34", selectcolor="#1e222b", activebackground="#282c34", activeforeground="#d19a66").pack(side="left", padx=(0, 10))
        tk.Checkbutton(frame_sev, text="Media", variable=self.var_medium, font=("Segoe UI", 9), fg="#e5c07b", bg="#282c34", selectcolor="#1e222b", activebackground="#282c34", activeforeground="#e5c07b").pack(side="left", padx=(0, 10))
        tk.Checkbutton(frame_sev, text="Baja", variable=self.var_low, font=("Segoe UI", 9), fg="#98c379", bg="#282c34", selectcolor="#1e222b", activebackground="#282c34", activeforeground="#98c379").pack(side="left")

        # Webhook de Slack
        tk.Label(inner_grid, text="Webhook Slack (Opcional):", font=("Segoe UI", 10), fg="#abb2bf", bg="#282c34").grid(row=2, column=0, sticky="w", pady=8)
        self.entry_slack = tk.Entry(inner_grid, font=("Segoe UI", 9), fg="#ffffff", bg="#1e222b", insertbackground="white", bd=1, relief="flat")
        self.entry_slack.grid(row=2, column=1, columnspan=3, sticky="we", padx=(10, 0), pady=8)

        # Programación Diaria (Hora de Ejecución)
        tk.Label(inner_grid, text="Hora Diaria (HH:MM):", font=("Segoe UI", 10), fg="#abb2bf", bg="#282c34").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_hora = tk.Entry(inner_grid, font=("Segoe UI", 10), fg="#ffffff", bg="#1e222b", insertbackground="white", bd=1, relief="flat", width=8)
        self.entry_hora.insert(0, "09:00")
        self.entry_hora.grid(row=3, column=1, padx=(10, 30), pady=5, sticky="w")

        self.btn_schedule = tk.Button(inner_grid, text="Programar Tarea Diaria", font=("Segoe UI", 9, "bold"), fg="#ffffff", bg="#98c379", activebackground="#a3be8c", bd=0, padx=10, pady=4, command=self.register_windows_task)
        self.btn_schedule.grid(row=3, column=2, columnspan=2, sticky="w", pady=5)

        # 3. Consola de Progreso / Log
        frame_console = tk.Frame(main_container, bg="#282c34", highlightbackground="#3e4452", highlightthickness=1, bd=0)
        frame_console.pack(fill="both", expand=True, pady=(0, 10))

        lbl_console_title = tk.Label(frame_console, text="LOG DE CONSULTAS Y ESTADO DE API", font=("Segoe UI", 9, "bold"), fg="#5c6370", bg="#282c34", padx=10, pady=5)
        lbl_console_title.pack(anchor="w")

        self.text_log = tk.Text(frame_console, wrap="word", height=8, font=("Consolas", 9), fg="#abb2bf", bg="#1e222b", insertbackground="white", bd=0, highlightthickness=0)
        self.text_log.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Barra de progreso integrada
        self.progress_bar = ttk.Progressbar(frame_console, style="Custom.Horizontal.TProgressbar", mode="determinate")
        self.progress_bar.pack(fill="x", padx=10, pady=(0, 10))

        # 4. Botonera
        frame_acciones = tk.Frame(main_container, bg="#1e222b")
        frame_acciones.pack(fill="x", side="bottom")

        self.btn_fetch = tk.Button(frame_acciones, text="Iniciar Búsqueda", font=("Segoe UI", 10, "bold"), fg="#ffffff", bg="#4b5263", activebackground="#5c6370", activeforeground="#ffffff", bd=0, padx=15, pady=8, command=self.start_fetch_thread)
        self.btn_fetch.pack(side="left", padx=(0, 10))

        self.btn_export_md = tk.Button(frame_acciones, text="Exportar Markdown (.md)", font=("Segoe UI", 10), fg="#ffffff", bg="#282c34", activebackground="#3e4452", bd=0, padx=12, pady=8, state="disabled", command=self.export_markdown)
        self.btn_export_md.pack(side="left", padx=5)

        self.btn_export_xlsx = tk.Button(frame_acciones, text="Exportar Excel (.xlsx)", font=("Segoe UI", 10), fg="#ffffff", bg="#282c34", activebackground="#3e4452", bd=0, padx=12, pady=8, state="disabled", command=self.export_excel)
        self.btn_export_xlsx.pack(side="left", padx=5)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Estilos de la barra de progreso
        style.configure("Custom.Horizontal.TProgressbar",
                        thickness=6,
                        troughcolor="#1e222b",
                        background="#5294e2",
                        bordercolor="#1e222b",
                        lightcolor="#5294e2",
                        darkcolor="#5294e2")

    def write_log(self, message):
        self.text_log.insert(tk.END, message + "\n")
        self.text_log.see(tk.END)

    def chunk_dates(self, start, end, delta_days=100):
        chunks = []
        curr = start
        while curr < end:
            next_date = curr + datetime.timedelta(days=delta_days)
            if next_date > end:
                next_date = end
            chunks.append((curr, next_date))
            curr = next_date + datetime.timedelta(seconds=1)
        return chunks

    def get_selected_severities(self):
        sevs = []
        if self.var_critical.get(): sevs.append("CRITICAL")
        if self.var_high.get(): sevs.append("HIGH")
        if self.var_medium.get(): sevs.append("MEDIUM")
        if self.var_low.get(): sevs.append("LOW")
        return sevs

    def start_fetch_thread(self):
        self.vulnerabilidades.clear()
        self.text_log.delete("1.0", tk.END)
        self.btn_export_md.config(state="disabled", bg="#282c34")
        self.btn_export_xlsx.config(state="disabled", bg="#282c34")

        # Validar fechas ingresadas en formato DD-MM-YYYY
        try:
            inicio_str = self.entry_inicio.get().strip()
            fin_str = self.entry_fin.get().strip()
            start_date = datetime.datetime.strptime(inicio_str, "%d-%m-%y" if len(inicio_str.split('-')[-1]) == 2 else "%d-%m-%Y").replace(tzinfo=datetime.timezone.utc)
            end_date = datetime.datetime.strptime(fin_str, "%d-%m-%y" if len(fin_str.split('-')[-1]) == 2 else "%d-%m-%Y").replace(hour=23, minute=59, second=59, tzinfo=datetime.timezone.utc)
        except ValueError:
            messagebox.showerror("Error de formato", "Formato de fecha inválido. Por favor utilice DD-MM-YYYY.")
            return

        if start_date > end_date:
            messagebox.showerror("Error de rango", "La fecha de inicio no puede ser posterior a la fecha de fin.")
            return

        selected_sevs = self.get_selected_severities()
        if not selected_sevs:
            messagebox.showerror("Error de selección", "Debe seleccionar al menos una severidad.")
            return

        # Cambiar aspecto visual del botón para indicar actividad
        self.btn_fetch.config(state="disabled", bg="#2c313c", text="Buscando...")
        
        threading.Thread(target=self.fetch_cves, args=(start_date, end_date, selected_sevs), daemon=True).start()

    def fetch_cves(self, start_date, end_date, selected_sevs):
        date_chunks = self.chunk_dates(start_date, end_date)
        total_steps = len(selected_sevs) * len(date_chunks)
        current_step = 0

        self.write_log(f"[INFO] Iniciando búsqueda de CVEs...")
        self.write_log(f"[INFO] Rango: {start_date.strftime('%d-%m-%Y')} a {end_date.strftime('%d-%m-%Y')}")

        for severidad in selected_sevs:
            self.write_log(f"\n[API] Consultando nivel: {severidad}")
            for start_chunk, end_chunk in date_chunks:
                str_inicio = start_chunk.strftime("%Y-%m-%dT%H:%M:%S.000")
                str_fin = end_chunk.strftime("%Y-%m-%dT%H:%M:%S.000")
                
                URL = (
                    f"https://services.nvd.nist.gov/rest/json/cves/2.0?"
                    f"pubStartDate={str_inicio}&pubEndDate={str_fin}&cvssV3Severity={severidad}"
                )
                
                self.write_log(f" -> Rango NVD: {start_chunk.strftime('%d-%m-%Y')} al {end_chunk.strftime('%d-%m-%Y')}")
                
                max_retries = 5
                for attempt in range(max_retries):
                    try:
                        response = requests.get(URL, headers=self.headers, timeout=40)
                        response.raise_for_status()
                        data = response.json()
                        nuevos_cves = data.get("vulnerabilities", [])
                        self.vulnerabilidades.extend(nuevos_cves)
                        self.write_log(f"    [OK] Obtenidos {len(nuevos_cves)} registros.")
                        break
                    except requests.exceptions.RequestException as e:
                        self.write_log(f"    [WARN] Intento {attempt + 1}/{max_retries} fallido: {e}")
                        if attempt == max_retries - 1:
                            self.write_log(f"    [ERROR] No se pudo completar este bloque de datos.")
                            break
                        self.write_log("    [WAIT] Servidor saturado. Reintentando en 6 segundos...")
                        time.sleep(6)

                current_step += 1
                self.progress_bar["value"] = (current_step / total_steps) * 100
                self.root.update_idletasks()
                time.sleep(3)

        total_cves = len(self.vulnerabilidades)
        self.write_log(f"\n[FIN] Descarga finalizada. Total vulnerabilidades: {total_cves}")
        self.btn_fetch.config(state="normal", bg="#4b5263", text="Iniciar Búsqueda")
        self.progress_bar["value"] = 100

        if total_cves > 0:
            self.btn_export_md.config(state="normal", bg="#5294e2")
            self.btn_export_xlsx.config(state="normal", bg="#98c379")
            
            # Enviar notificación a Slack si se configuró Webhook
            slack_url = self.entry_slack.get().strip()
            if slack_url:
                self.send_slack_notification(slack_url, start_date, end_date, total_cves)
                
            messagebox.showinfo("Búsqueda completada", f"Extracción completada. Se descargaron {total_cves} CVEs.")
        else:
            messagebox.showinfo("Búsqueda completada", "No se encontraron registros en el rango de fechas seleccionado.")

    def send_slack_notification(self, webhook_url, start_date, end_date, total_cves):
        self.write_log("\n[SLACK] Enviando resumen al canal de Slack...")
        payload = {
            "text": (
                f"🛡️ *Reporte de Vulnerabilidades Críticas/Altas Generado*\n"
                f"📅 *Rango:* {start_date.strftime('%d-%m-%Y')} al {end_date.strftime('%d-%m-%Y')}\n"
                f"🔥 *Total CVEs Encontrados:* `{total_cves}`\n"
                f"📥 _Vulnerabilidades listas en la consola SOC local._"
            )
        }
        try:
            response = requests.post(webhook_url, json=payload, timeout=10)
            if response.status_code == 200:
                self.write_log("   [SLACK OK] Notificación enviada correctamente.")
            else:
                self.write_log(f"   [SLACK ERROR] Código de error de Slack: {response.status_code}")
        except Exception as e:
            self.write_log(f"   [SLACK ERROR] Error de red al conectar: {e}")

    def register_windows_task(self):
        slack_url = self.entry_slack.get().strip()
        if not slack_url:
            messagebox.showerror("Error de entrada", "Se requiere ingresar una URL de Webhook de Slack válida para programar notificaciones.")
            return

        hora_ejecucion = self.entry_hora.get().strip()
        # Validar formato de hora HH:MM
        try:
            time.strptime(hora_ejecucion, "%H:%M")
        except ValueError:
            messagebox.showerror("Error de entrada", "Formato de hora inválido. Utilice HH:MM (ej. 09:00).")
            return

        import os
        script_path = os.path.abspath(__file__)
        python_exe = sys.executable

        selected_sevs = self.get_selected_severities()
        if not selected_sevs:
            messagebox.showerror("Error de selección", "Debe seleccionar al menos una severidad para programar la tarea.")
            return
            
        sevs_str = ",".join(selected_sevs)

        # Comando de schtasks para registrar la tarea en Windows de forma silenciosa
        task_name = "SOC_Diario_CVE_Fetcher"
        cmd = [
            "schtasks", "/Create", "/F",
            "/TN", task_name,
            "/TR", f'"{python_exe}" "{script_path}" --cron "{slack_url}" --severity "{sevs_str}"',
            "/SC", "DAILY",
            "/ST", hora_ejecucion
        ]

        try:
            # schtasks no requiere powershell de administrador si se ejecuta para el usuario actual
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            messagebox.showinfo("Programación Exitosa", f"La tarea diaria se ha programado correctamente en Windows a las {hora_ejecucion}.\nNombre: {task_name}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error de Programación", f"No se pudo programar la tarea automática.\nDetalle: {e.stderr}")

    def parse_vulnerabilities(self):
        parsed_data = []
        for item in self.vulnerabilidades:
            cve_data = item.get("cve", {})
            cve_id = cve_data.get("id", "N/A")
            published = cve_data.get("published", "N/A")
            
            descriptions = cve_data.get("descriptions", [])
            desc_text = "Sin descripción disponible."
            for d in descriptions:
                if d.get("lang") == "en":
                    desc_text = d.get("value")
                    break
            
            metrics = cve_data.get("metrics", {})
            cvss_v3x = metrics.get("cvssMetricV31", []) or metrics.get("cvssMetricV30", [])
            score = "N/A"
            vector = "N/A"
            nivel_str = "DESCONOCIDO"
            
            if cvss_v3x:
                cvss_data = cvss_v3x[0].get("cvssData", {})
                score = cvss_data.get("baseScore", "N/A")
                vector = cvss_data.get("vectorString", "N/A")
                if isinstance(score, (float, int)):
                    if score >= 9.0:
                        nivel_str = "CRÍTICA"
                    elif score >= 7.0:
                        nivel_str = "ALTA"
                    elif score >= 4.0:
                        nivel_str = "MEDIA"
            
            parsed_data.append({
                "CVE": cve_id,
                "Puntuación CVSS v3": score,
                "Severidad": nivel_str,
                "Fecha Publicación": published,
                "Vector de Ataque": vector,
                "Descripción": desc_text
            })
        return parsed_data

    def export_markdown(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Archivos Markdown", "*.md"), ("Todos los archivos", "*.*")],
            title="Guardar reporte en Markdown"
        )
        if not file_path:
            return

        data_list = self.parse_vulnerabilities()
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# Reporte de CVEs (Críticos y Altos)\n\n")
                f.write(f"**Fecha de generación:** {datetime.datetime.now(datetime.timezone.utc).strftime('%d-%m-%Y %H:%M:%S UTC')}\n")
                f.write(f"**Total encontrados:** {len(data_list)}\n\n")
                f.write("---\n\n")

                for item in data_list:
                    f.write(f"## [{item['CVE']}](https://nvd.nist.gov/vuln/detail/{item['CVE']})\n")
                    f.write(f"* **Puntuación CVSS v3:** `{item['Puntuación CVSS v3']}` ({item['Severidad']})\n")
                    f.write(f"* **Fecha de Publicación:** {item['Fecha Publicación']}\n")
                    f.write(f"* **Vector de Ataque:** `{item['Vector de Ataque']}`\n\n")
                    f.write(f"### Descripción\n{item['Descripción']}\n\n")
                    f.write("---\n\n")
            
            messagebox.showinfo("Exportación exitosa", "El reporte Markdown se ha guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo: {e}")

    def export_excel(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Archivos de Excel", "*.xlsx"), ("Todos los archivos", "*.*")],
            title="Guardar reporte en Excel"
        )
        if not file_path:
            return

        data_list = self.parse_vulnerabilities()
        df = pd.DataFrame(data_list)
        try:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Exportación exitosa", "El reporte en Excel se ha guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo: {e}")

def run_headless_cron(slack_url, severidades=None):
    if severidades is None:
        severidades = ["CRITICAL", "HIGH"]
    
    print(f"[CRON] Iniciando descarga diaria silenciosa para {', '.join(severidades)}...")
    # Rango de fechas: Ayer a Hoy
    end_date = datetime.datetime.now(datetime.timezone.utc)
    start_date = end_date - datetime.timedelta(days=1)
    
    headers = {
        "User-Agent": "CVE-Markdown-Fetcher-Script",
        "apiKey": "ce79f233-34e5-4445-a3fd-84a8cd00beb6"
    }
    vulnerabilidades = []
    
    # 24 horas en un solo chunk
    str_inicio = start_date.strftime("%Y-%m-%dT%H:%M:%S.000")
    str_fin = end_date.strftime("%Y-%m-%dT%H:%M:%S.000")
    
    for severidad in severidades:
        URL = (
            f"https://services.nvd.nist.gov/rest/json/cves/2.0?"
            f"pubStartDate={str_inicio}&pubEndDate={str_fin}&cvssV3Severity={severidad}"
        )
        print(f"[CRON] Consultando {severidad} de {start_date.date()} a {end_date.date()}...")
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(URL, headers=headers, timeout=40)
                response.raise_for_status()
                data = response.json()
                nuevos = data.get("vulnerabilities", [])
                vulnerabilidades.extend(nuevos)
                print(f"[CRON] Obtenidos {len(nuevos)} CVEs.")
                break
            except Exception as e:
                print(f"[CRON] Intento {attempt+1} fallido: {e}")
                time.sleep(6)
        time.sleep(3)
        
    total = len(vulnerabilidades)
    print(f"[CRON] Proceso terminado. Total encontrados: {total}")
    
    if total > 0:
        # Enviar a Slack
        payload = {
            "text": (
                f"🛡️ *Reporte Diario Automático de Vulnerabilidades (SOC)*\n"
                f"📅 *Rango:* {start_date.strftime('%d-%m-%Y')} al {end_date.strftime('%d-%m-%Y')}\n"
                f"🔥 *Total CVEs Nuevos ({', '.join(severidades)}):* `{total}`\n"
            )
        }
        try:
            requests.post(slack_url, json=payload, timeout=10)
            print("[CRON] Resumen enviado a Slack correctamente.")
        except Exception as e:
            print(f"[CRON] Error al enviar a Slack: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--cron":
        slack_url = sys.argv[2]
        severidades = ["CRITICAL", "HIGH"]
        if len(sys.argv) > 4 and sys.argv[3] == "--severity":
            severidades = sys.argv[4].split(",")
        run_headless_cron(slack_url, severidades)
    else:
        root = tk.Tk()
        app = CVEFetcherGUI(root)
        root.mainloop()
