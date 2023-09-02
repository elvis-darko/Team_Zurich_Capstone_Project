import streamlit as st
import joblib
import numpy as np

# Load the saved tuned Gradient Boosting model
model_path = r'D:\Projects\Team_Zurich_Capstone_Project\Assets\src\tuned_gb_model.joblib'
tuned_gb_model = joblib.load(model_path)

  # Add the image using st.image
image_url = "https://i.ytimg.com/vi/ocMd2loRfWE/maxresdefault.jpg"
st.image(image_url, caption='Team Zurich Churn Prediction App', use_column_width=True)

# Title of the app
st.title('Team Zurich Churn Prediction App')

# HOW TO USE THE APP
st.sidebar.title("How to Use the App")
st.sidebar.write("1. Provide the necessary input features.")
st.sidebar.write("2. Click the 'Predict")
                 
# Input form
tenure = st.slider('Tenure: Duration in the network', 1, 12, 7)
montant = st.number_input('Montant:Top-up amount', value=0.0)
frequence_rech = st.number_input('Frequence Recharge: Number of times the customer refilled', value=0.0)
revenue = st.number_input('Revenue: Monthly income of each client', value=0.0)
arpu_segment = st.number_input('ARPU Segment:  Income over 90 days / 3', value=0.0)
frequence = st.number_input('Frequency: Number of times the customer refilled', value=0.0)
data_volume = st.number_input('Data Volume:  Number of connections', value=0.0)
on_net = st.number_input('On Net:Inter-expresso call', value=0.0)
orange = st.number_input('Orange :Call to Orange', value=0.0)
tigo = st.number_input('Tigo:  Call to Tigo', value=0.0)
zone1 = st.number_input('Zone1: Call to Zone1', value=0.0)
zone2 = st.number_input('Zone2: Call to Zone2', value=0.0)
regularity = st.slider('Regularity: Number of times the client is active for 90 days', 1, 61, 30)
freq_top_pack = st.number_input('Frequency Top Pack:Number of times the client has activated the top pack packages', value=0.0)
total_recharge = st.number_input('Total Recharge', value=0.0)
avg_revenue_montant = st.number_input('Average Revenue Montant', value=0.0)
frequence_squared = st.number_input('Frequence Squared', value=0.0)
on_net_reg_ratio = st.number_input('On Net Reg Ratio', value=0.0)

# Create input features array
input_features = np.array([[tenure, montant, frequence_rech, revenue, arpu_segment, 
                            frequence, data_volume, on_net, orange, tigo, 
                            zone1, zone2, regularity, freq_top_pack, 
                            total_recharge, avg_revenue_montant, 
                            frequence_squared, on_net_reg_ratio]])

# Make prediction
if st.button('Predict'):
    prediction = tuned_gb_model.predict(input_features)
    if prediction == 0:
        st.write('Prediction: Not Churn')
    else:
        st.write('Prediction: Churn')