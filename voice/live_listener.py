import sounddevice as sd
import queue

SAMPLE_RATE = 16000
CHANNELS = 1
BLOCK_SIZE = 1024


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
            channels=CHANNELS,
            blocksize=BLOCK_SIZE,
            dtype="float32",
            callback=self.callback
        ):

            while True:

                yield self.queue.get()


listener = LiveListener()