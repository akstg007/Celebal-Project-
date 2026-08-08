# AI-Powered Multi-Agent Hospital Query System

An Orchestrator Agent classifies plain-English hospital staff queries and routes them to
either an **NLP-to-SQL Agent** (structured patient data) or a **RAG Agent** (hospital policy
documents), so structured and unstructured hospital knowledge is accessible through one
conversational interface.

## Architecture

```
                    ┌───────────────────┐
   User Question -> │  Orchestrator      │
                    │  Agent (router)    │
                    └─────────┬─────────┘
                   ┌───────────┴────────────┐
                   ▼                        ▼
        ┌─────────────────────┐   ┌────────────────────┐
        │  NLP-to-SQL Agent    │   │   RAG Agent         │
        │  -> SQLite DB        │   │  -> Chroma Vector DB│
        │  (patient records)   │   │  (policy documents) │
        └─────────────────────┘   └────────────────────┘
                   │                        │
                   └───────────┬────────────┘
                                ▼
                       Natural-language answer
                        (shown in Streamlit UI)
```


## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Get a **free** Groq API key at https://console.groq.com/keys (used from Day 3 onward),
then create a `.env` file (see `.env.example`).



```bash
# Cleans the CSV and (re)builds db/hospital.db
python src/data_prep.py

# Runs 10 hand-written test queries against the DB to confirm everything works
python src/sample_queries.py
```



```bash
# Regenerate the 15 synthetic policy .txt files (already included, but reproducible)
python src/generate_policies.py

# Chunk + embed + store policy docs in ChromaDB
# (downloads the embedding model on first run — needs internet, ~80MB, one-time)
python src/rag_ingest.py

# Test retrieval quality with 10 sample policy questions
python src/rag_test.py
```

## Project structure

```
hospital-agent-project/
├── data/
│   ├── healthcare_dataset.csv     # raw Kaggle data
│   └── policies/                  # 15 synthetic hospital policy .txt files
├── db/
│   ├── hospital.db                # cleaned data, built by data_prep.py
│   └── chroma/                    # persistent vector store, built by rag_ingest.py
├── src/
│   ├── data_prep.py               # Day 1: clean CSV -> SQLite
│   ├── sample_queries.py          # Day 1: ground-truth SQL test queries
│   ├── schema_reference.md        # Day 1: schema doc for later prompting
│   ├── generate_policies.py       # Day 2: writes the 15 policy documents
│   ├── rag_ingest.py              # Day 2: chunk -> embed -> store in ChromaDB
│   └── rag_test.py                # Day 2: ground-truth retrieval test questions
├── notebooks/                     # exploratory notebooks (optional)
├── requirements.txt
└── README.md
```

## Roadmap

| Day | Milestone |
|-----|-----------|
| 1   | Data cleaning + SQLite DB ✅ |
| 2   | Synthetic policy docs + RAG ingestion ✅ |
| 3   | NLP-to-SQL Agent |
| 4   | RAG Agent |
| 5   | Orchestrator Agent + LangGraph integration |
| 6   | Streamlit UI + testing |
| 7   | Polish, docs, deploy, demo prep |
