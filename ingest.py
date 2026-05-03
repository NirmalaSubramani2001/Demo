import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()

DATA_PATH = "data/documents.pdf"
INDEX_PATH = "faiss_index"

def ingest_documents():
    print("Loading document...")
    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()

    print("Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    print(f"Total chunks created: {len(chunks)}")

    print("Creating embeddings and FAISS index...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(INDEX_PATH)
    print("FAISS index saved successfully")

if __name__ == "__main__":
    ingest_documents()
