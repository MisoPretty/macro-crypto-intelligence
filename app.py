import streamlit as st

# page config
st.set_page_config(page_title="Macro Crypto Intelligence", layout="wide")

# title
st.title("📊 Macro-Crypto-Intelligence")
st.write("✅ App is running correctly!")

# simple input box
ticker = st.text_input("Enter a crypto ticker (example: BTC):", "BTC")
st.write(f"You entered: {ticker}")
