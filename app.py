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
    left_on="ZP_ITEM_CODE",
    right_on="DIST_SKU CODE",
    how="left"
)

df = fact

# ======================
# VARIABLES
# ======================

df["SALES_VALUE"] = pd.to_numeric(
    df["SALES_VALUE"],
    errors="coerce"
)

TOTAL_SALES = df["SALES_VALUE"].sum()

SALES_BY_MONTH = (
    df.groupby(
        ["PRINCIPAL_YEAR", "PERIOD_NO"],
        as_index=False
    )["SALES_VALUE"]
    .sum()
)

# ======================
# DASHBOARD
# ======================

st.title("📈 Sales Performance Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Sales",
        f"{TOTAL_SALES:,.0f}"
    )

with col2:
    st.metric(
        "Branch",
        f"{df['BRANCH'].nunique():,
