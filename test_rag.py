from src.ingest import (
    load_and_split_pdf
)

from src.vector_store import (
    create_vector_store
)

from src.rag import (
    ask_question
)


chunks = load_and_split_pdf(
    "data/documents/test.pdf"
)

vector_store = create_vector_store(
    chunks
)

question = input(
    "Pose une question : "
)

response = ask_question(
    question,
    vector_store
)

print("\nRéponse :\n")

print(response)
