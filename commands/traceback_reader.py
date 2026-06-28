import os


def get_latest_traceback():

    project_root = os.getcwd()

    latest_error = None

    for root, dirs, files in os.walk(project_root):

        dirs[:] = [
            d for d in dirs
            if d not in [".venv", "__pycache__", ".git"]
        ]

        for file in files:

            if file.endswith(".log") or file.endswith(".txt"):

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:

                        text = f.read()

                    if "Traceback" in text:

                        latest_error = text

                except:
                    pass

    return latest_error