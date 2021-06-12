# External Imports
import streamlit as st
import yfinance as yf
from googlesearch import search

#import inspect

#def getTickerName(compname):
def name_convert(self) :
    searchval = self + 'ticker yahoo finance'
    link = []
    #limits to the first link
    for url in search(searchval, lang='en', num_results=1):
        link.append(url)
    st.write(link)
    #print("\nTEST ",searchval,link,url)
    link = str(link[0])
    link=link.split("/")
    if link[-1]=='':
        ticker=link[-2]
    else:
        x=link[-1].split('=')
        ticker=x[-1]
    #st.error(url)
    #st.error(link)
    st.write(ticker)
    return(ticker)

# st.title("Search Ticker")
# companyname = st.text_input('Enter Company Name' , value='Microsoft', max_chars=None, key=None, type='default', help="Returns Ticker of Company")
# ticker = name_convert(companyname).upper()
# ans = yf.Ticker(ticker)

# tickerInfo = yf.Ticker(ticker).info
# #col1, col2  = st.beta_columns(2)
# try:
#     sect = (tickerInfo['sector'])
#     country = (tickerInfo['country'])
#     site = (tickerInfo['website'])
#     #curr = tickerInfo['currency']
    
# except (KeyError, IndexError, ValueError) as e :
#     st.warning("Please search for a valid Company")   
# else :
#     st.write("Company : ", (f'{tickerInfo["longName"]}'))
#     st.write("Website : ",(tickerInfo['website']))
#     st.write("Ticker : ", ticker)