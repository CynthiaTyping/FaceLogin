from flask import Flask, render_template, request, flash, redirect, url_for
import os
import base64
from flask import jsonify
from static.models.model import SiameseModel

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'secret_key_here'  # For flashing messages

# Path to the true image (you may need to adjust this based on your setup)
TRUE_IMAGE_PATH = os.path.join(app.config['UPLOAD_FOLDER'], 'true_img.png')

# Instantiate the SiameseModel class
siamese = SiameseModel()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def get_image():
    if request.method == 'POST':
        name = request.form.get('name')
        image_data = request.form.get('imageData')

        # Convert base64 image data to an image file
        image_data = image_data.split(",")[1]
        uploaded_img_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{name}.png")
        with open(uploaded_img_path, "wb") as f:
            f.write(base64.decodebytes(image_data.encode()))

        # Predict similarity
        similarity_score = siamese.predict_similarity(TRUE_IMAGE_PATH, uploaded_img_path)

        # Decide on a threshold for similarity score to consider the upload successful
        threshold = 0.7
        if similarity_score >= threshold:
            flash("Login successful!", "success")
        else:
            flash("Login failed! Please try again.", "danger")

        return redirect(url_for('home'))

    return render_template('index.html')

@app.route('/predict_similarity', methods=['POST'])
def predict_similarity():
    # Check if the post request has the files part
    if 'true_img' not in request.files or 'uploaded_img' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    true_img = request.files['true_img']
    uploaded_img = request.files['uploaded_img']

    # Check for empty files
    if true_img.filename == '' or uploaded_img.filename == '':
        return jsonify({"error": "No selected files"}), 400

    # Create temporary paths for saving uploaded files
    true_img_path = os.path.join("tmp", true_img.filename)
    uploaded_img_path = os.path.join("tmp", uploaded_img.filename)

    # Save the files
    true_img.save(true_img_path)
    uploaded_img.save(uploaded_img_path)

    # Predict
    similarity_score = siamese.predict_similarity(true_img_path, uploaded_img_path)

    # Cleanup
    os.remove(true_img_path)
    os.remove(uploaded_img_path)

    return jsonify({"similarity_score": similarity_score})


if __name__ == '__main__':
    app.run(debug=True)
