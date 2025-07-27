from fastapi import APIRouter
from pydantic import BaseModel
from services.chroma_handler import query_documents

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.get("/query")
async def query_kb(req: QueryRequest):
    result = query_documents(req.query)
    return {"result": result}
