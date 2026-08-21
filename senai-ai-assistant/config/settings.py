# config/settings.py
from dotenv import load_dotenv
import os

ENV_FILE = ".env"

load_dotenv()
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock")
LLM_MODEL=os.getenv("LLM_MODEL", "gpt-4o")
LLM_TEMP=os.getenv("LLM_TEMP", 0.7)
# Groq
GROQ_API_KEY=os.getenv("GROQ_API_KEY", "axaxaxa")
GROQ_LLM_MODEL=os.getenv("GROQ_LLM_MODEL", "gpt-4o")
GROQ_LLM_TEMP=os.getenv("GROQ_LLM_TEMP", 0.7)
# Azure
AZURE_OPENIA_URL=os.getenv("AZURE_OPENIA_URL", "https://<resource>.openai.azure.com/openai/v1")
AZURE_KEY=os.getenv("AZURE_KEY", "SUA_CHAVE_AQUI")
AZURE_PROJECT_URL=os.getenv("AZURE_PROJECT_URL", "https://<resource>.services.ai.azure.com/api/projects/xxxxxx")
AZURE_LLM_MODEL=os.getenv("AZURE_LLM_MODEL", "gpt-5")
AZURE_LLM_TEMP=os.getenv("AZURE_LLM_TEMP", 0.7)
# Gemini
GEMINI_KEY=os.getenv("GEMINI_KEY", "xxx")
GEMINI_LLM_BASE_URL=os.getenv("GEMINI_LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
GEMINI_LLM_MODEL=os.getenv("GEMINI_LLM_MODEL", "gemini-2.5-flash")
GEMINI_LLM_TEMP=os.getenv("GEMINI_LLM_TEMP", 1.0)
# Ollama
OLLAMA_KEY=os.getenv("OLLAMA_KEY", "qualquer-coisa")
OLLAMA_LLM_BASE_URL=os.getenv("OLLAMA_LLM_BASE_URL", "http://localhost:8080/v1")
OLLAMA_LLM_MODEL=os.getenv("OLLAMA_LLM_MODEL", "local")
OLLAMA_LLM_TEMP=os.getenv("OLLAMA_LLM_TEMP", 1.0)
# Embedding
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER","sentence")
# ocr
OCR_PROVIDER=os.getenv("OCR_PROVIDER","easyocr")
# visão
VISION_PROVIDER=os.getenv("VISION_PROVIDER","gemini")

def get_setting(key, default=None):
    return os.getenv(key, default)

def gravar_setting(key,value):
	  set_key(ENV_FILE,key,value)