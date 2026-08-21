# providers/llm/mock_llm.py
def chat(prompt: str, contexto: list[dict]) -> str:
    resposta = f"""
    Resposta simulada.
    Pergunta recebida:
    {prompt}
    """
    return resposta