from memory.memory_manager import load_memory


def get_today_recommendations():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    tasks = project.get("tasks", [])
    completed = project.get("completed_tasks", [])

    pending = [task for task in tasks if task not in completed]

    if not pending:
        return (
            f"Excellent work, Sir. "
            f"All tasks in {current_project} are completed."
        )

    recommendations = pending[:3]

    report = f"Project: {current_project}\n\n"
    report += "Recommended Tasks For Today:\n\n"

    for i, task in enumerate(recommendations, start=1):
        report += f"{i}. {task}\n"

    report += "\nReason:\n"
    report += "These are the highest-priority pending tasks."

    return report