from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))  
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_lstm_model(data):
    model = build_lstm_model(data.shape[1:])
    model.fit(data, data, epochs=100, batch_size=64)
    return model
