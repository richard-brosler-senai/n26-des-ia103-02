# providers/llm/groq_llm.py
import groq
from config.settings import (GROQ_LLM_MODEL, GROQ_LLM_TEMP, GROQ_API_KEY)

# Instanciando o client do groq
client = groq.Groq(api_key=GROQ_API_KEY)

def chat(prompt: str, contexto: list[dict]) -> str:
    cliente = client.chat.completions.create(
        messages=contexto,
        model=GROQ_LLM_MODEL,
        temperature=float(GROQ_LLM_TEMP)
    )
    print("Tokens entrada:", cliente.usage.prompt_tokens)
    print("Tokens saída:", cliente.usage.completion_tokens)
    print("Tokens total:", cliente.usage.total_tokens)
    return cliente.choices[0].message.content