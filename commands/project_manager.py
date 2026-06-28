from memory.memory_manager import load_memory, save_memory


def create_project(project_name):
    memory = load_memory()

    if "projects" not in memory:
        memory["projects"] = {}

    if project_name not in memory["projects"]:
        memory["projects"][project_name] = {
            "features": [],
            "notes": [],
            "tasks": []
        }

    memory["current_project"] = project_name

    save_memory(memory)

    return f"Project '{project_name}' created and selected, Sir."


def switch_project(project_name):
    memory = load_memory()

    if "projects" not in memory:
        return "No projects found, Sir."

    if project_name not in memory["projects"]:
        return f"Project '{project_name}' does not exist, Sir."

    memory["current_project"] = project_name

    save_memory(memory)

    return f"Switched to project '{project_name}', Sir."


def list_projects():
    memory = load_memory()

    projects = memory.get("projects", {})

    if not projects:
        return "No projects available, Sir."

    return "Projects: " + ", ".join(projects.keys())


def get_current_project():
    memory = load_memory()

    return memory.get("current_project", "No active project")