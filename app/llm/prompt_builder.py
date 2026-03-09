def build_prompt(question, contexts):

    context_text = "\n\n".join(contexts)

    prompt = f"""
You are an AI assistant that answers questions based only on the provided context.

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt