import streamlit as st
import pandas as pd
import numpy as np
import os

# Set Page Config
st.set_page_config(page_title="Interactive Streamlit App", page_icon="✨", layout="wide")

# App Title
st.title("Interactive Streamlit App")

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
    st.success(f"Hello, {name}! You are {age} years old and love {favorite_color}.")

# Random Chart Visualization
st.subheader("📊 Random Data Visualization")
num_points = st.slider("Select number of data points:", min_value=10, max_value=100, value=30)
chart_data = pd.DataFrame(np.random.randn(num_points, 3), columns=["X", "Y", "Z"])
st.line_chart(chart_data)

# Load CSV Data
st.subheader("📂 Dataset Explorer")

csv_path = r"C:/Streamlittt/olist_order_payments_dataset.csv"
data = None

# Check if the local file exists
if os.path.exists(csv_path):
    data = pd.read_csv(csv_path)
    st.write("### Preview of Local Dataset:")
    st.dataframe(data.head(20))
else:
    st.warning(f"⚠️ Local file not found: {csv_path}. Upload a CSV file instead.")

# File Upload Feature
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded File:")
    st.dataframe(data.head(20))

# Display dataset statistics if a valid dataset is loaded
if data is not None:
    st.subheader("📊 Dataset Statistics")
    st.write(data.describe())

# Footer
st.markdown("### Made with ❤️ using Streamlit")
