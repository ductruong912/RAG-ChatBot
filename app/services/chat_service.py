from app.retrieval.retriever import Retriever
from app.llm.prompt_builder import build_prompt
from app.llm.openai_client import generate_response


class ChatService:

    def __init__(self, vector_store):
        self.retriever = Retriever(vector_store)

    def chat(self, question):

        # 1 retrieve context
        contexts = self.retriever.retrieve(question)

        # 2 build prompt
        prompt = build_prompt(question, contexts)

        # 3 generate answer
        answer = generate_response(prompt)

        return {
            "answer": answer,
            "contexts": contexts
        }