import os
import glob
from markitdown import MarkItDown

def main():
    source_dir = r"C:\Users\kevinmoraes\Downloads\Analista SOC\Stellar Documentacion"
    target_dir = os.path.join(source_dir, "Markdown_Output")
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    pdf_files = glob.glob(os.path.join(source_dir, "*.pdf"))
    total = len(pdf_files)
    
    print(f"Iniciando conversión de {total} archivos PDF...")
    
    md = MarkItDown()
    success_count = 0
    error_count = 0

    for idx, pdf_path in enumerate(pdf_files, 1):
        filename = os.path.basename(pdf_path)
        md_filename = os.path.splitext(filename)[0] + ".md"
        target_path = os.path.join(target_dir, md_filename)
        
        # Skip if already exists
        if os.path.exists(target_path):
            print(f"[{idx}/{total}] Saltando (ya existe): {filename}")
            success_count += 1
            continue
            
        print(f"[{idx}/{total}] Convirtiendo: {filename} ...")
        
        try:
            result = md.convert(pdf_path)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(result.text_content)
            success_count += 1
        except Exception as e:
            print(f"  -> ERROR al convertir {filename}: {e}")
            error_count += 1

    print("\n--- RESUMEN ---")
    print(f"Total procesados: {total}")
    print(f"Éxitos: {success_count}")
    print(f"Errores: {error_count}")

if __name__ == "__main__":
    main()
