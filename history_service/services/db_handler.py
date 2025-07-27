# services/db_handler.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ai_agent_db"]
collection = db["chat_history"]

def save_message(chat_id, message, role, timestamp):
    doc = {"chat_id": chat_id, "role": role, "message": message, "timestamp": timestamp}
    collection.insert_one(doc)

def get_history(chat_id):
    messages = collection.find({"chat_id": chat_id}).sort("timestamp")
    return [{"role": m["role"], "message": m["message"], "timestamp": m["timestamp"]} for m in messages]
