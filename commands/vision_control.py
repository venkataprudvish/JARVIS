from PIL import ImageGrab
from ollama import chat


def capture_screen():

    screenshot = ImageGrab.grab()

    save_path = "screen_capture.png"

    screenshot.save(save_path)

    return save_path


def analyze_screen():

    image_path = capture_screen()

    response = chat(
        model="llava:latest",
        messages=[
            {
                "role": "user",
                "content": "Describe what is visible on this screen in detail.",
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]


def explain_screen_error():

    image_path = capture_screen()

    response = chat(
        model="llava:latest",
        messages=[
            {
                "role": "user",
                "content": """
Analyze this screenshot carefully.

If there is an error message:
- Explain the error.
- Explain the probable cause.
- Suggest how to fix it.

If there is no error:
- Explain what application is visible.
- Explain what the user is currently doing.
""",
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]


def review_code_on_screen():

    image_path = capture_screen()

    response = chat(
        model="llava:latest",
        messages=[
            {
                "role": "user",
                "content": """
You are a senior software engineer.

Analyze the code visible in this screenshot.

Provide:

1. What the code is doing.
2. Any bugs or potential issues.
3. Suggestions for improvement.
4. Code quality feedback.

Keep the response concise and practical.
""",
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]