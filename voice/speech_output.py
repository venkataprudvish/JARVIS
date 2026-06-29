import asyncio
import edge_tts
import tempfile
import os
import pygame
import threading

pygame.mixer.init()

ENGLISH_MALE = "en-US-GuyNeural"
ENGLISH_FEMALE = "en-US-JennyNeural"
TELUGU_FEMALE = "te-IN-ShrutiNeural"

current_voice = ENGLISH_MALE

is_speaking = False


async def _speak_async(text):

    global is_speaking

    is_speaking = True

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        filename = f.name

    try:

        communicate = edge_tts.Communicate(text, current_voice)
        await communicate.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.05)

    finally:

        is_speaking = False

        try:
            pygame.mixer.music.unload()
        except:
            pass

        await asyncio.sleep(0.1)

        try:
            os.remove(filename)
        except:
            pass


def _run_speech(text):

    try:
        asyncio.run(_speak_async(str(text)))
    except Exception as e:
        print("TTS ERROR:", e)


def speak(text):

    print("Jarvis:", text)

    thread = threading.Thread(
        target=_run_speech,
        args=(str(text),),
        daemon=True
    )

    thread.start()


def stop_speaking():

    global is_speaking

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    is_speaking = False


def set_english_male():

    global current_voice
    current_voice = ENGLISH_MALE


def set_english_female():

    global current_voice
    current_voice = ENGLISH_FEMALE


def set_telugu_female():

    global current_voice
    current_voice = TELUGU_FEMALE