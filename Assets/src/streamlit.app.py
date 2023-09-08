import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import requests


# Define the URL of your model on GitHub
model_url = "https://github.com/Preencez/Team_Zurich_Capstone_Project/raw/main/Assets/src/tuned_gb_model.joblib"

# Send a GET request to download the model file
response = requests.get(model_url)

# Check if the download was successful (status code 200)
if response.status_code == 200:
    # Save the model file locally
    with open("tuned_gb_model.joblib", "wb") as f:
        f.write(response.content)
# Load the model from the local file
tuned_gb_model = joblib.load("D:/Projects/Team_Zurich_Capstone_Project/Assets/src/tuned_gb_model.joblib")

# Title of the app
st.title('Team Zurich Churn Prediction App')

# Add the image using st.image
image_url = "https://i.ytimg.com/vi/ocMd2loRfWE/maxresdefault.jpg"
st.image(image_url, caption='Team Zurich Churn Prediction App', use_column_width=True)

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
    prediction_probability = tuned_gb_model.predict_proba(input_features)
    if prediction == 0:
        st.image("https://toppng.com/uploads/preview/sad-face-transparent-png-crying-emoji-transparent-background-11562873850hiicomfwuq.png", use_column_width=True)
        st.write('Prediction: Not Churn')
        
        # Display recommendations for customers who did not churn
        st.write("Recommendations for Customer Retention:")
        st.write("1. Consider subscribing to our loyalty program for exclusive benefits.")
        st.write("2. Explore our new product offerings for additional value.")
        st.write("3. Contact our customer support for any assistance or questions.")
    else:
        st.write('Prediction: Churn')
        st.write(f'Churn Probability: {prediction_probability[0][1]:.2f}')
        
        # Create input data dictionary
        input_data = {
            "tenure": tenure,
            "montant": montant,
            # Add other input features here
        }

        # Send a POST request to FastAPI to get predictions
        response = requests.post("http://localhost:8000/predict/", json=input_data)

        if response.status_code == 200:
            result = response.json()["result"]
            st.write(result)
        else:
            st.error("Prediction error. Please try again.")
     # Feature Importance Plot
    if hasattr(tuned_gb_model, 'feature_importances_'):
        feature_importance = tuned_gb_model.feature_importances_
        features = ['Tenure', 'Montant', 'Frequence Recharge', 'Revenue', 'ARPU Segment',
                    'Frequency', 'Data Volume', 'On Net', 'Orange', 'Tigo', 'Zone1', 'Zone2',
                    'Regularity', 'Frequency Top Pack', 'Total Recharge', 'Avg Revenue Montant',
                    'Frequence Squared', 'On Net Reg Ratio']
        plt.figure(figsize=(10, 6))
        plt.barh(features, feature_importance)
        plt.xlabel('Feature Importance')
        plt.title('Feature Importance for Churn Prediction')
        st.pyplot(plt)
