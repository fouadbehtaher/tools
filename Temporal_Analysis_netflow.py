import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def analyze_network_time_series(data):
    model = ARIMA(data, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=10)
    return forecast

def analyze_netflow_data(flow_data):
    df = pd.DataFrame(flow_data, columns=['source', 'destination', 'bytes_sent', 'bytes_received'])
    df_grouped = df.groupby(['source', 'destination']).agg({'bytes_sent': 'sum', 'bytes_received': 'sum'}).reset_index()
    return df_grouped
