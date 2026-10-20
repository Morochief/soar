import os
import re
import math
import pickle
import hashlib
from pathlib import Path
from collections import Counter
from typing import List, Dict, Any, Optional, Tuple

STOPWORDS = frozenset({
    # Español
    "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al",
    "a", "en", "con", "por", "para", "sin", "sobre", "entre", "hacia", "hasta",
    "desde", "que", "y", "e", "o", "u", "ni", "pero", "sino", "como", "cuando",
    "donde", "quien", "cual", "este", "esta", "estos", "estas", "ese", "esa",
    "esos", "esas", "aquel", "aquella", "su", "sus", "mi", "mis", "tu", "tus",
    "se", "lo", "le", "les", "me", "te", "nos", "es", "son", "fue", "era",
    "ser", "estar", "ha", "han", "hay", "mas", "muy", "ya", "no", "si", "todo",
    # Inglés
    "the", "a", "an", "of", "to", "in", "on", "at", "by", "for", "with",
    "from", "into", "about", "as", "is", "are", "was", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would", "can",
    "could", "should", "may", "might", "must", "and", "or", "but", "if", "then",
    "else", "when", "where", "which", "who", "whom", "this", "that", "these",
    "those", "it", "its", "their", "they", "them", "we", "us", "you", "your",
    "not", "no", "yes", "all", "any", "some", "such", "than", "too", "very",
})

# Pesos de prioridad según la capa de conocimiento del SOC
CATEGORY_WEIGHTS: Dict[str, float] = {
    "MEMORIA_SOC": 1.65,         # SOC_GEM_v2, plantillas_cierre, stellar_alerts, SMB_Rosetta_Stone
    "CASO_HISTORICO": 1.50,      # Analista SOC/Casos/* y Bitacora_Personal_Casos_SOC.md
    "PLAYBOOK": 1.45,            # 00_Playbooks y playbooks específicos
    "PROCEDIMIENTO_ARQ": 1.30,   # Procedimientos, Security Onion, Arquitectura, Filtros, Reportes
    "SKILL_SOC": 1.25,           # Las 60 Skills operativas de SKILLS_SOC
    "DOC_STELLAR": 1.00,         # Documentación oficial de Stellar Cyber (Markdown_Output)
    "ACADEMIA_SOC": 0.90,        # Google SecOps & Google Cybersecurity Certification
}

EXCLUDED_PATH_PARTS = (
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "markitdown",
    "graphify",
    "graphify-out",
    "obscura",
    "SKILLS_PROYECTO_SOC",  # espejo idéntico de SKILLS_SOC
    ".agents",              # copia de ECC
)


def classify_markdown_path(rel_path: str) -> str:
    """Clasifica cualquier archivo .md del repositorio en una de las 7 capas del SOC."""
    norm = rel_path.replace("\\", "/")
    norm_low = norm.lower()

    if norm_low.startswith("00_playbooks/") or "playbook" in os.path.basename(norm_low):
        return "PLAYBOOK"
    if norm_low.startswith("skills_soc/") or norm_low.startswith(".agent/skills/"):
        return "SKILL_SOC"
    if "analista soc/casos/" in norm_low or "bitacora" in os.path.basename(norm_low):
        return "CASO_HISTORICO"
    if "02_base_de_conocimiento" in norm_low or "soc_gem" in norm_low or "indice_maestro" in norm_low:
        return "MEMORIA_SOC"
    if any(k in norm_low for k in (
        "03_arquitectura_y_despliegue",
        "procedimientos",
        "security_onion",
        "stellar documentacion",
        "auditoria_cuota_stellar",
        "reportes",
        "investigacion",
        "novedades",
        "01_operacion_diaria_soc",
    )):
        return "PROCEDIMIENTO_ARQ"
    if "google cybersecurity" in norm_low or "google secops" in norm_low:
        return "ACADEMIA_SOC"
    if norm_low.startswith("markdown_output/"):
        return "DOC_STELLAR"
    return "MEMORIA_SOC"


class BM25Retriever:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.doc_freqs: List[Counter] = []
        self.idf: Dict[str, float] = {}
        self.doc_len: List[int] = []
        self.avgdl: float = 0.0
        self.corpus: List[str] = []
        self.doc_names: List[str] = []
        self.doc_categories: List[str] = []
        self.doc_paths: List[str] = []

    def _tokenize(self, text: str) -> List[str]:
        tokens = re.findall(r"\b\w+\b", text.lower())
        filtered = [t for t in tokens if len(t) > 1 and t not in STOPWORDS]
        return filtered if filtered else tokens

    def fit(
        self,
        corpus: List[str],
        doc_names: List[str],
        doc_categories: Optional[List[str]] = None,
        doc_paths: Optional[List[str]] = None,
    ) -> None:
        self.corpus = corpus
        self.doc_names = doc_names
        self.doc_categories = doc_categories or ["DOC_STELLAR"] * len(corpus)
        self.doc_paths = doc_paths or list(doc_names)
        self.doc_freqs = []
        self.doc_len = []
        self.idf = {}
        nd = len(corpus)
        num_doc = 0

        frequencies: Dict[str, int] = {}
        for document in corpus:
            tokens = self._tokenize(document)
            self.doc_len.append(len(tokens))
            num_doc += len(tokens)

            frequencies_in_doc = Counter(tokens)
            self.doc_freqs.append(frequencies_in_doc)

            for word in frequencies_in_doc:
                frequencies[word] = frequencies.get(word, 0) + 1

        self.avgdl = num_doc / nd if nd > 0 else 0.0

        for word, freq in frequencies.items():
            self.idf[word] = math.log(1 + (nd - freq + 0.5) / (freq + 0.5))

    def _score(self, query: List[str], index: int, boost_categories: bool = True) -> float:
        score = 0.0
        doc_len = self.doc_len[index]
        doc_freqs = self.doc_freqs[index]
        if self.avgdl == 0:
            return 0.0

        for word in query:
            if word not in doc_freqs:
                continue
            freq = doc_freqs[word]
            numerator = self.idf[word] * freq * (self.k1 + 1)
            denominator = freq + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
            score += numerator / denominator

        if boost_categories and score > 0 and index < len(self.doc_categories):
            cat = self.doc_categories[index]
            score *= CATEGORY_WEIGHTS.get(cat, 1.0)
        return score

    def search(
        self,
        query_string: str,
        top_k: int = 5,
        category_filter: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        if not self.corpus:
            return []

        query_tokens = self._tokenize(query_string)
        cat_norm = category_filter.strip().upper() if category_filter else None

        scores: List[Tuple[float, int]] = []
        for i in range(len(self.corpus)):
            if cat_norm and self.doc_categories[i] != cat_norm:
                continue
            s = self._score(query_tokens, i)
            if s > 0:
                scores.append((s, i))

        scores.sort(reverse=True)

        results = []
        for score, idx in scores[:top_k]:
            results.append({
                "score": round(score, 2),
                "category": self.doc_categories[idx],
                "doc_name": self.doc_names[idx],
                "rel_path": self.doc_paths[idx],
                "content": self.corpus[idx],
            })
        return results


class LocalRAG:
    """
    Motor de Memoria Unificada del SOC Technoma.
    Indexa el 100% de los Markdowns propios del SOC en 7 categorías:
      - MEMORIA_SOC
      - CASO_HISTORICO
      - PLAYBOOK
      - PROCEDIMIENTO_ARQ
      - SKILL_SOC
      - DOC_STELLAR
      - ACADEMIA_SOC
    Guarda el índice en disco (.rag_index_cache.pkl) para consultas en <15ms.
    """

    CACHE_VERSION = "v3_full_soc_brain_7_layers"
    MAX_FILE_BYTES = 1_500_000  # Ignorar volcados crudos >1.5MB como cve_reporte_completo de 9.4MB

    def __init__(self, docs_dir: str = "Markdown_Output", extra_dirs: Optional[List[str]] = None):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.docs_dir = docs_dir if os.path.isabs(docs_dir) else os.path.join(self.base_dir, docs_dir)
        self.cache_path = os.path.join(self.base_dir, ".rag_index_cache.pkl")
        self.catalog_path = os.path.join(self.base_dir, "CATALOGO_COMPLETO_MARKDOWNS_SOC.md")
        self.retriever = BM25Retriever()
        self.file_inventory: List[Dict[str, Any]] = []
        self.indexed = False

    def _iter_soc_markdown_files(self) -> List[Tuple[str, str, str]]:
        """
        Devuelve lista de (abs_path, rel_path, category) para todos los .md propios del SOC.
        Deduplica automáticamente archivos de documentación Stellar clonados con sufijos 1/2/3.
        """
        results: List[Tuple[str, str, str]] = []
        seen_sizes_in_markdown_output: set = set()

        for root, dirs, files in os.walk(self.base_dir):
            # Filtrar directorios de librerías externas en el propio walk
            dirs[:] = [
                d for d in dirs
                if d not in EXCLUDED_PATH_PARTS
                and not d.startswith(".git")
                and d != "ECC"
            ]
            for fname in sorted(files):
                if not fname.lower().endswith(".md"):
                    continue
                if fname == "CATALOGO_COMPLETO_MARKDOWNS_SOC.md":
                    continue
                fpath = os.path.join(root, fname)
                rel_path = os.path.relpath(fpath, self.base_dir).replace("\\", "/")
                if any(part in rel_path.split("/") for part in EXCLUDED_PATH_PARTS):
                    continue
                if "/ECC/" in f"/{rel_path}/":
                    continue

                try:
                    st = os.stat(fpath)
                except OSError:
                    continue

                if st.st_size == 0 or st.st_size > self.MAX_FILE_BYTES:
                    continue

                # En Markdown_Output hay copias exactas (ej. Understanding Cases1.md, Cases2.md)
                if rel_path.startswith("Markdown_Output/"):
                    stem_base = re.sub(r"[0-9j]+\.md$", ".md", fname)
                    dedup_key = (stem_base.lower(), st.st_size)
                    if dedup_key in seen_sizes_in_markdown_output:
                        continue
                    seen_sizes_in_markdown_output.add(dedup_key)

                category = classify_markdown_path(rel_path)
                results.append((fpath, rel_path, category))
        return results

    def _compute_corpus_signature(self, files_list: List[Tuple[str, str, str]]) -> str:
        h = hashlib.sha256()
        h.update(self.CACHE_VERSION.encode("utf-8"))
        for fpath, rel_path, cat in files_list:
            try:
                st = os.stat(fpath)
                h.update(f"{rel_path}:{cat}:{st.st_size}:{int(st.st_mtime)}|".encode("utf-8"))
            except OSError:
                pass
        return h.hexdigest()

    def build_index(self, force_rebuild: bool = False) -> None:
        files_list = self._iter_soc_markdown_files()
        signature = self._compute_corpus_signature(files_list)

        if not force_rebuild and os.path.exists(self.cache_path):
            try:
                with open(self.cache_path, "rb") as f:
                    cached = pickle.load(f)
                if isinstance(cached, dict) and cached.get("signature") == signature:
                    self.retriever = cached["retriever"]
                    self.file_inventory = cached.get("file_inventory", [])
                    self.indexed = True
                    return
            except Exception:
                pass

        print(f"[RAG] Construyendo Cerebro Unificado del SOC ({len(files_list)} archivos Markdown en 7 capas)...")
        corpus: List[str] = []
        doc_names: List[str] = []
        doc_categories: List[str] = []
        doc_paths: List[str] = []
        inventory: List[Dict[str, Any]] = []

        for fpath, rel_path, category in files_list:
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()

                # Extraer primera línea con título o resumen para el inventario
                first_heading = ""
                for line in text.splitlines()[:25]:
                    s = line.strip().lstrip("#").strip()
                    if len(s) >= 5 and not s.startswith("---"):
                        first_heading = s[:110]
                        break

                inventory.append({
                    "rel_path": rel_path,
                    "category": category,
                    "size_bytes": os.path.getsize(fpath),
                    "summary": first_heading or os.path.basename(rel_path),
                })

                display_name = f"[{category}] {rel_path}"
                paragraphs = text.split("\n\n")
                current_chunk: List[str] = []
                current_len = 0
                for p in paragraphs:
                    current_chunk.append(p)
                    current_len += len(p.split())
                    if current_len > 280:
                        chunk_text = f"Fuente: {rel_path} ({category})\n\n" + "\n\n".join(current_chunk)
                        corpus.append(chunk_text)
                        doc_names.append(display_name)
                        doc_categories.append(category)
                        doc_paths.append(rel_path)
                        current_chunk = []
                        current_len = 0

                if current_chunk:
                    chunk_text = f"Fuente: {rel_path} ({category})\n\n" + "\n\n".join(current_chunk)
                    corpus.append(chunk_text)
                    doc_names.append(display_name)
                    doc_categories.append(category)
                    doc_paths.append(rel_path)
            except Exception as e:
                print(f"[RAG] Error leyendo {rel_path}: {e}")

        self.retriever.fit(corpus, doc_names, doc_categories=doc_categories, doc_paths=doc_paths)
        self.file_inventory = inventory
        self.indexed = True
        print(f"[RAG] Cerebro SOC indexado: {len(inventory)} archivos -> {len(corpus)} bloques de memoria activa.")

        try:
            with open(self.cache_path, "wb") as f:
                pickle.dump({
                    "signature": signature,
                    "retriever": self.retriever,
                    "file_inventory": self.file_inventory,
                }, f)
        except Exception as e:
            print(f"[RAG] Advertencia: no se pudo guardar caché en disco: {e}")

    def query(
        self,
        query_string: str,
        top_k: int = 4,
        category: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        if not self.indexed:
            self.build_index()
        return self.retriever.search(query_string, top_k=top_k, category_filter=category)

    def query_multi_layer(self, query_string: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Consulta simultáneamente las capas operativas clave para un caso del SOC:
          - MEMORIA_SOC (SOC_GEM_v2, falsos positivos, plantillas de cierre)
          - CASO_HISTORICO (Casos previos resueltos por Kevin Moraes)
          - PLAYBOOK (Playbooks maestros y específicos)
          - PROCEDIMIENTO_ARQ (Guías de filtros, arquitectura, Security Onion, procedimientos)
          - DOC_STELLAR (Reglas oficiales de Stellar Cyber)
        """
        if not self.indexed:
            self.build_index()
        return {
            "MEMORIA_SOC": self.retriever.search(query_string, top_k=2, category_filter="MEMORIA_SOC"),
            "CASO_HISTORICO": self.retriever.search(query_string, top_k=2, category_filter="CASO_HISTORICO"),
            "PLAYBOOK": self.retriever.search(query_string, top_k=2, category_filter="PLAYBOOK"),
            "PROCEDIMIENTO_ARQ": self.retriever.search(query_string, top_k=2, category_filter="PROCEDIMIENTO_ARQ"),
            "SKILL_SOC": self.retriever.search(query_string, top_k=2, category_filter="SKILL_SOC"),
            "DOC_STELLAR": self.retriever.search(query_string, top_k=2, category_filter="DOC_STELLAR"),
        }

    def export_master_catalog_markdown(self) -> str:
        """Genera un archivo Markdown con el catálogo clasificado de todos los Markdowns del SOC."""
        if not self.indexed:
            self.build_index()

        by_cat: Dict[str, List[Dict[str, Any]]] = {}
        for item in self.file_inventory:
            by_cat.setdefault(item["category"], []).append(item)

        lines = [
            "# 🧠 CATÁLOGO UNIFICADO DE MEMORIA Y MARKDOWNS — TECHNOMA SOC",
            "",
            f"- **Total de documentos indexados en memoria activa:** `{len(self.file_inventory)}` archivos (divididos en `{len(self.retriever.corpus)}` bloques BM25 en `.rag_index_cache.pkl`).",
            "- **Tiempo de consulta en RAM/Disco:** `< 15 ms` (0 tokens consumidos al buscar).",
            "",
            "## Resumen por Capa de Conocimiento",
            "",
            "| Capa / Categoría | Archivos | Peso de Prioridad | Propósito en el SOAR |",
            "| :--- | :---: | :---: | :--- |",
        ]
        descriptions = {
            "MEMORIA_SOC": "Fuente de la verdad (`SOC_GEM_v2.md`, `plantillas_cierre_soc.md`, `stellar_alerts.md`, `SMB_Rosetta_Stone.md`, inventarios AD/Red)",
            "CASO_HISTORICO": "Los +35 casos reales ya investigados en `Analista SOC/Casos/` + `Bitacora_Personal_Casos_SOC.md`",
            "PLAYBOOK": "Catálogo maestro de 28 playbooks IR (`00_Playbooks/`) y playbooks específicos de remediación",
            "PROCEDIMIENTO_ARQ": "Guías de filtros Lucene/Pre-DPI, Security Onion 3, sensores NDR, ZeroTier, informes y procedimientos",
            "SKILL_SOC": "Las 60 Skills operativas y técnicas del SOC (`SKILLS_SOC/` y `.agent/skills/`)",
            "DOC_STELLAR": "Manuales oficiales de reglas y conectores de Stellar Cyber (`Markdown_Output/`)",
            "ACADEMIA_SOC": "Apuntes y laboratorios de Google SecOps y Google Cybersecurity Certification",
        }
        for cat in ["MEMORIA_SOC", "CASO_HISTORICO", "PLAYBOOK", "PROCEDIMIENTO_ARQ", "SKILL_SOC", "ACADEMIA_SOC", "DOC_STELLAR"]:
            items = by_cat.get(cat, [])
            w = CATEGORY_WEIGHTS.get(cat, 1.0)
            lines.append(f"| **`{cat}`** | {len(items)} | `{w}x` | {descriptions.get(cat, '')} |")

        for cat in ["MEMORIA_SOC", "CASO_HISTORICO", "PLAYBOOK", "PROCEDIMIENTO_ARQ", "SKILL_SOC", "ACADEMIA_SOC"]:
            items = by_cat.get(cat, [])
            if not items:
                continue
            lines.append(f"\n---\n\n## 📂 Capa `{cat}` ({len(items)} documentos)\n")
            lines.append("| Archivo | Tamaño | Función / Título Detectado |")
            lines.append("| :--- | :---: | :--- |")
            for it in items:
                kb = f"{it['size_bytes'] / 1024:.1f} KB"
                summary_clean = it["summary"].replace("|", "/")
                lines.append(f"| `{it['rel_path']}` | {kb} | {summary_clean} |")

        doc_stellar_items = by_cat.get("DOC_STELLAR", [])
        lines.append(f"\n---\n\n## 📘 Capa `DOC_STELLAR` ({len(doc_stellar_items)} manuales únicos de Stellar Cyber en `Markdown_Output/`)\n")
        lines.append("> Todos los manuales de reglas, conectores y arquitectura de Stellar Cyber están indexados y deduplicados en `.rag_index_cache.pkl`.")

        content = "\n".join(lines) + "\n"
        with open(self.catalog_path, "w", encoding="utf-8") as f:
            f.write(content)
        return self.catalog_path


    def instant_case_context(self, raw_case_or_text: str) -> str:
        """
        Extrae entidades locales (AD, IPs, hosts) + consulta en paralelo las 6 capas
        del Cerebro SOC en <20ms para entregar un paquete de memoria listo para el triaje.
        """
        if not self.indexed:
            self.build_index()

        # 1. Extraer palabras clave representativas del caso/JSON
        keywords: List[str] = []
        for pattern in [
            r'"event_name"\s*:\s*"([^"]+)"',
            r'"name"\s*:\s*"([^"]+)"',
            r'"msg_class"\s*:\s*"([^"]+)"',
            r'"title"\s*:\s*"([^"]+)"',
            r'\b(?:[a-zA-Z0-9-]+\.)+(?:local|com|py|net|org)\b',
            r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            r'\b(?:CJPPA\w*|nb-[\w-]+|srv-[\w-]+|HealthMailbox\w*)\b',
        ]:
            matches = re.findall(pattern, raw_case_or_text, re.IGNORECASE)
            for m in matches[:6]:
                if isinstance(m, str) and m not in keywords:
                    keywords.append(m)

        query_str = " ".join(keywords) if keywords else raw_case_or_text[:350]
        layers = self.query_multi_layer(query_str)

        out_blocks: List[str] = [
            "==========================================================================",
            f"🧠 PAQUETE DE MEMORIA INSTANTÁNEA SOC (Query: {query_str[:120]})",
            "==========================================================================",
        ]

        # Incluir auto-enriquecimiento de AD/Activos de soc_agent si está disponible
        try:
            from soc_agent import auto_enriquecer_contexto
            local_ev = auto_enriquecer_contexto(raw_case_or_text)
            if local_ev:
                out_blocks.append("\n### 1. ACTIVOS Y USUARIOS VERIFICADOS EN INVENTARIO LOCAL (0-LATENCY):")
                out_blocks.append(local_ev)
        except Exception:
            pass

        section_titles = {
            "MEMORIA_SOC": "### 2. MEMORIA INSTITUCIONAL Y PLANTILLAS (`SOC_GEM_v2` / `plantillas_cierre_soc`)",
            "CASO_HISTORICO": "### 3. CASOS HISTÓRICOS SIMILARES RESUELTOS EN TECHNOMA (`Analista SOC/Casos/`)",
            "PLAYBOOK": "### 4. PLAYBOOK OFICIAL ASIGNADO (`00_Playbooks/`)",
            "PROCEDIMIENTO_ARQ": "### 5. PROCEDIMIENTOS, ARQUITECTURA Y FILTROS LUCENE",
            "SKILL_SOC": "### 6. SKILLS OPERATIVAS APLICABLES (`SKILLS_SOC/`)",
            "DOC_STELLAR": "### 7. DOCUMENTACIÓN OFICIAL STELLAR CYBER (`Markdown_Output/`)",
        }

        for layer_key, header in section_titles.items():
            hits = layers.get(layer_key, [])
            if not hits:
                continue
            out_blocks.append(f"\n{header}")
            for h in hits:
                snippet = h["content"][:700].strip()
                out_blocks.append(f"- **[{h['rel_path']}] (Score: {h['score']}):**\n{snippet}\n")

        return "\n".join(out_blocks)


_rag_instance: Optional[LocalRAG] = None


def get_rag() -> LocalRAG:
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = LocalRAG()
        _rag_instance.build_index()
    return _rag_instance


if __name__ == "__main__":
    import time
    t0 = time.perf_counter()
    rag = get_rag()
    cat_file = rag.export_master_catalog_markdown()
    t1 = time.perf_counter()
    print(f"[RAG] Catálogo exportado en: {cat_file} ({(t1 - t0)*1000:.1f} ms)")
    layers = rag.query_multi_layer("DNS Tunneling wbx2 sati Internal Firewall Denial HealthMailbox")
    for layer_name, hits in layers.items():
        print(f"\n=== CAPA {layer_name} ===")
        for h in hits:
            print(f"  -> {h['rel_path']} (Score: {h['score']})")
