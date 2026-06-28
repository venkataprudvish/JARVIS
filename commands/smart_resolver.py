import webbrowser

from commands.app_launcher import launch_app
from commands.web_launcher import open_website
from commands.website_resolver import resolve_website
from commands.url_manager import resolve_url


def smart_open(name):


    name = name.lower().strip()

    # STEP 1 - Installed App
    response = launch_app(name)

    if response:
        return response

    # STEP 2 - Known Website
    response = open_website(name)


    if response:
        return response

    # STEP 3 - Website Cache Resolver
    response = resolve_website(name)

    if response:
        return response

    # STEP 4 - URL Manager

    response = resolve_url(name)

    if response:
        return response

    return f"Sorry Sir, I couldn't open {name}."