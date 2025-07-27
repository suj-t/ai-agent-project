from typing import Optional
from pydantic import BaseModel


class ChatRequest(BaseModel):
    chat_id: str
    message: str
    model: Optional[str] = "together"  # or "gemini"
