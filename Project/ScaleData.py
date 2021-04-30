"""ScaleData.py: Scales the data supplied"""


# External Imports
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
import streamlit as st

# Internal Imports
from . import constants

# Filenames of Scalers
featureScalerFilename = "saveScaler/featureScaler.save"
closeScalerFilename = "saveScaler/closeScaler.save"

# Function to perform scaling on the data


def Scale(train, validation):
    featureScaler = RobustScaler()
    scaledTrain, scaledValidation = train.copy(), validation.copy()
    for ticker in constants.TICKER_SET:
        featureScaler.fit(train.loc[:, ticker])
        scaledTrain.loc[:, ticker] = featureScaler.transform(train.loc[:, ticker])
        scaledValidation.loc[:, ticker] = featureScaler.transform(validation.loc[:, ticker])

    # Saving the scaler for later use
    joblib.dump(featureScaler, featureScalerFilename)

    return scaledTrain, scaledValidation

# Function to perform inverse scaling for vizualization and output


def inverseScale(train, YTrain, YValidation, YPred):

    closeScaler = RobustScaler()
    closeScaler.fit(np.array(train.loc[:, (constants.TICKER_TO_PREDICT, 'Close')]).reshape(-1, 1))

    YTrainInv = closeScaler.inverse_transform(YTrain.reshape(1, -1))
    YValidationInv = closeScaler.inverse_transform(YValidation.reshape(-1, 1))
    YPredInv = closeScaler.inverse_transform(YPred.reshape(-1, 1))

    joblib.dump(closeScaler, closeScalerFilename)

    return YPredInv, YValidationInv 


def ScaleForecast(forecastStocks):
    featureScaler = RobustScaler()
    scaledForecastStocks = forecastStocks.copy()
    for ticker in constants.TICKER_SET:
        featureScaler.fit(forecastStocks.loc[:, ticker])
        scaledForecastStocks.loc[:, ticker] = featureScaler.transform(forecastStocks.loc[:, ticker])

    return scaledForecastStocks

def inverseScaleForecast(forecastStocks, YPred):

    closeScaler = RobustScaler()
    closeScaler.fit(np.array(forecastStocks.loc[:, (constants.TICKER_TO_PREDICT, 'Close')]).reshape(-1, 1))
    YPredInv = closeScaler.inverse_transform(YPred.reshape(-1, 1))

    # joblib.dump(closeScaler, closeScalerFilename)

    return YPredInv