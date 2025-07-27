import re

def determine_route(query: str) -> str:
    query_lower = query.lower()

    if re.search(r"\b(what is|define|explain|how does|describe)\b", query_lower):
        return "KB"
    elif re.search(r"\b(latest|news|now|today|current|trending|live)\b", query_lower):
        return "Web"
    elif re.search(r"\b(write|story|note|essay|review|summarize|generate|create)\b", query_lower):
        return "LLM"
    else:
        return "LLM"  # default to LLM
