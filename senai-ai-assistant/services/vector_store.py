# services/vector_store.py
import faiss
import numpy as np

def build_index(vectors):
    dimension = len(vectors[0])
    index = faiss.IndexFlatL2(
        dimension
    )
    index.add(
        np.array(vectors)
        .astype("float32")
    )
    return index
    
def search(
        index,
        question_vector,
        top_k=3):
    distances, indices = index.search(
        np.array(
            [question_vector]
        ).astype("float32"),
        top_k
    )
    return indices[0]