"""
Day 2 - RAG Ingestion Pipeline
Chunks the synthetic policy documents, embeds them with a free local
embedding model, and stores them in a persistent ChromaDB collection.

Run:
    python src/rag_ingest.py

Requires: pip install sentence-transformers chromadb
(sentence-transformers will download the 'all-MiniLM-L6-v2' model the first
time you run this — needs an internet connection, ~80MB, one-time.)

Note: this uses a small custom chunker instead of LangChain's text splitter.
LangChain's API has churned a lot across versions (text_splitter moved to a
separate package, then moved again) — a ~20-line custom splitter is more
reliable here and easier to explain than tracking a moving dependency.
"""

from pathlib import Path
import re
import chromadb
from chromadb.utils import embedding_functions

POLICIES_DIR = Path(__file__).parent.parent / "data" / "policies"
CHROMA_DIR = Path(__file__).parent.parent / "db" / "chroma"
COLLECTION_NAME = "hospital_policies"

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"  # free, local, ~80MB, good quality for this size of corpus

CHUNK_SIZE = 400       # characters
CHUNK_OVERLAP = 80     # characters, preserves context across chunk boundaries


def load_documents():
    """Read every .txt policy file into (filename, text) pairs."""
    docs = []
    for path in sorted(POLICIES_DIR.glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        docs.append((path.stem, text))
    return docs


def split_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    """
    Sentence-aware sliding-window chunker.
    Splits on sentence boundaries first, then packs sentences into windows of
    ~chunk_size characters, carrying `overlap` characters of context into the
    next chunk so a fact split across a boundary isn't lost.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= chunk_size:
            current = f"{current} {sentence}".strip()
        else:
            if current:
                chunks.append(current)
            # start new chunk, carrying trailing overlap from previous chunk
            tail = current[-overlap:] if current else ""
            current = f"{tail} {sentence}".strip()

    if current:
        chunks.append(current)

    return chunks


def chunk_documents(docs):
    """Split each document into overlapping chunks, keeping track of source."""
    chunks, metadatas, ids = [], [], []
    for doc_name, text in docs:
        pieces = split_text(text)
        for i, piece in enumerate(pieces):
            chunks.append(piece)
            metadatas.append({"source": doc_name, "chunk_index": i})
            ids.append(f"{doc_name}_{i}")
    return chunks, metadatas, ids


def build_vector_store(chunks, metadatas, ids):
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL_NAME
    )

    # Fresh collection every run, so re-running this script is safe/idempotent
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=embed_fn,
        metadata={"hnsw:space": "cosine"},
    )

    # Batch add (Chroma handles embedding internally via embed_fn)
    collection.add(documents=chunks, metadatas=metadatas, ids=ids)
    return collection


if __name__ == "__main__":
    print(f"Loading policy documents from {POLICIES_DIR} ...")
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    chunks, metadatas, ids = chunk_documents(docs)
    print(f"Split into {len(chunks)} chunks (size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})")

    collection = build_vector_store(chunks, metadatas, ids)
    print(f"\nStored {collection.count()} chunks in ChromaDB collection "
          f"'{COLLECTION_NAME}' at {CHROMA_DIR}")
