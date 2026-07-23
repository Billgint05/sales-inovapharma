import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📈 Sales Dashboard")

df = pd.read_excel("DailySales_APL.xlsx")

st.success(f"Loaded {len(df):,} rows")

st.write("Columns:")

st.dataframe(
    pd.DataFrame({
        "Column Name": df.columns
    })
)

st.dataframe(df.head(20))
