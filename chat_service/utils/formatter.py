# chat_service/utils/formatter.py
def format_response(result: str, source: str):
    return f"[{source}] {result}"
