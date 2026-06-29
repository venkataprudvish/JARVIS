from collections import deque
import numpy as np
import soundfile as sf

from voice.config import SAMPLE_RATE, PRE_ROLL_SECONDS, BLOCK_SIZE


class AudioBuffer:

    def __init__(self):

        max_chunks = int((SAMPLE_RATE * PRE_ROLL_SECONDS) / BLOCK_SIZE)

        self.pre_roll = deque(maxlen=max_chunks)

        self.recording = []

    def add_live_chunk(self, chunk):

        self.pre_roll.append(chunk)

    def start_recording(self):

        self.recording = list(self.pre_roll)

    def add_recording_chunk(self, chunk):

        self.recording.append(chunk)

    def save(self, filename):

        if not self.recording:
            return False

        audio = np.concatenate(self.recording, axis=0)

        sf.write(filename, audio, SAMPLE_RATE)

        self.recording.clear()

        return True