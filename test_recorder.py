from voice.audio_recorder import record_audio
from voice.offline_listener import get_model

print("Recording...")
audio_file = record_audio()

print("Transcribing...")

model = get_model()

segments, info = model.transcribe(
    audio_file,
    beam_size=5
)

print("Detected language:", info.language)

print("\nYou said:")

for segment in segments:
    print(segment.text)