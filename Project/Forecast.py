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


def getStockChart(outputStocks, datelist):
    fig = px.line(outputStocks, x=datelist , y=outputStocks[constants.TICKER_TO_PREDICT]['Close'], title='Forecast')
    fig.layout.update(xaxis_rangeslider_visible=True)
    return fig

def getModelPrediction(loadedModel, stocks):
    XFinalForecastData, _ = initializeForecast(stocks)
    
    # Predict the value for 1 day
    YPred = Prediction.predictionForValidation(loadedModel, XFinalForecastData)

    # Inverse scale
    YPredInv = inverseScaleForecast(stocks, YPred)

    return YPredInv
    
def getForecast(period, modelFilename, weightsFilename):

    # DateList
    datelist = pd.date_range(datetime.today(), periods = period).to_pydatetime().tolist()

    # Loading Model from saved JSON and Weights
    with open(modelFilename , 'r') as jsonFile:
        jsonSavedModel = jsonFile.read()
    loadedModel = tf.keras.models.model_from_json(jsonSavedModel)
    loadedModel.load_weights(weightsFilename)
    loadedModel.compile(loss=constants.LOSS_FUNCTION,
                  optimizer=tf.keras.optimizers.Adam(learning_rate=constants.LEARNING_RATE),
                  metrics=constants.METRICS
                  )

    # Get the last 1 month data
    stocks = pd.DataFrame()
    stocks = getData(False, '1mo')

    for i in range(period):
        YPredInv = getModelPrediction(loadedModel, stocks)
        if i == 0:
            st.write(f'Forecast for tomorrow : {float(YPredInv[-1])}')
        lastRow = stocks.tail(1)
        lastRow[constants.TICKER_TO_PREDICT, 'Close'] = YPredInv[-1]
        stocks = stocks.append(lastRow)

    outputStocks = stocks.tail(period)
    if period > 1:
        st.write(f'Forecast forthe next {period} days')
        st.plotly_chart(getStockChart(outputStocks, datelist))

        











# def getForecast(period, modelFilename, weightsFilename):
#     with open(modelFilename , 'r') as jsonFile:
#         jsonSavedModel = jsonFile.read()
#     loadedModel = tf.keras.models.model_from_json(jsonSavedModel)
#     st.write(loadedModel.summary())
#     loadedModel.load_weights(weightsFilename)
#     loadedModel.compile(loss=constants.LOSS_FUNCTION,
#                   optimizer=tf.keras.optimizers.Adam(learning_rate=constants.LEARNING_RATE),
#                   metrics=constants.METRICS
#                   )
#     stocks = pd.DataFrame()
#     stocks = getData(False, '1mo')
#     XFinalForecastData, YFinalForecastData = initializeForecast(stocks)
#     YPred = Prediction.predictionForValidation(loadedModel, XFinalForecastData)
#     YPredInv = inverseScaleForecast(stocks, YPred)
#     st.write(YPredInv)