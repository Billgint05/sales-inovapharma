import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📈 Sales Performance Dashboard")

file = st.file_uploader(
    "Upload Sales File",
    type=["xlsx"]
)

if file:

    df = pd.read_excel(file)

    area_list = sorted(
        df["Area"].dropna().unique()
    )

    selected_area = st.selectbox(
        "Select Area",
        area_list
    )

    df_filtered = df[
        df["Area"] == selected_area
    ]

    st.dataframe(df_filtered)
