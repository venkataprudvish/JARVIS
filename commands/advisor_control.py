from memory.memory_manager import load_memory


def get_next_task_advice():
    memory = load_memory()

    current_project = memory.get("current_project")

    if not current_project:
        return "No active project selected, Sir."

    project = memory["projects"][current_project]

    tasks = project["tasks"]
    features = project["features"]

    if not tasks:
        return (
            f"Sir, {current_project} has no tasks yet. "
            f"I recommend creating implementation tasks first."
        )

    return (
        f"Based on {current_project}, "
        f"I recommend working on '{tasks[0]}' next. "
        f"The project currently contains {len(features)} features."
    )


def suggest_project_features():
    suggestions = [
        "AI Queue Prediction",
        "Smart Visitor Heat Maps",
        "Personalized Visit Planner",
        "Dynamic Pricing Engine",
        "Predictive Crowd Forecasting"
    ]

    return "Sir, I suggest these features: " + ", ".join(suggestions)