import streamlit as st
import requests
import pandas as pd
import pandas_ta as ta

st.set_page_config(page_title="Macro Crypto Intelligence", layout="wide")

st.title("📊 Macro-Crypto-Intelligence")

st.write("Use CoinGecko names: e.g. `bitcoin`, `ethereum`, `ripple`, `solana`")

ticker = st.text_input("Enter a crypto (CoinGecko ID):", "bitcoin")

if ticker:
    try:
        # fetch last 90 days of daily prices
        url = f"https://api.coingecko.com/api/v3/coins/{ticker.lower()}/market_chart?vs_currency=usd&days=90&interval=daily"
        r = requests.get(url)
        data = r.json()

        if "prices" in data:
            df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

            # TA indicators
            df["SMA20"] = ta.sma(df["price"], length=20)
            df["RSI14"] = ta.rsi(df["price"], length=14)

            # show chart with price + SMA20
            st.line_chart(df.set_index("timestamp")[["price", "SMA20"]])

            # show last few rows with RSI
            st.subheader("Latest data")
            st.write(df.tail())

        else:
            st.error("⚠️ Could not fetch historical data. Try another coin.")
    except Exception as e:
        st.error(f"API error: {e}")
