import speech_recognition as sr
import pyttsx3

from brain.ollama_brain import ask_jarvis


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


recognizer = sr.Recognizer()

print("=" * 50)
print("JARVIS VOICE MODE")
print("Say 'exit' to stop")
print("=" * 50)

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        text = recognizer.recognize_google(audio)

        print("You:", text)

        if text.lower() == "exit":
            print("Jarvis: Goodbye Sir!")
            speak("Goodbye Sir")
            break

        print("Thinking...")

        reply = ask_jarvis(text)

        print("\nJarvis:", reply)

        speak(reply)

    except sr.WaitTimeoutError:
        print("No voice detected.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

    except Exception as e:
        print("ERROR:", e)