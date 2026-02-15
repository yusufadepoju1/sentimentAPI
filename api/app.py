

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

from src.preprocessing import preprocess_review
from src.features import create_bow
from src.train import train_model
from src.predict import predict_sentiment

app = FastAPI(title="Sentiment Analysis API")

MODEL_PATH = "models/naive_bayes.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"
DATA_PATH = "data/raw/Restaurant_Reviews.tsv"

model = None
vectorizer = None

class TrainRequest(BaseModel):
    alpha: float = 0.2

class PredictRequest(BaseModel):
    text: str

@app.post("/train")
def train(request: TrainRequest):
    global model, vectorizer
    df = pd.read_csv(DATA_PATH, sep="\t")
    corpus = df["Review"].apply(preprocess_review)
    X, vectorizer = create_bow(corpus)
    y = df["Liked"].values
    model = train_model(X, y, alpha=request.alpha)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    return {"message": "Model trained successfully"}

@app.post("/predict")
def predict(request: PredictRequest):
    global model, vectorizer
    if model is None or vectorizer is None:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
    prediction = predict_sentiment(
        request.text, model, vectorizer, preprocess_review
    )
    return {"text": request.text, "sentiment": "positive" if prediction == 1 else "negative"}


print("All registered routes:")
for r in app.routes:
    print(r.path)
