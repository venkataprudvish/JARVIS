from memory.memory_manager import load_memory

memory = load_memory()

print(memory)
print("Name =", memory.get("name"))
print("University =", memory.get("university"))