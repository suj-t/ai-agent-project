from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Message(BaseModel):
    chat_id: str
    role: str  # "user" or "assistant"
    message: str
    timestamp: Optional[int]