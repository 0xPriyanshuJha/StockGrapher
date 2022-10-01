 #numerical python to deal with array 
 #(array is defined as a collection of items that are stored at contiguous memory locations)

import numpy as np 

#pandas is known as data analysis library.
#pandas is used to manipulate data frames.
import pandas as pd 

#yfinance is used to download historical market data from yahoo finance.
import yfinance as yf

#plotly is used to create interactive plots.
#plotly express is a high-level interface to plotly, which operates on "tidy" data and produces easy-to-style figures.

import plotly.graph_objs as go


#download historical data for required stocks
data = yf.download(tickers='BTC-USD', period='2d', interval='60m')
fig =go.Figure()

#Candlestick chart

fig.add_trace(go.Candlestick(x=data.index,

                open=data['Open'],

                high=data['High'],

                low=data['Low'],

                close=data['Close'], name = 'market data'))


# Add titles

fig.update_layout(

   
    title='Bitcoin',
    yaxis_title='BTC-USD')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),

            dict(count=6, label="6m", step="month", stepmode="backward"),

            dict(count=1, label="YTD", step="year", stepmode="todate"),

            dict(count=1, label="1y", step="year", stepmode="backward"),

            dict(step="all")
        ])
    )
)

# Show plot



fig.show()

#save the plot as html file