from keras.layers import Input, Dense
from keras.models import Model
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

def train_and_detect_anomalies(data):
    autoencoder = build_autoencoder(data.shape[1])
    autoencoder.fit(data, data, epochs=50, batch_size=64, validation_split=0.1)
    reconstruction_error = autoencoder.evaluate(data, data)
    return reconstruction_error
