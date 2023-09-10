import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import requests


# Load the model from the local file path
model_path = r"D:\Projects\Team_Zurich_Capstone_Project\Assets\src\tuned_gb_model.joblib"
tuned_gb_model = joblib.load(model_path)

# Define functions to calculate values
def calculate_total_recharge(montant, frequence_rech):
    return montant * frequence_rech

def calculate_avg_revenue_montant(revenue, montant):
    return (revenue + montant) / 2

def calculate_frequence_squared(frequence):
    return frequence ** 2

def calculate_on_net_reg_ratio(on_net, regularity):
    return on_net / regularity

def calculate_arpu_segment(revenue):
    return revenue / (90 * 3)

# Title of the app
st.title('Team Zurich Churn Prediction App')

# Add the image using st.image
image_url = "https://th.bing.com/th/id/OIP.Skl99UBPCZac2x6e6rZivwHaDz?pid=ImgDet&rs=1"
st.image(image_url, caption='Team Zurich Churn Prediction App', use_column_width=True)

# HOW TO USE THE APP
st.sidebar.title("How to Use the App")
st.sidebar.write("1. Input Features: Adjust values for customer features.")
st.sidebar.write("2. Click 'Predict': Get churn prediction.")
st.sidebar.write("3. Result: See if it's 'Churn' or 'Not Churn.'")
st.sidebar.write("4. Recommendations (Not Churn): Explore retention suggestions.")
st.sidebar.write("5. Accuracy Score: Check prediction performance.")

# Input form
tenure = st.slider('Tenure: Duration in the network', 1, 12, 7)
montant = st.number_input('Montant: Top-up amount', value=0.0)
frequence_rech = st.number_input('Frequence Recharge: Number of times the customer refilled', value=0.0)
revenue = st.number_input('Revenue: Monthly income of each client', value=0.0)
arpu_segment = st.number_input('ARPU Segment: Income over 90 days / 3', value=0.0)
frequence = st.number_input('Frequency: Number of times the customer refilled', value=0.0)
data_volume = st.number_input('Data Volume: Number of connections', value=0.0)
on_net = st.number_input('On Net: Inter-expresso call', value=0.0)
orange = st.number_input('Orange: Call to Orange', value=0.0)
tigo2 = st.number_input('Tigo: Call to Tigo', value=0.0)
zone1 = st.number_input('Zone1: Call to Zone1', value=0.0)
zone2 = st.number_input('Zone2: Call to Zone2', value=0.0)
regularity = st.slider('Regularity: Number of times the client is active for 90 days', 1, 61, 30)
freq_top_pack = st.number_input('Frequency Top Pack: Number of times the client has activated the top pack packages', value=0.0)

# Calculate values
total_recharge = calculate_total_recharge(montant, frequence_rech)
avg_revenue_montant = calculate_avg_revenue_montant(revenue, montant)
frequence_squared = calculate_frequence_squared(frequence)
on_net_reg_ratio = calculate_on_net_reg_ratio(on_net, regularity)

# Display calculated values
st.text("Total Recharge", total_recharge)
st.text("Average Revenue Montant", avg_revenue_montant)
st.text("Frequence Squared", frequence_squared)
st.text("On Net Reg Ratio", on_net_reg_ratio)

# Make prediction
if st.button('Predict'):
    input_data = {
        "tenure": tenure,
        "montant": montant,
        "frequence_rech": frequence_rech,
        "revenue": revenue,
        "arpu_segment": arpu_segment,
        "frequence": frequence,
        "data_volume": data_volume,
        "on_net": on_net,
        "orange": orange,
        "tigo2": tigo2,
        "zone1": zone1,
        "zone2": zone2,
        "regularity": regularity,
        "freq_top_pack": freq_top_pack
    }

    # Make an API request to FastAPI to get predictions
    response = requests.post("http://localhost:8000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.write('Prediction:', 'Churn' if result['prediction'] == 1 else 'Not Churn')
        st.write('Churn Probability Score:', result['churn_probability'])
        # Add the rest of the result display here

    else:
        st.write('Error:', response.status_code)