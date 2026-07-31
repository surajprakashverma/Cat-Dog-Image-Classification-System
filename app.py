import os
import numpy as np
from flask import Flask, render_template, request
from tensorflow import keras
from PIL import Image

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

MODEL_PATH = "cat_dog_model.keras"

model = keras.models.load_model(MODEL_PATH)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_image(file):
    img = Image.open(file).convert("RGB")
    img = img.resize((256, 256))

    img_array = np.array(img, dtype=np.float32)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)[0][0]

    if prediction < 0.5:
        label = "Cat"
        confidence = (1 - prediction) * 100
        emoji = "🐱"
    else:
        label = "Dog"
        confidence = prediction * 100
        emoji = "🐶"

    return label, confidence, prediction, emoji


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    raw_value = None
    emoji = None
    error = None

    if request.method == "POST":

        if "file" not in request.files:
            error = "No file uploaded. Please choose an image."
            return render_template("index.html", error=error)

        file = request.files["file"]

        if file.filename == "":
            error = "No image selected. Please upload a cat or dog image."
            return render_template("index.html", error=error)

        if file and allowed_file(file.filename):
            result, confidence, raw_value, emoji = predict_image(file)
        else:
            error = "Invalid file type. Please upload PNG, JPG, JPEG, or WEBP image."

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        raw_value=raw_value,
        emoji=emoji,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
