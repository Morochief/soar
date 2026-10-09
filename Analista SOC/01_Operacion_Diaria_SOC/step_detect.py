import json, os, sys
from graphify.detect import detect
from pathlib import Path

os.makedirs('soc_gem_graph/graphify-out', exist_ok=True)
Path('soc_gem_graph/graphify-out/.graphify_python').write_text(sys.executable, encoding='utf-8')
Path('soc_gem_graph/graphify-out/.graphify_root').write_text(str(Path('soc_gem_graph').resolve()), encoding='utf-8')

result = detect(Path('soc_gem_graph'))
Path('soc_gem_graph/graphify-out/.graphify_detect.json').write_text(json.dumps(result, ensure_ascii=False), encoding='utf-8')
print(f"Files: {result['total_files']}, Words: {result['total_words']}")
