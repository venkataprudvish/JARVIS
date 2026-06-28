def split_commands(command):
    command = command.lower()

    if " and " in command:
        return [cmd.strip() for cmd in command.split(" and ")]

    return [command]