from utils.pdf_loader import load_pdf
from utils.chunking import split_text
from utils.embeddings import create_embeddings
from utils.vector_store import create_vector_store
from utils.rag import ask_rag

from utils.memory import (
    add_to_history,
    get_history,
    clear_history
)

print("=" * 50)
print("Hybrid AI Tutor Chatbot")
print("=" * 50)

history = clear_history()

index = None
chunks = None

choice = input(
    "Do you want to use a PDF? (y/n): "
).lower()

if choice == "y":

    pdf_path = input(
        "Enter PDF path: "
    )

    if not pdf_path.lower().endswith(".pdf"):

        print("Please provide a PDF file.")
        exit()

    try:

        print("\nLoading PDF...")

        text = load_pdf(pdf_path)

        if not text.strip():

            print("PDF contains no readable text.")
            exit()

        print("Creating Chunks...")

        chunks = split_text(text)
        print(f"Total Chunks: {len(chunks)}")

        if len(chunks) == 0:

            print("No chunks created.")
            exit()

        print("Creating Embeddings...")

        embeddings = create_embeddings(chunks)

        print("Building Vector Database...")

        index = create_vector_store(
            embeddings
        )

        print("\nPDF Ready!\n")

    except FileNotFoundError:

        print("PDF not found.")
        exit()

    except Exception as e:

        print(e)
        exit()

else:

    print("\nRunning in General AI Mode.\n")

# ---------------------------------------
# Chat Loop
# ---------------------------------------

while True:

    question = input("You: ")

    if question.lower() == "exit":

        print("\nGoodbye!")
        break

    if not question.strip():

        continue

    add_to_history(
        history,
        "user",
        question
    )

    answer = ask_rag(
        question,
        history,
        index,
        chunks
    )

    print("\nBot:", answer)
    print()

    add_to_history(
        history,
        "model",
        answer
    )