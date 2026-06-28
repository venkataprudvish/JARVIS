import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000
CHANNELS = 1
BLOCK_SIZE = 4000


class LiveListener:

    def __init__(self):

        self.sample_rate = SAMPLE_RATE

        print("Live Listener Ready")

    def listen(self):

        print("Listening continuously...")

        while True:

            audio = sd.rec(
                BLOCK_SIZE,
                samplerate=self.sample_rate,
                channels=CHANNELS,
                dtype="float32"
            )

            sd.wait()

            yield audio


listener = LiveListener()