from memory.memory_manager import load_memory


def analyze_project_v3():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    features = project["features"]
    tasks = project["tasks"]
    notes = project["notes"]

    analysis = f"Project Analysis: {current_project}\n\n"

    analysis += f"Features: {len(features)}\n"
    analysis += f"Tasks: {len(tasks)}\n"
    analysis += f"Notes: {len(notes)}\n\n"

    missing = []

    if len(features) < 3:
        missing.append("More core features")

    if len(tasks) < len(features):
        missing.append("Implementation tasks")

    if not notes:
        missing.append("Project notes")

    if missing:
        analysis += "Potential Gaps:\n"

        for item in missing:
            analysis += f"- {item}\n"

    else:
        analysis += "No major gaps detected.\n"

    return analysis


def suggest_next_milestone():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    features = project["features"]

    if "dynamic pricing" in [f.lower() for f in features]:
        return (
            "Recommended Next Milestone: "
            "Build Visitor Analytics Dashboard because Dynamic Pricing "
            "requires visitor data and forecasting."
        )

    if features:
        return (
            f"Recommended Next Milestone: "
            f"Implement and test feature '{features[0]}'."
        )

    return "Add project features first, Sir."


def create_project_roadmap():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    roadmap = f"Roadmap for {current_project}\n\n"

    roadmap += "Phase 1\n"
    roadmap += "- Core Features\n"
    roadmap += "- Database Design\n\n"

    roadmap += "Phase 2\n"
    roadmap += "- Backend Development\n"
    roadmap += "- Analytics\n\n"

    roadmap += "Phase 3\n"
    roadmap += "- AI Features\n"
    roadmap += "- Testing\n\n"

    roadmap += "Phase 4\n"
    roadmap += "- Deployment\n"
    roadmap += "- Optimization\n"

    return roadmap