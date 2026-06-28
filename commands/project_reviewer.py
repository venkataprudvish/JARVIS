import os


def get_project_files():

    project_root = os.getcwd()

    files_found = []

    for root, dirs, files in os.walk(project_root):

        # Skip unnecessary folders
        dirs[:] = [
            d for d in dirs
            if d not in [".venv", "__pycache__", ".git"]
        ]

        for file in files:

            if file.endswith(".py"):

                files_found.append(file)

    return files_found


def review_project():

    files = get_project_files()

    report = "PROJECT FILES:\n\n"

    for file in files:
        report += f"- {file}\n"

    report += f"\nTotal Python Files: {len(files)}"

    return report