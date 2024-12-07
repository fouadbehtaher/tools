import xgboost as xgb
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input
from sklearn.model_selection import train_test_split
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest
import numpy as np

def xgboost_anomaly_detection(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    model = xgb.XGBClassifier(use_label_encoder=False)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred

# بناء نموذج LSTM
def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))  # التنبؤ بالقيمة المستقبلية
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def isolation_forest_anomaly_detection(data):
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    return predictions

def dbscan_anomaly_detection(data):
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    labels = dbscan.fit_predict(data)
    return labels

def train_lstm_model(data):
    model = build_lstm_model(data.shape[1:])
    model.fit(data, data, epochs=100, batch_size=64)
    return model
