import asyncio
import edge_tts
import tempfile
import os
from playsound import playsound


ENGLISH_MALE = "en-US-GuyNeural"
ENGLISH_FEMALE = "en-US-JennyNeural"
TELUGU_FEMALE = "te-IN-ShrutiNeural"

current_voice = ENGLISH_MALE





async def _speak_async(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        filename = f.name

    communicate = edge_tts.Communicate(text, current_voice)
    await communicate.save(filename)

    playsound(filename)

    os.remove(filename)


def speak(text):
    print("Jarvis:", text)
    asyncio.run(_speak_async(str(text)))

def set_english_male():
    global current_voice
    current_voice = ENGLISH_MALE


def set_english_female():
    global current_voice
    current_voice = ENGLISH_FEMALE


def set_telugu_female():
    global current_voice
    current_voice = TELUGU_FEMALE