# services/llm_service.py
from config.settings import (
    LLM_PROVIDER
)

def chat(prompt: str, contexto: list[dict]) -> str:
    # Provider Mockado
    if LLM_PROVIDER == "mock":
        from providers.llm.mock_llm import chat
        return chat(prompt, contexto)
    # Provider Groq
    if LLM_PROVIDER == "groq":
        from providers.llm.groq_llm import chat
        return chat(prompt, contexto)
    # Provider Azure
    if LLM_PROVIDER == "azure":
        from providers.llm.azure_llm import chat
        return chat(prompt, contexto)
    # Provider Gemini
    if LLM_PROVIDER == "gemini":
        from providers.llm.gemini_llm import chat
        return chat(prompt, contexto)
    # Provider Ollama
    if LLM_PROVIDER == "ollama":
        from providers.llm.ollama_llm import chat
        return chat(prompt, contexto)
    return "Provider não configurado."