# app.py
# (unchanged code above remains)

# =========================
# requirements.txt (place in project root)
# =========================
# streamlit web app framework
streamlit
# core data
pandas
numpy
requests
# technical indicators
pandas_ta
# RSS parsing
feedparser

# =========================
# README.md (place in project root)
# =========================
# Macro‑Crypto Intelligence MVP

🧠 **Macro‑Crypto Intelligence** is a free Streamlit web app that combines:
- Macro & liquidity proxies (BTC trend + stablecoin caps)
- Micro/technical analysis (EMA, RSI, ATR‑like)
- Geopolitical & economic event summaries (free RSS feeds)
- Simple transparent projections & adaptive exit levels
- XRP‑specific relative strength & volume signals

## Features
- Enter any crypto ticker (BTC, ETH, XRP, SOL, etc.)
- Live charts with EMAs (50/200)
- Market regime snapshot (ON/OFF proxy)
- Stablecoin capitalization snapshot
- News headlines from Reuters, BBC, IMF, CoinDesk, CoinTelegraph, The Block
- Simple forward projection (14 days) & ATR‑based stop/targets
- XRP special: RS vs BTC + volume Z‑score

## Quickstart
```bash
# 1. Clone repository
# git clone https://github.com/yourname/macro-crypto-intelligence
# cd macro-crypto-intelligence

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Streamlit app
streamlit run app.py
```

## Deployment (Free)
Deploy to **Streamlit Community Cloud**:
1. Push repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect repo and select `app.py` as entrypoint.
4. App runs free, 24/7.

## Notes
- Data via free public endpoints (CoinGecko, RSS).
- Educational prototype, **not financial advice**.
- Extend with free exchange endpoints (Binance, Deribit) for OHLC/ATR, funding, basis, and ETF flows.
