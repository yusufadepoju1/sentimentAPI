from src.data_loader import load_data
from src.preprocessing import preprocess_review
from src.features import create_bow
from src.train import train_model
from src.evaluate import evaluate
from src.predict import predict_sentiment
import joblib




DATA_PATH = "data/raw/Restaurant_Reviews.tsv"

df = load_data(DATA_PATH)

corpus = df["Review"].apply(preprocess_review)
X, vectorizer = create_bow(corpus)
y = df["Liked"].values


model, X_test, y_test = train_model(X, y)

metrics = evaluate(model, X_test, y_test)
print(metrics)


joblib.dump(model, "models/naive_bayes.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")


sample = "The food was terrible and service was slow"
result = predict_sentiment(sample, model, vectorizer, preprocess_review)

print("Positive" if result else "Negative")