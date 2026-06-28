import sounddevice as sd
import soundfile as sf
import numpy as np

from silero_vad import load_silero_vad
from voice.silence_detector import SilenceDetector


SAMPLE_RATE = 16000
CHUNK_DURATION = 0.25
SILENCE_LIMIT = 0.75


class SmartRecorder:

    def __init__(self):

        print("Loading Smart Recorder...")

        self.sample_rate = SAMPLE_RATE

        self.vad = load_silero_vad()

        self.detector = SilenceDetector(
            self.vad,
            self.sample_rate
        )

        print("Smart Recorder Ready")

    def record(self, filename="temp.wav"):

        print("Listening...")

        chunk_samples = int(CHUNK_DURATION * self.sample_rate)

        audio_chunks = []

        silence_time = 0.0
        speech_started = False

        while True:

            chunk = sd.rec(
                chunk_samples,
                samplerate=self.sample_rate,
                channels=1,
                dtype="float32"
            )

            sd.wait()

            audio_chunks.append(chunk)

            if self.detector.has_speech(chunk):

                speech_started = True
                silence_time = 0.0

            elif speech_started:

                silence_time += CHUNK_DURATION

                if silence_time >= SILENCE_LIMIT:
                    break

        audio = np.concatenate(audio_chunks, axis=0)

        sf.write(filename, audio, self.sample_rate)

        return filename


recorder = SmartRecorder()


def record_audio():
    return recorder.record()