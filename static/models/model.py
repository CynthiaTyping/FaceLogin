import os.path

import cv2
from keras.models import load_model
from keras import backend as K


class SiameseModel:
    def __init__(self):
        path = os.path.dirname(__file__)
        self.model = self.load_siamese_model(os.path.join(path, 'siamese_nn.h5'))

    @staticmethod
    def euclidean_distance(vectors):
        vector1, vector2 = vectors
        sum_square = K.sum(K.square(vector1 - vector2), axis=1, keepdims=True)
        return K.sqrt(K.maximum(sum_square, K.epsilon()))

    @staticmethod
    def contrastive_loss(Y_true, D):
        margin = 1
        return K.mean(Y_true * K.square(D) + (1 - Y_true) * K.maximum((margin-D),0))

    def load_siamese_model(self, model_path):
        return load_model(model_path, custom_objects={'contrastive_loss': self.contrastive_loss, 'euclidean_distance': self.euclidean_distance})

    def prepare_image(self, img_path):
        img = cv2.imread(img_path, 0)
        img = img.astype('float32')/255
        img = cv2.resize(img, (92, 112))
        img = img.reshape(1, img.shape[0], img.shape[1], 1)
        return img

    def predict_similarity(self, true_img_path, uploaded_img_path):
        true_img = self.prepare_image(true_img_path)
        uploaded_img = self.prepare_image(uploaded_img_path)
        return 1 - self.model.predict([true_img, uploaded_img])[0][0]
