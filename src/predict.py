def predict_sentiment(text, model, vectorizer, preprocess_fn):
    processed = preprocess_fn(text)
    vector = vectorizer.transform([processed]).toarray()
    return model.predict(vector)[0]



    