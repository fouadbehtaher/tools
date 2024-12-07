from sklearn.cluster import KMeans
import numpy as np

def network_anomaly_detection(data):
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(data)
    
    predictions = kmeans.predict(data)
    
    return predictions  # 0: سلوك طبيعي، 1: سلوك مشبوه

network_data = [
    [1, 0, 0, 1],  # آمن
    [0, 1, 1, 0],  # مشبوه
    [1, 1, 0, 1],  # آمن
    [0, 0, 1, 0],  # مشبوه
    [1, 0, 1, 1],  # آمن
]

predictions = network_anomaly_detection(network_data)
print(f"Network Anomaly Detection Predictions: {predictions}")
