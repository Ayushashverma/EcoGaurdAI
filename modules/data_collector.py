import pandas as pd

def load_sensor_data(file_path='data/sensor_data.csv'):
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    return df
