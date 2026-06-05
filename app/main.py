from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Student Performance Prediction API",
    version="1.0.0"
)

# Load trained model
model = joblib.load("models/student_model.joblib")


class StudentData(BaseModel):
    math: float
    english: float
    physics: float


@app.get("/")
def home():
    return {
        "message": "Student Performance Prediction API"
    }


@app.post("/predict")
def predict(data: StudentData):

    features = np.array([
        [data.math,
         data.english,
         data.physics]
    ])

    prediction = model.predict(features)[0]

    return {
        "predicted_grade": prediction
    }