from memory.memory_manager import load_memory


def get_project_dashboard():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    features = project.get("features", [])
    tasks = project.get("tasks", [])
    completed = project.get("completed_tasks", [])
    timeline = project.get("timeline", [])

    pending = len(tasks) - len(completed)

    if len(tasks) > 0:
        progress = int((len(completed) / len(tasks)) * 100)
    else:
        progress = 0

    dashboard = f"PROJECT DASHBOARD\n\n"

    dashboard += f"Project: {current_project}\n\n"

    dashboard += f"Features: {len(features)}\n"
    dashboard += f"Tasks: {len(tasks)}\n"
    dashboard += f"Completed: {len(completed)}\n"
    dashboard += f"Pending: {pending}\n"
    dashboard += f"Progress: {progress}%\n\n"

    dashboard += "Recent Activity:\n"

    if timeline:
        for item in reversed(timeline[-5:]):
            dashboard += f"- {item['activity']}\n"
    else:
        dashboard += "- No activity found\n"

    return dashboard