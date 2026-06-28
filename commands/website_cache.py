import json
import os

CACHE_FILE = os.path.join("data", "websites.json")


def load_cache():

    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cache(cache):

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)


def get_website(name):

    cache = load_cache()

    return cache.get(name.lower())


def add_website(name, url):

    cache = load_cache()

    cache[name.lower()] = url

    save_cache(cache)