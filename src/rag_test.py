"""
Day 2 - Test retrieval quality against the ingested policy documents.
Run this AFTER src/rag_ingest.py has successfully built the Chroma collection.

Run:
    python src/rag_test.py
"""

from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions

CHROMA_DIR = Path(__file__).parent.parent / "db" / "chroma"
COLLECTION_NAME = "hospital_policies"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Sample questions covering a spread of the 15 policy documents.
# Reuse this list on Day 4 to evaluate the RAG Agent's generated answers.
TEST_QUESTIONS = [
    "What are the visiting hours for the ICU?",
    "How do I file a complaint about my care?",
    "What insurance providers does the hospital directly bill?",
    "What is the RACE protocol for fires?",
    "How long after discharge is a summary sent to my primary care doctor?",
    "Can a patient withdraw consent during a procedure?",
    "What happens if I miss a scheduled admission with less than 24 hours notice?",
    "What PPE is required for droplet precautions?",
    "Who can access my medical records?",
    "What is Code Silver?",
]


def main():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL_NAME
    )
    collection = client.get_collection(COLLECTION_NAME, embedding_function=embed_fn)
    print(f"Loaded collection with {collection.count()} chunks\n")

    for q in TEST_QUESTIONS:
        print(f"Q: {q}")
        results = collection.query(query_texts=[q], n_results=3)
        for doc, meta, dist in zip(
            results["documents"][0], results["metadatas"][0], results["distances"][0]
        ):
            print(f"   [{meta['source']} #{meta['chunk_index']}] (distance={dist:.3f})")
            print(f"   {doc[:150].replace(chr(10), ' ')}...")
        print()


if __name__ == "__main__":
    main()
