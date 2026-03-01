📂 Files Included
app.py → 🚀 Main application file (training + prediction)

train/ → 🗂️ Dataset folder

healthy/ 🍀

diseased/ 🍂

uploads/ → 📥 Images uploaded by users

temp.jpg → 🖼️ Sample test image

🛠️ Technologies Used
🐍 Python

👁️ OpenCV

🤖 TensorFlow / Keras

🌐 Flask (for web interface)

▶️ How to Run
1️⃣ Install required libraries

pip install tensorflow opencv-python flask numpy
2️⃣ Arrange dataset
Place leaf images inside the train/ folder in two subfolders:

healthy

diseased

3️⃣ Run the application

python app.py
4️⃣ Open in browser 🌐
Go to: http://127.0.0.1:5000

5️⃣ Upload a leaf image 📤
The system will display:

🍃 Healthy Leaf
or

🦠 Diseased Leaf
