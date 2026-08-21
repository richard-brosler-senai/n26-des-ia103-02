import streamlit as st
import random

def show():
    st.title("🤖 ChatXPT")
           
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Carregando as mensagens que estão armazenadas
    for message in st.session_state.messages:
        with st.chat_message(
            message["role"]
        ):
            st.write(
                message["content"]
            )
    # Ajustando o layout para 3 colunas onde a coluna maior fica a conversa          
    _, col_novo, col_limpar = st.columns([6, 1, 1])
		# Para iniciar uma nova conversa com o modelo
    with col_novo:
        if st.button("➕", help="Novo chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.thread_id = None
            st.rerun()
   # Para limpar o contexto da conversa
    with col_limpar:
        if st.button("🗑️", help="Limpar conversa", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
		# Aqui abrimos o prompt para o usuário
    prompt = st.chat_input(
        "Digite sua pergunta..."
    )
		# Se escreveu algo, disparamos a chamada
    if prompt:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )
        # Aqui simulamos uma resposta
        resposta = random.choice(
            [
								"Olá! Como posso ajudar você hoje?",
							  "Oi, humano! Há algo em que eu possa ajudar?",
							  "Você precisa de ajuda?",
            ]
        )
        # Poderíamos chamar assim
        # resposta = chat(prompt)
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": resposta
            }
        )
        st.rerun()
        
if __name__ == "__main__":
    show()