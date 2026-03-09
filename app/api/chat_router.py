from fastapi import APIRouter
from app.schema.chat_schema import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    response = ChatService.chat(request.message)
    return response
