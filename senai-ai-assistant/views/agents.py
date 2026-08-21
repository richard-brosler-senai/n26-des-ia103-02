# views/agents.py

import streamlit as st

from services.agent_service import execute_agent

from services.settings_service import load_settings

settings = load_settings()

def show():

    st.title(
        "🧠 SENAI Agent"
    )
    st.write("Vision Provider: " + settings["VISION_PROVIDER"] + 
             " - LLM Provider: " + settings["LLM_PROVIDER"])

    # Históricos
    if "agent_messages" not in st.session_state:
        st.session_state.agent_messages = [
            {
                "role": "system",
                "content": """Você é um agente prestativo, atencioso e 
suas respostas devem ser em português do Brasil.
Seja objetivo nas respostas evitando respostas muito longas."""
            }
        ]
    for msg in st.session_state.agent_messages:
        if msg["role"]== "system": continue
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])        
    # Imagem
    image = st.file_uploader(
        "Imagem opcional",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )

    # Pdf
    pdf_file = st.file_uploader("Arquivo para RAG - Opcional",
                                type=["pdf"])
    # Se tiver documento para RAG, tratamos ele
    if pdf_file:
        from services.pdf_service import extract_text
        from services.chunk_service import create_chunks
        from services.embedding_service import generate_embedding
        from services.vector_store import build_index
        texto = extract_text(pdf_file)
        # Jogando para a session
        chunks = create_chunks(texto)
        st.session_state.document_chunks = chunks
        vectors = []
        for chunk in chunks:
            vectors.append(generate_embedding(chunk))
        st.session_state.vector_index = build_index(vectors)
        st.success("Documento processado")
        st.write(f"Chunks: {len(chunks)}")

    # Chat
    question = st.chat_input(
        "Digite sua solicitação"
    )

    if question:
        st.session_state.agent_messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )
        result = execute_agent(
            question,
            image=image,
            index=st.session_state.get("vector_index"),
            chunks=st.session_state.get("document_chunks"),
            contexto=st.session_state.agent_messages
        )
        response = f"""
Ferramenta utilizada:

**{result['tool']}**

---

{result['result']}
"""
        st.session_state.agent_messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )
        st.rerun()
        st.write(result)
