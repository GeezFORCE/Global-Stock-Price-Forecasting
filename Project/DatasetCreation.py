"""DatasetCreation.py: Creates datasets from the supplied data"""


# External Imports
import numpy as np

# Internal Imports
from . import constants
from . import SaveData
from . import ScaleData


# Function to create the dataset based on timestep provided

def createDataset(x, y, timeSteps=1):
    X, Y = [], []
    for i in range(len(x) - timeSteps):
        X.append(x.iloc[i:(i + timeSteps)].values)
        Y.append(y.iloc[i + timeSteps])
    return np.array(X), np.array(Y)


# Function to call Scale() and createDataset()

def initialize(stocks):
    trainSize = (len(stocks) - int(constants.VALIDATION_SET_PERCENTAGE*(len(stocks))))
    train, validation = stocks.iloc[0:trainSize], stocks.iloc[trainSize:len(stocks)]
    scaledTrain, scaledValidation = ScaleData.Scale(train, validation)
    SaveData.saveCSV(train, "Train")
    SaveData.saveCSV(validation, "Validation")
    SaveData.saveCSV(scaledTrain, "scaledTrain")
    SaveData.saveCSV(scaledValidation, "scaledValidation")
    yTrain = scaledTrain[constants.TICKER_TO_PREDICT]['Close']
    yValidation = scaledValidation[constants.TICKER_TO_PREDICT]['Close']
    XTrain, YTrain = createDataset(scaledTrain, yTrain, constants.TIMESTEPS)
    XValidation, YValidation = createDataset(scaledValidation, yValidation, constants.TIMESTEPS)
    SaveData.saveNumpy(XTrain, "XTrain")
    SaveData.saveNumpy(YTrain, "YTrain")
    SaveData.saveNumpy(XValidation, "XValidation")
    SaveData.saveNumpy(YValidation, "YValidation")
    return train, validation, XTrain, YTrain, XValidation, YValidation
