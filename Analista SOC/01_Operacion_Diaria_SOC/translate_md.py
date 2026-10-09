import time
import sys
import os
import requests
import urllib3

# Desactivar advertencias SSL e inyectar verify=False globalmente (Evasión de FortiGate)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
old_request = requests.Session.request
def new_request(*args, **kwargs):
    kwargs['verify'] = False
    return old_request(*args, **kwargs)
requests.Session.request = new_request

from deep_translator import GoogleTranslator

input_file = "securityonion-docs.md"
output_file = "securityonion-docs-ES.md"

def translate_text(text):
    if not text.strip():
        return text
    try:
        translated = GoogleTranslator(source='auto', target='es').translate(text)
        return translated if translated else text
    except Exception as e:
        print(f"Error translating: {e}")
        return text

if __name__ == "__main__":
    if not os.path.exists(input_file):
        print(f"File {input_file} not found.")
        sys.exit(1)
        
    print(f"Starting translation of {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8') as fout:
         
        in_code_block = False
        buffer = []
        
        def flush_buffer():
            if not buffer: return
            text = "\n".join(buffer)
            if len(text) > 4000:
                for line in buffer:
                    fout.write(translate_text(line) + "\n")
                    time.sleep(0.1)
            else:
                fout.write(translate_text(text) + "\n")
                time.sleep(0.2)
            buffer.clear()

        lines = fin.readlines()
        total_lines = len(lines)
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            if i % 100 == 0:
                print(f"Progress: {i}/{total_lines} lines...")
                
            if stripped.startswith("```"):
                flush_buffer()
                in_code_block = not in_code_block
                fout.write(line)
                continue
                
            if in_code_block:
                fout.write(line)
                continue
                
            if stripped.startswith("![") or stripped.startswith("<") or stripped.startswith("http") or stripped == "---":
                flush_buffer()
                fout.write(line)
                continue
                
            if not stripped:
                flush_buffer()
                fout.write(line)
                continue
                
            buffer.append(line.rstrip('\n'))
            
        flush_buffer()
        
    print(f"Translation completed successfully! File saved as {output_file}")
