
# My Personal RAG Assistant

A Retrieval-Augmented Generation (RAG) system that answers questions about my **CV, projects, and professional background** using grounded document retrieval.

---

## Problem Solved
This **Personal RAG Assistant** allows me to query my **own career documents** and receive accurate, source-backed answers.

It helps with:
- Preparing for technical and behavioral interviews  
- Answering questions about my experience consistently  
- Exploring my skills, projects, and growth areas  
- Reducing hallucinations by grounding answers in personal documents  

---

## Documents Used
- **CV.pdf** – Professional experience, skills, education  
- **Projects.pdf** – Detailed AI, data science, and analytics projects  
- **Certificates.pdf** – Certifications and completed programs  
- **Notes.pdf** – Learning notes, career goals, and reflections  

**Why these documents?**  
They represent verified personal knowledge that the assistant relies on when answering questions.

---

## Tech Stack

| Component | Tool / Library |
|---------|---------------|
| Language Model | OpenAI / compatible LLM |
| Embeddings |  OpenAI Embeddings |
| Vector Database | Chroma |
| RAG Framework | LangChain |
| Document Loaders | PyPDFLoader, DirectoryLoader |
| Environment | Python, Jupyter Notebook |
| Configuration | `.env` for API keys |

---

## Architecture

The system follows a standard **Retrieval-Augmented Generation (RAG)** pipeline:

### 1. Document Ingestion
- PDFs and text documents are loaded from a local directory  
- Documents are split into smaller semantic chunks  

### 2. Embeddings
- Each chunk is converted into a dense vector representation  
- Embeddings capture semantic meaning rather than keywords  

### 3. Vector Database
- All embeddings are stored in a vector database  
- Similarity search retrieves the most relevant chunks for a query  

### 4. LLM (Large Language Model)
- Retrieved chunks are injected as context  
- The LLM generates answers grounded strictly in retrieved documents  
- Sources are returned for transparency  

### Architecture Flow

Documents
↓
Text Chunking
↓
Embeddings
↓
Vector Database
↓
Similarity Search
↓
LLM
↓
Answer + Sources
---

## How to Run
1. Clone the repository  
   ```bash
   git clone <repo-url>
   cd personal-rag-assistant

pip install -r requirements.txt
