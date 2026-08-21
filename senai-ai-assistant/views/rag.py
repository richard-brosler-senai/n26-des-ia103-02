# views/rag.py
import streamlit as st

from services.pdf_service import (
    extract_text
)

from services.chunk_service import (
    create_chunks
)

from services.embedding_service import (
    generate_embedding
)

from services.vector_store import (
    build_index
)

from services.rag_service import (
    ask_question
)

def show():
    st.title("📚 Consulta de Documentos")

    arquivo = st.file_uploader(
        "Selecione um PDF",
        type=["pdf"]
    )
    if arquivo:
        texto = extract_text(
            arquivo
        )
        chunks = create_chunks(
            texto
        )
        vectors = []
        for chunk in chunks:
            vectors.append(
                generate_embedding(
                    chunk
                )
            )
        index = build_index(
            vectors
        )
        st.success(
            "Documento processado"
        )
        st.write(
            f"Chunks: {len(chunks)}"
        )
        # Perguntando ao chat
        if "index" not in st.session_state:
            st.session_state.index = None
        if "chunks" not in st.session_state:
            st.session_state.chunks = None
        if "messages" not in st.session_state:
            st.session_state.messages = []   
        for message in st.session_state.messages:
            if message["role"]== "system": continue
            with st.chat_message(
                message["role"]
            ):
                st.write(
                    message["content"]
                )
        question = st.chat_input(
					"Faça uma pergunta sobre o documento"
				)
        if question:
            with st.chat_message(
                "user"
            ):
                answer = ask_question(
                    question,
                    index,
                    chunks,
                    st.session_state.messages
                )
                st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": answer
                            }
                        )
                st.rerun()
