from memory.memory_manager import load_memory, save_memory
from commands.timeline_manager import log_activity


def mark_task_complete(task_name):
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    if "completed_tasks" not in project:
        project["completed_tasks"] = []

    for task in project["tasks"]:
        if task.lower() == task_name.lower():

            if task not in project["completed_tasks"]:

                project["completed_tasks"].append(task)

                save_memory(memory)

                log_activity(f"Completed task: {task}")

                return f"Task '{task}' marked as completed, Sir."

            return "Task already completed, Sir."

    return "Task not found, Sir."


def get_project_progress():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    tasks = project["tasks"]
    completed = project.get("completed_tasks", [])

    if not tasks:
        return "No tasks available, Sir."

    percentage = int((len(completed) / len(tasks)) * 100)

    report = f"Project: {current_project}\n\n"
    report += f"Progress: {percentage}%\n\n"

    report += "Completed Tasks:\n"

    for task in completed:
        report += f"✅ {task}\n"

    report += "\nPending Tasks:\n"

    for task in tasks:
        if task not in completed:
            report += f"⏳ {task}\n"

    return report