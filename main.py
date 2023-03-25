# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data("https://docs.google.com/spreadsheets/d/1bmMR23Jn9PabjIPN1M7wKAKC6qr4g8__IMF9_c2AmHI/edit?usp=sharing")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")