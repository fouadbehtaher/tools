import numpy as np
from models import train_lstm_model, arima_forecast, deep_learning_model

def analyze_time_series_with_lstm(data, labels):
    model = train_lstm_model(data, labels)
    return model

def analyze_time_series_with_arima(data):
    forecast = arima_forecast(data)
    return forecast

def deep_learning_for_time_series(data, labels):
    model = deep_learning_model(data, labels)
    return model
