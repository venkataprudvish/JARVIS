from ollama import chat


def generate_file(project_name, filename):

    prompt = f"""
You are an expert software engineer.

Project:
{project_name}

Generate ONLY the content for this file:

{filename}

Do not explain.
Do not use markdown.
Return only the file content.
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