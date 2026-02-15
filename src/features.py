from sklearn.feature_extraction.text import CountVectorizer


def create_bow(corpus, max_features=1500):
    vectorizer = CountVectorizer(max_features=max_features)
    X = vectorizer.fit_transform(corpus).toarray()
    return X, vectorizer



