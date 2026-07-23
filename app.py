import streamlit as st

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Performance Dashboard")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Sales FY26",
        "250 B",
        "5%"
    )

with col2:
    st.metric(
        "Sales FY27",
        "270 B",
        "8%"
    )

with col3:
    st.metric(
        "AO",
        "15,200",
        "500"
    )

with col4:
    st.metric(
        "Achievement",
        "95%",
        "2%"
    )

st.markdown("---")

st.subheader("Monthly Sales Trend")

sales = {
    "Jan": 20,
    "Feb": 18,
    "Mar": 22,
    "Apr": 24,
    "May": 25,
    "Jun": 28
}

st.line_chart(sales)

st.subheader("Detail Data")

st.dataframe(
    {
        "Area": ["Jakarta 1", "Jakarta 2", "West Java"],
        "Sales": [100, 80, 70],
        "AO": [5000, 4000, 3500]
    }
)
