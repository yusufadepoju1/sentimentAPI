from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)



    return {
    "accurary": accuracy_score(y_test, y_pred),
    "precision": precision_score(y_test, y_pred),
    "recall": recall_score(y_test, y_pred),
    "confusion_matrix": confusion_matrix(y_test, y_pred)
}