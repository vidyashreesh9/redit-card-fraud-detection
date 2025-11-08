import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# --- Configuration ---
MODEL_PATH = "backend/fraud_detection_model.joblib"
SCALER_PATH = "backend/scaler.joblib"

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="An API to predict fraudulent credit card transactions using a machine learning model.",
    version="1.0.0"
)

# --- CORS Middleware ---
# Allow requests from our React frontend (which will run on http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Model Loading ---
model = None
scaler = None

@app.on_event("startup")
def load_model():
    """Load the model and scaler at application startup."""
    global model, scaler
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        print("--- Model and Scaler loaded successfully ---")
    else:
        print("--- WARNING: Model or scaler not found. Prediction endpoint will not work. ---")
        print(f"--- Please train the model by running 'python backend/model.py' ---")


# --- Pydantic Model for Input Data ---
class Transaction(BaseModel):
    # We expect all 28 'V' features, plus Time and Amount
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# --- API Endpoints ---
@app.get("/")
def read_root():
    """A simple endpoint to confirm the API is running."""
    return {"status": "ok", "message": "Credit Card Fraud Detection API is running."}

@app.post("/predict")
def predict_fraud(transaction: Transaction):
    """
    Predicts whether a transaction is fraudulent.
    """
    if model is None or scaler is None:
        return {"error": "Model not loaded. Please train the model first."}

    # Convert input data to a DataFrame
    input_data = pd.DataFrame([transaction.dict()])

    # Preprocess the input data in the same way as the training data
    # The scaler expects a 2D array, so we reshape
    input_data['scaled_amount'] = scaler.transform(input_data['Amount'].values.reshape(-1, 1))
    input_data['scaled_time'] = scaler.transform(input_data['Time'].values.reshape(-1, 1))
    
    # Drop original 'Time' and 'Amount' and reorder columns to match training
    input_data = input_data.drop(['Time', 'Amount'], axis=1)
    
    # Ensure the column order matches the model's training data
    # This is crucial for the model to work correctly.
    # We get the expected feature names from the model if it has them.
    try:
        # Scikit-learn models store feature names if trained on a DataFrame
        expected_features = model.feature_names_in_
        input_data = input_data[expected_features]
    except AttributeError:
        # Fallback if feature_names_in_ is not available
        # This assumes the order is correct, which is less robust
        pass

    # Make prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    is_fraud = int(prediction[0])
    fraud_probability = float(probability[0][1])

    return {
        "is_fraud": is_fraud,
        "fraud_probability": f"{fraud_probability:.2%}",
        "prediction": "Fraudulent" if is_fraud == 1 else "Not Fraudulent"
    }
