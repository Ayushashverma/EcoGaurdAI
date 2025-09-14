from modules.data_collector import load_sensor_data
from modules.analyzer import plot_sensor_data
from modules.predictor import forecast_pm25
from modules.notifier import send_alert

THRESHOLD_PM25 = 60

def main():
    df = load_sensor_data()
    plot_sensor_data(df)
    forecast = forecast_pm25(df)
    print(forecast.tail())

    for _, row in forecast.tail(3).iterrows():
        if row['yhat'] > THRESHOLD_PM25:
            subject = "EcoGuard AI Alert: PM2.5 Spike"
            body = f"Predicted PM2.5 level: {row['yhat']:.2f} at {row['ds']}. Take necessary action!"
            send_alert(subject, body, "recipient@example.com")

if __name__ == "__main__":
    main()
