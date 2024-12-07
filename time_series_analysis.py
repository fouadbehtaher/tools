import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from statsmodels.tsa.arima.model import ARIMA
from fbprophet import Prophet
import pandas as pd

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))  # التنبؤ بالقيمة المستقبلية
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_lstm_model(data):
    model = build_lstm_model(data.shape[1:])
    model.fit(data, data, epochs=100, batch_size=64)
    return model

def arima_forecast(data):
    model = ARIMA(data, order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=10)
    return forecast

def prophet_analysis(data):
    df = pd.DataFrame(data, columns=['timestamp', 'value'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.rename(columns={'timestamp': 'ds', 'value': 'y'})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(df, periods=365)
    forecast = model.predict(future)
    return forecast
