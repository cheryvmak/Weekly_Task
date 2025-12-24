"""
Build RAG Index

This script builds the vector index from documents.
"""

from rag_core import build_rag_system


if __name__ == "__main__":
    # Build the complete RAG system
    doc_processor, vectorstore_manager, rag_generator = build_rag_system("documents")

    # Show stats
    stats = vectorstore_manager.get_stats()
    print(f"Total chunks indexed: {stats['total_chunks']}")
    print("\nReady! Run: python api.py")
