from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

app = FastAPI()

# Train and store model in memory
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Define input schema
class FlowerInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "FastAPI ML Backend is running!"}

@app.post("/predict")
def predict(flower: FlowerInput):
    input_data = [[
        flower.sepal_length,
        flower.sepal_width,
        flower.petal_length,
        flower.petal_width
    ]]
    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data)[0]
    flower_names = iris.target_names

    return {
        "prediction": flower_names[prediction],
        "confidence": {
            name: round(float(conf), 3)
            for name, conf in zip(flower_names, confidence)
        }
    }