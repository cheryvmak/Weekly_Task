"""
Simple RAG API with FastAPI

Provides endpoints to query the RAG system.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_core import VectorStoreManager, RAGGenerator


# Request/Response models
class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


class QueryResponse(BaseModel):
    question: str
    answer: str


class SearchResponse(BaseModel):
    query: str
    results: list


# Initialize FastAPI app
app = FastAPI(title="Simple RAG API", version="1.0.0")

# Global variables for RAG components
vectorstore_manager = None
rag_generator = None


@app.on_event("startup")
async def startup_event():
    """Load the RAG system on startup."""
    global vectorstore_manager, rag_generator

    print("Loading RAG system...")

    # Load vector store
    vectorstore_manager = VectorStoreManager()
    vectorstore_manager.load_vectorstore()

    # Create RAG generator
    rag_generator = RAGGenerator(vectorstore_manager)

    print("✅ RAG system loaded!")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Simple RAG API",
        "endpoints": {
            "/query": "Ask a question (POST)",
            "/search": "Search documents (POST)",
            "/stats": "Get index statistics (GET)"
        }
    }


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """
    Ask a question and get an AI-generated answer.
    """
    if rag_generator is None:
        raise HTTPException(status_code=500, detail="RAG system not initialized")

    try:
        result = rag_generator.query(request.question)
        return QueryResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search", response_model=SearchResponse)
async def search(request: QueryRequest):
    """
    Search for relevant documents (retrieval only).
    """
    if vectorstore_manager is None:
        raise HTTPException(status_code=500, detail="Vector store not initialized")

    try:
        result = vectorstore_manager.search(request.question, top_k=request.top_k)
        return SearchResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
async def get_stats():
    """
    Get statistics about the RAG system.
    """
    if vectorstore_manager is None:
        raise HTTPException(status_code=500, detail="Vector store not initialized")

    return vectorstore_manager.get_stats()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
