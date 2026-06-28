from memory.memory_manager import load_memory


def build_project_context():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project."

    project = memory["projects"][current_project]

    context = f"""
Current Project: {current_project}

Features:
{project["features"]}

Tasks:
{project["tasks"]}

Notes:
{project["notes"]}
"""

    return context