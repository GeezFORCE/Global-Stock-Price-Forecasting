"""Prediction.py: Prediction based on supplied data"""


# External Imports
import tensorflow as tf

# Function to perform prediction


def predictionForValidation(model, XValidation):
    YPred = model.predict(XValidation)
    return YPred
