from datetime import datetime
from memory.memory_manager import load_memory, save_memory


def log_activity(activity):
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return

    project = memory["projects"][current_project]

    if "timeline" not in project:
        project["timeline"] = []

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    project["timeline"].append(
        {
            "time": timestamp,
            "activity": activity
        }
    )

    save_memory(memory)


def get_project_history():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    timeline = project.get("timeline", [])

    if not timeline:
        return f"No history found for {current_project}, Sir."

    report = f"Project History: {current_project}\n\n"

    for item in reversed(timeline):
        report += f"{item['time']}\n"
        report += f"• {item['activity']}\n\n"

    return report