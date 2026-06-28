from commands.app_control import open_app


def execute_workflow(workflow_name):

    workflow_name = workflow_name.lower().strip()

    # ==========================
    # STUDY MODE
    # ==========================

    if workflow_name == "study":

        open_app("chrome")
        open_app("chatgpt")

        return "Study Mode Activated, Sir."

    # ==========================
    # CODING MODE
    # ==========================

    if workflow_name == "coding":

        open_app("pycharm")
        open_app("chrome")
        open_app("github")

        return "Coding Mode Activated, Sir."

    # ==========================
    # WORK MODE
    # ==========================

    if workflow_name == "work":

        open_app("chrome")

        return "Work Mode Activated, Sir."

    # ==========================
    # MOVIE MODE
    # ==========================

    if workflow_name == "movie":

        open_app("netflix")

        return "Movie Mode Activated, Sir."

    return None