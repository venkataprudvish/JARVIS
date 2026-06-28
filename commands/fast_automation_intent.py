def detect_fast_automation_intent(command):

    text = command.lower().strip()

    mapping = {

        "press enter": "press_enter",
        "hit enter": "press_enter",

        "press escape": "press_escape",
        "press esc": "press_escape",

        "press tab": "press_tab",

        "copy": "copy",
        "paste": "paste",
        "cut": "cut",

        "undo": "undo",
        "redo": "redo",

        "select all": "select_all",

        "show desktop": "show_desktop",

        "open run": "open_run",
        "run dialog": "open_run",

        "open task manager": "open_task_manager",
        "task manager": "open_task_manager"
    }

    for phrase, intent in mapping.items():

        if text == phrase:
            return {
                "intent": intent,
                "target": ""
            }

    return None