from openai import OpenAI
from config.settings import (OLLAMA_LLM_BASE_URL,
                             OLLAMA_LLM_MODEL,
                             OLLAMA_LLM_TEMP,
                             OLLAMA_KEY)
   
client = OpenAI(
     base_url=OLLAMA_LLM_BASE_URL,
     api_key=OLLAMA_KEY
)

def chat(prompt: str, contexto: list[dict]) -> str:
    cliente = client.chat.completions.create(
        messages=contexto,
        model=OLLAMA_LLM_MODEL,
        temperature=float(OLLAMA_LLM_TEMP)
    )
    print("Tokens entrada:", cliente.usage.prompt_tokens)
    print("Tokens saída:", cliente.usage.completion_tokens)
    print("Tokens total:", cliente.usage.total_tokens)
    return cliente.choices[0].message.content