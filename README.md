# 🐾 Cat & Dog Image Classification System

A Flask-based Deep Learning web application that classifies uploaded images as either **Cat 🐱** or **Dog 🐶** using a Convolutional Neural Network (CNN) built with TensorFlow/Keras.

The application provides a modern and interactive interface where users can upload an image, instantly receive a prediction with confidence score, and perform multiple predictions through an animated popup-based user experience.

https://img.shields.io/badge/Python-3.11+-blue.svg
![Flask](https://img.shields.io/badge/Flaskk.svg
![TensorFlow](https://img.sh/TensorFlow-2.x-orange.svg
![Kps://img.shields.io/badge/Keras-Deep%20Learning-red.svg
![Render](https://img.shieldsDeployment-Render-46E3B7.svg
![License](https://img.shields.io/badge/Licensesvg

---

# 🌐 Live Demo

**🚀 Try it live:**

https://cat-dog-classification-v4ob.onrender.com

> _Note: Render free-tier services may take a few seconds to wake up after inactivity._

---

# ✨ Features

## 🐾 Image Classification

- Upload Cat or Dog images.
- CNN-based prediction.
- Real-time classification.
- Confidence score display.
- Prediction popup modal.

## 🎨 User Interface

- Modern glassmorphism design.
- Fully responsive layout.
- Animated gradient background.
- Floating UI effects.
- One-page application.
- No scrolling required.
- Mobile-friendly design.

## ⚡ Performance

- Fast TensorFlow inference.
- Images processed directly in memory.
- No uploaded image storage.
- Lightweight Flask backend.

## ☁️ Deployment Ready

- Render deployment support.
- Gunicorn production server.
- Simple project structure.
- Easy GitHub integration.

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Flask, Python |
| Deep Learning | TensorFlow, Keras |
| Image Processing | Pillow, NumPy |
| Frontend | HTML5, CSS3, JavaScript |
| UI Design | Glassmorphism, Animations |
| Deployment | Render |
| Version Control | Git & GitHub |

---

# 📸 Screenshots

> Add screenshots after deployment.

- 🏠 Home Page
- 📤 Image Upload Screen
- 🐱 Cat Prediction Popup
- 🐶 Dog Prediction Popup
- 📱 Mobile Responsive View

---

# 📂 Project Structure

```text
CatDogClassifier/
│
├── app.py
├── cat_dog_model.keras
├── requirements.txt
├── render.yaml
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
```

---

# 🚀 Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/cat-dog-classification.git
```

```bash
cd cat-dog-classification
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Trained Model

Place your trained model file in the project root:

```text
cat_dog_model.keras
```

Example:

```python
model.save("cat_dog_model.keras")
```

---

## 5. Run Application

```bash
python app.py
```

---

## 6. Open Browser

```text
http://127.0.0.1:5000
```

---

# 💡 Usage

## Upload Image

1. Open the application.
2. Click **Choose Image**.
3. Select a Cat or Dog image.
4. Click **Predict Now**.

---

## View Prediction

The model will display:

- Predicted Class
- Confidence Score
- Prediction Emoji
- Popup Result Window

Example:

```text
Prediction: Cat 🐱
Confidence: 98.42%
```

or

```text
Prediction: Dog 🐶
Confidence: 99.15%
```

---

# 🧠 CNN Model Architecture

```text
Input Layer (256 × 256 × 3)

↓ Conv2D (32)
↓ BatchNormalization
↓ MaxPooling2D

↓ Conv2D (64)
↓ BatchNormalization
↓ MaxPooling2D

↓ Conv2D (128)
↓ BatchNormalization
↓ MaxPooling2D

↓ Flatten

↓ Dense (128)
↓ Dropout

↓ Dense (64)
↓ Dropout

↓ Dense (1)
↓ Sigmoid
```

---

# ⚙️ Training Configuration

## Optimizer

```python
adam
```

## Loss Function

```python
binary_crossentropy
```

## Metric

```python
accuracy
```

## Image Size

```python
256 x 256
```

## Batch Size

```python
32
```

---

# 🎯 Prediction Logic

```python
if prediction < 0.5:
    print("Cat")
else:
    print("Dog")
```

---

# 🔒 Privacy

This application does **not store uploaded images**.

Images are:

- Processed in memory
- Used only for prediction
- Discarded immediately after inference

This improves:

- Security
- Privacy
- Performance

---

# ☁️ Deployment on Render

## Required Files

```text
requirements.txt
render.yaml
app.py
cat_dog_model.keras
```

---

## Deployment Steps

### 1. Push Project to GitHub

```bash
git add .
git commit -m "Initial Commit"
git push
```

### 2. Login to Render

https://render.com

### 3. Create New Web Service

- Connect GitHub repository
- Select project repository

### 4. Configure Service

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
gunicorn app:app
```

Runtime

```text
Python
```

### 5. Deploy

Click:

```text
Create Web Service
```

Render will automatically deploy your application.

---

# 🔮 Future Enhancements

- Multi-animal classification
- Drag and drop uploads
- Model explainability
- Grad-CAM visualization
- Camera capture support
- User authentication
- Batch image prediction
- API endpoint support

---

# 👥 Who Is This For?

- 🎓 Students learning Deep Learning
- 🤖 Machine Learning Engineers
- 🧠 AI Enthusiasts
- 🎯 Computer Vision Practitioners
- 🌐 Flask Developers
- 📚 TensorFlow Learners

---

# ⚠️ Disclaimer

> This project is intended for educational and learning purposes.
>
> Prediction results depend on training data quality and model performance.
>
> The author does not guarantee 100% classification accuracy for unseen images.

---

# 👨‍💻 Author

**Suraj Prakash Verma**

- 🏢 UST Global
- 🌐 GitHub: https://github.com/surajprakashverma

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 🌟 Show Your Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🛠️ Contribute improvements

📢 Share with fellow developers

Happy Coding! 🚀
