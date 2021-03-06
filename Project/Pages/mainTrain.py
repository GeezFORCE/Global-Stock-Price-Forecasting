''' mainTrain.py : Page for training process'''


# External Imports
from logging import exception
import time
import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen

# Internal Imports
from .. import constants
from .. import Train

# Function to create UI for train 
def mainTrain():
    uinputticker = st.sidebar.text_input(label='Ticker', value='SBIN.NS', help='Input the ticker')
    constants.TICKER_TO_PREDICT = uinputticker.upper()
    st.sidebar.subheader('Related Tickers')
    defaultInputList = "ICICIBANK.NS" #  Default ticker inputs
    userInputTickers = st.sidebar.text_area(label='Related Tickers', 
                        value=defaultInputList, 
                        help='Enter similar tickers in comma separated form, greater the similarity between tickers greater the accuracy')
    
    constants.TICKER_SET = [i.strip(' ') for i in userInputTickers.upper().strip().split(',')]
    if constants.TICKER_TO_PREDICT not in constants.TICKER_SET:
        constants.TICKER_SET.append(constants.TICKER_TO_PREDICT)
    # Yfinance Controls
    st.sidebar.subheader('Data Parameters')
    constants.PERIOD = st.sidebar.select_slider(label='Period',
                                                value='10y',
                                                options=['1mo', '5mo', '1y', '5y', '10y', 'max'], 
                                                help='Range of data to be fetched, select smaller values for accurate results')
    
    # Training Controls
    st.sidebar.subheader('Training Parameters')
    constants.EPOCHS = st.sidebar.slider(label='Epochs', 
                                            min_value=1, 
                                            max_value=200, 
                                            value=50, 
                                            step=1, 
                                            help='Epochs the model should run')
    constants.BATCH_SIZE = st.sidebar.slider(label='Batch Size', 
                                            min_value=8, 
                                            max_value=256, 
                                            value=128, 
                                            step=8, 
                                            help='Batch Size of inputs')
    constants.VALIDATION_SET_PERCENTAGE =0.01*(st.sidebar.slider(label='Validation Split', 
                                            min_value=10, 
                                            max_value=50, 
                                            value=10, 
                                            step=10, 
                                            help='Percentage split for training and validation'))
    constants.LEARNING_RATE = st.sidebar.slider(label='Learning Rate', 
                                            min_value=0.001, 
                                            max_value=0.1, 
                                            value=0.03, 
                                            step=0.010, 
                                            help='Learning Rate for optimizer')

    # Model Controls
    st.sidebar.subheader('Model Parameters')

    constants.NO_OF_LSTM_UNITS = st.sidebar.slider(label='Number of Normal Units', 
                                                    min_value=64, 
                                                    max_value=2048, 
                                                    value=128, 
                                                    step=32, 
                                                    help='Number of neurons in each layer, Greater the neurons greater the time required')
    constants.NO_OF_DENSE_UNITS = st.sidebar.slider(label='Number of Dense Units', 
                                                    min_value=2, 
                                                    max_value=512, 
                                                    value=32, 
                                                    step=2, 
                                                    help='Number of neurons in each dense layer, Greater the neurons greater the time required')
    constants.NO_OF_BIDIRECTIONAL_LAYERS = st.sidebar.number_input(label='Number of Normal Layers', 
                                                            min_value=1, 
                                                            max_value=5, 
                                                            value=1, 
                                                            step=1, 
                                                            help='Number of LSTM Layers, Greater the layers greater the time required')
    constants.NO_OF_DENSE_LAYERS = st.sidebar.number_input(label='Number of Dense Layers', 
                                                    min_value=1, 
                                                    max_value=3, 
                                                    value=1, 
                                                    step=1, 
                                                    help='Number of Dense Layers,  Greater the layers greater the time required')
    constants.DROPOUTRATE = st.sidebar.slider(label='Dropout Rate', 
                                            min_value=0.01, 
                                            max_value=0.1, 
                                            value=0.02, 
                                            step=0.01, 
                                            help='Dropout Rate to prevent overfitting')
    # Automatically sets return sequences if number of bidirectional layers is > 1, else sets it false 
    if(constants.NO_OF_BIDIRECTIONAL_LAYERS>1):
        constants.RETURN_SEQUENCES = True
    else:
        constants.RETURN_SEQUENCES = False
    """constants.RETURN_SEQUENCES = st.sidebar.checkbox(label='Return Sequences',
                                                    value=False,
                                                    help='Check if you want bidirectional layers, Greater the time required')"""
    
    constants.NAME = f"{constants.TICKER_TO_PREDICT}-SEQ-{'-'.join(constants.TICKER_SET)}-PRED-{int(time.time())}"

    # Checks if dense layers and/or units are greater in number 
    # than LSTM units
    if constants.NO_OF_LSTM_UNITS <= constants.NO_OF_DENSE_UNITS:
        st.write('One or more inputs are invalid, please enter the right parameters')
    else:
        if st.sidebar.button(label='Train', help='Click to start Training, it may take some time'):
            try:
                tickers = st.beta_columns(len(constants.TICKER_SET))
                for i in range(len(constants.TICKER_SET)):
                    with tickers[i]:
                        tickerInfo = yf.Ticker(constants.TICKER_SET[i]).info
                        try:
                            st.image(Image.open(urlopen(tickerInfo['logo_url'])), use_column_width='auto')
                        except:
                            #Image Error
                            st.write(tickerInfo['logo_url'])
                            st.error("Something went wrong... Unable to load Logo")
                        st.write(f'Previous Close : {tickerInfo["previousClose"]}, {tickerInfo["currency"]}')
                placeholder = st.empty()
                with st.spinner("Training In Progress"):
                    fig = Train.trainModel()
                placeholder.plotly_chart(fig)
            except ValueError as ve:
                st.error("Please provide a Valid Ticker !")
            except KeyError as ke:
                st.error("Please provide a Valid Ticker !")
            except AssertionError as ae:
                st.error("Please provide atleast one unique Ticker in Related Set")