from langchain_openai import ChatOpenAI


def ask_question(
    question,
    vector_store,
):

    results = vector_store.max_marginal_relevance_search(
    question,
    k=3
)
    print("\n=== CHUNKS RETROUVÉS ===\n")

    for i, doc in enumerate(results):
        print(f"\n--- Chunk {i+1} ---\n")
        print(doc.page_content[:500])
        print(
            "Page récupérée :",
            doc.metadata.get("page", "Inconnue")
        )

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    prompt = f"""
    Tu es un assistant pédagogique spécialisé.

    Réponds uniquement à partir des informations présentes dans le contexte fourni.

    Reformule les informations avec tes propres mots afin de produire une réponse claire, pédagogique et structurée.

    N'ajoute aucune information qui n'est pas présente dans le contexte.

    Si les informations ne sont pas présentes dans le contexte, réponds exactement :

    "Je ne trouve pas cette information dans le document."

    Contexte :
    {context}

    Question :
    {question}

    Réponse :
    """

    print("\n=== CONTEXTE ENVOYÉ AU LLM ===\n")
    print(context)

    response = llm.invoke(prompt)

    sources = list(
        set(
            [
                doc.metadata.get("page", "Inconnue") + 1
                for doc in results
           ]
        )
    )

    return {
        "answer": response.content,
        "sources": sources
    }

