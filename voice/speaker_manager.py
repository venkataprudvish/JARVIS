from speechbrain.inference.speaker import EncoderClassifier

print("Loading Speaker Recognition Model...")

classifier = EncoderClassifier.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec"
)

print("Speaker Recognition Ready")