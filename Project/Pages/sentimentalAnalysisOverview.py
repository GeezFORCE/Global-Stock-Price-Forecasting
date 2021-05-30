''' sentimentalAnalysisOverview.py : Get Overview about sentimental analysis'''


# External Imports
import streamlit as st

# Internal Imports
from .. import FinvizSentimentalAnalysis

# Function fot sentimental analysis page
def startSentimentalAnalysis():
    st.sidebar.subheader('Tickers')
    defaultInputList = "GOOG, AMZN"  # Default ticker inputs
    userInputTickers = st.sidebar.text_area(label='Tickers',
                                            value=defaultInputList,
                                            help='Enter similar tickers in comma separated form, greater the similarity between tickers greater the accuracy')
    userInputTickers = [i.strip(' ')
                            for i in userInputTickers.strip().split(',')]
    if st.sidebar.button(label='Analyze', help='Click to start sentimental analysis, it may take some time'):
        with st.spinner("Performing Sentimental Analysis"):
            try:
                finvizMeanScores = FinvizSentimentalAnalysis.finvizSentimentalAnalysis(
                    userInputTickers)
                finviz, twitter = st.beta_columns(2)
                with finviz:
                    st.markdown('### Finviz Scores')
                    for i in range(len(finvizMeanScores.index)):
                        st.write(
                            f'{finvizMeanScores.index[i]} : {finvizMeanScores[finvizMeanScores.index[i]]}')
            except:
                st.error("Please provide a valid ticker !") 
