from commands.file_actions import create_file, create_folder
from voice.language_manager import set_language
from commands.file_finder import find_file
def detect_intent(user_input):

    text = user_input.lower()

    # Review File Intent
    if any(word in text for word in [
        "review",
        "check",
        "analyze",
        "analyse",
        "bugs",
        "look at"
    ]):

        for keyword in [
            "review",
            "check",
            "analyze",
            "analyse",
            "bugs",
            "look at"
        ]:

            if keyword in text:

                cleaned_text = text

                for word in [
                    "review",
                    "check",
                    "analyze",
                    "analyse",
                    "bugs",
                    "bugs in",
                    "look at",
                    "code",
                    "file",
                    "my",
                    "can",
                    "you",
                    "please",
                    "could",
                    "would",
                    "hey",
                    "jarvis"
                ]:
                    cleaned_text = cleaned_text.replace(word, "")

                cleaned_text = cleaned_text.strip()

                found_file = find_file(cleaned_text)

                if found_file:
                    return {
                        "intent": "review_file",
                        "target": found_file
                    }

    # Project Analysis Intent
    if (
        "my project" in text
        or "project health" in text
        or "project status" in text
    ):
        return {
            "intent": "analyze_project"
        }

    # Jarvis Analysis Intent
    if (
        "jarvis" in text
        and any(word in text for word in [
            "analyze",
            "analyse",
            "health",
            "status",
            "check"
        ])
    ):
        return {
            "intent": "analyze_jarvis"
        }
    # Language Mode Intent

    if (
            "tenglish mode" in text
            or "tenglish" in text
            or "ten english" in text
            or "10 english" in text
    ):
        set_language("tenglish")
        return {
            "intent": "language_changed",
            "message": "Tenglish mode activated"
        }

    if (
            "telugu mode" in text
            or text == "telugu"
    ):
        set_language("telugu")
        return {
            "intent": "language_changed",
            "message": "Telugu mode activated"
        }

    if (
            "english mode" in text
            or text == "english"
    ):
        set_language("english")
        return {
            "intent": "language_changed",
            "message": "English mode activated"
        }
    # Create File Intent

    if (
            "create file" in text
            or "make file" in text
            or "new file" in text
    ):
        return {
            "intent": "create_file",
            "target": text
        }

    # Create Folder Intent

    if (
            "create folder" in text
            or "make folder" in text
            or "new folder" in text
    ):
        return {
            "intent": "create_folder",
            "target": text
        }
    # Code Generation Intent

    if (
            "create program" in text
            or "write code" in text
            or "generate code" in text
    ):
        return {
            "intent": "generate_code",
            "target": text
        }

    return {
        "intent": "unknown"
    }