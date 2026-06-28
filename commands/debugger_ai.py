from ollama import chat


def debug_code(error_text):

    prompt = f"""
You are an expert Python debugging AI.

A user encountered this error:

{error_text}

Your job is to:

1. Explain the error in simple language.
2. Find the root cause.
3. Show how to fix it.
4. Provide the corrected code if possible.
5. Give tips to prevent this error in the future.

Return only the answer.
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

    return response["message"]["content"]