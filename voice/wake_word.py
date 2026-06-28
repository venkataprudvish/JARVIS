import speech_recognition as sr
from voice.offline_listener import transcribe_audio
from voice.audio_recorder import record_audio
import time

from brain.ollama_brain import ask_jarvis
from voice.speech_output import (
    speak,
    set_english_male,
    set_english_female,
    set_telugu_female
)
print("USING BRAIN:", ask_jarvis.__module__)


recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.5
recognizer.non_speaking_duration = 0.3
recognizer.energy_threshold = 300

print("=" * 50)
print("JARVIS WAKE WORD MODE")
print("Say 'Hey Jarvis'")
print("=" * 50)

print("\nWaiting for wake word...")

while True:

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=3
            )

        wake_text = recognizer.recognize_google(audio).lower()

        print("Heard:", wake_text)

        wake_text = wake_text.lower().strip()

        wake_words = [
            "hey jarvis",
            "jarvis",
            "okay jarvis",
            "ok jarvis",
            "hi jarvis"
        ]

        if not any(word in wake_text for word in wake_words):
            continue

        speak("Conversation Mode Activated, Sir")

        # Conversation Mode
        while True:

            try:

                print("Listening for command...")

                print("Listening for command...")

                t = time.time()
                audio_file = record_audio()
                print("RECORD:", round(time.time() - t, 2), "sec")

                t = time.time()
                command = transcribe_audio(audio_file)
                print("WHISPER:", round(time.time() - t, 2), "sec")

                if not command:
                    print("Didn't hear anything.")
                    continue

                print("You:", command)

                if command.lower() in [
                    "exit",
                    "sleep",
                    "go to sleep",
                    "goodbye"
                ]:
                    speak("Going to sleep, Sir")
                    print("\nWaiting for wake word...")
                    break

                print("Thinking...")

                t = time.time()
                reply = ask_jarvis(command)
                print("BRAIN:", round(time.time() - t, 2), "sec")

                print("REPLY =", reply)

                t = time.time()
                speak(reply)
                print("SPEAK:", round(time.time() - t, 2), "sec")

            except sr.UnknownValueError:

                print("Didn't understand. Still listening...")
                continue

            except sr.WaitTimeoutError:

                print("Still listening...")
                continue

            except Exception as e:

                print("COMMAND ERROR:", e)
                print("\nWaiting for wake word...")
                break

    except sr.UnknownValueError:
        continue

    except sr.WaitTimeoutError:
        continue

    except Exception as e:

        error = str(e)

        if "10054" in error:
            print("Connection lost. Reconnecting...")
            continue

        print("ERROR:", error)
        continue