import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("Delivery Time Estimator 📦")
st.write("Fill out the details below to estimate the delivery time for your order.")

# Sidebar Inputs
st.sidebar.header("Order Details")
category = st.sidebar.selectbox("Select Product Category", ["Electronics", "Books", "Clothing", "Furniture", "Toys"])
location = st.sidebar.text_input("Customer Location (City)")
shipping = st.sidebar.selectbox("Shipping Method", ["Standard", "Express", "Same-day"])

# Prediction Logic
def estimate_delivery(category, shipping):
    base = {
        "Electronics": 5,
        "Books": 3,
        "Clothing": 4,
        "Furniture": 7,
        "Toys": 2
    }
    modifier = {"Standard": 0, "Express": -1, "Same-day": -2}
    return max(1, base.get(category, 5) + modifier.get(shipping, 0))

# Button for Prediction
if st.sidebar.button("Estimate Delivery Time"):
    time = estimate_delivery(category, shipping)
    st.success(f"Estimated Delivery Time: **{time} days**")

# Visualization
st.subheader("📊 Comparison of Delivery Times by Category")
categories = ["Electronics", "Books", "Clothing", "Furniture", "Toys"]
methods = ["Standard", "Express", "Same-day"]

data = {
    cat: [estimate_delivery(cat, method) for method in methods]
    for cat in categories
}

df = pd.DataFrame(data, index=methods)
st.bar_chart(df)

# Footer
st.markdown("**Created by [Dhvani](https://github.com/ChavdaDhvani/Streamlit-App)**")
