import streamlit as st

st.sidebar.title("Menu")

opcoes = ["🏠 Início", "🤖 Chat IA", "📄 Documentos", "⚙ Configurações"]
opcao = st.sidebar.selectbox(
    "Escolha",opcoes
)

container = st.container()

with container:
    st.header("Dados")
    st.write("Informações")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Usuários",
        120,
        "+12%"
    )

with col2:
    st.metric(
        "Consultas",
        542,
        "-12%"
    )

with col3:
    st.metric(
        "Documentos",
        88
    )

tab1, tab2, tab3 = st.tabs(
    [
        "Chat",
        "Documentos",
        "Configurações"
    ]
)
with tab1:
    st.write("Área Chat")

with tab2:
    st.write("Área Documentos")

with tab3:
    st.write("Área Configurações")