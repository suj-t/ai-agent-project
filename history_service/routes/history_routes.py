# routes/history_routes.py
from fastapi import APIRouter
from models.message_model import Message
from services.db_handler import save_message, get_history

router = APIRouter()

@router.post("/history")
def save_chat(message: Message):
    save_message(message.chat_id, message.message, message.role, message.timestamp)

    return {"status": "saved"}

@router.get("/history/{chat_id}")
def fetch_history(chat_id: str):
    history = get_history(chat_id)
    return {"chat_id": chat_id, "messages": history}
