''' sentimentalAnalysisOverview.py : Get Overview about sentimental analysis'''


# External Imports
import streamlit as st

# Internal Imports
from .. import FinvizSentimentalAnalysis
from .. import TwitterSentimentalAnalysis
from .. import constants


def startSentimentalAnalysis():

    constants.TICKER_TO_PREDICT = st.sidebar.text_input(
        label='Ticker', value='GOOG', help='Input the ticker')
    st.sidebar.subheader('Related Tickers')
    defaultInputList = "MSFT, NVDA"  # Default ticker inputs
    userInputTickers = st.sidebar.text_area(label='Related Tickers',
                                            value=defaultInputList,
                                            help='Enter similar tickers in comma separated form, greater the similarity between tickers greater the accuracy')
    # Input Sanitation (Not Perfect)
    constants.TICKER_SET = [i.strip(' ')
                            for i in userInputTickers.strip().split(',')]
    if constants.TICKER_TO_PREDICT not in constants.TICKER_SET:
        constants.TICKER_SET.append(constants.TICKER_TO_PREDICT)
    if st.sidebar.button(label='Analyze', help='Click to start sentimental analysis, it may take some time'):
        try:
            # st.plotly_chart(FinvizSentimentalAnalysis.finvizSentimentalAnalysis(constants.TICKER_SET))
            finvizMeanScores = FinvizSentimentalAnalysis.finvizSentimentalAnalysis(
                constants.TICKER_SET)
            finviz, twitter = st.beta_columns(2)
            with finviz:
                st.markdown('### Finviz Scores')
                for i in range(len(finvizMeanScores.index)):
                    st.write(
                        f'{finvizMeanScores.index[i]} : {finvizMeanScores[finvizMeanScores.index[i]]}')
            #with twitter:
                #st.markdown('### Twitter')
                #st.write(TwitterSentimentalAnalysis.twitterSentimentalAnalysis())
        except:
            st.error("Please provide a valid ticker !") 
