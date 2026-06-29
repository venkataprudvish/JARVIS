from voice import speech_output


class SpeechManager:

    def speak(self, text):
        speech_output.speak(text)

    def stop(self):
        speech_output.stop_speaking()

    @property
    def speaking(self):
        return speech_output.is_speaking


speech_manager = SpeechManager()