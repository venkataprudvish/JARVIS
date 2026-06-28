import webbrowser

from commands.website_cache import (
    get_website,
    add_website
)


def resolve_website(name):

    # STEP 1 - Check Cache
    cached = get_website(name)

    if cached:
        webbrowser.open(cached)
        return f"Opening {name} from cache, Sir."

    # STEP 2
    return None