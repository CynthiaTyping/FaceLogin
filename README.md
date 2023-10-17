# FaceLogin
Face Recognition Web App This project is a web-based facial recognition application built with Flask, Keras, and OpenCV. The app captures images from a user's webcam, detects faces using Haar Cascades, and then authenticates users based on the similarity between the captured face and a stored reference using a pre-trained Siamese neural network.

1. index.html: 
This centralized page introduces the "Facial Login System" with a stylish gradient background. Users can input their name and upload an image for facial verification. The filename updates interactively upon file selection via jQuery. A footer credits designer Synthia Li with a linked personal website.
2. recognition.html:
This page can show a "processing" message or animation while the server processes the facial recognition.
3. result.html:
This page can be used to display the result of the recognition. You might have a success message and a failure message, and display one based on the result.
