import numpy as np
import xgboost as xgb
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def generate_realistic_data():
    data = [
        [1, 0, 0, 1],  # آمن
        [0, 1, 1, 0],  # غير آمن
        [1, 1, 0, 1],  # آمن
        [0, 0, 1, 0],  # غير آمن
        [1, 0, 1, 1],  # آمن
        [0, 1, 0, 1],  # غير آمن
    ]
    labels = [1, 0, 1, 0, 1, 0]
    return np.array(data), np.array(labels)

def train_xgboost_model():
    data, labels = generate_realistic_data()
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    print(f"XGBoost Model Accuracy: {accuracy * 100:.2f}%")
    
    return model

def train_isolation_forest():
    data, labels = generate_realistic_data()
    
    model = IsolationForest(n_estimators=100, contamination=0.2)
    model.fit(data)
    
    predictions = model.predict(data)
    return predictions

def real_time_alert(predictions):
    for prediction in predictions:
        if prediction == -1:
            print("Warning: Anomaly Detected!")
        else:
            print("Normal Behavior")
