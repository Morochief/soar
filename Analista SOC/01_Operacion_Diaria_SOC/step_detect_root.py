import json, os, sys
from graphify.detect import detect
from pathlib import Path

os.makedirs('graphify-out', exist_ok=True)
Path('graphify-out/.graphify_python').write_text(sys.executable, encoding='utf-8')
Path('graphify-out/.graphify_root').write_text(str(Path('.').resolve()), encoding='utf-8')

result = detect(Path('.'))
Path('graphify-out/.graphify_detect.json').write_text(json.dumps(result, ensure_ascii=False), encoding='utf-8')
print(f"Total files: {result['total_files']}, Words: {result['total_words']}")
print(f"Code: {len(result['files']['code'])}, Docs: {len(result['files']['document'])}, Papers: {len(result['files']['paper'])}, Images: {len(result['files']['image'])}")
