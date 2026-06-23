vector_store = None
current_pdf = None
import os
from fastapi import FastAPI
from pydantic import BaseModel

from src.ingest import load_and_split_pdf
from src.vector_store import create_vector_store
from src.rag import ask_question
from typing import List, Dict



app = FastAPI()

# Chargement du PDF au démarrage

vector_store = None

class QuestionRequest(BaseModel):

    question: str
    pdf_name: str


@app.get("/")
def home():

    return {
        "message": "RAG Chatbot API"
    }


@app.post("/ask")
def ask(request: QuestionRequest):

    global vector_store

    pdf_directory = "data/documents"

    pdf_files = [
        f for f in os.listdir(pdf_directory)
        if f.endswith(".pdf")
    ]

    global vector_store
    global current_pdf

    pdf_path = os.path.join(
        "data/documents",
        request.pdf_name
    )

    # Recréer Chroma uniquement si le PDF change

    if current_pdf != request.pdf_name:

        print(f"\nChargement du PDF : {request.pdf_name}\n")

        chunks = load_and_split_pdf(
            pdf_path
        )

        vector_store = create_vector_store(
            chunks
        )

        current_pdf = request.pdf_name

    else:

        print(
            "\nUtilisation du vector store déjà chargé.\n"
        )

    result = ask_question(
        request.question,
        vector_store,
    )

    return result