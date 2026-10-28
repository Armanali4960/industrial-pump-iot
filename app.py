from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model/pump_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    temperature = float(data["temperature"])
    pressure = float(data["pressure"])
    vibration = float(data["vibration"])
    rpm = float(data["rpm"])

    values = [[
        temperature,
        pressure,
        vibration,
        rpm
    ]]

    prediction = model.predict(values)[0]

    probability = model.predict_proba(values)[0]

    confidence = max(probability) * 100

    if prediction == 1:
        result = "PUMP FAILURE WARNING"
    else:
        result = "PUMP NORMAL"

    return jsonify({
        "prediction": result,
        "confidence": round(confidence, 1),
        "temperature": temperature,
        "pressure": pressure,
        "vibration": vibration,
        "rpm": rpm
    })


if __name__ == "__main__":
    app.run(debug=True)