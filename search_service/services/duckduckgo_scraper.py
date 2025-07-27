import requests
from bs4 import BeautifulSoup

def get_search_result(query):
    try:
        # ✅ Only scrape if query starts with 'scrap'
        if query.lower().startswith("scrap"):
            print("Scraping DuckDuckGo Lite...")
            return scrape_duckduckgo(query)

        # ✅ Otherwise, use DuckDuckGo Instant Answer API
        print("Using DuckDuckGo API...")
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url)
        data = response.json()

        result = data.get("AbstractText")
        if result:
            return result
        else:
            return "No direct answer found. Try a different query or use 'scrap' for web scraping."
    except Exception as e:
        return f"Search failed: {e}"

def scrape_duckduckgo(query):
    try:
        url = f"https://lite.duckduckgo.com/lite/?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        results = soup.find_all("a", class_="result-link")
        if not results:
            return "No search results found via scraping."

        top_results = []
        for r in results[:3]:
            title = r.text.strip()
            link = r.get("href")
            top_results.append(f"{title} - {link}")

        return "\n".join(top_results)

    except Exception as e:
        return f"Scraping failed: {e}"
