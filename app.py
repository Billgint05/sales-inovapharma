import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

df = pd.read_excel("DailySales_APL.xlsx")

st.title("📈 Sales Performance Dashboard")

# ==================
# FILTER
# ==================

branch_list = sorted(df["BRANCH"].dropna().unique())

selected_branch = st.selectbox(
    "Branch",
    branch_list
)

df_filtered = df[
    df["BRANCH"] == selected_branch
]

# ==================
# KPI
# ==================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Rows",
        f"{len(df_filtered):,}"
    )

with col2:
    st.metric(
        "Invoice",
        f"{df_filtered['INVOICE_NO'].nunique():,}"
    )

with col3:
    st.metric(
        "SKU",
        f"{df_filtered['ZP_ITEM_CODE'].nunique():,}"
    )

with col4:
    st.metric(
        "Outlet Group",
        f"{df_filtered['CUST_GROUP2_NAME'].nunique():,}"
    )

# ==================
# TOP SKU
# ==================

st.subheader("Top SKU")

top_sku = (
    df_filtered
    .groupby("ITEM_NAME")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_sku)

# ==================
# DATA
# ==================

st.subheader("Detail Data")

st.dataframe(df_filtered)
