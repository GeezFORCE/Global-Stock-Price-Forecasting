''' mainPredict.py : To display forecasting page'''


# External Imports
import streamlit as st
import glob

# Internal Imports
from Project import constants
from Project.Forecast import getForecast


# Function to take inputs and call forecasting method


def mainPredict():
    # Inputs

    constants.TICKER_TO_PREDICT = st.sidebar.text_input(
        label='Ticker', value='GOOG', help='Input the ticker')
    userInputTickers = st.sidebar.text_area(label='Related Tickers',
                                            value="AAPL, AMZN",
                                            help='Enter similar tickers in comma separated form, greater the similarity between tickers greater the accuracy')
    constants.TICKER_SET = [i.strip(' ')
                            for i in userInputTickers.strip().split(',')]
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
    selectedModelName = st.selectbox(label='Select Model', options=glob.glob(
        'savedModelInformation/modelInformation/*.json', recursive=True), index=0, help='Selecting Model used for Forecast')
    selectedModelWeights = st.selectbox(label='Select Model Weights', options=glob.glob(
        'savedModelInformation/modelWeights/*.h5', recursive=True), index=0, help='Selecting Weights of the model used for Forecast')
    if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
        st.sidebar.write('Forecast Started')
        getForecast(constants.PERIOD_TO_FORECAST,
                    selectedModelName, selectedModelWeights)
