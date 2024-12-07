from sklearn.cluster import KMeans
import numpy as np
import xgboost as xgb

def network_anomaly_detection(data):
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(data)
    
    predictions = kmeans.predict(data)
    return predictions  # 0: سلوك طبيعي، 1: سلوك مشبوه

def network_anomaly_detection_with_xgboost(data):
    model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')
    model.fit(data, [0] * len(data))  # البيانات المحاكاة
    predictions = model.predict(data)
    
    return predictions
