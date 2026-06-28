import numpy as np
from silero_vad import get_speech_timestamps


class SilenceDetector:

    def __init__(self, model, sample_rate=16000):
        self.model = model
        self.sample_rate = sample_rate

    def has_speech(self, audio):

        if len(audio.shape) > 1:
            audio = audio.flatten()

        audio = np.asarray(audio, dtype=np.float32)

        timestamps = get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=self.sample_rate
        )

        return len(timestamps) > 0