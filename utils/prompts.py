def build_prompt(context, conversation, question):

    if context.strip():

        return f"""
You are an AI Tutor.

You MUST answer using ONLY the information from the provided context.

If the answer is not present in the context,
reply exactly:

"I couldn't find that information in the uploaded PDF."

Do NOT use your own knowledge when context is available.

Previous Conversation:
{conversation}

Context:
{context}

Question:
{question}

Answer:
"""

    return f"""
You are a helpful AI Assistant.

Previous Conversation:
{conversation}

Question:
{question}

Answer:
"""
