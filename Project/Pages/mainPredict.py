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

    constants.TICKER_TO_PREDICT = (st.sidebar.text_input(
        label='Ticker', value='GOOG', help='Input the ticker')).upper()
    userInputTickers = st.sidebar.text_area(label='Related Tickers',
                                            value="AAPL, AMZN",
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
    selectedModelName = st.selectbox(label='Select Model', options=glob.glob(
        'savedModelInformation/modelInformation/*.json', recursive=True), index=0, help='Selecting Model used for Forecast')
    selectedModelWeights = st.selectbox(label='Select Model Weights', options=glob.glob(
        'savedModelInformation/modelWeights/*.h5', recursive=True), index=0, help='Selecting Weights of the model used for Forecast')
    if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
        st.sidebar.write('Forecast Started')
        with st.spinner("Forecasting In Progress"):
            getForecast(constants.PERIOD_TO_FORECAST,
                    selectedModelName, selectedModelWeights)


    # Code for Custom model uploading encounter UTF-8 Error, fix if can

    # st.caption("Number of tickers must be same as that of the model")
    # selectedOption = st.radio(label='Model Selector', 
    #                           options=['Choose From List', 'Upload Custom'], 
    #                           index=1, 
    #                           help='Select default to choose from pretrained models and Custom to upload locally trained model')
    # if selectedOption == 'Choose From List':
    #     selectedModelName = st.selectbox(label='Select Model', options=glob.glob(
    #         'savedModelInformation/modelInformation/*.json', recursive=True), index=0, help='Selecting Model used for Forecast')
    #     selectedModelWeights = st.selectbox(label='Select Model Weights', options=glob.glob(
    #         'savedModelInformation/modelWeights/*.h5', recursive=True), index=0, help='Selecting Weights of the model used for Forecast')
    #     if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
    #         with st.spinner("Forecasting In Progress"):
    #             getForecast(constants.PERIOD_TO_FORECAST,
    #                     selectedModelName, selectedModelWeights)
    # else:
    #     fileList = st.file_uploader(label='Upload Model Information', type=['json', 'h5'], accept_multiple_files=True, help='Upload Saved JSON and h5 files of the trained model')
    #     if fileList != 'None' and len(fileList) == 2:
    #         fileNames = [i.name for i in fileList]
    #         newFileList = []
    #         for file in fileList:
    #             convertedFile = file.getvalue()
    #             convertedFile = convertedFile.decode('utf8')
    #             newFileList.append(convertedFile)
    #         if ((fileNames[0].split('-')[-1]).split('.')[0] == (fileNames[1].split('-')[-1]).split('.')[0]) and ((fileNames[0].split('-')[-1]).split('.')[1] != (fileNames[1].split('-')[-1]).split('.')[1]):
    #             if (fileNames[0].split('-')[-1]).split('.')[1] == "json":
    #                 selectedModelName = newFileList[0]
    #                 selectedModelWeights = newFileList[1]
    #             else:
    #                 selectedModelName = newFileList[1]
    #                 selectedModelWeights = newFileList[0]
    #             # st.write(selectedModelName, selectedModelWeights)
    #             if st.sidebar.button(label='Forecast', help='Click to start Forecasting, it may take some time'):
    #                 with st.spinner("Forecasting In Progress"):
    #                     getForecast(constants.PERIOD_TO_FORECAST,
    #                             selectedModelName, selectedModelWeights)
    #         else:
    #             st.warning('Files uploaded are not compatible! Upload Again')

