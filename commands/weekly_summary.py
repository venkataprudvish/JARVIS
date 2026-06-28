from memory.memory_manager import load_memory


def generate_weekly_summary():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    features = project.get("features", [])
    tasks = project.get("tasks", [])
    completed = project.get("completed_tasks", [])
    timeline = project.get("timeline", [])

    progress = 0

    if len(tasks) > 0:
        progress = int((len(completed) / len(tasks)) * 100)

    summary = "WEEKLY PROJECT SUMMARY\n\n"

    summary += f"Project: {current_project}\n\n"

    summary += "Features Added:\n"

    if features:
        for feature in features[:5]:
            summary += f"- {feature}\n"
    else:
        summary += "- None\n"

    summary += "\nCompleted Tasks:\n"

    if completed:
        for task in completed[:5]:
            summary += f"✅ {task}\n"
    else:
        summary += "None\n"

    summary += f"\nCurrent Progress: {progress}%\n\n"

    summary += "Recent Activities:\n"

    if timeline:
        for item in reversed(timeline[-5:]):
            summary += f"• {item['activity']}\n"
    else:
        summary += "No recent activity\n"

    pending = [task for task in tasks if task not in completed]

    summary += "\nNext Priority:\n"

    if pending:
        summary += pending[0]
    else:
        summary += "Project completed, Sir."

    return summary