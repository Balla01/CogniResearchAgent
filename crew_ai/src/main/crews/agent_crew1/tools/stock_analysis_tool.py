from crewai.tools import tool

@tool
def analyze_stock(ticker: str) -> str:
    """Analyze stock data and generate a plot"""
    import yfinance as yf
    import pandas as pd
    import matplotlib.pyplot as plt
    import os
    from datetime import datetime, timedelta
    from pytz import timezone
    import numpy as np

    stock = yf.Ticker(ticker)
    end_date = datetime.now(timezone("UTC"))
    start_date = end_date - timedelta(days=365)
    hist = stock.history(start=start_date, end=end_date)
    if hist.empty:
        return f"No historical data for {ticker}"

    ma_50 = hist["Close"].rolling(window=50).mean().iloc[-1]
    ma_200 = hist["Close"].rolling(window=200).mean().iloc[-1]
    trend = "Upward" if ma_50 > ma_200 else "Downward"

    plt.figure(figsize=(12, 6))
    plt.plot(hist.index, hist["Close"], label="Close")
    plt.plot(hist.index, hist["Close"].rolling(window=50).mean(), label="50d MA")
    plt.plot(hist.index, hist["Close"].rolling(window=200).mean(), label="200d MA")
    plt.legend()
    os.makedirs("plots", exist_ok=True)
    path = f"plots/{ticker}_chart.png"
    plt.savefig(path)
    return f"{ticker} trend: {trend}. Chart saved at {path}"
