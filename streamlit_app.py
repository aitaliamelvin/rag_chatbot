import streamlit as st
from src.ingest import load_and_split_pdf
from src.vector_store import create_vector_store
from src.rag import ask_question
import os
import time

st.title("📚 Chatbot RAG")

if "toast_message" in st.session_state:

    st.toast(
        st.session_state["toast_message"]
    )

    del st.session_state["toast_message"]

if "pdf_deleted" in st.session_state:

    st.success(
        st.session_state["pdf_deleted"]
    )

    del st.session_state["pdf_deleted"]

if "messages" not in st.session_state:
    st.session_state.messages = []

pdf_directory = "data/documents"

# Création du dossier s'il n'existe pas
os.makedirs(pdf_directory, exist_ok=True)

with st.sidebar:

    st.header("📄 Gestion des documents")

    uploaded_file = st.file_uploader(
        "Déposez un PDF",
        type="pdf"
    )

# Sauvegarde du nouveau PDF

if "last_uploaded" not in st.session_state:
    st.session_state.last_uploaded = None

if (
    uploaded_file is not None
    and uploaded_file.name != st.session_state.last_uploaded
):

    save_path = os.path.join(
        pdf_directory,
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(
            uploaded_file.getbuffer()
        )

    st.toast(
        f"📄 {uploaded_file.name} ajouté avec succès."
    )

    st.session_state.last_uploaded = (
        uploaded_file.name
    )

pdf_files = [
    f for f in os.listdir(pdf_directory)
    if f.endswith(".pdf")
]

if pdf_files:
    with st.sidebar:

        if pdf_files:

            st.success(
                f"{len(pdf_files)} PDF disponible(s)"
            )

            selected_pdf = st.selectbox(
                "Choisissez le PDF à utiliser",
                pdf_files
            )
 
            if "last_pdf" not in st.session_state:
                st.session_state.last_pdf = selected_pdf

            if st.session_state.last_pdf != selected_pdf:
                st.session_state.messages = []
                st.session_state.last_pdf = selected_pdf

            if st.button(
                "🗑️ Supprimer le PDF sélectionné"
            ):

                file_path = os.path.join(
                    pdf_directory,
                    selected_pdf
                )

                os.remove(file_path)

                st.session_state["toast_message"] = (
                    f"🗑️ {selected_pdf} supprimé avec succès."
                )

                st.rerun()

            if st.button(
                "🧹 Effacer la conversation"
            ):

                st.session_state.messages = []

                st.session_state["toast_message"] = (
                    "🧹 Conversation réinitialisée."
                )

                st.rerun()

        else:

            st.info(
                "Aucun PDF disponible."
            )

            st.session_state.messages = []
            st.session_state.last_pdf = None

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

if not pdf_files:
    st.stop()

question = st.chat_input(
    "Posez votre question"
)

if question:

    if not pdf_files:

        st.warning(
            "Aucun PDF disponible. Veuillez en ajouter un."
        )
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner(
        "🔍 Analyse du document en cours..."
    ):

        pdf_path = os.path.join(
            pdf_directory,
            selected_pdf
        )

        chunks = load_and_split_pdf(
            pdf_path
        )

        vector_store = create_vector_store(
            chunks
        )

        result = ask_question(
            question,
            vector_store
        )

        answer = result["answer"]
        sources = result["sources"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):

        placeholder = st.empty()

        full_response = ""

        for word in answer.split():

            full_response += word + " "

            placeholder.markdown(full_response)

            time.sleep(0.03)
    
    