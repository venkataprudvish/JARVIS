import os
import json
from commands.app_scanner import scan_apps

APP_DB = os.path.join("data", "apps.json")


def load_apps():

    if not os.path.exists(APP_DB):
        return scan_apps()

    with open(APP_DB, "r", encoding="utf-8") as f:
        return json.load(f)


def refresh_apps():
    return scan_apps()


def get_app(name):

    apps = load_apps()

    name = name.lower().strip()

    # Exact Match
    if name in apps:
        return apps[name]

    # Partial Match
    for app in apps:

        if name in app or app in name:
            return apps[app]

    # Word Match
    words = name.split()

    for app in apps:

        app_words = app.split()

        for word in words:

            if word in app_words:
                return apps[app]

    # Fuzzy Match
    for app in apps:

        if app.startswith(name):
            return apps[app]

    return None