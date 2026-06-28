from commands.desktop_manager import (
    close_active_window,
    close_process,
    find_process,
    lock_pc,
    maximize_active_window,
    minimize_active_window,
    switch_to_window,
    take_screenshot
)


def system_control(ai_intent):

    intent = ai_intent["intent"]
    target = ai_intent.get("target", "").strip()

    # Lock PC
    if intent == "lock_pc":

        lock_pc()

        return "Locking your computer, Sir."

    # Screenshot
    if intent == "take_screenshot":

        path = take_screenshot()

        return f"Screenshot saved successfully.\n{path}"

    # Close Active Window
    if intent == "close_active_window":

        if close_active_window():
            return "Closing current application, Sir."

        return "Unable to close the current application."
    # Open App
    if intent == "open_app":
        from commands.app_control import open_app

        return open_app(target)

    # Close Specific App
    if intent == "close_app":

        process = find_process(target)

        if not process:
            return f"I couldn't find {target}."

        if close_process(process["pid"]):
            return f"Closing {target.title()}, Sir."

        return f"Unable to close {target.title()}."

    # Minimize Current Window
    if intent == "minimize_window":

        if minimize_active_window():
            return "Minimizing current window, Sir."

        return "Unable to minimize the current window."

    # Maximize Current Window
    if intent == "maximize_window":

        if maximize_active_window():
            return "Maximizing current window, Sir."

        return "Unable to maximize the current window."

    # Switch Window
    if intent == "switch_window":

        if switch_to_window(target):
            return f"Switching to {target.title()}, Sir."

        return f"I couldn't find {target.title()}."

    return None