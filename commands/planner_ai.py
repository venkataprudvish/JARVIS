from ollama import chat
from brain.context_builder import build_project_context
from commands.task_generator import save_generated_tasks


def create_implementation_plan(topic):
    project_context = build_project_context()

    system_prompt = f"""
You are JARVIS, a senior software architect.

Current Project Context:
{project_context}

Instructions:
- Create an implementation plan.
- Return exactly 6 numbered steps.
- Keep each step short.
- Each step should be a task.
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
                "content": f"Create implementation plan for {topic}"
            }
        ]
    )

    plan = response["message"]["content"]

    tasks = []

    for line in plan.split("\n"):
        line = line.strip()

        if (
            line.startswith("1.")
            or line.startswith("2.")
            or line.startswith("3.")
            or line.startswith("4.")
            or line.startswith("5.")
            or line.startswith("6.")
        ):
            task = line[2:].strip()
            tasks.append(task)

    if tasks:
        save_generated_tasks(tasks)

    return plan