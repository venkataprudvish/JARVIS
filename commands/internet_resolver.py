import requests

from config import TAVILY_API_KEY


def search_official_site(name):



    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": f"{name} official website",
        "search_depth": "basic",
        "max_results": 5
    }

    try:

        response = requests.post(url, json=payload)

        response.raise_for_status()

        data = response.json()

        if "results" not in data:
            return None

        blocked_domains = [
            "linkedin.com",
            "wikipedia.org",
            "crunchbase.com",
            "facebook.com",
            "x.com",
            "twitter.com",
            "youtube.com"
        ]

        for result in data["results"]:

            url = result["url"].lower()

            blocked = False

            for domain in blocked_domains:
                if domain in url:
                    blocked = True
                    break

            if not blocked:
                return result["url"]

        return None

    except Exception as e:
        print("Tavily Error:", e)
        return None