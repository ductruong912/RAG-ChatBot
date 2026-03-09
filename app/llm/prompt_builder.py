def build_prompt(question, contexts, history):

    context_text = "\n".join(contexts)

    history_text = ""

    for h in history[-5:]:
        history_text += f"{h['role']}: {h['content']}\n"

    prompt = f"""
You are an AI assistant answering questions using provided context.

Conversation History:
{history_text}

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt