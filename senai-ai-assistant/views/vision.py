# views/vision.py
import streamlit as st
from services.settings_service import load_settings
from services.vision_service import describe_image, detect_image_mimetype

def show():
    settings = load_settings()
    st.title("👁️ Visão Computacional")
    st.write("Vision Provider: " + settings["VISION_PROVIDER"])

    image = st.file_uploader(
        "Selecione uma imagem",
        type=[
            "png",
            "jpg",
            "jpeg"
        ]
    )

    if image:
        st.image(image)
        prompt = st.text_input("O que deseja analisar?")
        if st.button("Analisar"):
            tipo=detect_image_mimetype(image.getvalue())
            if tipo == None: tipo = "image/jpeg"
            result = describe_image(
                image.getvalue(),
                prompt,
                tipo
            )
            st.markdown(result)