#services/agent_service.py

from services.llm_service import chat
from services.vision_service import detect_image_mimetype

from tools.chat_tool import execute as chat_tool

from tools.rag_tool import execute as rag_tool

from tools.ocr_tool import execute as ocr_tool

from tools.vision_tool import execute as vision_tool

def select_tool(
        question,
        has_image=False):

    system_prompt = """
Você é um roteador de ferramentas.

Escolha SOMENTE UMA opçao.

CHAT
RAG
OCR
VISION

Regras:

CHAT
- Conversas gerais
- Dúvidas sobre IA
- Programação

RAG
- Perguntas sobre documentos carregados

OCR
- Extrair texto da imagem

VISION
- Descrever ou analisar imagens

Responda apenas com:
CHAT
RAG
OCR
VISION
"""
    if has_image:
        system_prompt += """
Se existir imagem:

- "extraia texto" => OCR
- "leia texto" => OCR
- "transcreva" => OCR

- "descreva" => VISION
- "analise" => VISION
- "o que há na imagem" => VISION
"""
    contexto = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    return chat(
        question,
        contexto
    )

def execute_agent(
        question,
        image=None,
        index=None,
        chunks=None,
        contexto=None):

    tool = select_tool(
        question,
        has_image=image is not None
    )
    # Obtendo a tool
    tool = tool.upper().strip()
    # Verificando se é CHAT
    if tool == "CHAT":
        return {
            "tool": "CHAT",
            "result": chat_tool(question, contexto)
        }
    # Verificando se é RAG
    if tool == "RAG":
        if not index:
            return {
                "tool": "RAG",
                "result":
                "Nenhum documento carregado."
            }
        return {
            "tool": "RAG",
            "result": rag_tool( question, index, chunks, contexto)
        }
    # Se é OCR
    if tool == "OCR":
        if image is None:
            return {
                "tool": "OCR",
                "result":
                "Nenhuma imagem enviada."
            }
        return {
            "tool": "OCR",
            "result": ocr_tool(image)
        }
    # se é visão
    if tool == "VISION":

        if image is None:

            return {
                "tool": "VISION",
                "result":
                "Nenhuma imagem enviada."
            }
        imageBytes=image.getvalue()
        image_type = detect_image_mimetype(imageBytes)
        return {
            "tool": "VISION",
            "result": vision_tool(
                imageBytes,
                question,
                image_type
            )
        }
    # Fallback
    return {
        "tool": "CHAT",
        "result": chat_tool(question, contexto)
    }