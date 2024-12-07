from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
import numpy as np

def anomaly_detection_kmeans(data, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    return kmeans.predict(data)

def anomaly_detection_isolation_forest(data):
    iso_forest = IsolationForest()
    return iso_forest.fit_predict(data)
