import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from statsmodels.tsa.arima.model import ARIMA
from fbprophet import Prophet

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

def prophet_analysis(data):
    df = pd.DataFrame(data, columns=['timestamp', 'value'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.rename(columns={'timestamp': 'ds', 'value': 'y'})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(df, periods=365)
    forecast = model.predict(future)
    return forecast

def arima_forecast(data):
    model = ARIMA(data, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=10)
    return forecast

def isolation_forest_anomaly_detection(data):
    model = IsolationForest()
    model.fit(data)
    predictions = model.predict(data)
    return predictions
