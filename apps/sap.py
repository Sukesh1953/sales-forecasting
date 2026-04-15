from flask import Flask, request, jsonify
import pandas as pd
import joblib

from src.insights import generate_insights

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Sales Prediction API is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    insights = generate_insights(df)

    return jsonify({
        "predicted_sales": int(prediction),
        "insights": insights
    })

if __name__ == "__main__":
    app.run(debug=True)