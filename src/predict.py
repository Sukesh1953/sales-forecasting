import pandas as pd
import joblib

model = joblib.load("model.pkl")  # adjust path if needed

def predict_sales(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return int(prediction)