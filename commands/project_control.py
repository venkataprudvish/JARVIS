from memory.memory_manager import load_memory, save_memory
from commands.timeline_manager import log_activity


def add_project_feature(feature):
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    memory["projects"][current_project]["features"].append(feature)

    save_memory(memory)

    log_activity(f"Added feature: {feature}")

    return f"Feature '{feature}' added to {current_project}, Sir."


def add_project_note(note):
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    memory["projects"][current_project]["notes"].append(note)

    save_memory(memory)

    log_activity(f"Added note: {note}")

    return f"Note added to {current_project}, Sir."


def get_project_features():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    features = memory["projects"][current_project]["features"]

    if not features:
        return f"No features found for {current_project}, Sir."

    return f"{current_project} features: " + ", ".join(features)


def get_project_notes():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    notes = memory["projects"][current_project]["notes"]

    if not notes:
        return f"No notes found for {current_project}, Sir."

    return f"{current_project} notes: " + ", ".join(notes)


def get_project_summary():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    summary = f"Project: {current_project}\n\n"

    summary += "Features:\n"
    for feature in project["features"]:
        summary += f"- {feature}\n"

    summary += "\nNotes:\n"
    for note in project["notes"]:
        summary += f"- {note}\n"

    summary += "\nTasks:\n"
    for task in project["tasks"]:
        summary += f"- {task}\n"

    return summary