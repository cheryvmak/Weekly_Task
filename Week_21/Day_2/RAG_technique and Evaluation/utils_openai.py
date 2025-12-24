"""
Shared utilities for Advanced RAG Techniques - OpenAI Version
"""

import pandas as pd
from uuid import uuid4
import os
from dotenv import load_dotenv
from typing import Tuple, List, Dict

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate


# ============================================
# API SETUP
# ============================================

def setup_openai_api() -> str:
    """
    Load OpenAI API key from environment
    """
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. "
            "Please set it in your .env file or environment variables."
        )

    return api_key


# ===========================================
# DATA LOADING
# ===========================================

def load_msme_data(file_path: str = "msme.csv") -> Tuple[List[str], List[Dict], List[str]]:
    """
    Load and prepare MSME dataset for RAG
    """
    msme = pd.read_csv(file_path)

    documents = []
    metadatas = []
    ids = []

    for index, row in msme.iterrows():
        # Extract content and metadata
        text = str(row["Content"])
        title = str(row["Title"])
        source = str(row["Sources"])

        # Prepare document components
        documents.append(text)
        metadatas.append({
            "source": source,
            "doc_title": title,
            "doc_id": index
        })
        ids.append(f"{title}-{uuid4()}")

    print(f"[OK] Loaded {len(documents)} documents from {file_path}")
    return documents, metadatas, ids


def load_msme_as_langchain_docs(file_path: str = "msme.csv") -> List[Document]:
    """
    Load MSME data as LangChain Document objects
    """
    msme = pd.read_csv(file_path)
    documents = []

    for index, row in msme.iterrows():
        text = str(row["Content"])
        title = str(row["Title"])
        source = str(row["Sources"])

        doc = Document(
            page_content=text,
            metadata={
                "source": source,
                "doc_title": title,
                "doc_id": index
            }
        )
        documents.append(doc)

    print(f"[OK] Loaded {len(documents)} LangChain Documents from {file_path}")
    return documents


# ==============================================
# MODEL INITIALIZATION
# ==============================================

def create_embeddings(
    api_key: str,
    model: str = "text-embedding-3-small"
) -> OpenAIEmbeddings:
    """
    Initialize OpenAI embeddings model
    """
    embeddings = OpenAIEmbeddings(
        model=model,
        openai_api_key=api_key
    )
    print(f"[OK] Initialized embeddings: {model}")
    return embeddings


def create_llm(
    api_key: str,
    model: str = "gpt-4o-mini",
    temperature: float = 0
) -> ChatOpenAI:
    """
    Initialize OpenAI chat model
    """
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=api_key
    )
    print(f"[OK] Initialized LLM: {model} (temp={temperature})")
    return llm


# ==============================================
# VECTOR STORE
# ==============================================

def create_vectorstore(
    documents: List[str],
    metadatas: List[Dict],
    ids: List[str],
    embeddings: OpenAIEmbeddings,
    collection_name: str = "msme",
    persist_directory: str = "./chroma_db"
) -> Chroma:
    """
    Create and populate ChromaDB vector store
    Uses SQLite backend to avoid Rust bindings issues on Windows
    """
    import chromadb
    from chromadb.config import Settings

    # Force SQLite backend (bypasses Rust bindings)
    client = chromadb.PersistentClient(
        path=persist_directory,
        settings=Settings(allow_reset=True)
    )

    vectorstore = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embeddings
    )

    # Add documents
    vectorstore.add_texts(
        texts=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"[OK] Created vector store: {collection_name} ({len(documents)} docs)")
    return vectorstore


def load_existing_vectorstore(
    embeddings: OpenAIEmbeddings,
    collection_name: str = "msme",
    persist_directory: str = "./chroma_db"
) -> Chroma:
    """
    Load existing ChromaDB vector store
    Uses SQLite backend to avoid Rust bindings issues on Windows
    """
    import chromadb
    from chromadb.config import Settings

    # Force SQLite backend (bypasses Rust bindings)
    client = chromadb.PersistentClient(
        path=persist_directory,
        settings=Settings(allow_reset=True)
    )

    vectorstore = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embeddings
    )

    print(f"[OK] Loaded existing vector store: {collection_name}")
    return vectorstore


# =================================================
# PROMPTS
# =================================================

def get_baseline_prompt() -> ChatPromptTemplate:
    """
    Get the standard MSME consultant prompt template
    """
    template = """You are a business consultant providing insights on MSMEs in Nigeria.

Context: {context}

Question: {question}

Provide a clear, professional response in 3-5 sentences. Include relevant sources from the context if available.

Answer:"""

    return ChatPromptTemplate.from_template(template)


def get_detailed_prompt() -> ChatPromptTemplate:
    """
    Get a more detailed MSME consultant prompt template
    """
    template = """You are a business consultant providing insights on MSMEs in Nigeria.

You will be provided with context to answer the user's question.
The context includes information on understanding, starting, growing, and sustaining MSMEs, policies, and industry-specific details.

Context: {context}

Question: {question}

Instructions:
- Provide a comprehensive and professional response
- Use 3-5 sentences maximum
- Include relevant sources or links from the context
- At the end, add: "To read more, check out: [insert source link]"
- Avoid unnecessary or unrelated details

Answer:"""

    return ChatPromptTemplate.from_template(template)


# =============================================================================
# UTILITIES
# =============================================================================

def print_retrieval_results(docs: List, max_docs: int = 3, max_chars: int = 200):
    """
    Pretty print retrieved documents
    """
    print(f"\n{'='*80}")
    print(f"Retrieved {len(docs)} documents:")
    print(f"{'='*80}\n")

    for i, doc in enumerate(docs[:max_docs], 1):
        content = doc.page_content if hasattr(doc, 'page_content') else str(doc)
        metadata = doc.metadata if hasattr(doc, 'metadata') else {}

        print(f"Document {i}:")
        print(f"Title: {metadata.get('doc_title', 'N/A')}")
        print(f"Content: {content[:max_chars]}...")
        print(f"{'-'*80}\n")


def count_tokens_approximate(text: str) -> int:
    """
    Approximate token count (rough estimate)
    """
    # Rough approximation: 1 token ≈ 4 characters
    # For more accuracy, use tiktoken:
    # import tiktoken
    # encoding = tiktoken.encoding_for_model("gpt-4")
    # return len(encoding.encode(text))
    return len(text) // 4


def calculate_token_reduction(before: int, after: int) -> float:
    """
    Calculate percentage token reduction
    """
    if before == 0:
        return 0
    return ((before - after) / before) * 100


def format_docs(docs: List) -> str:
    """
    Format retrieved documents into a single string for context
    """
    return "\n\n".join([
        doc.page_content if hasattr(doc, 'page_content') else str(doc)
        for doc in docs
    ])
