# tools/rag_tool.py
from services.rag_service import ask_question
def execute(
        question,
        index,
        chunks,
        context):

    return ask_question(
        question,
        index,
        chunks,
        context,
        True
    )