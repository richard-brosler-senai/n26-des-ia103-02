#views/settings.py
import streamlit as st
from dotenv import dotenv_values, set_key

from services.settings_service import (
    load_settings,
    save_settings
)
def show():

    st.title(
        "⚙️ Configurações"
    )

    settings = load_settings()
    #llm
    llm_provider = st.selectbox(
		    "LLM Provider",
		    [
		        "azure",
		        "groq",
		        "gemini",
		        "ollama"
		    ],
		    index=[
		        "azure",
		        "groq",
		        "gemini",
		        "ollama"
		    ].index(
		        settings["LLM_PROVIDER"]
		    )
		)    
	#ocr
    ocr_provider = st.selectbox(
        "OCR Provider",
        [
            "easyocr",
            "azure"
        ],
        index=[
            "easyocr",
            "azure"
        ].index(
            settings["OCR_PROVIDER"]
        )
    )
    #visão
    vision_provider = st.selectbox(
        "Vision Provider",
        [
            "gemini",
            "azure",
            "groq",
            "ollama"
        ],
        index=[
            "gemini",
            "azure",
            "groq",
            "ollama"
        ].index(
            settings["VISION_PROVIDER"]
        )
    )
    # testando o click do botão
    if st.button(
        "💾 Salvar Configurações"
    ):

        save_settings(
            "LLM_PROVIDER",
            llm_provider
        )

        save_settings(
            "OCR_PROVIDER",
            ocr_provider
        )

        save_settings(
            "VISION_PROVIDER",
            vision_provider
        )

        st.success(
            "Configurações salvas!"
        )