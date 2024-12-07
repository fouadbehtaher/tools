from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import numpy as np

def evaluate_model_performance(model, X_train, X_test, y_train, y_test):

    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='binary', pos_label=1)
    recall = recall_score(y_test, y_pred, average='binary', pos_label=1)
    
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    metrics = {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "Confusion Matrix": conf_matrix,
        "Classification Report": class_report
    }
    
    return metrics

def test_model_with_synthetic_data(model):
    np.random.seed(42)
    X = np.random.rand(1000, 10)  
    y = np.random.choice([0, 1], size=(1000,), p=[0.9, 0.1])  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    metrics = evaluate_model_performance(model, X_train, X_test, y_train, y_test)
    return metrics
