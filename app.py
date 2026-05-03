from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import load_qa_chain

app = FastAPI(
    title="RAG Chatbot",
    description="Retrieval Augmented Generation using LangChain + FAISS",
    version="1.0"
)

qa_chain = load_qa_chain()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    result = qa_chain(query.question)
    return {
        "answer": result["result"]
    }
