from app.services.memory_service import MemoryService
from app.llm.prompt_builder import build_prompt
from app.llm.openai_client import generate_response


class ChatService:

    def __init__(self, retriever):

        self.retriever = retriever

    def chat(self, session_id, message):

        # load history
        history = MemoryService.get_history(session_id)

        # retrieval
        contexts = self.retriever.retrieve(message)

        # build prompt
        prompt = build_prompt(message, contexts, history)

        # LLM
        answer = generate_response(prompt)

        # save memory
        MemoryService.save_user_message(session_id, message)
        MemoryService.save_ai_message(session_id, answer)

        return {
            "answer": answer,
            "contexts": contexts
        }