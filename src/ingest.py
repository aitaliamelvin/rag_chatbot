from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

def load_and_split_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(
        documents
    )
    print("\n=== METADONNEES DES CHUNKS ===\n")

    for i, chunk in enumerate(chunks[:10]):
        print(
            f"Chunk {i+1} :",
            chunk.metadata
        )
    return chunks