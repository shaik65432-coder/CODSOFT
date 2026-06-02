import cv2
import os
import numpy as np
from PIL import Image

# Face detector
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

label_map = {}
current_label = 0


# Read dataset
dataset_path = "dataset"

for person_name in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person_name)

    if os.path.isdir(person_path):

        label_map[current_label] = person_name

        for image_name in os.listdir(person_path):

            image_path = os.path.join(person_path, image_name)

            image = Image.open(image_path).convert('L')

            image_array = np.array(image, 'uint8')

            detected_faces = detector.detectMultiScale(image_array)

            for (x, y, w, h) in detected_faces:

                faces.append(image_array[y:y+h, x:x+w])

                labels.append(current_label)

        current_label += 1


# Train recognizer
recognizer.train(faces, np.array(labels))

# Save trained model
recognizer.save("trainer/trainer.yml")

print("Training completed successfully.")