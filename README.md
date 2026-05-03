# RAG Chatbot using LangChain, FAISS & OpenAI

## 🔍 Overview
This project implements a **Retrieval-Augmented Generation (RAG) chatbot** that answers questions based on custom documents. It reduces hallucinations by grounding responses with retrieved context.

## 🏗 Architecture
User Query → Embeddings → FAISS Similarity Search → Relevant Chunks → LLM → Answer

## 🛠 Tech Stack
- Python
- LangChain
- OpenAI
- FAISS
- FastAPI
