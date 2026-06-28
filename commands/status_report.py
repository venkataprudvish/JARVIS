from memory.memory_manager import load_memory


def generate_status_report():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    features = project.get("features", [])
    tasks = project.get("tasks", [])
    completed = project.get("completed_tasks", [])
    timeline = project.get("timeline", [])

    pending = [task for task in tasks if task not in completed]

    if len(tasks) > 0:
        progress = int((len(completed) / len(tasks)) * 100)
    else:
        progress = 0

    report = f"PROJECT STATUS REPORT\n\n"

    report += f"Project: {current_project}\n"
    report += f"Progress: {progress}%\n\n"

    report += "Features:\n"

    if features:
        for feature in features:
            report += f"- {feature}\n"
    else:
        report += "- None\n"

    report += "\nCompleted Tasks:\n"

    if completed:
        for task in completed:
            report += f"✅ {task}\n"
    else:
        report += "None\n"

    report += "\nPending Tasks:\n"

    if pending:
        for task in pending[:5]:
            report += f"⏳ {task}\n"
    else:
        report += "None\n"

    report += "\nRecent Activity:\n"

    if timeline:
        for item in reversed(timeline[-5:]):
            report += f"• {item['activity']}\n"
    else:
        report += "No recent activity\n"

    report += "\nRecommended Next Tasks:\n"

    if pending:
        for i, task in enumerate(pending[:3], start=1):
            report += f"{i}. {task}\n"
    else:
        report += "Project completed, Sir.\n"

    return report