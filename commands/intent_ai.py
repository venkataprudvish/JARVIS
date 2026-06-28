from ollama import chat
import json


def detect_intent_ai(user_input):

    prompt = f"""
You are an Intent Detection AI.

Return ONLY valid JSON.

Supported intents:

open_app
close_app
close_active_window
minimize_window
maximize_window
switch_window
search_google
review_file
read_file
create_file
create_folder
generate_code
analyze_project
analyze_jarvis
build_project
memory
shutdown_pc
restart_pc
lock_pc
take_screenshot
chat

Examples:

User:
Open WhatsApp

Output:
{{"intent":"open_app","target":"WhatsApp"}}

User:
Close Chrome

Output:
{{"intent":"close_app","target":"Chrome"}}

User:
Close the app I am using

Output:
{{"intent":"close_active_window","target":""}}

User:
Minimize this window

Output:
{{"intent":"minimize_window","target":""}}

User:
Maximize this window

Output:
{{"intent":"maximize_window","target":""}}

User:
Switch to Chrome

Output:
{{"intent":"switch_window","target":"Chrome"}}

User:
Take a screenshot

Output:
{{"intent":"take_screenshot","target":""}}

User:
Lock my PC

Output:
{{"intent":"lock_pc","target":""}}

User:
Can you review memory manager?

Output:
{{"intent":"review_file","target":"memory manager"}}

User:
Generate code for calculator

Output:
{{"intent":"generate_code","target":"calculator"}}

User:
Create a Python calculator project

Output:
{{"intent":"build_project","target":"Python calculator project"}}

User:
Search Google for Python

Output:
{{"intent":"search_google","target":"Python"}}

User:
{user_input}
"""

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    try:
        return json.loads(response["message"]["content"])

    except Exception:
        return {
            "intent": "chat",
            "target": user_input
        }