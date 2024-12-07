import psutil
import socket
import time
import numpy as np
from sklearn.cluster import KMeans
import xgboost as xgb
from sklearn.preprocessing import StandardScaler

def collect_network_data():
    net_io_counters = psutil.net_io_counters()
    network_data = {
        'bytes_sent': net_io_counters.bytes_sent,
        'bytes_recv': net_io_counters.bytes_recv,
        'packets_sent': net_io_counters.packets_sent,
        'packets_recv': net_io_counters.packets_recv
    }
    return network_data

def collect_network_usage():
    usage = []
    for _ in range(10):  # جمع 10 قيم
        data = collect_network_data()
        usage.append([data['bytes_sent'], data['bytes_recv'], data['packets_sent'], data['packets_recv']])
        time.sleep(1)
    return np.array(usage)

def detect_anomaly_with_kmeans(network_data):
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(network_data)
    return kmeans.predict(network_data)

def detect_anomaly_with_xgboost(network_data):
    model = xgb.XGBClassifier(objective='binary:logistic', eval_metric='logloss')
    model.fit(network_data, [0] * len(network_data))  # البيانات المحاكاة
    predictions = model.predict(network_data)
    return predictions

def analyze_network_activity():
    network_data = collect_network_usage()
    print("Network Data Collected:")
    print(network_data)

    predictions_kmeans = detect_anomaly_with_kmeans(network_data)
    print(f"KMeans Anomaly Detection Predictions: {predictions_kmeans}")
    
    predictions_xgboost = detect_anomaly_with_xgboost(network_data)
    print(f"XGBoost Anomaly Detection Predictions: {predictions_xgboost}")
