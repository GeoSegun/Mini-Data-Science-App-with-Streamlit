import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock price and volume of Google!!
""")

# define ticker symbols
tickerSymbol = 'GOOGL'

#get data on ticker
tickerData = yf.Ticker(tickerSymbol)

#get historical Price for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
