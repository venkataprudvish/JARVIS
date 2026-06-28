import os


def read_file(filename):

    project_root = os.getcwd()

    print("SEARCHING FOR:", filename)

    for root, dirs, files in os.walk(project_root):

        for file in files:

            print("FOUND FILE:", file)

            # Exact filename match
            if file.lower() == filename.lower():

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        return f.read()

                except Exception as e:
                    return f"Error reading file: {e}"

            # Match vision control -> vision_control.py
            clean_file = file.lower().replace("_", " ").replace(".py", "")
            clean_input = filename.lower().replace(".py", "")

            if clean_file == clean_input:

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        return f.read()

                except Exception as e:
                    return f"Error reading file: {e}"

    return f"File {filename} not found."