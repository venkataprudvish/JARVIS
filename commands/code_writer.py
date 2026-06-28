from ollama import chat


def generate_code(prompt):

    response = chat(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "user",
                "content": f"Write only Python code for: {prompt}"
            }
        ]
    )

    return response["message"]["content"]