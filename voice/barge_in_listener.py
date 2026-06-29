import threading
from voice.offline_listener import transcribe_audio
from voice.audio_recorder import record_audio
from voice.speech_manager import speech_manager


STOP_WORDS = [
    "stop",
    "jarvis stop",
    "stop jarvis",
    "cancel",
    "be quiet",
    "quiet"
]


class BargeInListener:

    def __init__(self):
        self.running = False

    def _listen(self):

        while self.running and speech_manager.speaking:

            audio = record_audio()

            text = transcribe_audio(audio).lower().strip()

            if text in STOP_WORDS:

                print("Interrupt Detected")

                speech_manager.stop()

                self.running = False

                break

    def start(self):

        if self.running:
            return

        self.running = True

        threading.Thread(
            target=self._listen,
            daemon=True
        ).start()

    def stop(self):

        self.running = False


barge_listener = BargeInListener()