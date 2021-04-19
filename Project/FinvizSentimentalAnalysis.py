"""FinvizSentimentalAnalysis.py: Performs sentimental analysis on news from Finviz.com"""

# Look into README.md for installing Vader

# Extrenal Imports
import pandas as pd
from urllib import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Internal Imports
from . import constants
from . import plot
from . import SaveData

# Figure out how to integrate this onto the main model
def finvizSentimentalAnalysis(tickers):
    newsTables = {}

    for ticker in tickers:
        url = constants.FINVIZ_URL + ticker
        req = Request(url=url, headers={'user-agent': 'GSPP'})
        response = urlopen(req)
        html = BeautifulSoup(response, 'lxml')
        newsTables[ticker] = html.find(id='news-table')

    parsedData = []

    for ticker, newsTable in newsTables.items():
        for row in newsTable.findAll('tr'):
            newsTitle = row.a.text
            dateData = row.td.text.split(' ')

            if len(dateData) == 1:
                time = dateData[0]
            else:
                date = dateData[0]
                time = dateData[1]
            parsedData.append([ticker, date, time, newsTitle])

    news = pd.DataFrame(parsedData, 
                        columns=['Ticker', 'Date', 'Time', 'News Title'])
    news['Date'] = pd.to_datetime(news.Date).dt.date

    vader = SentimentIntensityAnalyzer()

    news['Compound'] = news['News Title'].apply(
        lambda newsTitle: vader.polarity_scores(newsTitle)['compound'])

    SaveData.saveCSV(news, "FinvizNews")

    meanNewsData = news.groupby(['Ticker', 'Date']).mean().unstack()
    meanNewsData = meanNewsData.fillna(0)
    meanNewsData = meanNewsData.xs('Compound', axis="columns").transpose()
    meanScores = meanNewsData.mean()
    meanScores = meanScores*100
    return meanScores
    # plot.PlotlyPlotFinvizSentimentalAnalysisResults(news)
