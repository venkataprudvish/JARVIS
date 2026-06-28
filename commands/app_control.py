import os

from commands.smart_resolver import smart_open
from brain.conversation_engine import remember_application


def open_app(command):

    command = command.lower().strip()

    trigger_words = [
        "open",
        "launch",
        "start",
        "run",
        "can you open",
        "please open"
    ]

    app_name = command

    for word in trigger_words:
        app_name = app_name.replace(word, "")

    app_name = app_name.strip()

    if not app_name:
        return None

    # WhatsApp Desktop (Microsoft Store)
    if app_name == "whatsapp":
        try:
            os.system(
                r'explorer.exe shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App'
            )
            return "Opening WhatsApp, Sir."
        except Exception:
            pass

    # Universal Smart Resolver
    result = smart_open(app_name)

    if result:
        remember_application(app_name)

    return result