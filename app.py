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
st.sidebar.header('Global Stock Price Forecasting')
# constants.TICKER_TO_PREDICT = st.sidebar.text_input(label='Ticker', value='GOOG', help='Input the ticker')
# if not constants.TICKER_TO_PREDICT[0:len(constants.TICKER_TO_PREDICT)].isalpha():
#     st.write('Ticker is invalid, Enter again')
# else:
mainNavigation = st.sidebar.selectbox(label='Navigation',
                    options=['Overview', 'Train', 'Forecast', 'Sentimental Analysis', 'About'],
                    help='Switch between different views')

# If-Else statement to control Main Navigation
if mainNavigation == 'Overview':
    with st.beta_expander("Help"):
        st.write("Get information, charts and financials of any valid stock simply by entering it's name")
        videoFile = open('./Project/Pages/Videos/Overview-Editted.mp4', 'rb')
        videoBytes = videoFile.read()
        st.video(videoBytes)
    st.markdown('# Overview')
    mainOverview()
elif mainNavigation == 'Train':
    with st.beta_expander("Help"):
        st.write("Create custom machine learning models for specific stocks")
        videoFile = open('./Project/Pages/Videos/Train-Editted.mp4', 'rb')
        videoBytes = videoFile.read()
        st.video(videoBytes)
    st.markdown('# Train')
    mainTrain()
elif mainNavigation == 'Forecast':
    with st.beta_expander("Help"):
        st.write("Forecast the future price for any stock for a period of maximum 10 days")
        videoFile = open('./Project/Pages/Videos/Forecast-Editted.mp4', 'rb')
        videoBytes = videoFile.read()
        st.video(videoBytes)
    st.markdown('# Forecast')
    mainPredict()
elif mainNavigation == 'Sentimental Analysis':
    with st.beta_expander("Help"):
        st.write("Get scores based on market sentiment for any stock")
        videoFile = open('./Project/Pages/Videos/SA-Editted.mp4', 'rb')
        videoBytes = videoFile.read()
        st.video(videoBytes)
    st.markdown('# Sentimental Analysis')
    startSentimentalAnalysis()
elif mainNavigation == 'About':
    st.markdown('# About')
    mainAbout('main_about.html')
