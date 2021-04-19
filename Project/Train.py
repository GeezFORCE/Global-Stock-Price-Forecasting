#!/usr/bin/env python

"""Train.py: Main Program"""

# External Imports
import pandas as pd
import numpy as np
import tensorflow as tf
import streamlit as st
import plotly.graph_objs as go
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint

# Local Imports
from . import constants
from . import DataFetch
from . import DatasetCreation
from . import ModelDefenition
from . import Prediction
from . import SaveModel
from . import ScaleData
from . import plot

def trainModel():

    if __name__ != '__main__':
        st.sidebar.write('When training completes a graph will appear on your screen.')
        st.sidebar.write('To stop the training process, click on the stop button in the top right corner, Errors/ Warning may appear, ignore')
        st.sidebar.write('Donot click train again!!!!!!') 
    # Data Fetch
    stocks = pd.DataFrame()
    stocks = DataFetch.getData()

    # Dataset Creation and Scaling of Data
    train, validation, XTrain, YTrain, XValidation, YValidation = DatasetCreation.initialize(stocks)

    # Model Defenition

    # defineModel(XTrain, noOfLSTMUnits=128, noOfDenseUnits=1, noOfBiDirectionalLayers=1,
    #             noOfDenseLayers=1, dropoutRate=0.1, returnSequences=False)

    # model = ModelDefenition.defineModel(XTrain) #, 256, 64, 2, 2, 0.005, True)  

    model = ModelDefenition.defineModel(XTrain, 
                                        constants.NO_OF_LSTM_UNITS,
                                        constants.NO_OF_DENSE_UNITS,
                                        constants.NO_OF_BIDIRECTIONAL_LAYERS,
                                        constants.NO_OF_DENSE_LAYERS,
                                        constants.DROPOUTRATE,
                                        constants.RETURN_SEQUENCES)

    # Tensorboard Object
    tensorboard = TensorBoard(log_dir=f'logs/{constants.NAME}')

    # Checkpoint Defenition and Model Step Saves
    filepath = "RNN_Final-{epoch:02d}"
    checkpoint = ModelCheckpoint("models/{}.model".format(filepath, monitor='val_acc',
                                                        save_weights_only=False, verbose=0,
                                                        save_best_only=True, mode='max'))

    # Model Fit
    history = model.fit(
        XTrain, YTrain,
        epochs=constants.EPOCHS,
        batch_size=constants.BATCH_SIZE,
        validation_split=constants.VALIDATION_SET_PERCENTAGE,
        shuffle=False,
        callbacks=[tensorboard, checkpoint]
    )

    # Save Model
    SaveModel.saveModelInformation(model)

    # Prediction over Validation set
    YPred = Prediction.predictionForValidation(model, XValidation)

    # Scale the prediction
    YPredInv, YValidationInv = ScaleData.inverseScale(train,YTrain, YValidation, YPred)

    # Plot the results

    fig = plot.PlotlyPlotValidation(validation,YPredInv, YValidationInv)

    return fig    

if __name__ == "__main__":
    fig = trainModel()
    fig.show()