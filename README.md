# FaceLogin
Face Recognition Web App This project is a web-based facial recognition application built with Flask, Keras, and OpenCV. The app captures images from a user's webcam, detects faces using Haar Cascades, and then authenticates users based on the similarity between the captured face and a stored reference using a pre-trained Siamese neural network.

project structure:
FaceLogin/
│
├── face_detection/
│   ├── __init__.py
│   └── face_detector.py  (contains detect_faces function)
│
├── face_recognition/
│   ├── __init__.py
│   ├── siamese_network.py (contains model building and training if required)
│   └── recognizer.py (contains the face recognition logic)
│
├── utilities/
│   ├── __init__.py
│   └── helpers.py  (contains utility functions like write_on_frame)
│
├── static/
│   └── haarcascade_frontalface_default.xml
│
├── main.py  (entry point for the application)
│
└── .gitignore

