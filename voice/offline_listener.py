from faster_whisper import WhisperModel
from voice.audio_recorder import record_audio

print("Loading Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper Ready")
last_text = ""


def transcribe_audio(audio_file):
    global last_text

    segments, info = model.transcribe(
        audio_file,
        beam_size=1,
        vad_filter=True,
        language="en"
    )

    text = ""

    for segment in segments:
        text += segment.text

    text = text.strip()

    if text == "":
        return ""

    if text == last_text:
        return ""

    last_text = text

    return text


def get_model():
    return model