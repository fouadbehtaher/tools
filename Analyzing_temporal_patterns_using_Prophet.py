from fbprophet import Prophet
import pandas as pd

def prophet_analysis(data):
    df = pd.DataFrame(data, columns=['timestamp', 'value'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.rename(columns={'timestamp': 'ds', 'value': 'y'})

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(df, periods=365)
    forecast = model.predict(future)
    return forecast
