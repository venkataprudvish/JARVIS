import json
import os


CONTEXT_FILE = "memory/current_context.json"


def save_context(data):

    os.makedirs("memory", exist_ok=True)

    with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_context():

    if not os.path.exists(CONTEXT_FILE):
        return {}

    try:

        with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return {}