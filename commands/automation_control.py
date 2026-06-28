from commands.desktop_automation import (
    press_enter,
    press_key,
    copy,
    paste,
    cut,
    undo,
    redo,
    select_all,
    show_desktop,
    open_run,
    open_task_manager
)


def automation_control(ai_intent):

    intent = ai_intent["intent"]

    # ENTER

    if intent == "press_enter":

        press_enter()

        return "Pressed Enter, Sir."

    # ESC

    if intent == "press_escape":

        press_key("esc")

        return "Pressed Escape, Sir."

    # TAB

    if intent == "press_tab":

        press_key("tab")

        return "Pressed Tab, Sir."

    # COPY

    if intent == "copy":

        copy()

        return "Copied, Sir."

    # PASTE

    if intent == "paste":

        paste()

        return "Pasted, Sir."

    # CUT

    if intent == "cut":

        cut()

        return "Cut completed, Sir."

    # UNDO

    if intent == "undo":

        undo()

        return "Undo completed, Sir."

    # REDO

    if intent == "redo":

        redo()

        return "Redo completed, Sir."

    # SELECT ALL

    if intent == "select_all":

        select_all()

        return "Selected everything, Sir."

    # SHOW DESKTOP

    if intent == "show_desktop":

        show_desktop()

        return "Showing Desktop, Sir."

    # RUN

    if intent == "open_run":

        open_run()

        return "Opening Run, Sir."

    # TASK MANAGER

    if intent == "open_task_manager":

        open_task_manager()

        return "Opening Task Manager, Sir."

    return None