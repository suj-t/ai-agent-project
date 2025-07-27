🧠 AI Agent Project – Complete Setup Guide

This guide helps you clone, configure, and run the AI Agent Project on your machine without Docker, using Python, FastAPI, and Chromadb. This includes frontend setup and running all microservices.

sortcut
conse repo 
download requirements 
run batch file 
done 
    -sujal
if its not working see below 

🧰 Prerequisites
Tool	Purpose
Python 3.10+	Required to run all backend services
Git	Clone the repository
Node.js + npm	(Optional) For Angular frontend (if applicable)
MongoDB	Required for storing history data (local or Atlas)
Internet Access	For LLM API access (TogetherAI, Gemini)

🐍 Python Setup

    Install Python 3.10+
    Download Python and install with Add to PATH enabled.
    Install pip and virtualenv (optional but recommended)

pip install virtualenv

Clone the Repository
git clone https://github.com/suj-t/ai-agent-project.git

cd ai-agent-project
Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install Required Packages

    pip install -r requirements.txt

⚙️ Environment Variables (.env)

Create a .env file in the project root and add your API keys and MongoDB URI:

TOGETHER_API_KEY=your_together_api_key
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=mongodb://localhost:27017  # Or your MongoDB Atlas URI

▶️ Run All Services at Once (Windows)

Use the pre-configured batch script:

run_all.bat

This script will:

    Start chat_service on port 8000

    Start knowledge_base_service on port 8001

    Start search_service on port 8002

    Start history_service on port 8003

    Launch frontend at http://localhost:5500 using Python’s HTTP server

🚀 Manual Service Run (Optional)

Each service is FastAPI-based. You can run them manually:
1. Chat Service (Port 8000)

cd chat_service
uvicorn main:app --reload --port 8000

2. Knowledge Base Service (Port 8001)

cd knowledge_base_service
uvicorn main:app --reload --port 8001

3. Search Service (Port 8002)

cd search_service
uvicorn main:app --reload --port 8002

4. History Service (Port 8003)

cd history_service
uvicorn main:app --reload --port 8003

5. Frontend (Port 5500)

cd frontend
python -m http.server 5500

Visit http://localhost:5500 in your browser.
📚 Ingesting Knowledge Base Documents

    Add .txt files inside knowledge_base_service/data/docs/.

    Use Swagger UI:
    Visit http://localhost:8001/docs, then POST /ingest.

    OR run this via curl:

    curl -X POST http://localhost:8001/ingest

🗨️ How It Works
Query Route	Description
Knowledge Base	First checks documents using semantic search (ChromaDB + embedding)
Web Search	If KB fails, scrapes DuckDuckGo Lite for relevant info
LLM Fallback	If search fails, uses TogetherAI or Gemini LLM to generate a response
History Storage	All messages stored using MongoDB via History Service
🧪 Testing the Project

    Open browser: http://localhost:5500

    Type a message → Choose LLM → Send

    Toggle history → See previous messages

    Try KB queries like:
    FastAPI usage, Who made FastAPI, etc.

    For web search: Start message with scrap, e.g.,
    scrap Elon Musk, scrap OpenAI CEO.

🐞 Troubleshooting
Problem	Solution
API Key Errors	Ensure .env file is set correctly
Port Already in Use	Change port in uvicorn or shut conflicting app
Chat Not Responding	Check service logs → Ensure all 4 services are running
Frontend Not Loading	Check you’re running python -m http.server 5500 inside frontend
LLM Token Limit Exceeded	Increase max_tokens in query_together or query_gemini
MongoDB Not Connecting	Confirm URI, database is running, and correct port is used
