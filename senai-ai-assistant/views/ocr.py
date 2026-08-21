#views/ocr.py
import streamlit as st

from services.ocr_service import (
    process_image
)

def show():

    st.title("📄 OCR")

    image = st.file_uploader(
        "Selecione uma imagem",
        type=["png","jpg","jpeg"]
    )

    if image:

        st.image(image)

        if st.button(
            "Extrair Texto"
        ):

            texto = process_image(
                image
            )

            st.text_area(
                "Resultado",
                texto,
                height=300
            )