import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="Macro-Crypto-Intelligence", page_icon="📊")
st.title("📊 Macro-Crypto-Intelligence")

# Input
ticker = st.text_input("Enter a crypto ticker (example: BTC, ETH, XRP):", "BTC").upper()

if ticker:
    try:
        # Fetch data
        data = yf.download(f"{ticker}-USD", period="6mo", interval="1d")
        if data.empty:
            st.error("No data found. Try another ticker like BTC, ETH, or XRP.")
        else:
            # Show current price
            current_price = data["Close"].iloc[-1]
            st.success(f"💰 {ticker} current price: ${current_price:,.2f}")

            # Moving Average
            data["MA20"] = data["Close"].rolling(window=20).mean()

            # RSI Calculation
            delta = data["Close"].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            data["RSI"] = 100 - (100 / (1 + rs))

            # Plot price + MA
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data.index, data["Close"], label="Close Price", color="blue")
            ax.plot(data.index, data["MA20"], label="20-Day MA", color="orange")
            ax.set_title(f"{ticker} Price & Moving Average")
            ax.legend()
            st.pyplot(fig)

            # Plot RSI
            fig, ax = plt.subplots(figsize=(10, 3))
            ax.plot(data.index, data["RSI"], label="RSI", color="purple")
            ax.axhline(70, color="red", linestyle="--", alpha=0.7)
            ax.axhline(30, color="green", linestyle="--", alpha=0.7)
            ax.set_title(f"{ticker} Relative Strength Index (RSI)")
            ax.legend()
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Error fetching data: {e}")
