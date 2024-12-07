from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=False, input_shape=input_shape))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def predict_with_lstm(data):
    model = build_lstm_model(data.shape[1:])
    model.fit(data, data, epochs=50, batch_size=64)
    predictions = model.predict(data)
    mse = np.mean(np.power(data - predictions, 2), axis=1)
    return mse
