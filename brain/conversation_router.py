from brain.conversation_engine import (
    last_application,
    current_project,
    current_task
)


def resolve_conversation(command):

    text = command.lower().strip()

    context = {
        "application": last_application(),
        "project": current_project(),
        "task": current_task()
    }

    # ---------- Browser Follow-ups ----------

    if (
        text.startswith("search ")
        or text.startswith("search for ")
    ):

        if context["application"]:

            return {
                "intent": "continue_browser",
                "application": context["application"],
                "query": command
            }

    # ---------- Play Something ----------

    if text.startswith("play "):

        if context["application"]:

            return {
                "intent": "continue_browser",
                "application": context["application"],
                "query": command
            }

    # ---------- Application Follow-ups ----------

    if (
        text == "close it"
        or text == "close that"
        or text == "close the app"
        or text == "close current application"
        or text == "close current app"
    ):

        if context["application"]:

            return {
                "intent": "close_last_application",
                "application": context["application"]
            }

    if (
        text == "open it again"
        or text == "open it"
        or text == "reopen it"
    ):

        if context["application"]:

            return {
                "intent": "reopen_last_application",
                "application": context["application"]
            }

    # ---------- Continue Project ----------

    if (
        "continue" in text
        or "resume" in text
    ):

        if context["project"]:

            return {
                "intent": "continue_project",
                "project": context["project"]
            }

    # ---------- Continue Task ----------

    if (
        text == "do it"
        or text == "do that"
        or text == "continue"
    ):

        if context["task"]:

            return {
                "intent": "continue_task",
                "task": context["task"]
            }

    return None