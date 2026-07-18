from google import genai
from dotenv import load_dotenv
import os
import numpy as np

from config import EMBEDDING_MODEL

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)


def create_embeddings(chunks):
    """
    Creates embeddings for all text chunks.
    """

    try:

        embeddings = []

        BATCH_SIZE = 100

        for i in range(0, len(chunks), BATCH_SIZE):

            batch = chunks[i:i + BATCH_SIZE]

            response = client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=batch
            )

            for embedding in response.embeddings:
                embeddings.append(embedding.values)

        return np.array(
            embeddings,
            dtype="float32"
        )

    except Exception as e:

        raise RuntimeError(
            f"Embedding Error: {e}"
        )