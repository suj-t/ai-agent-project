# chat_service/app.py
from fastapi import FastAPI
from routes.chat_routes import router as chat_router
from services.llm_service import get_llm_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chat Service")


app.add_middleware(
    CORSMiddleware,
      allow_origins=["http://localhost:5500"],  # Allow all origins for testing. Use ["http://localhost:5500"] for specific
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include chat routes
app.include_router(chat_router)

# Run with: uvicorn app:app --reload --port 8000
