import pvporcupine

print("=" * 50)
print("TESTING PORCUPINE")
print("=" * 50)

try:
    porcupine = pvporcupine.create(
        access_key="YOUR_ACCESS_KEY",
        keywords=["jarvis"]
    )

    print("SUCCESS!")
    print("Porcupine loaded successfully.")

    porcupine.delete()

except Exception as e:
    print("ERROR:")
    print(e)