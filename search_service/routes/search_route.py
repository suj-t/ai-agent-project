from fastapi import APIRouter, Query
from services.duckduckgo_scraper import get_search_result

router = APIRouter()

@router.get("/search")
async def search(query: str = Query(...)):
    result = get_search_result(query)
    return {"result": result}
