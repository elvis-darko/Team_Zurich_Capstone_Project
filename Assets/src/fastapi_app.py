import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load the saved tuned Gradient Boosting model
model_path = r'D:\Projects\Team_Zurich_Capstone_Project\Assets\src\tuned_gb_model.joblib'
tuned_gb_model = joblib.load(model_path)

# Create a FastAPI app
app = FastAPI(debug=True)

class InputFeatures(BaseModel):
    tenure: int
    montant: float
    frequence_rech: float
    revenue: float
    arpu_segment: float
    frequence: float
    data_volume: float
    on_net: float
    orange: float
    tigo: float
    zone1: float
    zone2: float
    regularity: int
    freq_top_pack: float
    total_recharge: float
    avg_revenue_montant: float
    frequence_squared: float
    on_net_reg_ratio: float

# Streamlit prediction function
def predict_churn(input_data):
    input_features = np.array([list(input_data.dict().values())])
    prediction = tuned_gb_model.predict(input_features)
    prediction_probability = tuned_gb_model.predict_proba(input_features)

    result = {
        'prediction': int(prediction[0]),
        'churn_probability': float(prediction_probability[0][1])
    }
    return result

# FastAPI endpoint to predict churn
@app.post("/predict/")
async def predict(input_data: InputFeatures):
    try:
        result = predict_churn(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI endpoint to serve the Streamlit app
@app.get("/streamlit/")
async def get_streamlit_app():
    st_app_html = """
    <iframe src="http://localhost:8501" width="1000" height="800"></iframe>
    """
    return st_app_html
