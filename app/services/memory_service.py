from app.storage.session_store import SessionStore

session_store = SessionStore()


class MemoryService:

    @staticmethod
    def get_history(session_id):

        return session_store.get_history(session_id)

    @staticmethod
    def save_user_message(session_id, message):

        session_store.append(session_id, "user", message)

    @staticmethod
    def save_ai_message(session_id, message):

        session_store.append(session_id, "assistant", message)