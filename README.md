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

## Project status

### Day 1 — complete
- [x] Project structure set up
- [x] Raw Kaggle `healthcare_dataset.csv` cleaned (deduped, name casing fixed, dates parsed,
      invalid rows dropped) → 54,860 usable rows
- [x] Loaded into local SQLite DB: `db/hospital.db`, table `patients`
- [x] Indexes added on commonly-filtered columns
- [x] 10 manual test queries validated against the DB (`src/sample_queries.py`) — this is
      the ground-truth set we'll use on Day 3 to evaluate the NLP-to-SQL agent
- [x] Schema reference written (`src/schema_reference.md`) — will be injected into the SQL
      agent's prompt later

### Day 2 — complete
- [x] 15 synthetic hospital policy documents written (`data/policies/*.txt`, ~3,400 words
      total) covering admission, discharge, billing, visiting hours, infection control,
      data privacy, emergency protocols, medication administration, room allocation,
      complaints, patient rights, fire safety, consent, non-discrimination, refunds
- [x] Custom sentence-aware chunker (`src/rag_ingest.py`) — 98 chunks, ~310 chars avg,
      80-char overlap between chunks
- [x] ChromaDB ingestion pipeline using local `all-MiniLM-L6-v2` embeddings (free, no API
      cost, runs on CPU)
- [x] Retrieval tested with 10 sample policy questions (`src/rag_test.py`) — this becomes
      the ground-truth set for evaluating the RAG Agent on Day 4

**Note:** `src/rag_ingest.py` and `src/rag_test.py` need one-time internet access to
download the embedding model (~80MB from Hugging Face) the first time you run them. After
that, everything runs fully offline/local — no API calls, no cost for the RAG side.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Get a **free** Groq API key at https://console.groq.com/keys (used from Day 3 onward),
then create a `.env` file (see `.env.example`).

## Run Day 1 scripts

```bash
# Cleans the CSV and (re)builds db/hospital.db
python src/data_prep.py

# Runs 10 hand-written test queries against the DB to confirm everything works
python src/sample_queries.py
```

## Run Day 2 scripts

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
