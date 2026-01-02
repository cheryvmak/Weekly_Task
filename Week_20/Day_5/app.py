from fastapi import FastAPI
from pydantic import BaseModel
from rag_query import run_rag

app = FastAPI()

class Query(BaseModel):
    question: str


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/query")
def query_rag(q: Query):
    answer = run_rag(q.question)
    return {"answer": answer}
# To run the app, use the command:
# uvicorn app:app --reload
