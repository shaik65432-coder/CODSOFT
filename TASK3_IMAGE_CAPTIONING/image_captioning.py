import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing import image


# Load pretrained model
model = MobileNetV2(weights="imagenet")


# Load image
img_path = "sample.jpg"

img = image.load_img(img_path, target_size=(224, 224))

img_array = image.img_to_array(img)

img_array = np.expand_dims(img_array, axis=0)

img_array = preprocess_input(img_array)


# Predict image content
predictions = model.predict(img_array)

decoded = decode_predictions(predictions, top=1)[0]


# Get detected object
label = decoded[0][1]

confidence = decoded[0][2]


# Generate caption
caption = f"This image contains a {label}."


print("\n=== IMAGE CAPTIONING AI ===\n")

print("Generated Caption:")
print(caption)

print(f"\nConfidence Score: {confidence:.2f}")