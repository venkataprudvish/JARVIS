import os
import subprocess


def close_app(app_name):

    app_path = get_app(app_name)

    if not app_path:
        return f"I couldn't find {app_name}, Sir."

    exe_name = os.path.basename(app_path)

    print("Closing process:", exe_name)

    result = subprocess.run(
        ["taskkill", "/F", "/IM", exe_name],
        capture_output=True,
        text=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode == 0:
        return f"Closing {app_name.title()}, Sir."

    return f"Unable to close {app_name.title()}, Sir."