from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server Running"}

@app.post("/predict")
def predict(data: dict):

    red = data["red"]
    green = data["green"]
    blue = data["blue"]

    # Dummy prediction logic
    theta = red * 0.1
    phi = green * 0.2
    distance = blue * 0.05

    return {
        "theta": float(theta),
        "phi": float(phi),
        "distance": float(distance)
    }