from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask import render_template

from src.insights import generate_insights

app = Flask(__name__)

model = joblib.load("models/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

# Add predicted sales into dataframe
    df["Sales"] = prediction

    insights = generate_insights(df)

    return jsonify({
        "predicted_sales": int(prediction),
        "insights": insights
    })

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)