# chat_service/services/history_client.py
import requests

HISTORY_SERVICE_URL = "http://localhost:8003/history"

def save_history(chat_id: str, user_msg: str, bot_msg: str):
    payload = {"chat_id": chat_id, "user": user_msg, "bot": bot_msg}
    try:
        requests.post(HISTORY_SERVICE_URL, json=payload)
    except:
        pass
