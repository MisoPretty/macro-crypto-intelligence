import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Macro-Crypto-Intelligence", layout="wide")

st.title("📊 Macro-Crypto-Intelligence with Backtesting")

ticker = st.text_input("Enter a crypto ticker (example: BTC, ETH, XRP):", "BTC")

if ticker:
    try:
        data = yf.download(ticker + "-USD", period="6mo", interval="1d")

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
            def get_signal(row):
                if row["RSI_14"] < 30 and row["Close"] > row["SMA_14"]:
                    return "BUY"
                elif row["RSI_14"] > 70 and row["Close"] < row["SMA_14"]:
                    return "SELL"
                return "HOLD"

            data["Signal"] = data.apply(get_signal, axis=1)

            # === Backtesting ===
            position = None
            entry_price = 0
            trades = []

            for i, row in data.iterrows():
                if row["Signal"] == "BUY" and position is None:
                    position = "LONG"
                    entry_price = row["Close"]
                elif row["Signal"] == "SELL" and position == "LONG":
                    exit_price = row["Close"]
                    profit = (exit_price - entry_price) / entry_price
                    trades.append(profit)
                    position = None

            # Compute results
            if trades:
                total_return = (1 + pd.Series(trades)).prod() - 1
                win_rate = (pd.Series(trades) > 0).mean() * 100
                st.subheader("📊 Backtest Results (last 6 months)")
                st.write(f"✅ Total Trades: {len(trades)}")
                st.write(f"📈 Win Rate: {win_rate:.2f}%")
                st.write(f"💵 Total Return: {total_return*100:.2f}%")
            else:
                st.info("No completed trades in this period.")

            # === Plot Price + SMA + Signals ===
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data.index, data["Close"], label="Close Price", color="blue")
            ax.plot(data.index, data["SMA_14"], label="14-day SMA", color="orange")

            # Mark signals
            buy_signals = data[data["Signal"] == "BUY"]
            sell_signals = data[data["Signal"] == "SELL"]
            ax.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="green", label="BUY", s=100)
            ax.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", label="SELL", s=100)

            ax.set_title(f"{ticker} Price, SMA & Signals")
            ax.legend()
            st.pyplot(fig)

            # === Plot RSI ===
            fig, ax = plt.subplots(figsize=(10, 3))
            ax.plot(data.index, data["RSI_14"], label="RSI", color="purple")
            ax.axhline(70,
