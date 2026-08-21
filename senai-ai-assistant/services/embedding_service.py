# services/embedding_service.py
from config.settings import (EMBEDDING_PROVIDER)

def generate_embedding(text):
    if EMBEDDING_PROVIDER == "sentence":
        from providers.embedding.sentence_embedding \
            import generate
        return generate(text)
    raise Exception(
        "Provider não encontrado"
    )