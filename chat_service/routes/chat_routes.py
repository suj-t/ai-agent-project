# chat_service/routes/chat_routes.py
from fastapi import APIRouter
from pydantic import BaseModel
from services.kb_client import query_knowledge_base
from services.search_client import search_web
from services.history_client import save_history
from utils.formatter import format_response
from services.llm_service import get_llm_response
from utils.detector import determine_route

router = APIRouter()

class ChatRequest(BaseModel):
    chat_id: str
    message: str
    model: str

@router.post("/chat")
async def chat_endpoint(chat_req: ChatRequest):
    query = chat_req.message
    chat_id = chat_req.chat_id
    model = chat_req.model.lower()  # "gemini" or "together"
    route = determine_route(query)
    response = ""
    source = ""

    try:
        if route == "KB":
            kb_result = query_knowledge_base(query)
            if kb_result and kb_result != "Error in search":
                response = format_response(kb_result, source="KB")
                source = "KB"
            else:
                route = "Web"  # fallback to Web

        if route == "Web" and not response:
            web_result = search_web(query)
            if web_result and web_result != "No search results found.":
                response = format_response(web_result, source="Web")
                source = "Web"
            else:
                route = "LLM"  # fallback to LLM

        if route == "LLM" and not response:
            llm_result = get_llm_response(query, model=model)
            response = format_response(llm_result, source=f"{model.upper()}")
            source = model.upper()

    except Exception as e:
        response = f"[Error] {str(e)}"
        source = "Error"

    save_history(chat_id, query, response)
    return {"chat_id": chat_id, "response": response}



# @router.post("/chat")
# async def chat_endpoint(chat_req: ChatRequest):
#     query = chat_req.message
#     chat_id = chat_req.chat_id

#     # 1. Try Knowledge Base
#     kb_result = query_knowledge_base(query)
#     if kb_result:
#         response = format_response(kb_result, source="KB")

#     else:
#         # 2. Try Web Search
#         search_result = search_web(query)
        
#         if search_result and search_result != "No search result found.":
#             response = format_response(search_result, source="Web")
#         else:
#             # 3. Fallback to LLM
#             llm_result = get_llm_response(query)
#             response = format_response(llm_result, source="LLM")

#     # Save history (regardless of which source was used)
#     save_history(chat_id, query, response)

#     return {"chat_id": chat_id, "response": response}


# @router.post("/chat")
# async def chat_endpoint(chat_req: ChatRequest):
#     query = chat_req.message
#     chat_id = chat_req.chat_id

#     # Try knowledge base first
#     kb_result = query_knowledge_base(query)
#     if kb_result:
#         response = format_response(kb_result, source="KB")
#     else:
#         # Fallback to web search
#         search_result = search_web(query)
#         response = format_response(search_result, source="Web")

#     # Save history
#     save_history(chat_id, query, response)

#     return {"chat_id": chat_id, "response": response}
