# External Imports
import streamlit as st
import glob

# Internal Imports
from Project import constants
from Project.Forecast import getForecast

def mainPredict(ticker):
    constants.PERIOD_TO_FORECAST = st.sidebar.number_input(label='Forecast Period', min_value=1, max_value=10, step=1, help='Period to Forecast')
    # st.write(getForecast(constants.PERIOD_TO_FORECAST))
    selectedModelName = st.selectbox(label='Select Model', options=glob.glob('savedModelInformation/modelInformation/*.json', recursive=True), index=0, help='Selecting Model used for Forecast')
    selectedModelWeights = st.selectbox(label='Select Model Weights', options=glob.glob('savedModelInformation/modelWeights/*.h5', recursive=True), index=0, help='Selecting Weights of the model used for Forecast')
    if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
        st.sidebar.write('Forecast Started')
        getForecast(constants.PERIOD_TO_FORECAST, selectedModelName, selectedModelWeights)