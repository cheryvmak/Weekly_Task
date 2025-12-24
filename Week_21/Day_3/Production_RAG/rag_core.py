"""
Simple RAG System with LangChain & OpenAI
"""

import os
from typing import List, Dict
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document


class DocumentProcessor:
    """
    Handles document loading and chunking.
    """

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initialize the document processor.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def load_documents(self, documents_folder: str) -> List[Document]:
        """
        Load all text documents from a folder.
        """
        loader = DirectoryLoader(
            documents_folder,
            glob="**/*.txt",
            loader_cls=TextLoader
        )
        documents = loader.load()
        print(f"✅ Loaded {len(documents)} documents")
        return documents

    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into smaller chunks.
        """
        chunks = self.text_splitter.split_documents(documents)
        print(f"✅ Created {len(chunks)} chunks")
        return chunks


class VectorStoreManager:
    """
    Manages vector embeddings and ChromaDB storage/retrieval.
    """

    def __init__(
        self,
        embedding_model: str = "text-embedding-3-small",
        persist_directory: str = "./chroma_db"
    ):
        """
        Initialize the vector store manager.
        """
        load_dotenv()  # Load environment variables from .env

        self.embedding_model = embedding_model
        self.persist_directory = persist_directory

        # Initialize embeddings
        print(f"Loading embedding model: {embedding_model}...")
        self.embeddings = OpenAIEmbeddings(
            model=embedding_model
        )
        print("✅ Embedding model loaded!")

        self.vectorstore = None

    def create_vectorstore(self, chunks: List[Document]):
        """
        Create a vector store from document chunks.
        """
        print("Creating vector store with embeddings...")
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        print(f"✅ Vector store created with {len(chunks)} chunks!")

    def load_vectorstore(self):
        """
        Load an existing vector store from disk.
        """
        print("Loading existing vector store...")
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )
        print("✅ Vector store loaded!")

    def search(self, query: str, top_k: int = 3) -> Dict:
        """
        Search for relevant documents.
        """
        if self.vectorstore is None:
            raise ValueError("No vector store loaded. Create or load one first.")

        results_with_scores = self.vectorstore.similarity_search_with_score(
            query, k=top_k
        )

        formatted_results = {
            "query": query,
            "results": []
        }

        for doc, score in results_with_scores:
            formatted_results["results"].append({
                "text": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            })

        return formatted_results

    def get_retriever(self, top_k: int = 3):
        """
        Get a LangChain retriever for the vector store.
        """
        if self.vectorstore is None:
            raise ValueError("No vector store loaded. Create or load one first.")

        return self.vectorstore.as_retriever(search_kwargs={"k": top_k})

    def get_stats(self) -> Dict:
        """
        Get statistics about the vector store.
        """
        if self.vectorstore is None:
            return {"error": "No vector store loaded"}

        collection = self.vectorstore._collection
        return {
            "total_chunks": collection.count(),
            "embedding_model": self.embedding_model
        }


class RAGGenerator:
    """
    Generates answers by combining retrieval with an LLM.
    """

    def __init__(
        self,
        vectorstore_manager: VectorStoreManager,
        openai_model: str = "gpt-3.5-turbo",
        temperature: float = 0.0,
        top_k: int = 3
    ):
        """
        Initialize the RAG generator.
        """
        load_dotenv()

        self.vectorstore_manager = vectorstore_manager
        self.openai_model = openai_model
        self.temperature = temperature
        self.top_k = top_k

        # Initialize LLM
        self.llm = ChatOpenAI(
            model=openai_model,
            temperature=temperature
        )
        print(f"✅ OpenAI LLM initialized ({openai_model})!")

        # Build RAG chain
        self._build_rag_chain()

    def _build_rag_chain(self):
        """
        Build the RAG chain (retrieval + generation pipeline).
        """
        # Get retriever
        retriever = self.vectorstore_manager.get_retriever(top_k=self.top_k)

        # Create prompt template
        template = """You are a helpful assistant answering questions based on the provided context.

Context:
{context}

Question: {question}

Answer the question based on the context above. If you cannot answer based on the context, say so.

Answer:"""

        prompt = ChatPromptTemplate.from_template(template)

        # Helper function to format documents
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # Build the RAG chain
        self.rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )

        print("✅ RAG chain built!")

    def query(self, question: str) -> Dict:
        """
        Ask a question and get an AI-generated answer.
        """
        answer = self.rag_chain.invoke(question)

        return {
            "question": question,
            "answer": answer
        }


# Convenience function to build a complete RAG system
def build_rag_system(documents_folder: str) -> tuple:
    """
    Build a complete RAG system from documents.
    """
    print(f"\n{'='*60}")
    print("BUILDING RAG SYSTEM")
    print(f"{'='*60}\n")

    # Step 1: Process documents
    doc_processor = DocumentProcessor()
    documents = doc_processor.load_documents(documents_folder)
    chunks = doc_processor.chunk_documents(documents)

    # Step 2: Create vector store
    vectorstore_manager = VectorStoreManager()
    vectorstore_manager.create_vectorstore(chunks)

    # Step 3: Create RAG generator
    rag_generator = RAGGenerator(vectorstore_manager)

    print(f"\n{'='*60}")
    print("RAG SYSTEM READY!")
    print(f"{'='*60}\n")

    return doc_processor, vectorstore_manager, rag_generator
