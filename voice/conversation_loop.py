from voice.live_listener import listener
from voice.audio_buffer import AudioBuffer
from voice.vad_engine import vad


class ConversationLoop:

    def __init__(self):

        self.buffer = AudioBuffer()

        self.is_talking = False

        print("Conversation Loop Ready")


conversation = ConversationLoop()