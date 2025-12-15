# Advanced RAG Techniques

A hands-on tutorial demonstrating progressive Retrieval-Augmented Generation (RAG) techniques using real-world MSME data from Nigeria.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API key:**
   - Create `.env` file in project root
   - Add: `OPENAI_API_KEY=your_key_here`

3. **Run notebooks in order:**
   - Start with `Technique_0_Setup_Baseline.ipynb`
   - Progress through Techniques 1-5
   - Evaluate with `RAG_Evaluation_RAGAS.ipynb`

## Techniques Overview

| Technique | Description | Difficulty |
|-----------|-------------|------------|
| **Technique 0: Baseline** | Standard semantic search | ⭐⭐☆☆☆ |
| **Technique 1: Multiple Query** | Generate query variations | ⭐⭐⭐☆☆ |
| **Technique 2: Contextual Compression** | Filter irrelevant content | ⭐⭐⭐☆☆ |
| **Technique 3: Semantic Chunking** | Smart document splitting | ⭐⭐⭐⭐☆ |
| **Technique 4: Reranking** | Two-stage retrieval with cross-encoders | ⭐⭐⭐⭐☆ |
| **Technique 5: HyDE** | Hypothetical Document Embeddings | ⭐⭐⭐⭐☆ |
| **RAGAS Evaluation** | Performance measurement | ⭐⭐⭐☆☆ |

## Project Structure

```
Rag_Techniques/
├── msme.csv                              # Knowledge base (14 docs)
├── utils_openai.py                       # Shared utilities
├── Technique_0_Setup_Baseline.ipynb     # Start here
├── Technique_1-5 notebooks               # Advanced techniques
├── RAG_Evaluation_RAGAS.ipynb           # Evaluation
└── .env                                  # Your API key
```

## Dataset

**msme.csv** - 14 documents about Nigerian MSMEs covering business registration, financing, challenges, and government programs.

## Tech Stack

- **LangChain** - RAG framework
- **ChromaDB** - Vector database
- **OpenAI** - Embeddings (text-embedding-3-small) & LLM (gpt-4o-mini)
- **RAGAS** - Evaluation metrics

## Sample Queries

- "What are the financing options for MSMEs in Nigeria?"
- "How do I register a business in Nigeria?"
- "What challenges do MSMEs face?"

## Troubleshooting

- **API errors:** Check `.env` file and OpenAI credits
- **Import errors:** Run `pip install -r requirements.txt`
- **ChromaDB issues:** Delete `./chroma_db_*` folders to rebuild

