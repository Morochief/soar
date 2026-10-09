import sys, json, glob
from pathlib import Path

# STEP B3 - Merge chunks
chunks = sorted(glob.glob('soc_gem_graph/graphify-out/.graphify_chunk_*.json'))
all_nodes, all_edges, all_hyperedges = [], [], []
total_in, total_out = 0, 0
for c in chunks:
    d = json.loads(Path(c).read_text(encoding="utf-8"))
    all_nodes += d.get('nodes', [])
    all_edges += d.get('edges', [])
    all_hyperedges += d.get('hyperedges', [])
    total_in += d.get('input_tokens', 0)
    total_out += d.get('output_tokens', 0)

seen = set()
deduped = []
for n in all_nodes:
    if n['id'] not in seen:
        seen.add(n['id'])
        deduped.append(n)

merged_semantic = {
    'nodes': deduped,
    'edges': all_edges,
    'hyperedges': all_hyperedges,
    'input_tokens': total_in,
    'output_tokens': total_out,
}
Path('soc_gem_graph/graphify-out/.graphify_semantic.json').write_text(json.dumps(merged_semantic, indent=2, ensure_ascii=False), encoding="utf-8")

# STEP C - Merge AST + Semantic
ast = json.loads(Path('soc_gem_graph/graphify-out/.graphify_ast.json').read_text(encoding="utf-8"))
sem = json.loads(Path('soc_gem_graph/graphify-out/.graphify_semantic.json').read_text(encoding="utf-8"))

seen_ast = {n['id'] for n in ast['nodes']}
merged_nodes = list(ast['nodes'])
for n in sem['nodes']:
    if n['id'] not in seen_ast:
        merged_nodes.append(n)
        seen_ast.add(n['id'])

merged_edges = ast['edges'] + sem['edges']
merged_hyperedges = sem.get('hyperedges', [])
merged_extract = {
    'nodes': merged_nodes,
    'edges': merged_edges,
    'hyperedges': merged_hyperedges,
    'input_tokens': sem.get('input_tokens', 0),
    'output_tokens': sem.get('output_tokens', 0),
}
Path('soc_gem_graph/graphify-out/.graphify_extract.json').write_text(json.dumps(merged_extract, indent=2, ensure_ascii=False), encoding="utf-8")

# STEP 4 - Build graph, cluster, analyze, report
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json

extraction = merged_extract
detection = json.loads(Path('soc_gem_graph/graphify-out/.graphify_detect.json').read_text(encoding="utf-8"))

G = build_from_json(extraction, root='soc_gem_graph', directed=False)
if G.number_of_nodes() == 0:
    print('ERROR: Graph is empty - extraction produced no nodes.')
    sys.exit(1)

communities = cluster(G)
cohesion = score_all(G, communities)
tokens = {'input': extraction.get('input_tokens', 0), 'output': extraction.get('output_tokens', 0)}
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: 'Community ' + str(cid) for cid in communities}
questions = suggest_questions(G, communities, labels)

wrote = to_json(G, communities, 'soc_gem_graph/graphify-out/graph.json')
report = generate(G, communities, cohesion, labels, gods, surprises, detection, tokens, 'soc_gem_graph', suggested_questions=questions)
Path('soc_gem_graph/graphify-out/GRAPH_REPORT.md').write_text(report, encoding="utf-8")

analysis = {
    'communities': {str(k): v for k, v in communities.items()},
    'cohesion': {str(k): v for k, v in cohesion.items()},
    'gods': gods,
    'surprises': surprises,
    'questions': questions,
}
Path('soc_gem_graph/graphify-out/.graphify_analysis.json').write_text(json.dumps(analysis, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Graph built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
