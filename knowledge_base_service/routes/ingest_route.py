from fastapi import APIRouter
from services.chroma_handler import ingest_documents

router = APIRouter()

@router.post("/ingest")
async def ingest():
    success = ingest_documents()
    return {"status": "success" if success else "failed"}
