import re


def detect_fast_intent(command):
    print("FAST ROUTER RECEIVED:",command)

    text = command.lower().strip()

    # ---------- Screenshot ----------

    if (
        "screenshot" in text
        or "capture screen" in text
        or "capture my screen" in text
    ):
        return {
            "intent": "take_screenshot",
            "target": ""
        }

    # ---------- Lock PC ----------

    if (
        "lock pc" in text
        or "lock computer" in text
        or "lock my pc" in text
        or "lock my laptop" in text
    ):
        return {
            "intent": "lock_pc",
            "target": ""
        }

    # ---------- Close Current Window ----------

    if (
        "close this window" in text
        or "close current window" in text
        or "close the app i am using" in text
        or "close the application i am using" in text
    ):
        return {
            "intent": "close_active_window",
            "target": ""
        }

    # ---------- Minimize ----------

    if (
        "minimize" in text
        or "minimise" in text
    ):
        return {
            "intent": "minimize_window",
            "target": ""
        }

    # ---------- Maximize ----------

    if (
        "maximize" in text
        or "maximise" in text
    ):
        return {
            "intent": "maximize_window",
            "target": ""
        }
    # ---------- Voice ----------

    # English Male
    if (
            "english male voice" in text
            or "male voice" in text
    ):
        return {
            "intent": "english_male_voice",
            "target": ""
        }

    # English Female
    if (
            "english female voice" in text
            or "female voice" in text
    ):
        return {
            "intent": "english_female_voice",
            "target": ""
        }

    # Telugu Female
    if (
            "telugu female voice" in text
            or "telugu voice" in text
    ):
        return {
            "intent": "telugu_female_voice",
            "target": ""
        }

    # ---------- Switch ----------

    if text.startswith("switch to "):

        target = re.sub(
            r"^switch to\s+",
            "",
            text
        ).strip()

        return {
            "intent": "switch_window",
            "target": target
        }

    # ---------- Close App ----------

    if text.startswith("close "):

        target = re.sub(
            r"^close\s+",
            "",
            text
        ).strip()

        if target not in [
            "this window",
            "current window",
            "current app",
            "current application",
            "the app i am using",
            "the application i am using"
        ]:
            return {
                "intent": "close_app",
                "target": target
            }
    # ---------- Open App ----------

    if text.startswith("open "):
        target = re.sub(
            r"^open\s+",
            "",
            text
        ).strip()
        if target in ["it", "that", "the app"]:
            return None

        return {
            "intent": "open_app",
            "target": target
        }

    return None