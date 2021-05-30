''' mainPredict.py : To display forecasting page'''


# External Imports
import streamlit as st
import glob
import json

# Internal Imports
from Project import constants
from Project.Forecast import getForecast
from Project.Forecast import getuploadedForecast
from Project.Forecast import getuploadedForecast2


# Function to take inputs and call forecasting method


def mainPredict():
    # Inputs

    constants.TICKER_TO_PREDICT = (st.sidebar.text_input(
        label='Ticker', value='GOOG', help='Input the ticker')).upper()
    userInputTickers = st.sidebar.text_area(label='Related Tickers',
                                            value="AMZN",
                                            help='Enter similar tickers in comma separated form, greater the similarity between tickers greater the accuracy')
    constants.TICKER_SET = [i.strip(' ')
                            for i in userInputTickers.upper().strip().split(',')]
    if constants.TICKER_TO_PREDICT not in constants.TICKER_SET:
        constants.TICKER_SET.append(constants.TICKER_TO_PREDICT)
    constants.PERIOD_TO_FORECAST = st.sidebar.number_input(
        label='Forecast Period', min_value=1, max_value=10, step=1, help='Period to Forecast')

    '''
    The number of tickers entered should be the same number of tickers
    that is used to train the model.                                  
    Eg : If we use FB, AAPL, GOOG to train then, the resultant model  
    can only take in three tickers                                    
    '''

    st.caption("Number of tickers must be same as that of the model")
    selectedOption = st.radio(label='Model Selector', 
                              options=['Choose From List','Upload Custom Model: Model and weights separately' ,'Upload Custom Model: Model and weights together'], 
                              index=0, 
                              help='Select default to choose from pretrained models and Custom to upload locally trained model')
    if selectedOption == 'Choose From List':
        selectedModelName = st.selectbox(label='Select Model', options=glob.glob(
            'savedModelInformation/modelInformation/*.json', recursive=True), index=0, help='Selecting Model used for Forecast')
        selectedModelWeights = st.selectbox(label='Select Model Weights', options=glob.glob(
            'savedModelInformation/modelWeights/*.h5', recursive=True), index=0, help='Selecting Weights of the model used for Forecast')
        if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
            with st.spinner("Forecasting In Progress"):
                getForecast(constants.PERIOD_TO_FORECAST,
                        selectedModelName, selectedModelWeights)

    elif selectedOption == 'Upload Custom Model: Model and weights separately':
        uploadedmodel = st.file_uploader(label='Upload Model', type=['json'], accept_multiple_files=False, help='Upload Saved JSON files of the trained model')
        uploadedweight = st.file_uploader(label='Upload Weight (.h5py.zip)', type='zip', accept_multiple_files=False, help='Upload Saved h5 files of the trained model as zipped file')
        if(uploadedmodel!=None and uploadedweight!=None):
            if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
                with st.spinner("Forecasting In Progress"):
                    getuploadedForecast(constants.PERIOD_TO_FORECAST,uploadedmodel,uploadedweight)
        else:
            st.error("Waiting for files to be uploaded.")

    else:
        
        stream = st.file_uploader('TF.Keras model file (.h5py.zip)', type='zip')
        if(stream!=None):
        
            if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
                with st.spinner("Forecasting In Progress"):
                    getuploadedForecast2(constants.PERIOD_TO_FORECAST,stream)
        else:
             st.error("Waiting for file to be uploaded.")
       
