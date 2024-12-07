from fbprophet import Prophet

def predict_network_performance(data):
    df = pd.DataFrame(data, columns=['ds', 'y'])
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(df, periods=10)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

def analyze_congestion(data):
    congestion = np.mean(data)
    return congestion
