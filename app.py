from flask import Flask, render_template, request, flash, redirect, url_for
import os
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'secret_key_here'  # For flashing messages


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
        with open(os.path.join(app.config['UPLOAD_FOLDER'], f"{name}.png"), "wb") as f:
            f.write(base64.decodebytes(image_data.encode()))

        # Now you have the image, integrate the facial recognition logic here

        flash("Login successful!", "success")
        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
