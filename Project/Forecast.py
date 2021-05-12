''' Forecast.py : Get forecast for the selected tickers'''


# External Imports
import tensorflow as tf
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Internal Imports
from .DataFetch import getData
from .DatasetCreation import initializeForecast
from .ScaleData import inverseScaleForecast
from . import constants
from . import Prediction

# Function to generate a plotly graph of the forecast 

def getStockChart(outputStocks, datelist):
    fig = px.line(outputStocks, x=datelist,
                  y=outputStocks[constants.TICKER_TO_PREDICT]['Close'], title='Forecast')
    fig.layout.update(xaxis_rangeslider_visible=True)
    return fig


# Function to get the model prediction

def getModelPrediction(loadedModel, stocks):
    XFinalForecastData, _ = initializeForecast(stocks)

    # Predict the value for 1 day
    YPred = Prediction.predictionForValidation(loadedModel, XFinalForecastData)

    # Inverse scale
    YPredInv = inverseScaleForecast(stocks, YPred)

    return YPredInv


# Function to start the forecasting process 

def getForecast(period, modelFilename, weightsFilename):

    # Get the dates from today upto a specific period specified
    datelist = pd.date_range(
        datetime.today(), periods=period).to_pydatetime().tolist()

    # Loading the model from the specified files
    with open(modelFilename, 'r') as jsonFile:
        jsonSavedModel = jsonFile.read()
    loadedModel = tf.keras.models.model_from_json(jsonSavedModel)
    loadedModel.load_weights(weightsFilename)
    loadedModel.compile(loss=constants.LOSS_FUNCTION,
                        optimizer=tf.keras.optimizers.Adam(
                            learning_rate=constants.LEARNING_RATE),
                        metrics=constants.METRICS
                        )

    # Get the last 1 month data
    stocks = pd.DataFrame()
    stocks = getData(False, '1mo')

    # Get forecast to the next day and the subsequent period if specified
    for i in range(period):
        YPredInv = getModelPrediction(loadedModel, stocks)
        if i == 0:
            st.write(f'Forecast for tomorrow : {float(YPredInv[-1])}')
        lastRow = stocks.tail(1)
        lastRow[constants.TICKER_TO_PREDICT, 'Close'] = YPredInv[-1]
        stocks = stocks.append(lastRow)

    # Output the forecasts
    outputStocks = stocks.tail(period)
    if period > 1:
        st.write(f'Forecast forthe next {period} days')
        st.plotly_chart(getStockChart(outputStocks, datelist))
