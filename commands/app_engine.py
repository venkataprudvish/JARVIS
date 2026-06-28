import json
import os

from commands.app_scanner import scan_apps
from commands.registry_scanner import scan_registry
from commands.store_scanner import scan_store_apps

APP_DB = os.path.join("data", "apps.json")


def build_database():

    apps = {}

    print("Scanning Start Menu...")
    apps.update(scan_apps())

    print("Scanning Windows Registry...")
    apps.update(scan_registry())

    print("Scanning Microsoft Store Apps...")
    apps.update(scan_store_apps())

    os.makedirs("data", exist_ok=True)

    with open(APP_DB, "w", encoding="utf-8") as f:
        json.dump(apps, f, indent=4)

    print(f"\nTotal Apps Found: {len(apps)}")

    return apps