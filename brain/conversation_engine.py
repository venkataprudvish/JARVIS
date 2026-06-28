conversation_state = {
    "active": False,
    "last_command": None,
    "last_subject": None,
    "last_application": None,
    "current_task": None,
    "current_project": None,
    "conversation_history": []
}


def start_conversation():

    conversation_state["active"] = True

    return True


def end_conversation():

    conversation_state["active"] = False

    return True


def is_active():

    return conversation_state["active"]


def remember_command(command):

    conversation_state["last_command"] = command

    conversation_state["conversation_history"].append(command)

    if len(conversation_state["conversation_history"]) > 20:
        conversation_state["conversation_history"].pop(0)


def last_command():

    return conversation_state["last_command"]


def remember_subject(subject):

    conversation_state["last_subject"] = subject


def last_subject():

    return conversation_state["last_subject"]


def remember_application(app):

    conversation_state["last_application"] = app


def last_application():

    return conversation_state["last_application"]


def remember_task(task):

    conversation_state["current_task"] = task


def current_task():

    return conversation_state["current_task"]


def remember_project(project):

    conversation_state["current_project"] = project


def current_project():

    return conversation_state["current_project"]


def conversation_history():

    return conversation_state["conversation_history"]


def clear_history():

    conversation_state["conversation_history"].clear()