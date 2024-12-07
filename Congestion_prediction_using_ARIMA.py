from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(data):
    model = ARIMA(data, order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=10)
    return forecast
