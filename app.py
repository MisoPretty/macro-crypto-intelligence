# app.py
# Macro-Crypto Intelligence — free Streamlit MVP
# Data: CoinGecko (no API key) + RSS headlines

import os
import json
import datetime as dt
from typing import Dict, List

import requests
import pandas as pd
import numpy as np
import streamlit as st

try:
    import pandas_ta as ta  # indicators (RSI)
except Exception:
    ta = None

# -------------------------
# Config
# -------------------------
st.set_page_config(page_title="Macro-Crypto Intelligence", layout="wide")
COINGECKO = "https://api.coingecko.com/api/v3"
UA = {"User-Agent": "MacroCryptoIntelligence/0.1 (free, educational)"}

RSS_FEEDS = {
    "Geopolitics": [
        "https://www.reuters.com/world/rss",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
    ],
    "Economy (US/Global)": [
        "https://www.reuters.com/markets/us/rss",
        "https://www.reuters.com/markets/asia/rss",
        "https://www.reuters.com/markets/europe/rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
        "https://www.imf.org/en/News/Articles/News-RSS",
    ],
    "Crypto/Markets": [
        "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "https://cointelegraph.com/rss",
        "https://www.theblock.co/rss",
    ],
}

# -------------------------
# Helpers
# -------------------------
@st.cache_data(ttl=600)
def cg_get(path: str, params: Dict | None = None):
    r = requests.get(f"{COINGECKO}{path}", params=params or {}, headers=UA, timeout=30)
    r.raise_for_status()
    return r.json()

@st.cache_data(ttl=1800)
def get_coins_list() -> pd.DataFrame:
    data = cg_g_
