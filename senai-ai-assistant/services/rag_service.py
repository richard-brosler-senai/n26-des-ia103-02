# services/rag_service.py
from services.embedding_service import (
    generate_embedding
)

from services.vector_store import search
from services.llm_service import chat

def retrieve_context(
        question,
        index,
        chunks):

    question_embedding = (
        generate_embedding(question)
    )

    positions = search(
        index,
        question_embedding
    )

    context_parts = []

    for pos in positions:

        context_parts.append(
            chunks[pos]
        )

    return "\n".join(context_parts)
    
def build_system_prompt(
        context,
        question):

    return f"""
Você deve responder
utilizando apenas as
informações do contexto.
Se a resposta não estiver
no contexto, informe que
não encontrou a informação.

Contexto:

{context}
"""

def ask_question(
        question,
        index,
        chunks,
        context,
        is_tool = False):

    dados = retrieve_context(
        question,
        index,
        chunks
    )
    if not any(item.get("role") == "system" for item in context) or is_tool:
        prompt = build_system_prompt(
            dados,
            question
        )
        context.clear()
        context.append({
                        "role": "system",
                        "content": prompt
                    })
        
    context.append({
                    "role": "user",
                    "content": question
                })
    return chat(question,context)