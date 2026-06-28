import time
from ollama import chat
from memory.memory_manager import load_memory
from brain.context_builder import build_project_context
from voice.language_manager import get_language
from commands.file_reader import read_file
from commands.app_control import open_app
from commands.browser_control import search_google
from commands.memory_control import learn_memory
from commands.multi_command import split_commands
from commands.project_reviewer import review_project
from commands.project_analyzer import analyze_project_ai
from commands.jarvis_analyzer import analyze_jarvis
from commands.intent_engine import detect_intent
from memory.context_memory import save_context, load_context
from commands.file_actions import create_file, create_folder
from commands.code_writer import generate_code
from voice.speech_output import (
    set_english_male,
    set_english_female,
    set_telugu_female
)

from commands.project_builder import build_project
from commands.debug_manager import debug_manager
from commands.activity_engine import activity_engine
from commands.fast_intent import detect_fast_intent
from commands.fast_automation_intent import detect_fast_automation_intent
from brain.conversation_engine import (
    start_conversation,
    end_conversation,
    remember_command,
    remember_application,
    remember_project,
    remember_task,
    last_application,
    last_subject,
    current_project,
    current_task
)
from brain.conversation_router import resolve_conversation

from commands.project_manager import (
    create_project,
    switch_project,
    list_projects,
    get_current_project
)

from commands.project_control import (
    add_project_feature,
    add_project_note,
    get_project_features,
    get_project_notes,
    get_project_summary
)

from commands.task_control import (
    add_task,
    get_tasks
)

from commands.advisor_control import (
    suggest_project_features
)

from commands.advisor_v2 import (
    analyze_current_project,
    get_next_task_smart
)

from commands.advisor_v3 import (
    analyze_project_v3,
    suggest_next_milestone,
    create_project_roadmap
)
from commands.advisor_ai import ai_project_advisor
from commands.planner_ai import create_implementation_plan
from commands.progress_tracker import (
    mark_task_complete,
    get_project_progress
)
from commands.daily_manager import get_today_recommendations
from commands.timeline_manager import get_project_history
from commands.dashboard_manager import get_project_dashboard
from commands.status_report import generate_status_report
from commands.weekly_summary import generate_weekly_summary
from commands.vision_control import (
    analyze_screen,
    explain_screen_error,
    review_code_on_screen
)




def process_single_command(command, memory):

    t = time.time()
    user_input_lower = command.lower()


    t = time.time()
    intent = detect_intent(command)


    t = time.time()
    conversation_intent = resolve_conversation(command)


    if conversation_intent:

        if conversation_intent["intent"] == "continue_browser":

            print("Continuing Browser Context:", conversation_intent)

        elif conversation_intent["intent"] == "continue_project":

            print("Continuing Project Context:", conversation_intent)

        elif conversation_intent["intent"] == "continue_task":

            print("Continuing Task Context:", conversation_intent)

        elif conversation_intent["intent"] == "close_last_application":

            from commands.app_manager import close_app

            return close_app(conversation_intent["application"])

        elif conversation_intent["intent"] == "reopen_last_application":

            from commands.app_manager import reopen_last_app

            return reopen_last_app()

    if conversation_intent:

        if conversation_intent["intent"] == "continue_browser":

            print("Continuing Browser Context:", conversation_intent)

        elif conversation_intent["intent"] == "continue_project":

            print("Continuing Project Context:", conversation_intent)

        elif conversation_intent["intent"] == "continue_task":

            print("Continuing Task Context:", conversation_intent)

        elif conversation_intent["intent"] == "close_last_application":

            from commands.app_manager import close_app

            return close_app(conversation_intent["application"])

        elif conversation_intent["intent"] == "reopen_last_application":

            from commands.app_manager import reopen_last_app

            return reopen_last_app()
    fast_intent = detect_fast_intent(command)
    print("FAST INTENT =", fast_intent)

    if fast_intent:

        if fast_intent["intent"] == "english_male_voice":
            set_english_male()
            return "English male voice activated."

        if fast_intent["intent"] == "english_female_voice":
            set_english_female()
            return "English female voice activated."

        if fast_intent["intent"] == "telugu_female_voice":
            set_telugu_female()
            return "Telugu female voice activated."

        from commands.system_control import system_control
        return system_control(fast_intent)
    fast_automation = detect_fast_automation_intent(command)

    if fast_automation:
        from commands.automation_control import automation_control
        return automation_control(fast_automation)
    ai_intent = {
        "intent": "chat",
        "target": command
    }

    # PROJECT MANAGER

    if user_input_lower.startswith("create project "):
        project_name = command[15:].strip()
        return create_project(project_name)

    if user_input_lower.startswith("switch project "):
        project_name = command[15:].strip()
        return switch_project(project_name)

    if "list projects" in user_input_lower:
        return list_projects()

    if "current project" in user_input_lower:
        return f"Current project is {get_current_project()}, Sir."
    # AI PROJECT ADVISOR

    if "how can i improve my project" in user_input_lower:
        return ai_project_advisor(command)

    if "what should i build after" in user_input_lower:
        return ai_project_advisor(command)

    if "suggest next 3 tasks" in user_input_lower:
        return ai_project_advisor(command)

    if "give project advice" in user_input_lower:
        return ai_project_advisor(command)
    # PLANNER AI

    if user_input_lower.startswith("plan this feature "):
        feature = command[18:].strip()
        return create_implementation_plan(feature)

    if user_input_lower.startswith("how do i build "):
        feature = command[15:].strip()
        return create_implementation_plan(feature)

    if user_input_lower.startswith("create implementation plan for "):
        feature = command[31:].strip()
        return create_implementation_plan(feature)

    if user_input_lower.startswith("generate development steps for "):
        feature = command[31:].strip()
        return create_implementation_plan(feature)

    # ADVISOR V3

    if "analyze my project" in user_input_lower:
        return analyze_project_v3()

    if "what is missing in my project" in user_input_lower:
        return analyze_project_v3()

    if "suggest next milestone" in user_input_lower:
        return suggest_next_milestone()

    if "create roadmap" in user_input_lower:
        return create_project_roadmap()

    # ADVISOR V2

    if "what should i build next" in user_input_lower:
        return get_next_task_smart()

    if "what should i do next" in user_input_lower:
        return get_next_task_smart()

    # FEATURE SUGGESTIONS

    if "suggest 5 new features" in user_input_lower:
        return suggest_project_features()

    if "suggest new features" in user_input_lower:
        return suggest_project_features()

    # CONTINUE PROJECT

    if "continue my project" in user_input_lower:
        return get_project_summary()

    if "continue my smart park project" in user_input_lower:
        return get_project_summary()

    # TASKS

    if user_input_lower.startswith("add task "):
        task = command[9:].strip()

        remember_task(task)

        return add_task(task)

    if "project tasks" in user_input_lower:
        return get_tasks()

    # PROGRESS TRACKER

    if user_input_lower.startswith("mark task complete "):
        task = command[19:].strip()
        return mark_task_complete(task)

    if "project progress" in user_input_lower:
        return get_project_progress()
    # DAILY MANAGER

    if "what should i work on today" in user_input_lower:
        return get_today_recommendations()

    if "today recommendations" in user_input_lower:
        return get_today_recommendations()

    if "today tasks" in user_input_lower:
        return get_today_recommendations()
    # TIMELINE

    if "project history" in user_input_lower:
        return get_project_history()

    if "show history" in user_input_lower:
        return get_project_history()

    if "show timeline" in user_input_lower:
        return get_project_history()
    # DASHBOARD

    if "project dashboard" in user_input_lower:
        return get_project_dashboard()

    if "show dashboard" in user_input_lower:
        return get_project_dashboard()

    if "dashboard" == user_input_lower.strip():
        return get_project_dashboard()
    # STATUS REPORT

    if "summarize my project" in user_input_lower:
        return generate_status_report()

    if "project report" in user_input_lower:
        return generate_status_report()

    if "status report" in user_input_lower:
        return generate_status_report()
    # WEEKLY SUMMARY

    if "weekly summary" in user_input_lower:
        return generate_weekly_summary()

    if "project summary" in user_input_lower:
        return generate_weekly_summary()

    if "weekly report" in user_input_lower:
        return generate_weekly_summary()
    # SCREEN VISION

    if "what is on my screen" in user_input_lower:
        return analyze_screen()

    if "analyze my screen" in user_input_lower:
        return analyze_screen()

    if "describe my screen" in user_input_lower:
        return analyze_screen()
    # CODE REVIEWER

    if "review the code on my screen" in user_input_lower:
        return review_code_on_screen()

    if "review my code" in user_input_lower:
        return review_code_on_screen()

    if "analyze the code on my screen" in user_input_lower:
        return review_code_on_screen()
    # SCREEN ERROR ANALYZER

    if "explain the error on my screen" in user_input_lower:
        return explain_screen_error()

    if "analyze the error on my screen" in user_input_lower:
        return explain_screen_error()

    if "what error is on my screen" in user_input_lower:
        return explain_screen_error()

    # FEATURES

    if user_input_lower.startswith("add feature "):
        feature = command[12:].strip()
        return add_project_feature(feature)

    if user_input_lower.startswith("add note "):
        note = command[9:].strip()
        return add_project_note(note)

    if "project features" in user_input_lower:
        return get_project_features()

    if "project notes" in user_input_lower:
        return get_project_notes()

    # MEMORY LEARNING

    memory_response = learn_memory(command)

    if memory_response:
        return memory_response

    # SEARCH

    if "search" in user_input_lower:
        query = user_input_lower.replace("search",

        "")
        query = query.replace("google", "")
        query = query.replace("for", "")
        query = query.strip()

        return search_google(query)

    # MEMORY RECALL

    if "my name" in user_input_lower:

        if get_language() == "telugu":
            return f"మీ పేరు {memory.get('name', 'Unknown')}"

        if get_language() == "tenglish":
            return f"Mee peru {memory.get('name', 'Unknown')}"

        return f"Your name is {memory.get('name', 'Unknown')}, Sir."

    if "university" in user_input_lower:

        if get_language() == "telugu":
            return f"మీరు {memory.get('university', 'Unknown')} లో చదువుతున్నారు"

        if get_language() == "tenglish":
            return f"Meeru {memory.get('university', 'Unknown')} lo chadutunnaru"

        return f"You are studying at {memory.get('university', 'Unknown')}, Sir."

    if "branch" in user_input_lower:

        if get_language() == "telugu":
            return f"మీ బ్రాంచ్ {memory.get('branch', 'Unknown')}"

        if get_language() == "tenglish":
            return f"Mee branch {memory.get('branch', 'Unknown')}"

        return f"Your branch is {memory.get('branch', 'Unknown')}, Sir."

    # ACTIVITY ENGINE

    activity = activity_engine(command)


    if activity:
        return activity

    # AI INTENT ENGINE

    if ai_intent["intent"] == "open_app":
        remember_application(ai_intent["target"])

        return open_app(ai_intent["target"])
    if ai_intent["intent"] in [
        "shutdown_pc",
        "restart_pc"
    ]:
        from commands.system_control import system_control
        return system_control(ai_intent)

    if ai_intent["intent"] == "search_google":

        return search_google(ai_intent["target"])

    if ai_intent["intent"] == "generate_code":

        return generate_code(ai_intent["target"])

    if ai_intent["intent"] == "build_project":
        remember_project(ai_intent["target"])

        return build_project(ai_intent["target"])

    # DEBUG ENGINE

    debug_response = debug_manager(command)

    if debug_response:
        return debug_response

    # INTENT ENGINE

    if intent["intent"] == "language_changed":
        return intent["message"]

    if intent["intent"] == "create_file":

        text = intent["target"]

        words = text.split()

        filename = None

        for word in words:
            if "." in word:
                filename = word
                break

        if filename:
            return create_file(filename)

        return "Please specify a filename."

    if intent["intent"] == "create_folder":
        text = intent["target"]

        words = text.split()

        foldername = words[-1]

        return create_folder(foldername)

    if intent["intent"] == "generate_code":
        prompt = intent["target"]

        return generate_code(prompt)

    if intent["intent"] == "review_file":
        filename = intent["target"]

        save_context({
            "last_file": filename,
            "last_intent": "review_file"
        })

        file_content = read_file(filename)

        review_prompt = f"""
    Review this Python file.

    Explain:
    1. What this file does.
    2. Any bugs.
    3. Improvements.

    Code:

    {file_content}
    """

        t_ai = time.time()

        response = chat(
            model="qwen3:1.7b",
            messages=[
                {
                    "role": "user",
                    "content": review_prompt
                }
            ]
        )



        return response["message"]["content"]

    if intent["intent"] == "analyze_project":
        return analyze_project_ai()

    if intent["intent"] == "analyze_jarvis":
        return analyze_jarvis()

    # APP CONTROL

    trigger_words = [
        "open",
        "launch",
        "start",
        "run",
        "please open",
        "can you open"
    ]

    if any(command.lower().startswith(word) for word in trigger_words):

        app_response = open_app(command)

        if app_response:
            return app_response
    # FILE READER

    if user_input_lower.startswith("read file "):
        filename = command[10:].strip()

        return read_file(filename)

    if user_input_lower.startswith("show file "):
        filename = command[10:].strip()

        return read_file(filename)
    # FILE REVIEWER

    if user_input_lower.startswith("review file "):

        filename = command[12:].strip()

        file_content = read_file(filename)

        if file_content.startswith("File ") or file_content.startswith("Error"):
            return file_content

        review_prompt = f"""
    You are an expert Python code reviewer.

    Analyze this file and provide:

    1. What this file does
    2. Strengths
    3. Possible bugs
    4. Improvements
    5. Short summary

    Code:

    {file_content}
    """

        response = chat(
            model="qwen3:1.7b",
            messages=[
                {
                    "role": "user",
                    "content": review_prompt
                }
            ]
        )

        return response["message"]["content"]
    # PROJECT REVIEWER

    if "review my project" in user_input_lower:
        return review_project()
    # PROJECT ANALYZER

    if (
            "analyze my project" in user_input_lower
            or "analyse my project" in user_input_lower
    ):
        return analyze_project_ai()
    # JARVIS ANALYZER

    if (
            "analyze jarvis" in user_input_lower
            or "analyse jarvis" in user_input_lower
    ):
        return analyze_jarvis()
    context = load_context()

    if (
            "any bugs" in user_input_lower
            or "explain more" in user_input_lower
            or "tell me more" in user_input_lower
    ):

        if context.get("last_file"):
            filename = context["last_file"]

            file_content = read_file(filename)

            review_prompt = f"""
    The user is asking a follow-up question about this file.

    Question:
    {command}

    File:
    {filename}

    Code:
    {file_content}

    Answer the user's question.
    """

            response = chat(
                model="qwen3:1.7b",
                messages=[
                    {
                        "role": "user",
                        "content": review_prompt
                    }
                ]
            )

            return response["message"]["content"]

    # AI BRAIN

    project_context = build_project_context()

    system_prompt = f"""
    You are JARVIS.

    Be brief.
    Answer in one or two sentences.
    Never say you are Qwen.
    Never add extra explanations.
    """
    language = get_language()

    if language == "telugu":
        command = "Answer completely in Telugu.\n\n" + command

    elif language == "tenglish":
        command = "Answer in Telugu written using English letters (Tenglish).\n\n" + command

    t_ai = time.time()

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )



    return response["message"]["content"]

def ask_jarvis(user_input):



    start = time.time()

    t = time.time()
    memory = load_memory()


    t = time.time()
    start_conversation()


    t = time.time()
    remember_command(user_input)


    t = time.time()
    commands = split_commands(user_input)


    responses = []

    for command in commands:

        response = process_single_command(command, memory)

        if response:
            responses.append(response)





    return " ".join(responses)



