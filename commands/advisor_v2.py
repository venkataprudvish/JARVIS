from memory.memory_manager import load_memory


def analyze_current_project():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    features = project["features"]
    tasks = project["tasks"]
    notes = project["notes"]

    report = f"Project Analysis: {current_project}\n\n"

    report += f"Features Count: {len(features)}\n"
    report += f"Tasks Count: {len(tasks)}\n"
    report += f"Notes Count: {len(notes)}\n\n"

    if len(features) < 3:
        report += "Recommendation: Add more core features.\n"

    if len(tasks) < len(features):
        report += "Recommendation: Create implementation tasks for all features.\n"

    if not notes:
        report += "Recommendation: Add project notes and design decisions.\n"

    report += "\nProject looks good, Sir."

    return report


def get_next_task_smart():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    tasks = project["tasks"]

    if not tasks:
        return "No tasks found. Create some tasks first, Sir."

    return (
        f"For {current_project}, "
        f"I recommend working on '{tasks[0]}' next because it is the first pending task."
    )