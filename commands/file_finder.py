import os


def find_file(name):

    project_root = os.getcwd()

    search_name = (
        name.lower()
        .replace(".py", "")
        .replace("_", " ")
        .replace("-", " ")
        .strip()
    )

    print("SEARCH NAME =", search_name)

    best_match = None

    for root, dirs, files in os.walk(project_root):

        dirs[:] = [
            d for d in dirs
            if d not in [".venv", "__pycache__", ".git"]
        ]

        for file in files:

            clean_file = (
                file.lower()
                .replace(".py", "")
                .replace("_", " ")
            )

            print("SEARCH NAME =", search_name)

            # Exact match
            if search_name == clean_file:
                return file

            # Partial match
            if search_name in clean_file:
                return file

            # Reverse partial match
            if clean_file in search_name:
                best_match = file

    if best_match:
        return best_match

    return None