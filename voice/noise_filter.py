import numpy as np
import noisereduce as nr


def reduce_noise(audio, sample_rate):

    if len(audio.shape) > 1:
        audio = audio.flatten()

    cleaned = nr.reduce_noise(
        y=audio,
        sr=sample_rate,
        stationary=True
    )

    return np.asarray(cleaned, dtype=np.float32)