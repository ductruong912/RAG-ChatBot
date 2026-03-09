import pickle
from fastapi import APIRouter
from app.schema.chat_schema import ChatRequest
from app.services.chat_service import ChatService

with open("vector_store.pkl", "rb") as f:
    vector_store = pickle.load(f)

chat_service = ChatService(vector_store)

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    response = chat_service.chat(request.message)
    return response
