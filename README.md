# ⚡ Tesla Stock Price Time Series Analysis

A time series project that analyzes Tesla (TSLA) stock prices and explores future price forecasting using **SARIMAX**.

## 📌 Project Overview

The project includes:

- Historical Tesla stock data from Yahoo Finance 
- Price and volume analysis
- Daily return analysis
- Candlestick visualization
- Seasonal decomposition
- SARIMAX forecasting
- Streamlit visualization app

## 📊 Dataset

Tesla stock data is downloaded with `yfinance` from **January 2021 to September 2026**.

The notebook contains **1,435 trading-day records** with:

- Open
- High
- Low
- Close
- Volume

No missing values are reported.

## 📈 Time Series Analysis

The notebook includes:

- Closing-price trend
- Candlestick chart
- Trading-volume chart
- Daily-return distribution
- Seasonal decomposition
- SARIMAX forecasting

## 🔮 SARIMAX Model

The notebook uses Tesla's closing price to generate short- and long-term forecasts.

```text id="4xm2dm"
SARIMAX(1, 0, 0)
```

## 🖥️ Streamlit App

The `tesla.py` application downloads TSLA data from Yahoo Finance and displays an interactive closing-price chart.

```bash id="8sjm72"
streamlit run tesla.py
```

> Note: The current Streamlit app visualizes Tesla prices but does not yet generate a forecast.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Statsmodels
- yfinance
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text id="1xnos9"
tesla-time-series/
├── TeslaTS.ipynb
├── tesla.py
└── README.md
```

## 🎯 Skills Demonstrated

- Financial data analysis
- Time series analysis
- Data visualization
- Seasonal decomposition
- SARIMAX modeling
- Streamlit development

---

Built with Python, Statsmodels, yfinance, and Streamlit. ⚡📈
