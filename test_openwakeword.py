from openwakeword.model import Model

print("=" * 50)
print("TESTING OPENWAKEWORD")
print("=" * 50)

print("Loading model...")

model = Model(
    inference_framework="onnx"
)


print("SUCCESS!")
print(type(model))