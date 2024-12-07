from keras.models import Model
from keras.layers import Input, Dense
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
import numpy as np

def build_autoencoder(input_dim):
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(32, activation='relu')(input_layer)
    encoded = Dense(16, activation='relu')(encoded)
    decoded = Dense(32, activation='relu')(encoded)
    decoded = Dense(input_dim, activation='sigmoid')(decoded)
    
    autoencoder = Model(input_layer, decoded)
    autoencoder.compile(optimizer='adam', loss='mean_squared_error')
    
    return autoencoder

def train_autoencoder(data):
    autoencoder = build_autoencoder(data.shape[1])
    autoencoder.fit(data, data, epochs=50, batch_size=64, validation_split=0.1)
    reconstruction_error = autoencoder.evaluate(data, data)
    return reconstruction_error

def isolation_forest_anomaly_detection(data):
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    return predictions

def dbscan_anomaly_detection(data):
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(data)
    return labels
