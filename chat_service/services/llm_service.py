import requests
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()

# Get the Together.ai API key from environment variables
TOGETHER_API_KEY = "put your together api key"
#how to get together api key visit https://api.together.xyz/
GEMINI_API_KEY = "put gemini key here"



def query_together(prompt: str) -> str:
    url = "https://api.together.xyz/inference"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    refined_prompt = f"Write a short, factual, and formal note in 1-2 paragraphs on the topic below. Do not ask questions or include personal opinions.\n\nTopic: {prompt}\n\nNote:"
    
    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "prompt": refined_prompt,
        "max_tokens": 900,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        output = data.get("output")
        if output and "choices" in output and len(output["choices"]) > 0:
            llm_text = output["choices"][0].get("text", "").strip()
            return llm_text if llm_text else "LLM returned empty response."
        else:
            return "LLM returned no choices."
    except Exception as e:
        return f"Together LLM error: {str(e)}"

# ----------------- GEMINI HANDLER -----------------
def query_gemini(prompt: str) -> str:
#    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        candidates = data.get("candidates", [])
        if candidates:
            text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()
            return text if text else "Gemini returned empty response."
        else:
            return "Gemini returned no candidates."
    except Exception as e:
        if hasattr(e, 'response'):
            print(f"Response status: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return f"Gemini LLM error: {str(e)}"

# ----------------- UNIFIED INTERFACE -----------------
def get_llm_response(prompt: str, model: str = "together") -> str:
    print("model::"+model)
    if model == "together":
        return query_together(prompt)
    elif model == "gemini":
        return query_gemini(prompt)
    else:
        return "Invalid model specified."
