import matplotlib.pyplot as plt
import seaborn as sns

def plot_sensor_data(df):
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x='timestamp', y='pm25', label='PM2.5')
    sns.lineplot(data=df, x='timestamp', y='pm10', label='PM10')
    sns.lineplot(data=df, x='timestamp', y='no2', label='NO2')
    plt.xticks(rotation=45)
    plt.title("Air Quality Trends")
    plt.ylabel("Pollutant Level")
    plt.tight_layout()
    plt.show()
