import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Load documents
loader = DirectoryLoader(
    "documents/",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)
docs = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
chunks = splitter.split_documents(docs)

# Create embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=api_key
)

# Create vector store
Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db1"
)

print("✅ Vector database created successfully")

# Run this ONCE:
# python rag_index.py
