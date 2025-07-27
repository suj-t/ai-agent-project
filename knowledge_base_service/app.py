from fastapi import FastAPI
from routes.ingest_route import router as ingest_router
from routes.query_route import router as query_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Knowledge Base Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ingest_router)
app.include_router(query_router)

# Run: uvicorn app:app --reload --port 8001
