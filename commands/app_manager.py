import os
import subprocess

from commands.app_database import get_app
from brain.conversation_engine import (
    remember_application,
    last_application
)
def close_app(app_name):

    app_path = get_app(app_name)

    if not app_path:
        return f"I couldn't find {app_name}, Sir."

    exe_name = os.path.basename(app_path)

    print("Closing:", exe_name)

    try:

        subprocess.run(
            ["taskkill", "/IM", exe_name, "/F"],
            capture_output=True,
            text=True
        )

        return f"Closing {app_name.title()}, Sir."

    except Exception as e:

        return f"Unable to close {app_name}. Error: {e}"

def reopen_last_app():

    app = last_application()

    if not app:
        return "There is no recently opened application, Sir."

    from commands.app_control import open_app

    return open_app(app)
