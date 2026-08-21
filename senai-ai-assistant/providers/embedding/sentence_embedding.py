# providers/embedding/sentence_embedding.py
from sentence_transformers import (SentenceTransformer)
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate(text):
    return model.encode(text)
