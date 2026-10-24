import os, datetime

path = r'c:\Users\kevinmoraes\Desktop\SOC\soar'
cutoff = datetime.datetime(2026, 10, 21, 0, 0, 0)

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
