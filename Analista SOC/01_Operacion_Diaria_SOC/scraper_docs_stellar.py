import time
import os
import re
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright

# --- CONFIGURACIÓN ---
# REEMPLAZA ESTA URL con el enlace real donde lees la documentación
BASE_URL = "https://docs.stellarcyber.ai/prod-docs/6.6.xs/Common/Overview-Product.htm?tocpath=_____1"
OUTPUT_DIR = "Stellar_Docs_PDF"

def sanitize_filename(name):
    """Limpia caracteres inválidos para nombres de archivos en Windows"""
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def run():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with sync_playwright() as p:
        # headless=False abre una ventana visible para que puedas iniciar sesión si hace falta
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print(f"Navegando a la página principal: {BASE_URL}")
        try:
            page.goto(BASE_URL, wait_until="domcontentloaded")
        except Exception as e:
            print("Por favor configura una URL válida en BASE_URL dentro del script.")
            browser.close()
            return
        
        # Pausa para iniciar sesión manualmente o aceptar cookies
        print("⏳ Tienes 15 segundos... Si necesitas iniciar sesión en el portal, hazlo AHORA en la ventana que se abrió.")
        time.sleep(15)

        print("🔍 Buscando enlaces en el menú lateral (sidenav)...")
        try:
            page.wait_for_selector('.sidenav', timeout=15000)
        except:
            print("⚠️ No se encontró el menú '.sidenav'. Asegúrate de que la URL es correcta y la página cargó completamente.")
        
        # Extraemos todos los enlaces de la barra lateral (href y texto visible)
        links = page.locator('.sidenav a').evaluate_all(
            "elements => elements.map(el => ({ text: el.innerText.trim(), href: el.href }))"
        )
        
        # Filtramos enlaces válidos y quitamos duplicados (usando set temporal para href)
        seen = set()
        valid_links = []
        for l in links:
            href = l['href']
            # Ignoramos si es javascript, anclas vacías o si ya lo agregamos
            if href and href.startswith('http') and href not in seen:
                seen.add(href)
                valid_links.append(l)

        print(f"✅ Se encontraron {len(valid_links)} páginas únicas para descargar.")

        for index, link in enumerate(valid_links, start=1):
            title = link['text'] if link['text'] else f"Seccion_Sin_Nombre_{index}"
            safe_title = sanitize_filename(title)
            # Reemplazar retornos de carro si el titulo es multilínea
            safe_title = safe_title.replace('\n', '_')
            url = link['href']
            
            # Nombre del archivo: 001_Titulo_Del_Doc.pdf
            pdf_filename = os.path.join(OUTPUT_DIR, f"{index:03d}_{safe_title}.pdf")
            
            if os.path.exists(pdf_filename):
                print(f"[{index}/{len(valid_links)}] ⏭️ Saltando (ya existe): {safe_title}")
                continue

            print(f"[{index}/{len(valid_links)}] 📥 Descargando: {safe_title}")
            try:
                page.goto(url, wait_until="networkidle")
                
                # Opcional: inyectar algo de CSS para ocultar el menú al imprimir, 
                # así el PDF queda más limpio. (Ajustable según el HTML real).
                page.evaluate("""
                    try {
                        const sidenav = document.querySelector('.sidenav-wrapper');
                        if (sidenav) sidenav.style.display = 'none';
                    } catch(e) {}
                """)

                # Esperamos un momento para renderizado de fuentes/imágenes
                time.sleep(2)
                
                page.pdf(path=pdf_filename, format="A4", print_background=True, margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"})
            except Exception as e:
                print(f"❌ Error al descargar {url}: {e}")
            
            # Pausa para comportamiento humano y no saturar el servidor
            time.sleep(3)

        print("\n🎉 ¡Descarga finalizada! Revisa la carpeta:", OUTPUT_DIR)
        browser.close()

if __name__ == "__main__":
    run()
