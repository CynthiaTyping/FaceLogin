from flask import Flask, render_template, request, flash, redirect, url_for
import os
import base64
from flask import jsonify
from static.models.model import SiameseModel

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'secret_key_here'

TRUE_IMAGE_PATH = os.path.join(app.config['UPLOAD_FOLDER'], 'true_img.png')

siamese = SiameseModel()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def get_image():
    if request.method == "POST":
        name = request.form.get('name')
        image_data = request.form.get('imageData')

        image_data = image_data.split(",")[1]
        dir_path = app.config['UPLOAD_FOLDER']
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        uploaded_img_path = os.path.join(dir_path, f"{name}.png")
        flash("Login successful!", "success")

        with open(uploaded_img_path, "wb") as f:
            f.write(base64.decodebytes(image_data.encode()))

        similarity_score = siamese.predict_similarity(TRUE_IMAGE_PATH, uploaded_img_path)

        threshold = 0.5
        if similarity_score >= threshold:
            flash("Login successful!", "success")
        else:
            flash("Login failed! Please try again.", "danger")

        return redirect(url_for('home'))
    return render_template('index.html')


@app.route('/predict_similarity', methods=['POST'])
def predict_similarity():
    if 'true_img' not in request.files or 'uploaded_img' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    true_img = request.files['true_img']
    uploaded_img = request.files['uploaded_img']

    if true_img.filename == '' or uploaded_img.filename == '':
        return jsonify({"error": "No selected files"}), 400

    true_img_path = os.path.join("tmp", true_img.filename)
    uploaded_img_path = os.path.join("tmp", uploaded_img.filename)

    true_img.save(true_img_path)
    uploaded_img.save(uploaded_img_path)

    similarity_score = siamese.predict_similarity(true_img_path, uploaded_img_path)

    os.remove(true_img_path)
    os.remove(uploaded_img_path)

    return jsonify({"similarity_score": similarity_score})


if __name__ == '__main__':
    app.run(debug=True)
