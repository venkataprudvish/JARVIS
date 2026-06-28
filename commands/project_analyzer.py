import os
from ollama import chat


def analyze_project():

    project_root = os.getcwd()

    total_files = 0
    total_lines = 0

    python_files = []

    for root, dirs, files in os.walk(project_root):

        dirs[:] = [
            d for d in dirs
            if d not in [".venv", "__pycache__", ".git"]
        ]

        for file in files:

            if file.endswith(".py"):

                total_files += 1

                file_path = os.path.join(root, file)

                python_files.append(file)

                try:

                    with open(file_path, "r", encoding="utf-8") as f:

                        lines = len(f.readlines())

                        total_lines += lines

                except:
                    pass

    report = f"""
PROJECT ANALYSIS

Python Files: {total_files}

Total Lines Of Code: {total_lines}

Files:

"""

    for file in python_files:

        report += f"- {file}\n"

    return report


def analyze_project_ai():

    report = analyze_project()

    prompt = f"""
Analyze this software project report.

Give:

1. Project Health Score out of 10
2. Strengths
3. Weaknesses
4. Missing Features
5. Recommended Next Steps

Project Report:

{report}
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