import streamlit as st
import pandas as pd
import numpy as np
import os

# Set Page Config
st.set_page_config(page_title="🚀 Interactive Streamlit App", page_icon="✨", layout="wide")

# App Title
st.title("🚀 Interactive Streamlit App")

# Sidebar Section
st.sidebar.header("User Input")

# Text Input with Placeholder
name = st.sidebar.text_input("Enter your name:", placeholder="Type your name here...")

# Number Input with a Wider Range
age = st.sidebar.number_input("Enter your age:", min_value=1, max_value=120, value=25)

# Select Box with More Options
favorite_color = st.sidebar.selectbox(
    "Pick your favorite color:",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Black", "White"]
)


# Button for Greeting
if st.sidebar.button("Greet Me!"):
    st.success(f"Hello, {name}! 🎉 You are {age} years old and love {favorite_color}.")

# Random Chart Visualization
st.subheader("📊 Random Data Visualization")
num_points = st.slider("Select number of data points:", min_value=10, max_value=100, value=30)
chart_data = pd.DataFrame(np.random.randn(num_points, 3), columns=["X", "Y", "Z"])
st.line_chart(chart_data)

# Load CSV from a specific path
csv_path = r"C:/all practicals/olist_order_payments_dataset.csv"

st.subheader("📂 Olist Order Payments Dataset")

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.write("### Preview of Dataset:")
    st.dataframe(df.head(20))  # Display first 20 rows
else:
    st.error(f"⚠️ File not found: {csv_path}")

# File Upload Feature
st.subheader("📂 Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded File:")
    st.dataframe(uploaded_df.head(20))

# Footer
st.markdown("### Made with ❤️ using Streamlit")
