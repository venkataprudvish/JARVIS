import os
import subprocess

from commands.app_database import get_app


def launch_app(app_name):

    app_path = get_app(app_name)

    if not app_path:
        return None

    try:

        # Shortcut (.lnk)
        if app_path.lower().endswith(".lnk"):
            os.startfile(app_path)
            return f"Opening {app_name.title()}, Sir."

        # Executable (.exe)
        subprocess.Popen(app_path)

        return f"Opening {app_name.title()}, Sir."

    except Exception as e:
        return f"Unable to open {app_name}. Error: {e}"