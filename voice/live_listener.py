import queue
import sounddevice as sd

from voice.config import (
    SAMPLE_RATE,
    BLOCK_SIZE,
)


class LiveListener:

    def __init__(self):

        self.queue = queue.Queue()

        print("Live Listener Ready")

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.queue.put(indata.copy())

    def listen(self):

        print("Listening continuously...")

        with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            blocksize=BLOCK_SIZE,
            callback=self.callback
        ):

            while True:

                yield self.queue.get()


listener = LiveListener()