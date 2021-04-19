"""plot.py: Visualizations of Data"""


# External Imports
import matplotlib.pyplot as plt
import  plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np
import pandas as pd

# Internal Imports
from . import constants


def PlotlyPlotValidation(validation, YPredInv, YValidationInv):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=validation.index, y=YPredInv.flatten(), mode='lines', name='Prediction'))
    fig.add_trace(go.Scatter(x=validation.index, y=YValidationInv.flatten(), mode='lines', name='Actual'))
    if constants.PERIOD in ['1y', '5y', '10y', 'max']:
            fig.layout.update(xaxis_rangeslider_visible=True)
    return fig


# Function to plot the output graph


def PlotValidation(YPredInv, YValidationInv):
    plt.plot(YValidationInv.flatten(), marker='.', label="True")
    plt.plot(YPredInv.flatten(), 'r', label="Prediction")
    plt.ylabel('Close')
    plt.xlabel('Date Step')
    plt.legend()
    plt.show()

# Function to plot the compound scores of Finviz Sentimental Analysis

def PlotFinvizSentimentalAnalysisResults(news):
    # plt.figure(figsize=(20,20))
    meanNewsData = news.groupby(['Ticker', 'Date']).mean().unstack()
    meanNewsData = meanNewsData.xs(
        'Compound', axis="columns").transpose()
    meanNewsData.plot(kind='bar')
    plt.show()

def PlotlyPlotFinvizSentimentalAnalysisResults(news):
    meanNewsData = news.groupby(['Ticker', 'Date']).mean().unstack()
    meanNewsData = meanNewsData.fillna(0)
    meanNewsData = meanNewsData.xs(
        'Compound', axis="columns").transpose()
    Dates = []
    for i in range(len(meanNewsData.columns)):
        Dates.append(meanNewsData.columns.values[1][1])
    st.write(meanNewsData)
    fig = go.Figure()
    for i in range(len(meanNewsData.index)):
        fig.add_trace(go.Scatter(x=Dates, y=meanNewsData.iloc[i, ], mode='lines', name=meanNewsData.index[i]))
    return fig
    


    