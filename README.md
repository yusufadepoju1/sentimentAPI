<<<<<<< HEAD
# Sentiment Analysis API (FastAPI + Machine Learning)

A production-style **Sentiment Analysis REST API** built with **FastAPI** and **scikit-learn**.  
The system trains a machine learning model and predicts whether input text expresses **positive** or **negative** sentiment.

This project demonstrates practical skills in **ML pipelines**, **API design**, and **model inference**.

---

## Why This Project Matters

This project showcases:

- End-to-end machine learning workflow
- Clean separation of training, preprocessing, and inference logic
- Real-world API design using FastAPI
- Debugging and deployment-ready structure
- Hands-on experience with NLP preprocessing and feature engineering

Ideal for demonstrating **backend + ML engineering skills**.

---

## Key Features

- REST API for training and inference
- Text preprocessing with stopword handling
- Bag-of-Words feature extraction
- Scikit-learn model training
- Interactive API documentation (Swagger UI)
- Modular and scalable codebase

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- scikit-learn
- NLTK
- Pandas
- NumPy

---

## Project Structure

```

sentiment/
│
├── api/
│   └── app.py              # FastAPI application and routes
│
├── src/
│   ├── preprocessing.py    # Text cleaning logic
│   ├── features.py         # Feature extraction (BoW)
│   ├── train.py            # Model training pipeline
│   └── predict.py          # Model inference
│
├── data/
│   └── dataset.csv         # Training dataset
│
├── requirements.txt
└── README.md

````

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd sentiment
````

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the development server:

```bash
uvicorn api.app:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Interactive API docs available at:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Train Model

**POST** `/train`

Trains the sentiment classification model.

Response:

```json
{
  "message": "Model trained successfully"
}
```

---

### Predict Sentiment

**POST** `/predict`

Request:

```json
{
  "text": "The food was terrible and the service was slow"
}
```

Response:

```json
{
  "text": "The food was terrible and the service was slow",
  "sentiment": "negative"
}
```

---

## Engineering Highlights

* Modular ML pipeline design
* Clear separation of concerns
* Error handling for missing resources
* API-first approach to ML inference
* Ready for model persistence and deployment

---



=======
# sentimentAPI
>>>>>>> 5059adf5917f28e9dd6a1a5f44624265512afc2d
