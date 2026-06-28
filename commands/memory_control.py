from memory.memory_manager import remember


def learn_memory(user_input):
    text = user_input.lower()

    if "my name is" in text:
        value = user_input.split("my name is", 1)[1].strip()
        remember("name", value)
        return f"Understood Sir. I will remember your name is {value}."

    if "i am from" in text:
        value = user_input.split("i am from", 1)[1].strip()
        remember("location", value)
        return f"Understood Sir. I will remember you are from {value}."

    if "my project is" in text:
        value = user_input.split("my project is", 1)[1].strip()
        remember("project", value)
        return f"Understood Sir. I will remember your project is {value}."

    if "my favourite language is" in text:
        value = user_input.split("my favourite language is", 1)[1].strip()
        remember("favourite language", value)
        return f"Understood Sir. I will remember your favourite language is {value}."

    return None