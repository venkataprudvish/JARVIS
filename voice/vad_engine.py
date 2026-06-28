from voice.silence_detector import SilenceDetector
from silero_vad import load_silero_vad


class VADEngine:

    def __init__(self, sample_rate=16000):

        print("Loading VAD Engine...")

        self.sample_rate = sample_rate

        self.model = load_silero_vad()

        self.detector = SilenceDetector(
            self.model,
            self.sample_rate
        )

        print("VAD Engine Ready")

    def is_speaking(self, audio):

        return self.detector.has_speech(audio)


vad = VADEngine()