import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd 

st.title("Tesla Stock Price Prediction Time Series")

# Data fetch
data = yf.download("TSLA", start="2021-01-01", end="2026-09-22")

# MultiIndex sütun yapısını temizleme
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)  # 'TSLA' seviyesini kaldırır

df = data.reset_index()

# Plot
fig = px.line(df, x="Date", y="Close", title="Time Series Analysis (Line Plot)")
st.plotly_chart(fig)