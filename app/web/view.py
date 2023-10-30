# coding: UTF-8
# @Time    : 2023/10/30
# @Author  : Qi Ming
# @WeChat  : 19310619597
# @FileName: view.py
# @Software: Pycharm
from . import web
from flask import render_template, request, flash, redirect, url_for, jsonify
import os
import base64
from common import UPLOAD_FOLDER
from ..model import Users
from .. import db

TRUE_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, 'true_img.png')

from app.static.mod.modl import SiameseModel

siamese = SiameseModel()


@web.route('/')
def home():
    return render_template('index.html')


@web.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        image_data = request.form.get('imageData')
        user = Users.query.filter(username=name).first()
        if user:
            data = {
                'status': 1,
                'message': '您可以直接登录'  # 前端直接跳转登录
            }
            return jsonify(data)

        image_data = image_data.split(",")[1]
        dir_path = UPLOAD_FOLDER
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        uploaded_img_path = os.path.join(dir_path, f"{name}.png")
        new = Users(username=name, path=uploaded_img_path)
        db.session.add(new)
        db.session.commit()
        data = {
            'status': 1,
            'message': 'Success'
        }
        return jsonify(data)


@app.route('/predict', methods=['POST'])
def predict_similarity():
    if 'true_img' not in request.json or 'uploaded_img' not in request.json:
        return jsonify({"error": "No file part in the request"}), 400

    true_img_path = request.json['true_img']
    uploaded_img_path = request.json['uploaded_img']

    similarity_score = siamese.predict_similarity(true_img_path, uploaded_img_path)

    return jsonify({"similarity_score": similarity_score})


@web.route('/upload', methods=['GET', 'POST'])
def get_image():
    if request.method == "POST":
        name = request.form.get('name')
        image_data = request.form.get('imageData')

        image_data = image_data.split(",")[1]
        dir_path = UPLOAD_FOLDER
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


@web.route('/predict', methods=['POST'])
def predict_similarity():
    if 'true_img' not in request.json or 'uploaded_img' not in request.json:
        return jsonify({"error": "No file part in the request"}), 400

    true_img_path = request.json['true_img']
    uploaded_img_path = request.json['uploaded_img']

    similarity_score = siamese.predict_similarity(true_img_path, uploaded_img_path)

    return jsonify({"similarity_score": similarity_score})
