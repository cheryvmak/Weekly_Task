# Simple RAG API Workshop

**Transform RAG from Notebook to Production API**

Learn to build a complete Retrieval-Augmented Generation (RAG) system with LangChain, ChromaDB, and OpenAI, then deploy it as a FastAPI application.

---

## What You'll Build

1. **Part 1:** Complete RAG system in a notebook
2. **Part 2:** Refactor into clean, modular Python classes
3. **Part 3:** Deploy as a production-ready API

---

## Prerequisites

- Python 3.8+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Basic Python knowledge
- Understanding of RAG concepts (optional but helpful)

---

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file:

```
OPENAI_API_KEY=your-key-here
```

### 3. Start Learning

**Option A: Full Workshop**

Open `Simple_RAG_API_Tutorial.ipynb` and follow along!

**Option B: Jump to Production**

```bash
# Build the index
python build_index.py

# Start the API
python api.py
```

Visit: http://localhost:8000/docs

---

## Workshop Structure

### Part 1: Learn RAG

**File:** `messy_rag_notebook.ipynb`

- Load and chunk documents
- Create embeddings with OpenAI
- Store in ChromaDB vector database
- Retrieve relevant chunks
- Generate answers with OpenAI GPT

### Part 2: Clean Code

**File:** `rag_core.py`

Three simple classes:

1. **DocumentProcessor** - Load & chunk documents
2. **VectorStoreManager** - Embeddings & retrieval
3. **RAGGenerator** - Answer generation

### Part 3: Production API

**Files:** `build_index.py`, `api.py`

- Build vector index
- FastAPI endpoints
- Auto-generated docs
- Ready to deploy

---

## File Structure

```
Simple_RAG_API_Workshop/
├── README.md                        # This file
├── requirements.txt                 # Dependencies
├── .env                            # API keys (create this)
│
├── Simple_RAG_API_Tutorial.ipynb   # Main workshop guide
├── messy_rag_notebook.ipynb        # Part 1: Learn RAG
│
├── rag_core.py                     # Part 2: Clean classes
├── build_index.py                  # Build the index
├── api.py                          # Part 3: FastAPI app
│
└── documents/                      # Sample documents
    ├── machine_learning.txt
    ├── python_basics.txt
    └── web_apis.txt
```

---

## API Endpoints

### POST /query
Ask a question, get an AI-generated answer

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is machine learning?"}'
```

### POST /search
Search for relevant documents (no generation)

```bash
curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are Python data types?", "top_k": 3}'
```

### GET /stats
Get index statistics

```bash
curl http://localhost:8000/stats
```

---

## Customization

### Change Chunk Size

Edit `rag_core.py`:

```python
doc_processor = DocumentProcessor(
    chunk_size=1000,  # Change this
    chunk_overlap=100
)
```

### Use Different Embedding Model

Edit `rag_core.py`:

```python
vectorstore_manager = VectorStoreManager(
    embedding_model="text-embedding-3-large"  # Change this
)
```

### Use GPT-4

Edit `rag_core.py`:

```python
rag_generator = RAGGenerator(
    vectorstore_manager,
    openai_model="gpt-4"  # Change this
)
```

---

## Troubleshooting

### "OPENAI_API_KEY not found"

Create a `.env` file with your API key:
```
OPENAI_API_KEY=sk-...
```

### "No vector store loaded"

Build the index first:
```bash
python build_index.py
```

### "Port 8000 already in use"

Use a different port:
```bash
uvicorn api:app --port 8001
```

---

## Dependencies

- **LangChain** - RAG orchestration
- **ChromaDB** - Vector database
- **OpenAI** - Embeddings & LLM
- **FastAPI** - API framework

---

## Next Steps

After completing the workshop:

1. Add your own documents
2. Experiment with different models
3. Add authentication to the API
4. Deploy to a cloud platform
5. Explore advanced RAG techniques

---

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## License

Educational use only.

---

**Happy Learning!** 🚀
