from memory.memory_manager import load_memory, save_memory
from commands.timeline_manager import log_activity


def add_task(task):
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    memory["projects"][current_project]["tasks"].append(task)

    save_memory(memory)

    log_activity(f"Added task: {task}")

    return f"Task '{task}' added to {current_project}, Sir."


def get_tasks():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    tasks = memory["projects"][current_project]["tasks"]

    if not tasks:
        return f"No tasks found for {current_project}, Sir."

    return f"{current_project} tasks: " + ", ".join(tasks)