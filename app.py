import streamlit as st
import requests

# page config
st.set_page_config(page_title="Macro Crypto Intelligence", layout="wide")

# title
st.title("📊 Macro-Crypto-Intelligence")

# input box
ticker = st.text_input("Enter a crypto ticker (example: BTC, ETH, XRP):", "BTC")

if ticker:
    try:
        # map tickers to CoinGecko IDs
        mapping = {
            "BTC": "bitcoin",
            "ETH": "ethereum",
            "XRP": "ripple",
            "SOL": "solana"
        }
        coin_id = mapping.get(ticker.upper(), ticker.lower())

        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        r = requests.get(url)
        data = r.json()

        if coin_id in data:
            price = data[coin_id]["usd"]
            st.success(f"💰 {ticker.upper()} current price: ${price:,.2f}")
        else:
            st.error("⚠️ Could not fetch price. Try BTC, ETH, XRP, SOL.")
    except Exception as e:
        st.error(f"API error: {e}")
