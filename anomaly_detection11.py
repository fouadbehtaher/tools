import xgboost as xgb
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest
import numpy as np

def xgboost_anomaly_detection(data):
    model = xgb.XGBClassifier(use_label_encoder=False)
    model.fit(data)
    predictions = model.predict(data)
    return predictions

def isolation_forest_anomaly_detection(data):
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    return predictions

def dbscan_anomaly_detection(data):
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(data)
    return labels

def ai_anomaly_detection(data):
    xgb_predictions = xgboost_anomaly_detection(data)
    isolation_forest_predictions = isolation_forest_anomaly_detection(data)
    dbscan_labels = dbscan_anomaly_detection(data)
    return xgb_predictions, isolation_forest_predictions, dbscan_labels
