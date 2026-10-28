import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("data/pump_data.csv")

X = df[["temperature", "pressure", "vibration", "rpm"]]
y = df["failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "model/pump_model.pkl")

print("Model saved successfully!")