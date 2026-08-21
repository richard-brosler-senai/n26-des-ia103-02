# views/dashboard.py
import streamlit as st

def show():
    st.title("Home")
    st.write("Bem vindo ao SENAI AI Assistant")
    # Definições
    tabs = [ 
    {"titulo": "Chat", "conteudo": "Chat"},
    {"titulo": "Documentos", "conteudo": "Documentos"},
    {"titulo": "Sobre", "conteudo": """Projeto desenvolvido  
durante o curso  
Desenvolvimento de Agentes com IA"""},
]
    metricas = [
                {"descricao":"IA Ativas", "valor":150, "variacao": None},
                {"descricao":"Documentos", "valor":45, "variacao": None},
                {"descricao":"Usuários", "valor":38, "variacao": None},
                {"descricao":"Consultas IA", "valor":5, "variacao": None},
                {"descricao":"Documentos Analisados", "valor":2, "variacao": None},
                {"descricao":"Agentes Criados", "valor":3, "variacao": None},
                ]

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
            if ele["titulo"]=="Documentos":
                documento = st.file_uploader(
                    "Envie um arquivo"
                )
                if documento:
                    st.success(
                        "Arquivo enviado"
                    )