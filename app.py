import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Ecommerce Dashboard",
    layout="wide"
)

df = pd.read_csv("ecommerce_data.csv")

st.title("📊 E-Commerce Analytics Dashboard")

total_revenue = df["Purchase_Amount"].sum()
avg_order = df["Purchase_Amount"].mean()
total_customers = df["Customer_ID"].nunique()

col1,col2,col3 = st.columns(3)

col1.metric("Revenue",f"₹{total_revenue:,.0f}")
col2.metric("Avg Order",f"₹{avg_order:,.0f}")
col3.metric("Customers",total_customers)

st.subheader("Revenue By Category")

fig = px.bar(
    df.groupby("Category")["Purchase_Amount"]
    .sum()
    .reset_index(),
    x="Category",
    y="Purchase_Amount"
)

st.plotly_chart(fig,use_container_width=True)

st.subheader("Gender Distribution")

fig2 = px.pie(
    df,
    names="Gender"
)

st.plotly_chart(fig2,use_container_width=True)

st.subheader("Purchase Amount Distribution")

fig3 = px.histogram(
    df,
    x="Purchase_Amount"
)

st.plotly_chart(fig3,use_container_width=True)

st.subheader("Customer Segmentation")

fig4 = px.scatter(
    df,
    x="Order_Count",
    y="Purchase_Amount",
    color="Category"
)

st.plotly_chart(fig4,use_container_width=True)
