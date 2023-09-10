import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import requests

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

# Raw GitHub URL of your model
model_url = "https://github.com/Preencez/Team_Zurich_Capstone_Project/raw/main/Assets/src/tuned_gb_model.joblib"

# Download the model file from the URL and save it locally
response = requests.get(model_url)
if response.status_code == 200:
    with open("tuned_gb_model.joblib", "wb") as f:
        f.write(response.content)
    tuned_gb_model = joblib.load("tuned_gb_model.joblib")
else:
    st.error("Failed to load the model from GitHub.")

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
st.text_input("Total Recharge", total_recharge)
st.text_input("Average Revenue Montant", avg_revenue_montant)
st.text_input("Frequence Squared", frequence_squared)
st.text_input("On Net Reg Ratio", on_net_reg_ratio)

# Make prediction
if st.button('Predict'):
    input_features = np.array([[tenure, montant, frequence_rech, revenue, arpu_segment, 
                                frequence, data_volume, on_net, orange,tigo2, 
                                zone1, zone2, regularity, freq_top_pack, 
                                total_recharge, avg_revenue_montant, 
                                frequence_squared, on_net_reg_ratio]])
    
    prediction = tuned_gb_model.predict(input_features)
    prediction_probability = tuned_gb_model.predict_proba(input_features)[:, 1]  # Probability of churn

    if prediction[0] == 0:
        st.image("https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/65532/happy-emoji-clipart-md.png", use_column_width=True)
        st.write('Prediction: Not Churn')
        
        # Display churn probability score
        st.write(f'Churn Probability Score: {round(prediction_probability[0] * 100, 2)}%')
        
        # Display accuracy score
        accuracy = 0.80  # Replace with your actual accuracy score
        st.write(f'Accuracy Score: {accuracy:.2f}')
        
        # Display feature importance as a bar chart
        feature_importance = tuned_gb_model.feature_importances_
        feature_names = ["tenure", "montant", "frequence_rech", "revenue", "arpu_segment",
                         "frequence", "data_volume", "on_net", "orange", "tigo",
                         "zone1", "zone2", "regularity", "freq_top_pack", "total_recharge",
                         "avg_revenue_montant", "frequence_squared", "on_net_reg_ratio"]
        
        # Create a bar chart
        plt.barh(feature_names, feature_importance)
        plt.xlabel('Feature Importance')
        plt.ylabel('Features')
        plt.title('Feature Importance Scores')
        
        # Display the chart using Streamlit
        st.pyplot(plt)
        
        # Display recommendations for customers who did not churn
        st.write("Recommendations for Customer Retention:")
        st.write("Thank you for choosing to stay with us. We truly value your business, Your loyalty means a lot to us, and we're here to serve you")
        st.write("1. Kindly consider subscribing to our loyalty program for exclusive benefits.")
        st.write("2. Explore our new product offerings for additional benefits")
        st.write("3. Unlock personalized recommendations and tailored experiences as a loyalty program member. We'll cater to your preferences and needs like never before.")
        st.write("4. Get an exclusive sneak peek at upcoming features or products. You can even participate in beta testing and help shape our future offerings.")
        st.write("5. Accumulate rewards points with every purchase, which you can redeem for exciting prizes, discounts, or even free products.")
        
    else:
        # Handle the case where the prediction is churn
        st.image("https://www.bing.com/images/search?view=detailV2&ccid=NomGYb2F&id=CFAB1B8951296B62ED3B4EDC7875A6AC9A9C2102&thid=OIP.NomGYb2FFUxlWnpSHC6Y4gHaHa&mediaurl=https%3a%2f%2ffiles.123freevectors.com%2fwp-content%2foriginal%2f33898-sad-face-emoji-vector.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.36898661bd85154c655a7a521c2e98e2%3frik%3dAiGcmqymdXjcTg%26pid%3dImgRaw%26r%3d0&exph=3333&expw=3333&q=sad+emoji&simid=608004405752765317&FORM=IRPRST&ck=9B0C4D788378CB0CB7A59FBF9C10D4EB&selectedIndex=7", use_column_width=True)  # Replace with an appropriate churn image
        st.write('Prediction: Churn')
        
        # Display churn probability score
        st.write(f'Churn Probability Score: {round(prediction_probability[0] * 100, 2)}%')
        
        # Add a message to clients who churn
        st.write("We're sorry to see you go. If you have any feedback or concerns, please don't hesitate to reach out to us. We value your input and are always looking to improve our services.")