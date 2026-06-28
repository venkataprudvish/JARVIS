import os
import json
from ollama import chat


def build_project(project_name):

    folder = project_name.replace(" ", "_")

    os.makedirs(folder, exist_ok=True)

    prompt = f"""
You are an expert software engineer.

Create a complete Python project named:

{project_name}

Generate ALL of these files:

main.py
utils.py
config.py
README.md
requirements.txt
.gitignore
tests/test_main.py

Return ONLY valid JSON.

Example:

{{
    "main.py": "content",
    "utils.py": "content",
    "config.py": "content",
    "README.md": "content",
    "requirements.txt": "content",
    ".gitignore": "content",
    "tests/test_main.py": "content"
}}

Do not explain anything.
Do not use markdown.
Return only JSON.
"""

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    try:
        files = json.loads(response["message"]["content"])

    except Exception as e:
        return f"JSON Error: {e}"

    for filename, content in files.items():

        full_path = os.path.join(folder, filename)

        parent = os.path.dirname(full_path)

        if parent:
            os.makedirs(parent, exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    return f"{project_name} created successfully."