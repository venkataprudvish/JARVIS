def detect_debug_intent(user_input):

    text = user_input.lower()

    debug_keywords = [
        "debug",
        "bug",
        "error",
        "exception",
        "traceback",
        "fix",
        "crash",
        "crashing",
        "not working",
        "issue",
        "problem",
        "stack trace"
    ]

    if any(keyword in text for keyword in debug_keywords):
        return {
            "intent": "debug",
            "target": user_input
        }

    return {
        "intent": "unknown",
        "target": ""
    }