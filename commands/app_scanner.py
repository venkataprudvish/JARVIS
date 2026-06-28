import os
import json

APP_DB = os.path.join("data", "apps.json")


SEARCH_FOLDERS = [

    os.path.join(os.environ["ProgramData"],
                 "Microsoft",
                 "Windows",
                 "Start Menu",
                 "Programs"),

    os.path.join(os.environ["APPDATA"],
                 "Microsoft",
                 "Windows",
                 "Start Menu",
                 "Programs"),

    r"C:\Program Files",

    r"C:\Program Files (x86)",

    os.path.expandvars(r"%LOCALAPPDATA%")
]


EXTENSIONS = (
    ".exe",
    ".lnk"
)


def scan_apps():

    apps = {}

    for folder in SEARCH_FOLDERS:

        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.lower().endswith(EXTENSIONS):

                    name = os.path.splitext(file)[0].lower()

                    path = os.path.join(root, file)

                    apps[name] = path

    os.makedirs("data", exist_ok=True)

    with open(APP_DB, "w", encoding="utf-8") as f:

        json.dump(apps, f, indent=4)

    return apps