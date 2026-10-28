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

    prediction = model.predict(
        [[temperature, pressure, vibration, rpm]]
    )[0]

    if prediction == 1:
        result = "PUMP FAILURE WARNING"
    else:
        result = "PUMP NORMAL"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)