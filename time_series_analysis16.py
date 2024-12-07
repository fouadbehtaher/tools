import numpy as np
from models import train_lstm_model, arima_forecast

def analyze_time_series_with_lstm(data, labels):
    model = train_lstm_model(data, labels)
    return model

def analyze_time_series_with_arima(data):
    forecast = arima_forecast(data)
    return forecast
