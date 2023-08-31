from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load the saved tuned Gradient Boosting model
model_path = 'tuned_gb_model.joblib'
tuned_gb_model = joblib.load(model_path)

@app.post('/predict')
def predict_churn(features: dict):
    input_features = np.array([[features['tenure'], features['montant'], features['frequence_rech'], ...]])
    prediction = tuned_gb_model.predict(input_features)
    return {'prediction': prediction[0]}

# Run the FastAPI app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
