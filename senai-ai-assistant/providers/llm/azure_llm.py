# providers/llm/azure_llm.py
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from config.settings import (AZURE_LLM_MODEL,
                             AZURE_LLM_TEMP,
                             AZURE_OPENIA_URL)

# Instanciando the OpenAI client
token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://ai.azure.com/.default"
)
    
client = OpenAI(
     base_url=AZURE_OPENIA_URL,
     api_key=token_provider
)

def chat(prompt: str, contexto: list[dict]) -> str:
    cliente = client.chat.completions.create(
        messages=contexto,
        model=AZURE_LLM_MODEL,
        temperature=float(AZURE_LLM_TEMP)
    )
    print("Tokens entrada:", cliente.usage.prompt_tokens)
    print("Tokens saída:", cliente.usage.completion_tokens)
    print("Tokens total:", cliente.usage.total_tokens)
    return cliente.choices[0].message.content