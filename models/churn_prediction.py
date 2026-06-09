import joblib
import numpy as np

model = joblib.load("models/xgb_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_churn(age, income, score):
    input_data = np.array([[age, income, score]])
    scaled = scaler.transform(input_data)

    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    if prediction == 1:
        return f"⚠️ High Churn Risk (Probability: {round(probability,2)})"
    else:
        return f"✅ Low Churn Risk (Probability: {round(probability,2)})"