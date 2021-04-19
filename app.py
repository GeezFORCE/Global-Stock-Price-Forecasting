# External Imports
import streamlit as st

# Internal Imports
from Project.Pages.mainOverview import mainOverview
from Project.Pages.mainAbout import mainAbout
from Project.Pages.mainTrain import mainTrain
from Project.Pages.sentimentalAnalysisOverview import startSentimentalAnalysis
from Project import constants

# Sidebar component for Main Navigation
# Controls Overview, Train,, Predict, Sentimental Analysis and About Pages
st.sidebar.header('Main Project')
constants.TICKER_TO_PREDICT = st.sidebar.text_input(label='Ticker', value='AAPL', help='Input the ticker')
if not constants.TICKER_TO_PREDICT[0:len(constants.TICKER_TO_PREDICT)].isalpha():
    st.write('Ticker is invalid, Enter again')
else:
    mainNavigation = st.sidebar.selectbox(label='Navigation',
                        options=[ 'Sentimental Analysis', 'Train', 'About', 'Overview', 'Predict'],
                        help='Switch between different views')

    # If-Else statement to control Main Navigation
    if mainNavigation == 'Overview':
        st.markdown('# Overview')
        mainOverview(constants.TICKER_TO_PREDICT)
    elif mainNavigation == 'Train':
        st.markdown('# Train')
        mainTrain(constants.TICKER_TO_PREDICT)
    elif mainNavigation == 'Predict':
        st.markdown('# Predict')
    elif mainNavigation == 'Sentimental Analysis':
        st.markdown('# Sentimental Analysis')
        startSentimentalAnalysis(constants.TICKER_TO_PREDICT)
    elif mainNavigation == 'About':
        st.markdown('# About')
        mainAbout()