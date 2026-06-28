import webbrowser

from commands.website_cache import get_website, add_website
from commands.internet_resolver import search_official_site


def resolve_url(name):

    # STEP 1 - Cache
    cached = get_website(name)

    if cached:
        webbrowser.open(cached)
        return f"Opening {name.title()} from cache, Sir."

    # STEP 2 - Tavily
    url = search_official_site(name)

    if url:
        add_website(name, url)
        webbrowser.open(url)
        return f"Opening official website of {name.title()}, Sir."

    # STEP 3 - Google Backup
    webbrowser.open(
        f"https://www.google.com/search?q={name}+official+website"
    )

    return f"Tavily unavailable. Searching Google for {name}, Sir."