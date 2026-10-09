import json
from pathlib import Path
from collections import Counter

detect = json.loads(Path('graphify-out/.graphify_detect.json').read_text(encoding='utf-8'))
root = Path(detect['scan_root'])

all_files = []
for cat in ['code', 'document', 'paper', 'image', 'video']:
    all_files.extend(detect['files'].get(cat, []))

subdirs = Counter()
for f in all_files:
    try:
        p = Path(f).relative_to(root)
        if len(p.parts) > 1:
            subdirs[p.parts[0]] += 1
        else:
            subdirs['(root)'] += 1
    except ValueError:
        pass

for name, count in subdirs.most_common(5):
    print(f"{name}: {count} files")
