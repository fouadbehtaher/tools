from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.layers import Input, Dense
import numpy as np
from keras.layers import LSTM

def detect_anomaly_with_dbscan(data):
    model = DBSCAN(eps=0.5, min_samples=5)
    return model.fit_predict(data)

def build_autoencoder(input_dim):
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(64, activation='relu')(input_layer)
    decoded = Dense(input_dim, activation='sigmoid')(encoded)
    autoencoder = Model(input_layer, decoded)
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
    return autoencoder

def detect_anomaly_with_autoencoder(data):
    model = build_autoencoder(data.shape[1])
    model.fit(data, data, epochs=50, batch_size=256, shuffle=True, validation_data=(data, data))
    reconstructed = model.predict(data)
    mse = np.mean(np.power(data - reconstructed, 2), axis=1)
    return mse

def build_lstm_model(input_shape):
    model = LSTM(units=50, return_sequences=False, input_shape=input_shape)
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def detect_anomaly_with_lstm(data):
    model = build_lstm_model(data.shape[1:])
    model.fit(data, data, epochs=50, batch_size=64)
    predictions = model.predict(data)
    mse = np.mean(np.power(data - predictions, 2), axis=1)
    return mse
