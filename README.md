## 🌿 Leaf Disease Detection — CNN Image Classification

### 📖 Project Description

This project is a deep learning–based web application that detects whether a plant leaf is **Healthy 🍃** or **Diseased 🦠** using a Convolutional Neural Network (CNN). The model is trained on a dataset of leaf images stored in two categories: healthy and diseased. After training, users can upload a leaf image through the frontend interface, and the system predicts its condition instantly with high accuracy. This helps in early detection of plant diseases and supports smart agriculture.

---

### 📂 Project Structure

```
Leaf-Disease-Detection/
│── app.py                # Main application (training + prediction)
│── train/                # Dataset folder
│    ├── healthy/         # Healthy leaf images
│    └── diseased/        # Diseased leaf images
│── uploads/              # User uploaded images
│── temp.jpg              # Sample test image
│── requirements.txt      # Required libraries
│── README.md             # Project documentation
```

---

### 🛠️ Technologies Used

* 🐍 Python
* 🤖 TensorFlow / Keras (CNN Model)
* 👁️ OpenCV (Image Processing)
* 🌐 Flask (Web Interface)
* 🔢 NumPy

---

### ▶️ How to Run the Project

#### 1️⃣ Install Dependencies

```bash
pip install tensorflow opencv-python flask numpy
```

#### 2️⃣ Prepare Dataset

Place images inside:

* `train/healthy/` 🍀
* `train/diseased/` 🍂

#### 3️⃣ Run Application

```bash
python app.py
```

#### 4️⃣ Open in Browser 🌐

Go to:

```
http://127.0.0.1:5000
```

#### 5️⃣ Upload Leaf Image 📤

The system will display:

* 🍃 **Healthy Leaf**
  or
* 🦠 **Diseased Leaf**

---

### 🎯 Features

✔️ Train model automatically
✔️ Upload image from frontend
✔️ Instant prediction
✔️ Simple and user-friendly interface

---

If you want, I can also give you a **perfect GitHub README.md file**, **requirements.txt**, and a **project title + description for resume/LinkedIn** 🚀
