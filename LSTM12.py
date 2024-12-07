from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

def build_improved_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=100, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=100))
    model.add(Dense(units=1))  # تنبؤ بالقيمة المستقبلية
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_improved_lstm_model(data, labels):
    model = build_improved_lstm_model(data.shape[1:])
    model.fit(data, labels, epochs=50, batch_size=32)
    return model
