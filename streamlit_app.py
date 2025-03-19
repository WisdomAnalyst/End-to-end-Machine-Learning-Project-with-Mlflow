import streamlit as st
import numpy as np
import pandas as pd
import os
import sys
from pathlib import Path

# Add root directory to path
root_dir = Path(__file__).resolve().parent
sys.path.append(str(root_dir))

try:
    from Mlproject.pipeline.prediction import PredictionPipeline
except ImportError:
    st.error("Could not import PredictionPipeline. Check your project structure.")


# Set page config
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="wide"
)

# Main title
st.title("Wine Quality Prediction App 🍷")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Input fields
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=20.0, value=7.0)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, value=0.5)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=2.0, value=0.3)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=50.0, value=6.0)
    chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, value=0.05)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, max_value=100.0, value=30.0)

with col2:
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, max_value=300.0, value=100.0)
    density = st.number_input("Density", min_value=0.9, max_value=1.1, value=0.996)
    pH = st.number_input("pH", min_value=2.0, max_value=5.0, value=3.2)
    sulphates = st.number_input("Sulphates", min_value=0.0, max_value=2.0, value=0.5)
    alcohol = st.number_input("Alcohol", min_value=8.0, max_value=15.0, value=10.5)

# Predict button
if st.button("Predict Wine Quality"):
    try:
        # Prepare input data
        input_data = {
            'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid,
            'residual_sugar': residual_sugar,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol
        }
        
        # Convert to numpy array
        data = np.array(list(input_data.values())).reshape(1, -1)
        
        # Make prediction
        obj = PredictionPipeline()
        prediction = obj.predict(data)
        
        # Display prediction
        st.success(f"Predicted Wine Quality: {prediction[0]}")
        
        # Display input values
        st.subheader("Input Parameters:")
        st.json(input_data)
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add information about the project
st.sidebar.header("About")
st.sidebar.info("""
This app predicts the quality of wine based on physicochemical tests.
The prediction is made using a machine learning model trained on the Wine Quality Dataset.
""")

# Add footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Made with ❤️ by Wisdom")