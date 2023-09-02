import streamlit as st
import joblib
import numpy as np

# Load the saved tuned Gradient Boosting model
model_path = r'D:\Projects\Team_Zurich_Capstone_Project\Assets\src\tuned_gb_model.joblib'
tuned_gb_model = joblib.load(model_path)

# Create a function for the About page content
def about_page():
    st.title('About the App')
    st.write("Welcome to the Team Zurich Churn Prediction App!")
    st.write("This app allows you to predict whether a customer will churn or not based on the provided features.")
    st.write("Variable Definitions:")
    
# Streamlit UI
st.title('Team Zurich Churn Prediction App')

# Create a menu to navigate between pages
menu = ['Variable Definitions', 'Predict']
choice = st.sidebar.selectbox('Select Page', menu)

# Display the selected page
if choice == 'Variable Definitions':
    st.title('Variable Definitions')
    st.write("Variable Definitions:")
    st.write("**user_id**: Unique identifier for each client.")
    st.write("**REGION**: Location of each client.")
    st.write("**TENURE**: Duration in the network.")
    st.write("**MONTANT**: Top-up amount.")
    st.write("**FREQUENCE_RECH**: Number of times the customer refilled.")
    st.write("**REVENUE**: Monthly income of each client.")
    st.write("**ARPU_SEGMENT**: Income over 90 days / 3.")
    st.write("**FREQUENCE**: Number of times the client has made an income.")
    st.write("**DATA_VOLUME**: Number of connections.")
    st.write("**ON_NET**: Inter-expresso call.")
    st.write("**ORANGE**: Call to Orange.")
    st.write("**TIGO**: Call to Tigo.")
    st.write("**ZONE1**: Call to Zone1.")
    st.write("**ZONE2**: Call to Zone2.")
    st.write("**MRG**: A client who is going.")
    st.write("**REGULARITY**: Number of times the client is active for 90 days.")
    st.write("**TOP_PACK**: The most active packs.")
    st.write("**FREQ_TOP_PACK**: Number of times the client has activated the top pack packages.")
    st.write("**CHURN**: Variable to predict - Target.")
    
else:
    # Input form and prediction logic
    st.title('Predict Churn')

# Input form
tenure = st.slider('Tenure', 1, 12, 7)
montant = st.number_input('Montant', value=0.0)
frequence_rech = st.number_input('Frequence Recharge', value=0.0)
revenue = st.number_input('Revenue', value=0.0)
arpu_segment = st.number_input('ARPU Segment', value=0.0)
frequence = st.number_input('Frequence', value=0.0)
data_volume = st.number_input('Data Volume', value=0.0)
on_net = st.number_input('On Net', value=0.0)
orange = st.number_input('Orange', value=0.0)
tigo = st.number_input('Tigo', value=0.0)
zone1 = st.number_input('Zone1', value=0.0)
zone2 = st.number_input('Zone2', value=0.0)
regularity = st.slider('Regularity', 1, 61, 30)
freq_top_pack = st.number_input('Frequency Top Pack', value=0.0)
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