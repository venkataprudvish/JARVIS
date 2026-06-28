LANGUAGE_MODE = "english"


def set_language(mode):

    global LANGUAGE_MODE

    LANGUAGE_MODE = mode

    return f"Language changed to {mode}"


def get_language():

    return LANGUAGE_MODE