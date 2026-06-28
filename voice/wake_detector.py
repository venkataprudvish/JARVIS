from openwakeword.model import Model

model = Model(
    wakeword_models=[]
)


def detect(audio_data):
    prediction = model.predict(audio_data)
    return prediction