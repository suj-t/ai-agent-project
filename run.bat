@echo off
echo Starting AI Agent Microservices...

start cmd /k "cd chat_service && python -m uvicorn app:app --reload --port 8000"
start cmd /k "cd knowledge_base_service && python -m uvicorn app:app --reload --port 8001"
start cmd /k "cd search_service && python -m uvicorn app:app --reload --port 8002"
start cmd /k "cd history_service && python -m uvicorn app:app --reload --port 8003"
start cmd /k "cd frontend && python -m http.server 5500"



REM 
start http://localhost:5500

echo All services and frontend started!
pause
