from crewai.tools import tool

@tool
def google_search(query: str, num_results: int = 2, max_chars: int = 500) -> str:
    """Search Google for information, returns results with a snippet and body content."""
    import requests, time
    from bs4 import BeautifulSoup
    from dotenv import load_dotenv

    load_dotenv()
    api_key = "AIzaSyCTpU6r9lpy4B3OoJ0RGINPCOQ8vfB3-S4"
    search_engine_id = "d42ba021527284c1d"

    url = "https://customsearch.googleapis.com/customsearch/v1"
    params = {"key": api_key, "cx": search_engine_id, "q": query, "num": num_results}
    response = requests.get(url, params=params)
    results = response.json().get("items", [])

    def get_page_content(url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            return " ".join(text.split()[:max_chars])
        except Exception as e:
            return f"Error fetching {url}: {str(e)}"

    enriched_results = []
    for item in results:
        body = get_page_content(item["link"])
        enriched_results.append(f"{item['title']}\n{item['snippet']}\n{body}\n\n")
        time.sleep(1)

    return "\n".join(enriched_results)
