import sounddevice as sd
import soundfile as sf
import numpy as np

from silero_vad import load_silero_vad
from voice.silence_detector import SilenceDetector

SAMPLE_RATE = 16000


class AudioRecorder:

    def __init__(self):
        self.sample_rate = SAMPLE_RATE

        print("Loading Silero VAD...")

        self.vad = load_silero_vad()

        self.detector = SilenceDetector(
            self.vad,
            self.sample_rate
        )

        print("Silero Ready")

    def record(self, filename="temp.wav", duration=5):

        print("Listening...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(filename, audio, self.sample_rate)

        return filename


recorder = AudioRecorder()


def record_audio():
    return recorder.record()