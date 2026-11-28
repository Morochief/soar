import os, sys, datetime

# Carpeta del propio script (antes: ruta absoluta de Windows). Uso: python list_recent_mods.py [dias]
path = os.path.dirname(os.path.abspath(__file__))
dias = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 7
cutoff = datetime.datetime.now() - datetime.timedelta(days=dias)

files = []
for f in os.listdir(path):
    full = os.path.join(path, f)
    if os.path.isfile(full):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(full))
        if mtime >= cutoff:
            files.append((mtime, f, os.path.getsize(full)))

files.sort()
print(f'Total files: {len(files)}')
for mtime, name, size in files:
    d_str = mtime.strftime('%Y-%m-%d %H:%M:%S')
    print(f'{d_str} | {size:>8} bytes | {name}')
