from app.llm.openai_client import generate_response

class ChatService:
    @staticmethod
    def chat(message: str):

        answer = generate_response(message)

        return {
            "answer": answer
        }