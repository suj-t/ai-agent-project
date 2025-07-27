from fastapi import FastAPI
from routes.history_routes import router as history_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="History Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],  # Or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(history_router)
