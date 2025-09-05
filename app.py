import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Macro-Crypto-Intelligence", layout="wide")

st.title("📊 Macro-Crypto-Intelligence")

ticker = st.text_input("Enter a crypto ticker (example: BTC, ETH, XRP):", "BTC")

if ticker:
    try:
        data = yf.download(ticker + "-USD", period="3mo", interval="1d")

        if not data.empty:
            # ✅ Get latest closing price
            latest_price = float(data["Close"].iloc[-1])
            st.success(f"💰 {ticker} current price: ${latest_price:,.2f}")

            # === Indicators ===
            # SMA (14-day)
            data["SMA_14"] = data["Close"].rolling(window=14).mean()

            # RSI (14-day)
            delta = data["Close"].diff()
            gain = (delta.where(delta > 0, 0)).rolling(14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
            rs = gain / loss
            data["RSI_14"] = 100 - (100 / (1 + rs))

            # === Trading Signal ===
            latest_rsi = data["RSI_14"].iloc[-1]
            latest_sma = data["SMA_14"].iloc[-1]

            if latest_rsi < 30 and latest_price > latest_sma:
                signal = "🟢 BUY (Oversold & above SMA)"
            elif latest_rsi > 70 and latest_price < latest_sma:
                signal = "🔴 SELL (Overbought & below SMA)"
            else:
                signal = "🟡 HOLD (No strong signal)"

            st.subheader("📈 Trading Signal")
            st.info(signal)

            # === Plot Price + SMA ===
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data.index, data["Close"], label="Close Price", color="blue")
            ax.plot(data.index, data["SMA_14"], label="14-day SMA", color="orange")
            ax.set_title(f"{ticker} Price & SMA")
            ax.legend()
            st.pyplot(fig)

            # === Plot RSI ===
            fig, ax = plt.subplots(figsize=(10, 3))
            ax.plot(data.index, data["RSI_14"], label="RSI", color="purple")
            ax.axhline(70, linestyle="--", color="red", alpha=0.5)
