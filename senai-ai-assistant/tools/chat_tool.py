# tools/chat_tool.py
from services.llm_service import chat

def execute(question, context):
    return chat(question, context)