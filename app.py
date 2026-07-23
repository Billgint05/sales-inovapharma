import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📈 Sales Performance Dashboard")

file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if file:

    df = pd.read_excel(file)

    st.success("File uploaded successfully")

    st.dataframe(df)
``
