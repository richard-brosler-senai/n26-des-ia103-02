# providers/llm/gemini_llm.py
from openai import OpenAI
from config.settings import (GEMINI_KEY,
                             GEMINI_LLM_BASE_URL,
                             GEMINI_LLM_MODEL,
                             GEMINI_LLM_TEMP)
   
client = OpenAI(
     api_key=GEMINI_KEY,
     base_url=GEMINI_LLM_BASE_URL,
)

def chat(prompt: str, contexto: list[dict]) -> str:
    cliente = client.chat.completions.create(
        messages=contexto,
        model=GEMINI_LLM_MODEL,
        temperature=float(GEMINI_LLM_TEMP)
    )
    print("Tokens entrada:", cliente.usage.prompt_tokens)
    print("Tokens saída:", cliente.usage.completion_tokens)
    print("Tokens total:", cliente.usage.total_tokens)
    return cliente.choices[0].message.content