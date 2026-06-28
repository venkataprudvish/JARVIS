from voice.live_listener import listener
from voice.audio_buffer import AudioBuffer
from voice.vad_engine import vad


class ConversationLoop:

    def __init__(self):

        self.buffer = AudioBuffer()

        self.is_talking = False

        self.silence_count = 0

        print("Conversation Loop Ready")

    def start(self):

        print("Starting conversation loop...")

        for chunk in listener.listen():


            import numpy as np

            volume = np.abs(chunk).mean()

            THRESHOLD = 0.003

            if volume > THRESHOLD:

                self.silence_count = 0

                if not self.is_talking:
                    self.is_talking = True

                    print("🎤 Speech Started")

            elif self.is_talking:

                self.silence_count += 1

                if self.silence_count >= 10:
                    self.is_talking = False

                    self.silence_count = 0

                    print("🛑 Speech Ended")


conversation = ConversationLoop()