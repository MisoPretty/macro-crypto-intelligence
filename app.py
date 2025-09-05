import streamlit as st

st.set_page_config(page_title="Macro Crypto Intelligence", layout="wide")

st.title("📊 Macro-Crypto-Intelligence")
st.write("Welcome! If you see this text, the app is running correctly.")

# simple input test
ticker = st.text_input("Enter a crypto ticker (example: BTC):", "BTC")
st.write(f"You entered: {ticker}")
