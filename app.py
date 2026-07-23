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

outlet = pd.read_csv(
    "IMS Mapping - Outlet.csv",
    dtype=str
)

sku = pd.read_csv(
    "IMS Mapping - SKU.csv",
    dtype=str
)

# ======================
# FORMAT KEY
# ======================

fact["CUSTOMER_CODE"] = (
    fact["CUSTOMER_CODE"]
    .astype(str)
    .str.strip()
)

outlet["Distributor Customer ID"] = (
    outlet["Distributor Customer ID"]
    .astype(str)
    .str.strip()
)

fact["ZP_ITEM_CODE"] = (
    fact["ZP_ITEM_CODE"]
    .astype(str)
    .str.strip()
)

sku["DIST_SKU CODE"] = (
    sku["DIST_SKU CODE"]
    .astype(str)
    .str.strip()
)

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
    left_on="ZP_ITEM
