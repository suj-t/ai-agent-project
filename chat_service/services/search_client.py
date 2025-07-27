# chat_service/services/search_client.py
import requests

SEARCH_SERVICE_URL = "http://localhost:8002/search"

def search_web(query: str):
    try:
        response = requests.get(SEARCH_SERVICE_URL, params={"query": query})
        if response.status_code == 200:
            data = response.json()
            return data.get("result")
    except:
        pass
    return "No search result found."
