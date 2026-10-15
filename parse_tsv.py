import csv
import sys
import os

tsv_path = r"C:\Users\kevinmoraes\Documents\SOC_SOAR\soar\XQL-QUERY-18508 - 2026_10_15.tsv"

if not os.path.exists(tsv_path):
    print("File not found:", tsv_path)
    sys.exit(1)

file_size = os.path.getsize(tsv_path)
print(f"File size: {file_size} bytes")

with open(tsv_path, 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.reader(f, delimiter='\t')
    try:
        header = next(reader)
    except StopIteration:
        print("Empty file")
        sys.exit(0)
        
    print("Header columns:", header)
    
    rows = []
    event_types = set()
    files = []
    
    for idx, row in enumerate(reader):
        if not row:
            continue
        rows.append(row)
        # Check columns
        # Map headers
        row_dict = {header[i]: row[i] if i < len(row) else '' for i in range(len(header))}
        
        evt = row_dict.get('event_type', '')
        if evt:
            event_types.add(evt)
            
        fname = row_dict.get('action_file_name', '').strip()
        fpath = row_dict.get('action_file_path', '').strip()
        actor = row_dict.get('actor_process_image_name', '').strip()
        time_val = row_dict.get('_time', '')
        
        if fname or fpath:
            files.append({
                'time': time_val,
                'file_name': fname,
                'file_path': fpath,
                'actor': actor,
                'event_type': evt
            })

print(f"Total rows: {len(rows)}")
print(f"Distinct event types: {event_types}")
print(f"Rows with file info: {len(files)}")

if files:
    print("\n--- SAMPLE FILES FOUND (First 40) ---")
    for f in files[:40]:
        print(f"[{f['time']}] {f['file_name']} -> {f['file_path']} (by {f['actor']} / {f['event_type']})")
        
    # Group by file extension
    from collections import Counter
    exts = [os.path.splitext(f['file_name'])[1].lower() for f in files if f['file_name']]
    print("\nFile extension distribution:")
    for ext, count in Counter(exts).most_common(15):
        print(f"  {ext if ext else '[no-ext]'}: {count}")
else:
    print("\nNo rows with action_file_name or action_file_path.")
    print("Sample of first 5 raw rows:")
    for r in rows[:5]:
        print(" ", r)
