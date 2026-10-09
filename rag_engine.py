import os
import re
import math
from collections import Counter

class BM25Retriever:
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.doc_freqs = []
        self.idf = {}
        self.doc_len = []
        self.avgdl = 0
        self.corpus = []
        self.doc_names = []
        
    def _tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())
        
    def fit(self, corpus, doc_names):
        self.corpus = corpus
        self.doc_names = doc_names
        nd = len(corpus)
        num_doc = 0
        
        frequencies = {}
        for document in corpus:
            tokens = self._tokenize(document)
            self.doc_len.append(len(tokens))
            num_doc += len(tokens)
            
            frequencies_in_doc = Counter(tokens)
            self.doc_freqs.append(frequencies_in_doc)
            
            for word in frequencies_in_doc:
                frequencies[word] = frequencies.get(word, 0) + 1
                
        self.avgdl = num_doc / nd if nd > 0 else 0
        
        for word, freq in frequencies.items():
            # Standard BM25 IDF formulation
            self.idf[word] = math.log(1 + (nd - freq + 0.5) / (freq + 0.5))
            
    def _score(self, query, index):
        score = 0.0
        doc_len = self.doc_len[index]
        doc_freqs = self.doc_freqs[index]
        
        for word in query:
            if word not in doc_freqs:
                continue
            freq = doc_freqs[word]
            numerator = self.idf[word] * freq * (self.k1 + 1)
            denominator = freq + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
            score += numerator / denominator
        return score
        
    def search(self, query_string, top_k=3):
        if not self.corpus:
            return []
            
        query_tokens = self._tokenize(query_string)
        scores = [(self._score(query_tokens, i), i) for i in range(len(self.corpus))]
        scores.sort(reverse=True)
        
        results = []
        for score, idx in scores[:top_k]:
            if score > 0:
                results.append({
                    "score": score,
                    "doc_name": self.doc_names[idx],
                    "content": self.corpus[idx]
                })
        return results

class LocalRAG:
    """Manages the indexing and searching of Markdown_Output docs."""
    def __init__(self, docs_dir="Markdown_Output"):
        self.docs_dir = docs_dir
        self.retriever = BM25Retriever()
        self.indexed = False
        
    def build_index(self):
        print(f"[RAG] Building local index from {self.docs_dir}...")
        corpus = []
        doc_names = []
        
        if not os.path.exists(self.docs_dir):
            print(f"[RAG] Warning: directory {self.docs_dir} not found.")
            return
            
        for filename in os.listdir(self.docs_dir):
            if filename.endswith(".md"):
                filepath = os.path.join(self.docs_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        text = f.read()
                        
                    # Split huge files into smaller chunks of approx 500 words to improve retrieval focus
                    paragraphs = text.split('\n\n')
                    current_chunk = []
                    current_len = 0
                    for p in paragraphs:
                        current_chunk.append(p)
                        current_len += len(p.split())
                        if current_len > 300:
                            chunk_text = "\n\n".join(current_chunk)
                            corpus.append(chunk_text)
                            doc_names.append(filename)
                            current_chunk = []
                            current_len = 0
                            
                    if current_chunk:
                        chunk_text = "\n\n".join(current_chunk)
                        corpus.append(chunk_text)
                        doc_names.append(filename)
                except Exception as e:
                    print(f"[RAG] Error reading {filename}: {e}")
                    
        self.retriever.fit(corpus, doc_names)
        self.indexed = True
        print(f"[RAG] Index built successfully with {len(corpus)} document chunks.")

    def query(self, query_string, top_k=3):
        if not self.indexed:
            self.build_index()
        return self.retriever.search(query_string, top_k=top_k)

# Global RAG instance (Lazy loaded)
_rag_instance = None

def get_rag():
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = LocalRAG()
        _rag_instance.build_index()
    return _rag_instance

if __name__ == "__main__":
    rag = get_rag()
    res = rag.query("Suspicious PowerShell Script", top_k=2)
    for r in res:
        print(f"--- MATCH (Score: {r['score']:.2f}) from {r['doc_name']} ---")
        print(r['content'][:200] + "...")
