import streamlit as st
import pandas as pd

st.title("Sales Dashboard")

df = pd.read_excel("DailySales_APL.xlsx")

st.write(df.shape)

st.dataframe(df.head(20))
