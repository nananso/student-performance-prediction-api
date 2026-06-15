Student Performance Prediction API
A Machine Learning API built with FastAPI and Scikit-Learn that predicts whether a student is likely to pass or fail based on academic scores.

Features
•	Train a machine learning model using student performance data
•	Predict student outcomes using a REST API
•	FastAPI-powered backend
•	Scikit-Learn Random Forest model
•	Docker containerization
•	Swagger API documentation
•	JSON responses

Tech Stack
•	Python
•	FastAPI
•	Scikit-Learn
•	Pandas
•	Joblib
•	Docker
•	Git & GitHub

Project Structure
week2-student-performance-prediction/
│
├── app/
│   ├── main.py
│   └── __init__.py
│
├── data/
│   └── students.csv
│
├── models/
│   └── student_model.joblib
│
├── train_model.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── pytest.ini
├── README.md
└── .gitignore

Installation

Clone Repository
git clone https://github.com/nananso/student-performance-prediction-api.git

Navigate into Project
cd student-performance-prediction-api

Create Virtual Environment
python -m venv venv

Activate Virtual Environment
Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Train the Model
python train_model.py

Expected output:
Model Accuracy: 1.00
Model saved successfully.

Run the API
uvicorn app.main:app --reload

API Documentation
Open:
http://127.0.0.1:8000/docs

Prediction Endpoint

POST /predict
Example Request:
{
  "math": 80,
  "english": 75,
  "physics": 85
}
Example Response:
{
  "prediction": "Pass"
}

Docker Usage
Build Image:
docker build -t student-performance-api .
Run Container:
docker run -p 8000:8000 student-performance-api

Future Improvements
•	Larger training datasets
•	Model evaluation metrics
•	CI/CD pipelines
•	Cloud deployment
•	Experiment tracking
•	Model monitoring

Author
Uchenna Nsoha
Aspiring MLOps Engineer | Backend Developer | Python Programmer

