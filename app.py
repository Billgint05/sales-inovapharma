import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📈 Sales Dashboard")

# GANTI DENGAN LINK SHAREPOINT COPY LINK
DAILYSALES_URL = "https://inovapharma.sharepoint.com/:x:/s/Indonesia/IQBSk90CCW1qTaqGADTBFrfeAVLOChDuyW2pXTGYy1I1-kU?e=uhsLLD"


def make_download_url(url):
    if "?" in url:
        return url + "&download=1"
    else:
        return url + "?download=1"


@st.cache_data
def load_sales():
    download_url = make_download_url(DAILYSALES_URL)

    response = requests.get(download_url)

    if response.status_code != 200:
        st.error(f"Gagal baca SharePoint. Status code: {response.status_code}")
        st.stop()

    return pd.read_excel(BytesIO(response.content))


df = load_sales()

st.success(f"Loaded {len(df):,} rows")

st.write("Columns:")

st.dataframe(
    pd.DataFrame({
        "Column Name": df.columns
    })
)

st.dataframe(df.head(100))
