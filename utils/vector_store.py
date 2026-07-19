import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Creates a FAISS vector database.
    """

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(
        embeddings,
        dtype="float32"
    )

    index.add(vectors)

    return index
