from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def train_model(X, y, alpha=0.2):
    # Only use train split
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=0)

    model = MultinomialNB(alpha=alpha)
    model.fit(X_train, y_train)

    # RETURN ONLY THE MODEL
    return model
