from memory.memory_manager import load_memory, save_memory


def save_generated_tasks(tasks):
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    for task in tasks:
        if task not in project["tasks"]:
            project["tasks"].append(task)

    save_memory(memory)

    return f"{len(tasks)} tasks added to {current_project}, Sir."