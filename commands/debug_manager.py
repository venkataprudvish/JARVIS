from commands.debug_intent import detect_debug_intent
from commands.debugger_ai import debug_code


def debug_manager(user_input):

    intent = detect_debug_intent(user_input)

    if intent["intent"] != "debug":
        return None

    return debug_code(intent["target"])