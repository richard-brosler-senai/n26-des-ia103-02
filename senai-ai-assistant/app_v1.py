import streamlit as st
# Utilizar data
from datetime import datetime

st.set_page_config(
    page_title="SENAI AI Assistant",
    page_icon="./assets/senai_logo.jpg",  # Can be an emoji ("📊"), local path ("path/to/icon.png"), or URL
)

st.title("SENAI AI Assistant")
# Canto superior esquerdo - Pequeno
st.logo("./assets/senai_logo.jpg")
# Obtendo a data/hora atual
hoje = datetime.now()
# Mostrando a data
st.write(hoje.strftime("%d/%m/%Y"))
# Utilizando a imagem
# st.image("./assets/senai_logo.jpg",None,150)
st.image("./assets/senai_logo.jpg",width=150)
st.write("Minha primeira aplicação Streamlit")

# Para entradas de texto
nome = st.text_input("Digite seu nome")
# Para entradas de números
idade = st.number_input("Idade")
# Para caixa de seleção
curso = st.selectbox(
    "Curso",
    ["IA", "Python", "Power BI"]
)