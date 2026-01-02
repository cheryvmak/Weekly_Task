import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Load vector store
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=api_key
)

vectorstore = Chroma(
    persist_directory="chroma_db1",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=api_key
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answering questions using personal documents. Use only the provided context."),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# RAG chain
rag_chain = (
    RunnableParallel(
        context=retriever | format_docs,
        question=RunnablePassthrough()
    )
    | prompt
    | llm
    | StrOutputParser()
)

def run_rag(question: str):
    """
    This function is what the FRONTEND will call
    """
    answer = rag_chain.invoke(question)
    return answer
