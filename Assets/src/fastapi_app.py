from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model here
model_path = r"path_to_your_model_file.joblib"
tuned_gb_model = joblib.load(model_path)

app = FastAPI()

class PredictionRequest(BaseModel):
    tenure: int
    montant: float
    frequence_rech: float
    revenue: float
    arpu_segment: float
    frequence: float
    data_volume: float
    on_net: float
    orange: float
    tigo2: float
    zone1: float
    zone2: float
    regularity: int
    freq_top_pack: float
    total_recharge: float
    avg_revenue_montant: float
    frequence_squared: float
    on_net_reg_ratio: float

@app.post("/predict/")
async def predict_churn(request: PredictionRequest):
    input_features = np.array([list(request.dict().values())])
    prediction = tuned_gb_model.predict(input_features)
    prediction_probability = tuned_gb_model.predict_proba(input_features)[:, 1]
    
    response = {
        "prediction": prediction[0],
        "churn_probability": round(prediction_probability[0] * 100, 2),
    }
    return response
