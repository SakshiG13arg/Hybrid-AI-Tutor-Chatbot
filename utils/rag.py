from google import genai
from dotenv import load_dotenv
import os
import numpy as np

from utils.prompts import build_prompt
from utils.generation import generation_config

from config import (
    MODEL_NAME,
    EMBEDDING_MODEL,
    TOP_K,
    SIMILARITY_THRESHOLD
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)


def ask_rag(question, history, index=None, chunks=None):
    """
    Hybrid chatbot.

    Uses PDF when relevant.
    Otherwise answers normally.
    """

    context = ""

    # -----------------------------
    # Retrieve PDF Context
    # -----------------------------

    if index is not None and chunks is not None:

        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=question
        )

        question_embedding = np.array(
            [response.embeddings[0].values],
            dtype="float32"
        )

        distances, indices = index.search(
    question_embedding,
    k=TOP_K
)

    for distance, idx in zip(distances[0], indices[0]):

        if idx != -1 and distance < SIMILARITY_THRESHOLD:

            context += chunks[idx] + "\n\n"

    # -----------------------------
    # Conversation History
    # -----------------------------

    conversation = ""

    recent_history = history[-10:]

    for message in recent_history:

        role = message["role"]

        content = message["parts"][0]["text"]

        conversation += f"{role}: {content}\n"

    # -----------------------------
    # Prompt
    # -----------------------------

    prompt = build_prompt(
        context,
        conversation,
        question
    )

    # -----------------------------
    # Gemini
    # -----------------------------

    try:

        answer = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=generation_config
        )

        return answer.text

    except Exception as e:

        print("\n========== GEMINI ERROR ==========")
        print(type(e).__name__)
        print(e)
        print("==================================\n")

        return "Sorry, I couldn't generate a response right now."
