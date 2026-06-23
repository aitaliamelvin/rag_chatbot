from langchain_openai import ChatOpenAI


def ask_question(
    question,
    vector_store,
):

    results = vector_store.max_marginal_relevance_search(
    question,
    k=6
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

    Produis une réponse complète, détaillée, pédagogique et bien structurée.

    Lorsque le contexte contient suffisamment d'informations, développe les explications de façon approfondie.

    Utilise des paragraphes, des listes à puces et des titres lorsque cela améliore la compréhension.

    Reformule toujours avec tes propres mots.

    N'ajoute aucune information absente du contexte.

    Si l'information n'est pas présente dans le contexte, réponds exactement :

    "Je ne trouve pas cette information dans le document."

    Contexte :
    {context}

    Question :
    {question}

    Réponse détaillée :
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

