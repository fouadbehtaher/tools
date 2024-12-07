from fbprophet import Prophet
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import xgboost as xgb
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.cluster import DBSCAN
from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

def prophet_forecast(dataframe):
    model = Prophet()
    model.fit(dataframe)
    future = model.make_future_dataframe(dataframe, periods=365)
    forecast = model.predict(future)
    return forecast

def transformer_forecast(data, model_name='facebook/prophet'):
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    inputs = tokenizer(data, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)
    forecast = outputs.logits
    return forecast

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

def xgboost_anomaly_detection(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier(use_label_encoder=False)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

def isolation_forest_anomaly_detection(data):
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    return predictions

def dbscan_anomaly_detection(data):
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(data)
    return labels
