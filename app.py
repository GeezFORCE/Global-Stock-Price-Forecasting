# External Imports
import streamlit as st

# Internal Imports
from Project.Pages.mainOverview import mainOverview
from Project.Pages.mainAbout import mainAbout
from Project.Pages.mainTrain import mainTrain
from Project.Pages.mainPredict import mainPredict
from Project.Pages.sentimentalAnalysisOverview import startSentimentalAnalysis
from Project import constants

# Sidebar component for Main Navigation
# Controls Overview, Train,, Predict, Sentimental Analysis and About Pages
st.sidebar.header('Global Stock Price Prediction')
# constants.TICKER_TO_PREDICT = st.sidebar.text_input(label='Ticker', value='GOOG', help='Input the ticker')
# if not constants.TICKER_TO_PREDICT[0:len(constants.TICKER_TO_PREDICT)].isalpha():
#     st.write('Ticker is invalid, Enter again')
# else:
mainNavigation = st.sidebar.selectbox(label='Navigation',
                    options=['Overview', 'Train', 'Forecast', 'Sentimental Analysis', 'About'],
                    help='Switch between different views')

# If-Else statement to control Main Navigation
if mainNavigation == 'Overview':
    st.markdown('# Overview')
    mainOverview()
elif mainNavigation == 'Train':
    st.markdown('# Train')
    mainTrain()
elif mainNavigation == 'Forecast':
    st.markdown('# Forecast')
    mainPredict()
elif mainNavigation == 'Sentimental Analysis':
    st.markdown('# Sentimental Analysis')
    startSentimentalAnalysis()
elif mainNavigation == 'About':
    st.markdown('# About')
    mainAbout()
