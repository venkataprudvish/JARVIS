import os
from ollama import chat


def analyze_jarvis():

    project_root = os.getcwd()

    jarvis_features = []

    for root, dirs, files in os.walk(project_root):

        dirs[:] = [
            d for d in dirs
            if d not in [".venv", "__pycache__", ".git"]
        ]

        for file in files:

            if file.endswith(".py"):

                jarvis_features.append(file)

    report = f"""
JARVIS PROJECT

Files Found:

{chr(10).join("- " + file for file in jarvis_features)}

Total Files: {len(jarvis_features)}
"""

    prompt = f"""
You are an expert AI software architect.

Analyze this JARVIS AI assistant project.

Give:

1. Jarvis Health Score out of 10
2. Completed Features
3. Missing Features
4. Weaknesses
5. Recommended Next Feature
6. Short Summary

Project Report:

{report}

Focus ONLY on improving JARVIS.
Ignore Smart Park and other unrelated projects.
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

    return response["message"]["content"]