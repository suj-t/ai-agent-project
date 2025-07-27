# chat_service/services/kb_client.py
import requests

KB_SERVICE_URL = "http://localhost:8001/query"

def query_knowledge_base(query: str):
    try:
        response = requests.post(KB_SERVICE_URL, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            return data.get("result")
    except:
        pass
    return None
