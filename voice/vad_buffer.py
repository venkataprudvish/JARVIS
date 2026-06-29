from collections import deque
import numpy as np

from voice.config import SAMPLE_RATE


class VADBuffer:

    def __init__(self):

        self.window = deque(maxlen=SAMPLE_RATE // 2)

    def add(self, chunk):

        self.window.extend(chunk.flatten())

    def get_audio(self):

        return np.array(self.window, dtype=np.float32)