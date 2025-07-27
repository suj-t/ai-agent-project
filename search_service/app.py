from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.search_route import router as search_router

app = FastAPI(title="Search Service")

# Enable CORS for Swagger
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router)

# Run: uvicorn app:app --reload --port 8002
