import webbrowser


def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"

    webbrowser.open(search_url)

    return f"Searching Google for {query}, Sir."