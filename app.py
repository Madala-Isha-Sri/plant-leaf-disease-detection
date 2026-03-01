import os
import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.utils import shuffle

IMG_SIZE = 128

# ================= TRAIN MODEL =================
@st.cache_resource
def train_model():
    data = []
    labels = []

    dataset_path = "train"

    for category in ["healthy", "diseased"]:
        path = os.path.join(dataset_path, category)
        class_num = 0 if category == "healthy" else 1

        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            img = cv2.imread(img_path)

            if img is None:
                continue

            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            data.append(img)
            labels.append(class_num)

    data = np.array(data) / 255.0
    labels = np.array(labels)

    # 🔥 Shuffle data (VERY IMPORTANT)
    data, labels = shuffle(data, labels)

    # 🔥 Improved CNN
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        MaxPooling2D(2,2),

        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),

        Conv2D(128, (3,3), activation='relu'),
        MaxPooling2D(2,2),

        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 🔥 More training for accuracy
    model.fit(data, labels, epochs=25, batch_size=16)

    return model


# ================= STREAMLIT UI =================
st.title("🌿 Leaf Disease Detector")
st.write("Upload a leaf image to check if it is Healthy or Diseased")

# Train model once internally
model = train_model()

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    st.image(img, caption="Uploaded Image", use_container_width=True)

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.reshape(img, (1, IMG_SIZE, IMG_SIZE, 3))

    prediction = model.predict(img)

    confidence = prediction[0][0]
    st.write("Confidence:", float(confidence))

    if confidence > 0.5:
        st.error("❌ Diseased Leaf")
    else:
        st.success("✅ Healthy Leaf")