from langchain_community.vectorstores import (
    Chroma
)

from langchain_openai import (
    OpenAIEmbeddings
)

from dotenv import load_dotenv

load_dotenv()


def create_vector_store(chunks):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    return vector_store