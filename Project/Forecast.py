''' Forecast.py : Get forecast for the selected tickers'''


# External Imports
import tensorflow as tf
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
import zipfile
import tempfile

# Internal Imports
from .DataFetch import getData
from .DatasetCreation import initializeForecast
from .ScaleData import inverseScaleForecast
from . import constants
from . import Prediction
from .CurrencyConversion import inverseConvertCurrency

# Function to generate a plotly graph of the forecast 

def getStockChart(outputStocks, datelist):
    fig = px.line(outputStocks, x=datelist,
                  y=inverseConvertCurrency(outputStocks[constants.TICKER_TO_PREDICT]['Close']), title='Forecast')
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
    
    today=stocks[constants.TICKER_TO_PREDICT, 'Close'][-1]

    # Get forecast to the next day and the subsequent period if specified
    for i in range(period):
        YPredInv = getModelPrediction(loadedModel, stocks)
        if i == 0:
            st.write(f'Forecast for tomorrow : {float(inverseConvertCurrency(YPredInv[-1]))}')
        lastRow = stocks.tail(1)
        lastRow[constants.TICKER_TO_PREDICT, 'Close'] = YPredInv[-1]
        stocks = stocks.append(lastRow)

    # Output the forecasts
    outputStocks = stocks.tail(period)
    if period > 1:
        st.write(f'Forecast forthe next {period} days')
        st.plotly_chart(getStockChart(outputStocks, datelist))
    
    #Generate comparison table for showing increase or decrease in close price
    closepricetable=pd.DataFrame()
    for i in range(len(datelist)):
        datefinal=pd.to_datetime(datelist[i],utc=False)
        newrow=pd.DataFrame([inverseConvertCurrency(outputStocks[constants.TICKER_TO_PREDICT]['Close'][i])], index = [datefinal.date()],columns=['ClosePrice'])
        closepricetable=pd.concat([newrow,closepricetable])
    
    closepricetable=closepricetable.sort_index()
    def color_table(val):
        if val-inverseConvertCurrency(today)>0:
            color = 'green'
        elif val-inverseConvertCurrency(today)<0:
            color='red'
        else:
            color='grey'
        return f'background-color: {color}'
    a,b,c=st.beta_columns(3)
    with b:
        st.write(closepricetable.style.applymap(color_table, subset=['ClosePrice']))

# Function to start the forecasting process for uploaded model with model and weights separately
def getuploadedForecast(period, uploadedmodel, uploadedweight):

    # Get the dates from today upto a specific period specified
    datelist = pd.date_range(
    datetime.today(), periods=period).to_pydatetime().tolist()

    #load json and create model from disk     
    loaded_model_json = uploadedmodel.read()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    
    #loading weights to newly loaded model
    if uploadedweight is not None:
        myzipfile = zipfile.ZipFile(uploadedweight)
        with tempfile.TemporaryDirectory() as tmp_dir:
            myzipfile.extractall(tmp_dir)
            root_folder = myzipfile.namelist()[0] 
            model_dir = os.path.join(tmp_dir, root_folder)
            loaded_model.load_weights(model_dir)
            loaded_model.compile(loss=constants.LOSS_FUNCTION,
                        optimizer=tf.keras.optimizers.Adam(
                            learning_rate=constants.LEARNING_RATE),
                        metrics=constants.METRICS
                        )

    # Get the last 1 month data
    stocks = pd.DataFrame()
    stocks = getData(False, '1mo')
    
    today=stocks[constants.TICKER_TO_PREDICT, 'Close'][-1]

    # Get forecast to the next day and the subsequent period if specified
    for i in range(period):
        YPredInv = getModelPrediction(loaded_model, stocks)
        if i == 0:
            st.write(f'Forecast for tomorrow : {float(inverseConvertCurrency(YPredInv[-1]))}')
        lastRow = stocks.tail(1)
        lastRow[constants.TICKER_TO_PREDICT, 'Close'] = YPredInv[-1]
        stocks = stocks.append(lastRow)
    
    # Output the forecasts
    outputStocks = stocks.tail(period)
    print(outputStocks.columns)
    if period > 1:
        st.write(f'Forecast forthe next {period} days')
        st.plotly_chart(getStockChart(outputStocks, datelist))
    
    #Generate comparison table for showing increase or decrease in close price
    closepricetable=pd.DataFrame()
    for i in range(len(datelist)):
        datefinal=pd.to_datetime(datelist[i],utc=False)
        newrow=pd.DataFrame([inverseConvertCurrency(outputStocks[constants.TICKER_TO_PREDICT]['Close'][i])], index = [datefinal.date()],columns=['ClosePrice'])
        closepricetable=pd.concat([newrow,closepricetable])
    
    closepricetable=closepricetable.sort_index()
    def color_table(val):
        if val-inverseConvertCurrency(today)>0:
            color = 'green'
        elif val-inverseConvertCurrency(today)<0:
            color='red'
        else:
            color='grey'
        return f'background-color: {color}'
    a,b,c=st.beta_columns(3)
    with b:
        st.write(closepricetable.style.applymap(color_table, subset=['ClosePrice']))

# Function to start the forecasting process for uploaded model with model and weights together
def getuploadedForecast2(period,uploadedfile):

    # Get the dates from today upto a specific period specified
    datelist = pd.date_range(
    datetime.today(), periods=period).to_pydatetime().tolist()
    
    #loading single zipped file of model already containing weights
    if uploadedfile is not None:
        myzipfile = zipfile.ZipFile(uploadedfile)
        with tempfile.TemporaryDirectory() as tmp_dir:
            myzipfile.extractall(tmp_dir)
            root_folder = myzipfile.namelist()[0] 
            model_dir = os.path.join(tmp_dir, root_folder)
            loaded_model = tf.keras.models.load_model(model_dir)
            loaded_model.compile(loss=constants.LOSS_FUNCTION,
                        optimizer=tf.keras.optimizers.Adam(
                            learning_rate=constants.LEARNING_RATE),
                        metrics=constants.METRICS
                        )

    # Get the last 1 month data
    stocks = pd.DataFrame()
    stocks = getData(False, '1mo')
    
    today=stocks[constants.TICKER_TO_PREDICT, 'Close'][-1]  

    # Get forecast to the next day and the subsequent period if specified
    for i in range(period):
        YPredInv = getModelPrediction(loaded_model, stocks)
        if i == 0:
            st.write(f'Forecast for tomorrow : {float(inverseConvertCurrency(YPredInv[-1]))}')
            lastRow = stocks.tail(1)
            lastRow[constants.TICKER_TO_PREDICT, 'Close'] = YPredInv[-1]
            stocks = stocks.append(lastRow)
    
    # Output the forecasts
    outputStocks = stocks.tail(period)
    print(outputStocks.columns)
    if period > 1:
        st.write(f'Forecast forthe next {period} days')
        st.plotly_chart(getStockChart(outputStocks, datelist))
    
    #Generate comparison table for showing increase or decrease in close price
    closepricetable=pd.DataFrame()
    for i in range(len(datelist)):
        datefinal=pd.to_datetime(datelist[i],utc=False)
        newrow=pd.DataFrame([inverseConvertCurrency(outputStocks[constants.TICKER_TO_PREDICT]['Close'][i])], index = [datefinal.date()],columns=['ClosePrice'])
        closepricetable=pd.concat([newrow,closepricetable])
    
    closepricetable=closepricetable.sort_index()
    def color_table(val):
        if val-inverseConvertCurrency(today)>0:
            color = 'green'
        elif val-inverseConvertCurrency(today)<0:
            color='red'
        else:
            color='grey'
        return f'background-color: {color}'
    a,b,c=st.beta_columns(3)
    with b:
        st.write(closepricetable.style.applymap(color_table, subset=['ClosePrice']))
        
