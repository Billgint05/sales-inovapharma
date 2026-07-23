import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# GANTI NANTI DENGAN LINK SHAREPOINT
DAILYSALES_URL = "https://inovapharma.sharepoint.com/:x:/s/Indonesia/IQBSk90CCW1qTaqGADTBFrfeAVLOChDuyW2pXTGYy1I1-kU?e=uhsLLD"

st.title("📈 Sales Dashboard")

@st.cache_data
def load_sales():
    return pd.read_excel(DAILYSALES_URL)

df = load_sales()

st.success(f"Loaded {len(df):,} rows")

st.dataframe(df.head(100))
