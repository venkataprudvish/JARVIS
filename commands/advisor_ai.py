from ollama import chat
from brain.context_builder import build_project_context


def ai_project_advisor(question):
    project_context = build_project_context()

    system_prompt = f"""
You are JARVIS, an expert software architect and project mentor.

Current Project Context:
{project_context}

Instructions:
- Analyze the current project.
- Use the project context when answering.
- Give practical recommendations.
- Suggest next actions when appropriate.
- Keep answers concise but useful.
"""

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]