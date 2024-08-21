from django.db import models
from django.contrib.auth.models import User
import pickle
import joblib
import sklearn

class IrisPredictor:
    model = None
    species_mapping = {
        1: 'Iris-Setosa',
        2: 'Iris-Versicolor',
        3: 'Iris-Virginica',
    }
    @classmethod
    def load_model(cls):
        if cls.model is None:
           cls.model = joblib.load(r'C:\Users\USER\Desktop\flower\classification\classi\iris.pkl')
    @staticmethod
    def predict(sepal_length, sepal_width, petal_length, petal_width):
        IrisPredictor.load_model()

        # Preprocess the input
        features = [sepal_length, sepal_width, petal_length, petal_width] 
        prediction_encoded = IrisPredictor.model.predict([features])[0]
        prediction = IrisPredictor.species_mapping.get(prediction_encoded, 'unknown species')

        return prediction 



