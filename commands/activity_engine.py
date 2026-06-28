
from commands.workflow_manager import execute_workflow


def activity_engine(command):


    command = command.lower().strip()

    # STUDY MODE
    if (
        "study" in command
        or "going to study" in command
        or "i am going to study" in command
    ):
        return execute_workflow("study")

    # CODING MODE
    if (
        "code" in command
        or "coding" in command
        or "programming" in command
        or "going to code" in command
        or "i am going to code" in command
    ):
        return execute_workflow("coding")

    # WORK MODE
    if (
        "work" in command
        or "going to work" in command
        or "i am going to work" in command
    ):
        return execute_workflow("work")

    # MOVIE MODE
    if (
        "movie" in command
        or "watch movie" in command
        or "going to watch a movie" in command
    ):
        return execute_workflow("movie")

    return None