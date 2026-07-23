import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# ======================
# LOAD FILES
# ======================

fact = pd.read_excel("DailySales_APL.xlsx")

outlet = pd.read_csv("IMS Mapping - Outlet.csv")

sku = pd.read_csv("IMS Mapping - SKU.csv")

# ======================
# MERGE OUTLET
# ======================

fact = fact.merge(
    outlet,
    left_on="CUSTOMER_CODE",
    right_on="Distributor Customer ID",
    how="left"
)

# ======================
# MERGE SKU
# ======================

fact = fact.merge(
    sku,
    left_on="ZP_ITEM_CODE",
    right_on="DIST_SKU CODE",
    how="left"
)

df = fact

st.title("📈 Sales Performance Dashboard")

st.write(df.shape)

st.dataframe(df.head(20))
