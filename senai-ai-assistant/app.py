import streamlit as st
# importando biblioteca de tratamento de datas
from datetime import datetime

st.set_page_config(
    page_title="SENAI AI Assistant",
    page_icon="./assets/senai_logo.jpg",  # Can be an emoji ("📊"), local path ("path/to/icon.png"), or URL
)
# Definições
metricas = [
            {"descricao":"IA Ativas", "valor":150, "variacao": None},
            {"descricao":"Documentos", "valor":45, "variacao": None},
            {"descricao":"Usuários", "valor":38, "variacao": None},
            {"descricao":"Consultas IA", "valor":5, "variacao": None},
            {"descricao":"Documentos Analisados", "valor":2, "variacao": None},
            {"descricao":"Agentes Criados", "valor":3, "variacao": None},
            ]
tabs = [ #"Chat","Documentos","Sobre"
    {"titulo": "Chat", "conteudo": "Chat"},
    {"titulo": "Documentos", "conteudo": "Documentos"},
    {"titulo": "Sobre", "conteudo": """Projeto desenvolvido  
durante o curso  
Desenvolvimento de Agentes com IA"""},
]
st.title("SENAI AI Assistant")
# Menu Lateral
st.sidebar.write(f"""**Richard**  
**Usuário**  
{datetime.now().strftime("%d/%m/%Y %H:%M")}
""")
st.sidebar.selectbox("Menu Lateral",[
    "🏠 Home",
    "🤖 Chat",
    "📄 Documentos",
    "⚙ Configurações"]
    )
# Indicadores
st.write("## Indicadores") # MarkDown ## corresponde ao titulo 2 ou H2
# Colunas
for col, ele in zip(st.columns(len(metricas)), metricas):
    with col: st.metric(ele["descricao"],ele["valor"],ele["variacao"])
# Tabs
# tab1, tab2, tab3 = st.tabs(["Chat","Documentos","Sobre"])
for tab, ele in zip(st.tabs([it["titulo"] for it in tabs]),tabs):
    with tab:
        if not ele["conteudo"] == None:
            st.write(ele["conteudo"])
