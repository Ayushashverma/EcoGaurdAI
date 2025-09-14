from prophet import Prophet

def forecast_pm25(df):
    df_prophet = df[['timestamp','pm25']].rename(columns={'timestamp':'ds', 'pm25':'y'})
    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=3, freq='H')
    forecast = model.predict(future)
    return forecast[['ds','yhat','yhat_lower','yhat_upper']]
