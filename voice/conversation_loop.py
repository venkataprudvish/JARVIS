import numpy as np
from voice.vad_engine import vad
from voice.vad_buffer import VADBuffer
from voice.live_listener import listener
from voice.audio_buffer import AudioBuffer
from voice.offline_listener import transcribe_audio
from brain.ollama_brain import ask_jarvis

from voice.speech_manager import speech_manager
WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "hi jarvis",
    "okay jarvis",
    "ok jarvis",
]
from voice.config import (
    VOICE_THRESHOLD,
    SILENCE_SECONDS,
    SAMPLE_RATE,
    BLOCK_SIZE,
)


class ConversationLoop:

    def __init__(self):

        self.buffer = AudioBuffer()
        self.vad_buffer = VADBuffer()

        self.state = "IDLE"

        self.silence_chunks = int(
            (SILENCE_SECONDS * SAMPLE_RATE) / BLOCK_SIZE
        )

        self.silence_counter = 0

        print("Conversation Loop Ready")

    def start(self):

        print("Starting conversation loop...")

        for chunk in listener.listen():

            volume = np.abs(chunk).mean()
            speaking = vad.is_speaking(
                self.vad_buffer.get_audio()
            )

            # Always keep last 0.5 sec
            self.buffer.add_live_chunk(chunk)
            self.vad_buffer.add(chunk)

            # ----------------------------
            # IDLE
            # ----------------------------

            if self.state == "IDLE":

                if speaking:
                    print("volume:",volume)

                    self.state = "RECORDING"

                    self.buffer.start_recording()
                    print("pre-roll copied")

                    self.buffer.add_recording_chunk(chunk)
                    print("first chunk added")

                    self.silence_counter = 0

                    print("🎤 Speech Started")

            # ----------------------------
            # RECORDING
            # ----------------------------

            elif self.state == "RECORDING":

                self.buffer.add_recording_chunk(chunk)

                if speaking:

                    self.silence_counter = 0
                    self.conversation_mode = False

                else:

                    self.silence_counter += 1

                    if self.silence_counter >= self.silence_chunks:

                        print("🛑 Speech Ended")

                        self.state = "IDLE"

                        self.silence_counter = 0
                        print("Recording chunks:", len(self.buffer.recording))

                        saved = self.buffer.save("temp.wav")

                        if saved:

                            print("✅ Audio Saved")

                            text = transcribe_audio("temp.wav").strip()

                            if not text:
                                continue
                            text_lower = text.lower().strip()

                            if speech_manager.speaking:

                                stop_words = [
                                    "stop",
                                    "jarvis stop",
                                    "stop jarvis",
                                    "cancel",
                                    "be quiet",
                                    "quiet"
                                ]

                                if any(word == text_lower for word in stop_words):
                                    print("Interrupt Detected")

                                    speech_manager.stop()

                                    continue

                            print("You:", text)

                            text_lower = text.lower()

                            if not any(word in text_lower for word in WAKE_WORDS):
                                print("Ignored (No Wake Word)")
                                continue

                            for word in WAKE_WORDS:
                                text = text.replace(word, "", 1)
                                text = text.replace(word.title(), "", 1)

                            text = text.strip(",.!?")

                            if not text:
                                speech_manager.speak("Yes Sir.")
                                continue

                            response = ask_jarvis(text)

                            if response:
                                print()
                                speech_manager.speak(response)


conversation = ConversationLoop()