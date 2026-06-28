from brain.ollama_brain import ask_jarvis
from memory.memory_manager import remember, recall

print("=" * 50)
print("JARVIS ONLINE")
print("Type 'exit' to stop")
print("=" * 50)

while True:
    user_input = input("You: ")

    # Remember anything
    if user_input.lower().startswith("remember "):
        data = user_input[9:]

        if "=" in data:
            key, value = data.split("=", 1)

            key = key.strip()
            value = value.strip()

            remember(key, value)

            print(f"Jarvis: I will remember that, Sir.")
            print()
            continue

    # Recall anything
    if user_input.lower().startswith("what is "):
        key = user_input[8:].replace("?", "").strip()

        print(f"Jarvis: {recall(key)}")
        print()
        continue

    # Exit
    if user_input.lower() == "exit":
        print("Jarvis: Goodbye Sir!")
        break

    print("Thinking...")

    reply = ask_jarvis(user_input)

    print("\nJarvis:", reply)
    print()